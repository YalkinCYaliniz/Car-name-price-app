print("How many cars will you add?")
numberofCars = int(input())
cars = []
i = 1
a = 1
while i <= numberofCars:
    carName = input(f"{i}.Cars name: ")
    carPrice = input(f"{i}.Cars price: ")
    cars.append({
        'carNameId': carName,
        'carPriceId': carPrice
    })
    i+=1
for car in cars:
    print(f"{a}.Name:{car['carNameId']} {a}.Price:{car['carPriceId']}€")
    a +=1
