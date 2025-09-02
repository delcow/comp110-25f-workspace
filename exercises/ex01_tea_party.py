"This program is being performed to pratice basic Python skills and functions."

__author__: str = "730754916"


def main_planner(guests: int) -> None:
    "Function is the entry point of the program and helps organize the information."
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    "Function calculates number of tea bags needed for given number of people."
    return people * 2


def treats(people: int) -> int:
    "Function calculates number of treats needed for a given number of people."
    return int(tea_bags(people) * 1.5)


def cost(tea_bags: int, treats: int) -> float:
    "Function calculates the cost of tea bags and treats."
    return tea_bags * 0.50 + treats * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
