"""This is FlightCal.

The program calculates the cost of the flight using the age, destination,
and class (flight-wise) of the customer, as well as the number of seats
remaining, and then provides a simple copy-pastable email for the agent
to send.
"""

import os
import xml.etree.ElementTree as ET


def base_price_resolver(destination):
    """Determine the base price of the flight based on the destination.

    Args:
        destination (str): The destination city.

    Returns:
        int: The base price of the flight in dollars.
    """
    price = 0
    if destination == "Auckland":
        price = 300
    elif destination == "Christchurch":
        price = 220
    elif destination == "Queenstown":
        price = 400
    elif destination == "Dunedin":
        price = 360
    elif destination == "Rotorua":
        price = 500
    elif destination == "Wellington":
        price = 200
    return price


def class_resolver(seat_class):
    """Return the multiplier for the flight class.

    Args:
        seat_class (str): The class of the seat (e.g., "Economy", "Business").

    Returns:
        float: The multiplier for the base price based on seat class.
    """
    class_cost = 1
    if seat_class == "Economy":
        class_cost = 1
    elif seat_class == "Premium Economy":
        class_cost = 1.2
    elif seat_class == "Business Class":
        class_cost = 1.6
    elif seat_class == "First Class":
        class_cost = 2
    return class_cost


def age_resolver(age):
    """Return the discount percentage based on the client's age.

    Args:
        age (int): The client's age.

    Returns:
        int: The discount percentage based on the client's age.
    """
    age_discount = 0
    if age <= 18:
        age_discount = 15
        print("Your client is under or is 18, and will thus get a 15% off discount!")
    elif age >= 60:
        age_discount = 20
        print("Your client is over or is 60, and will thus get 20% off!")
    return age_discount


def final_cost_resolver(info, cost_info):
    """Calculate the final cost after applying seat and age discounts.

    Args:
        info (dict): A dictionary containing client information.
        cost_info (dict): A dictionary containing cost-related information.

    Returns:
        dict: The updated cost information, including the final cost.
    """
    cost_info["cost_withclass"] = int(cost_info["init_cost"]) * float(
        cost_info["class_raise"]
    )

    seat_discount_undone = int(cost_info["remaining_seats"]) / int(cost_info["total_seats"])
    cost_info["seat_discount"] = 1 - float(seat_discount_undone)

    if float(cost_info["seat_discount"]) > 0.4:
        cost_info["seat_discount"] = 0.4

    age_discount_float = int(cost_info["age_discount"]) / 100
    cost_info["discount"] = float(cost_info["seat_discount"]) + float(age_discount_float)

    cost_percentage = 1 - cost_info["discount"]
    cost_info["final_cost"] = round(cost_info["cost_withclass"] * float(cost_percentage))

    return cost_info


def email(info, cost_info):
    """Generate a formatted email with flight details and pricing.

    Args:
        info (dict): A dictionary containing client information.
        cost_info (dict): A dictionary containing the cost and discount information.
    """
    discount = round(-((float(cost_info["final_cost"]) / float(cost_info["cost_withclass"]) * 100 - 100) * 1), 2)
    print("\n")
    print("sendto: {}@example.com".format(info["name"].lower().replace(" ", "")))
    print("subject: FlightCal Daily Deal")
    print("body:")
    print("Hey there {}!".format(info["name"]))
    print("We remembered your interest for flights to {}!".format(info["destination"]))
    print(
        "If you order your tickets today, tomorrow's flight would come to just ${}!".format(
            cost_info["final_cost"]
        )
    )
    if cost_info["final_cost"] != cost_info["cost_withclass"]:
        print(
            "Normally this flight would come to ${}, but today you'd get {}% off!".format(
                cost_info["cost_withclass"],
                discount,
            )
        )
    print("Thanks for subscribing to updates from us!\n")


