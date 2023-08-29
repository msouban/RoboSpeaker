import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Souban")
    while True:
        x = input("Enter what you want me to speak:  ")
        if x == "q":
            os.system("narrator 'bye bye friend'")
            break
        command = f"narrator {x}"
        os.system(command)


