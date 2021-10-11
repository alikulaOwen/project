import random

print("Enter the number of friends joining (including you): ")
try:
    friends = int(input())
    print()
    if friends > 0:
        dict_list = {}
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(friends):
            friend = input()
            dict_list[friend] = 0
        print()
        total = int(input("Enter the total bill value: "))
        split = total / friends
        updated_dict = dict.fromkeys(dict_list, round(split, 2))
        print()
        lucky_choice = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
        user_choice = lucky_choice.lower()
        if user_choice == "yes":
            names = [key for key in updated_dict]
            name = random.choice(names)
            del updated_dict[name]
            new_split_bill = total / (friends - 1)
            unlucky_dict = dict.fromkeys(updated_dict, round(new_split_bill, 2))
            unlucky_dict[name] = 0
            print()
            print("{} is the lucky one!\n".format(name))
            print(unlucky_dict)
        else:
            print()
            print("No one is going to be lucky\n")
            # print updated dictionary
            print(updated_dict)

    else:
        print("No one is joining for the party")
except Exception:
    print("No one is joining for the party")