class XMLHandler:
    def __init__(self, filename="flight_data.xml"):
        self.filename = filename

    def write_to_xml(self, info, cost_info):
        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
        except (ET.ParseError, FileNotFoundError):
            root = ET.Element("FlightData")

        client_element = ET.SubElement(root, "Client", name=info["name"])
        info_element = ET.SubElement(client_element, "Info")
        for key, value in info.items():
            ET.SubElement(info_element, key).text = str(value)

        cost_info_element = ET.SubElement(client_element, "CostInfo")
        for key, value in cost_info.items():
            ET.SubElement(cost_info_element, key).text = str(value)

        tree = ET.ElementTree(root)
        tree.write(self.filename)
        print(f"Data for {info['name']} saved to {self.filename}")

    def read_from_xml(self, client_name):
        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
        except FileNotFoundError:
            print("No data file found.")
            return None, None

        for client in root.findall("Client"):
            if client.get("name") == client_name:
                info = {}
                cost_info = {}
                
                info_element = client.find("Info")
                for elem in info_element:
                    info[elem.tag] = elem.text
                
                cost_info_element = client.find("CostInfo")
                for elem in cost_info_element:
                    cost_info[elem.tag] = elem.text

                return info, cost_info

        print(f"No data found for client '{client_name}'.")
        return None, None

    def list_client_names(self):
        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
            client_names = [client.get("name") for client in root.findall("Client")]
            return client_names
        except (FileNotFoundError, ET.ParseError):
            return []

    def display_data_as_table(self, info, cost_info):
        cost_labels = {
            "init_cost": "Initial Cost ($)",
            "cost_withclass": "Cost with Class ($)",
            "final_cost": "Final Cost ($)"
        }

        print("\n" + "=" * 40)
        print("           Client Information          ")
        print("=" * 40)
        
        print(f"{'Field':<20} {'Value':<20}")
        print("-" * 40)
        for key, value in info.items():
            label = key.replace("_", " ").title()
            print(f"{label:<20} {value:<20}")

        print("\n" + "=" * 40)
        print("           Cost Information           ")
        print("=" * 40)
        
        print(f"{'Field':<20} {'Value':<20}")
        print("-" * 40)
        for key, value in cost_info.items():
            if value in ("0", "0.0", "", None):
                continue
            
            if key in ["init_cost", "cost_withclass", "final_cost"]:
                label = cost_labels.get(key, key.replace("_", " ").title())
                if "Cost" in label and not label.endswith("(%)"):
                    value = f"${value}"
                print(f"{label:<20} {value:<20}")
        
        try:
            total_discount_percentage = round((1 - (float(cost_info["final_cost"]) / float(cost_info["cost_withclass"]))) * 100)
            print(f"{'Total Discount (%):':<20} {total_discount_percentage:.2f}%")
        except (KeyError, ValueError, ZeroDivisionError):
            print("Total Discount (%) could not be calculated due to missing or invalid data.")
        
        print("=" * 40 + "\n")

