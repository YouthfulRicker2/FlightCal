def base_price_resolver(destination):  
    price = 0
    if destination = "Auckland"
        price = 300

def age_resolver(age):
    age_discount = 0
    if age <= 18:
        age_discount = 20
        print("Your client is under 18, and will thus get a 20% off discount!")
        return(age_discount)
    elif age >= 60:
        age_discount = 25  
        print("Your client is over 60, and will thus get 25% off!")
        return(age_discount)
    return(age_discount)


info = {
    "name" : "",
    "age" : "",
    "class" : ""
}

cost_info = {
    "init_cost" : "",
    "total_seats" : "",
    "remaining_seats" : ""
}

class_list = ["Economy", "Premium Economy", "Business Class", "First Class"]
destination_list = ["Auckland", "Christchurch", "Queenstown", "Dunedin", "Rotorua"]

info["name"] = input("Welcome to FlightCal!\nPlease state the name of your client.\n")
info["age"] = int(input("\nHow old is your client?\n"))
print("What class will your client {} be flying in?\nPick 1-4 in Left to Right order out of the following:\n".format(info["age"]))
print(', '.join(class_list))
temp_class = input("")
info["class"] = class_list[int(temp_class)-1]

age_resolver(info["age"])
