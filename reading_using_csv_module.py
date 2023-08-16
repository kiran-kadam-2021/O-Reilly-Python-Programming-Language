import csv
with open("Data/people-100.csv", "r") as file:
    lines = csv.reader(file)
    num = 0
    for line in lines:
        print(line)
        num += 1
        if num == 5:
            break