vistors = []

print("welcome to the club\n")

def entering_club(entry_limit,age_limit):
    for i in range(entry_limit):
        club = input("enter: ")
        age = int(input("whats your age? "))
        if age_limit <= age:
            print("come in")
        else:
            print("your too young")
            continue

        vistors.append(club)
    print(vistors)

    print("club is full now")

entering_club(entry_limit=3,age_limit=20)