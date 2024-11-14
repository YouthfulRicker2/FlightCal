"""This is FlightCal.

The program calculates the cost of the flight using the age, destination,
and class (flight-wise) of the customer, as well as the number of seats
remaining, and then provides a simple copy-pastable email for the agent 
to send.
"""


def base_price_resolver(destination):
    """Provide the initial price of the flight based on the destination."""
    price = 0
    if destination == "Auckland":
        price = 300
    elif destination == "Christchurch":
        price = 220
    elif destination == "Wellington":
        price = 200
    return price


def age_resolver(age):
    """Check whether there's an age discount applicable."""
    age_discount = 0
    if age <= 18:
        age_discount = 15
        print(
            "Your client is under or is 18, and will thus get a 15% discount!"
        )
    elif age >= 60:
        age_discount = 20
        print(
            "Your client is over or is 60, and will thus get 20% off!"
        )
    return age_discount


def final_cost_resolver(info, cost_info):
    """Calculate the final cost of the flight."""
    seat_discount_undone = int(cost_info["remaining_seats"]) / int(
        cost_info["total_seats"]
    )
    cost_info["seat_discount"] = 1 - float(seat_discount_undone)
    if float(cost_info["seat_discount"]) > 0.4:
        cost_info["seat_discount"] = 0.4
    age_discount_float = int(cost_info["age_discount"]) / 100
    cost_info["discount"] = float(cost_info["seat_discount"]) + age_discount_float
    cost_percentage = 1 - cost_info["discount"]
    cost_info["final_cost"] = round(
        cost_info["init_cost"] * cost_percentage
    )
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

destination_list = ["Auckland", "Christchurch", "Wellington"]

# info["name"]
temp_name = input(
    "\nWelcome to FlightCal!\nPlease state the name of your client.\n"
)
while any(chr.isdigit() for chr in temp_name):
    temp_name = input("\nPlease Enter a Valid Name:\n")
info["name"] = temp_name

temp_age = input("\nHow old is your client?\n")
try:
    info["age"] = int(temp_age)
except ValueError:
    age_is_int = False
else:
    age_is_int = True

while not age_is_int or int(temp_age) > 160:
    temp_age = input(
        "Either your client is a Vampire or you accidentally added a digit.\n"
        "Please re-enter your client's age:\n"
    )
    try:
        info["age"] = int(temp_age)
    except ValueError:
        age_is_int = False
    else:
        age_is_int = True

print(
    "\nWhere will your client {} be flying to?\nPick 1-3 in Left to Right "
    "order out of the following:".format(info["name"])
)
print(', '.join(destination_list))
temp_dest = input("")

try:
    info["destination"] = destination_list[int(temp_dest) - 1]
except (IndexError, ValueError):
    dest_is_int = False
else:
    dest_is_int = True

while not dest_is_int or int(temp_dest) > 3 or int(temp_dest) < 1:
    temp_dest = input("Please input a number from 1-3\n")
    try:
        info["destination"] = destination_list[int(temp_dest) - 1]
    except (IndexError, ValueError):
        dest_is_int = False
    else:
        dest_is_int = True

cost_info["init_cost"] = base_price_resolver(info["destination"])
cost_info["age_discount"] = age_resolver(info["age"])

cost_info["remaining_seats"] = input("\nHow many seats are left?\n")
try:
    int(cost_info["remaining_seats"])
except ValueError:
    rem_seat_is_int = False
else:
    rem_seat_is_int = True

while not rem_seat_is_int or int(cost_info["remaining_seats"]) > 250:
    cost_info["remaining_seats"] = input(
        "There are only 250 seats on this plane.\n"
        "Please re-enter the count of remaining seats:\n"
    )
    try:
        int(cost_info["remaining_seats"])
    except ValueError:
        rem_seat_is_int = False
    else:
        rem_seat_is_int = True

cost_info = final_cost_resolver(info, cost_info)

print("The price of the flight will be ${}".format(cost_info["final_cost"]))
print("\n")
