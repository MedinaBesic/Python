# @TODO: Your code here
my_dict= {
    "name": "Medina",
    "age": "28",
    "hobbies": ["hiking", "kayaking", "reading"],
    "wakeup": {"Monday": "5:30 AM", "Wednesday": "7:00 AM", "Sunday": "10:00 AM"}
}

print(f'{my_dict["name"]} has {len(my_dict["hobbies"])} hobbies and will typically wakeup at {my_dict["wakeup"]["Monday"]} on a Monday.')