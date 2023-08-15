with open("Data/people-100.csv", "r") as file:
    num = 0
    for line in file:
        print(line.strip())
        # print(line, end="")
        num += 1
        if num == 5:
            break
    