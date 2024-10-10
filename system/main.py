############################################################
# - - - - - - - - - - STUDENT LIFE - - - - - - - - - - - - -#
# - - - - - - Fan project created as homework - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#By Kozosvyst_S for the STEP IT Academy Python Senior Course#
#############################################################
# Copyright (c) 2024 Kozosvyst Stas (StasX)
#############################################################

from colorama import Fore
import time
import random
import json
import os

class StudentLifeGame:
    def __init__(self):
        with open("config.json", "r") as data:
            config = json.load(data)

        self.name = str(config["Student"]["name"])
        self.start_age = int(config["Student"]["start_age"])
        self.academy = str(config["Student"]["academy"])
        self.course_level = int(config["Student"]["start_course"])
        self.group = str(config["Student"]["group"])
        self.start_balance = int(config["Student"]["start_balance"])

        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.hunger = 50
        self.alive = True
        self.job = False
        self.business = False
        self.physical_health = 100
        self.course_progress = 0
        self.exam_failed = False
        self.months = 0

        self.save_results_status=config["Global"]["results"]
        self.game_type = str(config["Global"]["Type"])
        self.game_license = str(config["Global"]["Licene"])
        self.game_by = str(config["Global"]["By"])
        self.game_description = str(config["Global"]["Description"])
        self.game_version = str(config["Global"]["Version"])

        self.project_copyright = str(config[".sxscli"]["copyright"])

    class Design:
        def display_menu(self):
            print(Fore.WHITE + f"""
  ____  _             _            _     _ _  __      _ 
 / ___|| |_ _   _  __| | ___ _ __ | |_  | (_)/ _| ___| |
 \___ \| __| | | |/ _` |/ _ \ '_ \| __| | | | |_ / _ \ |
  ___) | |_| |_| | (_| |  __/ | | | |_  | | |  _|  __/_|
 |____/ \__|\__,_|\__,_|\___|_| |_|\__| |_|_|_|  \___(_)
                                    {self.game_version}
 Welcome to {self.game_description}!""")
            time.sleep(0.1)
            print(Fore.LIGHTWHITE_EX + f"""
    -> Start game - 0
    -> Game info  - 1
    -> Exit       - 2

{self.project_copyright}
""")

        def display_end_of_day_status(self, gladness, progress, money, hunger, health):
            print(Fore.WHITE+f" -> Gladness = {gladness}")
            print(Fore.WHITE+f" -> Progress = {round(progress, 2)}")
            print(Fore.WHITE+f" -> Money = {money}")
            print(Fore.WHITE+f" -> Hunger = {hunger}")
            print(Fore.WHITE+f" -> Physical health = {health}")

    def input_command(self):
        try:
            while True:
                command = input(Fore.GREEN + " >>> ")
                try:
                    command = int(command)
                    if command == 0:
                        self.start_game()
                    elif command == 1:
                        self.show_game_info()
                    elif command == 2:
                        print(Fore.RED + " -> Please wait, exiting the program...")
                        time.sleep(2)
                        exit()
                    else:
                        print(Fore.RED + " -> Invalid command! Please enter 0, 1, or 2.")
                except ValueError:
                    print(Fore.RED + " -> Please enter a number!")
                    time.sleep(0.5)

        except Exception as e:
            print("Sorry, you need to install the 'colorama' library.")
            time.sleep(5)
            exit()

    def start_game(self):
        for day in range(365):
            if not self.alive:
                self.save_results(self.gladness, self.progress, self.money, self.hunger, self.physical_health, day)
                print(Fore.WHITE+"Results saved!")
                print(Fore.WHITE+"Thank you for playing!")
                print(Fore.GREEN+"Restart the game and try again!")
                time.sleep(5)
                exit()
            self.live(day)
        self.save_results(self.gladness, self.progress, self.money, self.hunger, self.physical_health, day)
        print(Fore.WHITE+"Results saved!")
        print(Fore.WHITE+"Thank you for playing!")
        print(Fore.GREEN+"Restart the game and try again!")
        time.sleep(5)
        exit()

    def show_game_info(self):
        print(Fore.WHITE + f"""
   ____                        _        __       
  / ___| __ _ _ __ ___   ___  (_)_ __  / _| ___  
 | |  _ / _` | '_ ` _ \ / _ \ | | '_ \| |_ / _ \ 
 | |_| | (_| | | | | | |  __/ | | | | |  _| (_) |
  \____|\__,_|_| |_| |_|\___| |_|_| |_|_|  \___/ 

   🎉 Hey! Welcome to {self.game_description}! 🎉
   
   This short game is about the life of a student.
   Experience one year in the life of a student!
   This game is open source and was primarily created 
   as homework by a student for Step IT Academy. You 
   are free to modify this code for your needs, but 
   please indicate the copyright if you use it.

   📅 Game version: {self.game_version} 
   📜 License: {self.game_license}

Project developer: {self.game_by}
{self.project_copyright}
""")

    def perform_daily_actions(self):
        action = random.randint(1, 6)
        if action == 1:
            self.study()
        elif action == 2:
            self.sleep()
        elif action == 3:
            self.chill()
        elif action == 4:
            self.eat()
        elif action == 5:
            if not self.business and self.money > 150:
                self.start_business()
            elif self.business:
                self.run_business()
            else:
                self.work()
        elif action == 6:
            self.study_course()

    def study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.hunger -= 4
        self.course_progress += 0.2

    def sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.hunger -= 3

    def chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.hunger -= 2

    def eat(self):
        print("Eating food")
        self.hunger += 10
        self.money -= 5

    def work(self):
        if self.job:
            print("Working...")
            self.money += 20
            self.gladness -= 3
            self.hunger -= 5
        else:
            print(Fore.RED+"You don't have a job yet!")

    def start_business(self):
        if self.money >= 200:
            print("Starting your own business!")
            self.business = True
            self.money -= 200
        else:
            print(Fore.RED+"Not enough money to start a business.")

    def run_business(self):
        if self.business:
            print("Running business")
            self.money += 50
            self.gladness += 5
        else:
            print(Fore.RED+"You don't have a business!")

    def study_course(self):
        self.course_progress += 0.2
        print(f"Studying course. Progress: {round(self.course_progress, 2)}")
        if self.course_progress >= 1:
            self.take_exam()

    def take_exam(self):
        print("Taking exam...")
        exam_result = random.choice([True, False])
        if exam_result:
            print(Fore.GREEN+f"Passed the exam for course {self.course_level}!")
            self.money += 120
            self.course_level += 1
            self.course_progress = 0
        else:
            print(Fore.RED+"Failed the exam... Retaking the course.")
            self.course_progress = 0

    def disease(self):
        if random.randint(1, 20) == 1:
            print(Fore.RED+"Got sick!")
            self.physical_health -= random.randint(10, 30)

    def check_alive(self):
        if self.progress < -0.5:
            print(Fore.RED+"Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            if random.randint(1, 2) == 1:
                print(Fore.RED+"Died from depression…")
                self.alive = False
        elif self.hunger <= 0:
            print("Starvation…")
            if random.randint(1, 2) == 1:
                print(Fore.RED+"Died from starvation...")
                self.alive = False
        elif self.progress > 5:
            print(Fore.RED+"Passed externally…")
            self.alive = False
        elif self.physical_health <= 0:
            print(Fore.RED+"Died from illness…")
            self.alive = False
    
    def save_results(self, gladness, progress, money, hunger, health, day):
        if self.save_results_status==True:
            path="system/results/"
            os.makedirs(path, exist_ok=True)
            text=f"""
RESULTS -> {time.strftime('%Y-%m-%d %H:%M:%S')}

DAY -> {day}

Student Info:
 - Name: {self.name}
 - Academy: {self.academy}
 - Course: {self.course_level}
 - Group: {self.group}
 - Gladness: {gladness}
 - Progress: {round(progress, 2)}
 - Money: {money}
 - Hunger: {hunger}
 - Physical health: {health}

Game Info:
    - Game by: {self.game_by}
    - Game version: {self.game_version}
    - Game description: {self.game_description}

Thank you for playing!

{self.project_copyright}
"""
            with open(f"{path}{random.randint(999,999999)}_results.txt", "a") as file:
                file.write(text)
        else:
            pass
    
    def live(self, day):
        time.sleep(0.01)
        day_header = f"Day {day} of {self.name}'s life"
        print(f"{day_header:=^50}")
        self.disease()

        self.perform_daily_actions()
        self.Design().display_end_of_day_status(self.gladness, self.progress, self.money, self.hunger, self.physical_health)
        self.check_alive()
            

    def start(self):
        self.Design.display_menu(self)
        self.input_command()