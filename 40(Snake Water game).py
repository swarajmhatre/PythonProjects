import random

print("\n Hi! It's Swaraj! Welcome to my first game! \n Select anything between \n \"Snake, Water and Gun\"")
print("Press: \n \'s\' for Snake \'w\' for Water and \'g\' for Gun ")


p_points = 0
c_points = 0
round = 0
while round < 10:
    list = ["Snake", "Water", "Gun"]
    choice = input("Enter your choice: \n")
    if choice == "s":
        list.pop(0)
        c_choice = random.choice(list)
        print(f"Computer chose {c_choice}")
        if c_choice == "Water":
            print("You won +1 pt")
            p_points = p_points +1
        elif c_choice == "Gun":
            print("Comp won +1pt")
            c_points = c_points +1    
    elif choice == "w":
        list.pop(1)
        c_choice = random.choice(list)
        print(f"Computer chose {c_choice}")
        if c_choice == "Gun":
            print("You won +1 pt")
            p_points = p_points +1
        elif c_choice == "Snake":
            print("comp won +1pt")
            c_points = c_points +1    
    elif choice == "g":
        list.pop(2)
        c_choice = random.choice(list)
        print(f"Computer chose {c_choice}")
        if c_choice == "Snake":
            print("You won +1 pt")
            p_points = p_points +1
        elif c_choice == "Water":
            print("comp won +1pt")
            c_points = c_points +1    

    round = round +1

print(f"Your total points are {p_points}")
print(f"Computer's total points are {c_points}")
if p_points > c_points:
    print(f"Congratulations you have won by {p_points - c_points} points!")
elif c_points > p_points:
    print(f"Oops you have lost by {c_points - p_points} points to Mr.Computer!")
else:
    print("Ohh! It's a tie! Play again!")