info = {
    "name" : "",
    "age" : "",
    "class" : ""
}

cost_info = {
    "init_cost" : "",
    "total_seats" : "",
    "remaining_seats" : "",
}

class_list = ["Economy", "Premium_Economy", "Business", "First"]

info["name"] = input("Welcome to FlightCal!\nPlease state the name of your client.\n")
info["age"] = input("\nHow old is your client?\n")
temp_class = input("What class will your client {} be flying in?\nPick 1-4 in Left to Right order out of the following:\n{}\n".format(info["age"], class_list))
info["class"] = class_list[int(temp_class)]
print(info["class"])