def collect_client_data():
    info = {
        "name": "",
        "age": "",
        "class": "",
        "destination": ""
    }

    cost_info = {
        "init_cost": "",
        "total_seats": "250",
        "remaining_seats": "",
        "age_discount": "",
        "class_raise": ""
    }

    class_list = ["Economy", "Premium Economy", "Business Class", "First Class"]
    destination_list = ["Auckland", "Christchurch", "Wellington", "Queenstown", "Dunedin", "Rotorua"]

    temp_name = input("\nPlease state the name of your client:\n")
    while any(chr.isdigit() for chr in temp_name) == True:
        temp_name = input("\nPlease Enter a Valid Name:\n")
    info["name"] = temp_name

    temp_age = input("\nHow old is your client?\n")
    try:
        info["age"] = int(temp_age)
    except:
        age_is_int = False
    else: 
        age_is_int = True
        
    while age_is_int == False or int(temp_age) > 160:
        temp_age = input("Either your client is a Vampire or you accidentally added a digit.\nPlease re-enter your client's age:\n")
        try:
            info["age"] = int(temp_age)
        except:
            age_is_int = False
        else: 
            age_is_int = True

    print("\nWhat class will your client be flying in?\nPick 1-4 in Left to Right order out of the following:\n")
    print(', '.join(class_list))
    temp_class = input("")
    try:
        info["class"] = class_list[int(temp_class)-1]
    except:
        class_is_int = False
    else: 
        class_is_int = True
        
    while class_is_int == False or int(temp_class) > 4 or int(temp_class) < 1:
        temp_class = input("Please input a number from 1-4\n")
        try:
            info["class"] = class_list[int(temp_class)-1]
        except:
            class_is_int = False
        else: 
            class_is_int = True

    print("\nWhere will your client be flying to?\nPick 1-6 in Left to Right order out of the following:")
    print(', '.join(destination_list))
    temp_dest = input("")
    try:
        info["destination"] = destination_list[int(temp_dest)-1]
    except:
        dest_is_int = False
    else: 
        dest_is_int = True
        
    while dest_is_int == False or int(temp_dest) > 6 or int(temp_dest) < 1:
        temp_dest = input("Please input a number from 1-6\n")
        try:
            info["destination"] = destination_list[int(temp_dest)-1]
        except:
            dest_is_int = False
        else: 
            dest_is_int = True

    cost_info["init_cost"] = base_price_resolver(info["destination"])
    cost_info["age_discount"] = age_resolver(info["age"])
    cost_info["class_raise"] = class_resolver(info["class"])
    cost_info["remaining_seats"] = input("\nHow many seats are available on the plane out of 250?\n")
    try:
        int(cost_info["remaining_seats"])
    except:
        rem_seat_is_int = False
    else: 
        rem_seat_is_int = True
        
    while rem_seat_is_int == False or int(cost_info["remaining_seats"]) > 250:
        cost_info["remaining_seats"] = input("There are only 250 seats on this plane.\nPlease re-enter the count of remaining seats:\n")
        try:
            int(cost_info["remaining_seats"])
        except:
            rem_seat_is_int = False
        else: 
            rem_seat_is_int = True

    cost_info = final_cost_resolver(info, cost_info)
    email(info, cost_info)
    
    return info, cost_info

def main():
    xml_handler = XMLHandler()
    user_choice = ""

    print("Welcome to FlightCal!")

    if os.path.isfile("flight_data.xml"):
        user_choice = input("Would you like to:\n1. Enter new client data\n2. Retrieve existing client data\nor 3. Clear client data\nEnter 1, 2, or 3: ")
    else:
        print("\n\nNo data present. Defaulting to entry mode.\n")
        user_choice = "1"

    if user_choice == "1":
        info, cost_info = collect_client_data()
        xml_handler.write_to_xml(info, cost_info)
    elif user_choice == "2":
        client_names = xml_handler.list_client_names()
        if client_names:
            print("\nAvailable clients:")
            print(", ".join(client_names))
        else:
            print("\nNo clients found in the database.")
        
        client_name = input("\nEnter the name of the client to retrieve their data:\n")
        info, cost_info = xml_handler.read_from_xml(client_name)
        
        if info and cost_info:
            xml_handler.display_data_as_table(info, cost_info)
            email(info, cost_info)
        else:
            print("No data found for client with name:", client_name)
    elif user_choice == "3":
        try:
            os.remove("flight_data.xml")
            print("Client data removed.")
        except:
            print("No data present.")
    else:
        print("Invalid choice.\n\n")
        return True  
    
    while True:
        program_state = input("Would you like to return to the main menu? Type 'yes' or 'no': ").strip().lower()
        if program_state in ("yes", "no"):
            return program_state == "yes"

if __name__ == "__main__":
    while True:
        print("\n\n")
        program_restart = main()
        if not program_restart:
            print("Goodbye!")
            break

