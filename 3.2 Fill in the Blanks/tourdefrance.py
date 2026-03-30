"""
3.2PP Fill in the Blanks: Tour de France Wrap-up
"""

__author__ = "Niko Stoner"


def main():
    print("Tour de France 2025 – Final Standings")
    print()

    first_place: str = input("Enter the name of the rider in first place: ")
    country_1: str = input("What country is the first-placed rider from? ") 
    total_time_1: float = float(input("Enter the total time (in hours) of the first-placed rider: "))
    second_place: str = input("Enter the name of the rider in second place: ")
    country_2: str = input("What country is the second-placed rider from? ")
    total_time_2: float = float(input("Enter the total time (in hours) of the second-placed rider: "))
    margin: float = total_time_2 - total_time_1
    print(f"{first_place} " "from "f"{country_1} " "has claimed victory in the 2025 Tour de France")
    print(f"They beat {second_place} from {country_2} by {margin:.2f} hours.")
    print("With a total time of " f"{total_time_1:.2f} hours, " f"{first_place} has secured their place in cycling history!")

    

if __name__ == "__main__":
    main()