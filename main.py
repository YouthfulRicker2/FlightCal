def base_price_resolver(destination):  
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
    return(price)

def age_resolver(age):
    age_discount = 0
    if age <= 18:
        age_discount = 20
        print("Your client is under or is 18, and will thus get a 20% off discount!")
    elif age >= 60:
        age_discount = 25  
        print("Your client is over or is 60, and will thus get 25% off!")
    return(age_discount)


info = {
    "name" : "",
    "age" : "",
    "class" : "",
    "destination" : ""

}

cost_info = {
    "init_cost" : "",
    "total_seats" : "",
    "remaining_seats" : "",
    "age_discount" : ""
}

class_list = ["Economy", "Premium Economy", "Business Class", "First Class"]
destination_list = ["Auckland", "Christchurch", "Queenstown", "Dunedin", "Rotorua"]

info["name"] = input("Welcome to FlightCal!\nPlease state the name of your client.\n")
info["age"] = int(input("\nHow old is your client?\n"))

print("\nWhat class will your client {} be flying in?\nPick 1-4 in Left to Right order out of the following:\n".format(info["name"]))
print(', '.join(class_list))
temp_class = input("")
info["class"] = class_list[int(temp_class)-1]

print("\nWhere will your client {} be flying to?\nPick 1-5 in Left to Right order out of the following:".format(info["name"]))
print(', '.join(destination_list))
temp_dest = input("")
info["destination"] = destination_list[int(temp_dest)-1]

print(info["destination"])

cost_info["age_discount"] = age_resolver(info["age"])

print(cost_info["age_discount"])
