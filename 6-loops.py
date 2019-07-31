item = ""
while item != "quit":
    print("Enter an item to check the price:")
    item = input()

    if item == "pizza":
        print("3$ per slice")
    else:
        print("we don't have that")