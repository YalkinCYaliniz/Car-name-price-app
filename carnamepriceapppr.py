def main(numberofCars):
    "Print car specifications by number of cars"

    cars = []
    i = 1

    # get car specifications
    for i in range(numberofCars):
        carName = input(f"{i}.Cars name: ")
        carPrice = input(f"{i}.Cars price: ")

        cars.append({"carNameId": carName, "carPriceId": carPrice})

    for index, car in enumerate(cars):
        # print(f"{a}.Name:{car['carNameId']} {a}.Price:{car['carPriceId']}€")
        print(f"{index}.Name:{car['carNameId']} {index}.Price:{car['carPriceId']}€")


if __name__ == "__main__":
    # print("How many cars will you add?")
    numberofCars = int(input("How many cars will you add?"))
    main(numberofCars)
