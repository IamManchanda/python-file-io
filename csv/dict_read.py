from csv import DictReader

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    next(csv_reader)
    for fighter in csv_reader:
        print(f"{fighter['Name']} is from {fighter['Country']} and is {fighter['Height (in cm)']} cm tall.")
