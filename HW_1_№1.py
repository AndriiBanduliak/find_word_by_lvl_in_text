user_level = "0"
while user_level not in ["1", "2", "3"]:
    user_level = input("You level? (1, 2, 3) ")
print("Level - ", user_level)

user_word = " " + (input("Word? "))

if user_level == "1":

    counter = 0
    with open("1.txt", "r") as file_r:
        for line in file_r:
            if user_word in line and counter < 2:
                print(line)
                counter += 1

if user_level == "2":
    counter = 0
    with  open("2.txt", "r") as file_r:
        for line in file_r:
            if user_word in line and counter < 2:
                print(line)
                counter += 1
if user_level == "3":
    counter = 0
    with  open("3.txt", "r") as file_r:
        for line in file_r:
            if user_word in line and counter < 2:
                print(line)
                counter += 1