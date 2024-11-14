"""This is FlightCal.

The program calculates the cost of the flight using the age, destination,
and class (flight-wise) of the customer, as well as the number of seats
remaining, and then provides a simple copy-pastable email for the agent
to send.
"""

def base_price_resolver(destination):
    """Provide the initial price of the flight based on the destination.

    This function returns the base price depending on where the flight is
    headed.
    """
    price = 0
    if destination == "Auckland":
        price = 300
    elif destination == "Christchurch":
        price = 220
    elif destination == "Wellington":
        price = 200
    return price


def class_resolver(seat_class):
    """Provide the multiplication variable based on the class of the seat."""
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
    """Check whether there's an age discount applicable."""
    age_discount = 0
    if age <= 18:
        age_discount = 15
        print("Your client is under or is 18, and will thus get a 15% off discount!")
    elif age >= 60:
        age_discount = 20
        print("Your client is over or is 60, and will thus get 20% off!")
    return age_discount


def final_cost_resolver(info, cost_info):
    """Calculate the final cost of the flight."""
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
    "class_raise": "",
}

class_list = ["Economy", "Premium Economy", "Business Class", "First Class"]
destination_list = ["Auckland", "Christchurch", "Wellington"]

# Collecting client details
temp_name = input("\nWelcome to FlightCal!\nPlease state the name of your client.\n")
while any(chr.isdigit() for chr in temp_name):
    temp_name = input("\nPlease Enter a Valid Name:\n")
info["name"] = temp_name

# Collecting and validating age
temp_age = input("\nHow old is your client?\n")
while not temp_age.isdigit() or int(temp_age) > 160:
    temp_age = input(
        "Either your client is a Vampire or you accidentally added a digit.\n"
        "Please re-enter your client's age:\n"
    )
info["age"] = int(temp_age)

# Collecting and validating class
print("\nWhat class will your client be flying in?\nPick 1-4 in Left to Right order out of the following:\n")
print(', '.join(class_list))
temp_class = input("")
while not temp_class.isdigit() or not (1 <= int(temp_class) <= 4):
    temp_class = input("Please input a number from 1-4\n")
info["class"] = class_list[int(temp_class) - 1]

# Collecting and validating destination
print("\nWhere will your client be flying to?\nPick 1-3 in Left to Right order out of the following:")
print(', '.join(destination_list))
temp_dest = input("")
while not temp_dest.isdigit() or not (1 <= int(temp_dest) <= 3):
    temp_dest = input("Please input a number from 1-3\n")
info["destination"] = destination_list[int(temp_dest) - 1]

# Collecting seat information
cost_info["init_cost"] = base_price_resolver(info["destination"])
cost_info["age_discount"] = age_resolver(info["age"])
cost_info["class_raise"] = class_resolver(info["class"])
cost_info["remaining_seats"] = input("\nHow many seats are left?\n")

while not cost_info["remaining_seats"].isdigit() or int(cost_info["remaining_seats"]) > 250:
    cost_info["remaining_seats"] = input(
        "There are only 250 seats on this plane.\nPlease re-enter the count of remaining seats:\n"
    )

cost_info = final_cost_resolver(info, cost_info)

print(f"The price of the flight will be ${cost_info['final_cost']}")
