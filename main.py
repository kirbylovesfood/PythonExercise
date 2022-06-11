# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Programming for Beginners Using Python

#coding exercise 1.10

character_job = "pirate"
character_ride = "ship"
character_souvenir = "gold"
character_pet = "parrot"

print("There was once a " + character_job + "who loved adventure")
print("The " + character_job + " would take her " + character_ride + " to unknown places.")
print("She brings home a lot of " + character_souvenir + ".")
print("Then she goes home to her pet " + character_pet + ", Chuckles")

#coding exercise 1.14

print("Roses are red, viiolets are blue")
if 10 > 7:
    print("Ten is greater than seven!")
if 16 < 42:
    print("Sixteen is less than forty-two!")
print("A long time ago, in a galaxy far, far, away.....")

#codiing exercise 2.3

def nice_day(name):
    print("Have a nice day, " + name + "!")

nice_day("Marissa")

#coding exercise 2.7

name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")
favorite_movie = input("Enter your favorite movie: ")
mobile_number = int(input("Enter your 11-digit mobile number: "))
motto_in_life = input("Enter your motto in life: ")

#coding exercise 2.11

print(10>7)
print(str(73911))
print(tuple("Thank God it's Friday"))
print(float(4302))
print(int(3299.35640))

#coding exercise 3.4

class Customers:
    greeting = "Welcome to Coffee Palace!"
c_l = Customers()
c_l.name = "Samirah"
c_l.beverage = "Iced caffe latte"
c_l.food = "Cinnamon roll"
c_l.total = 225

c_2 = Customers()
c_2.name = "Jerry"
c_2.beverage = "Caramel macchiato"
c_2.food = "Glazed doughnut"
c_2.total = 230

print(Customers.greeting)
print(c_l.beverage)
print(c_2.food)

#coding exercise 3.8

print(217 * 6)
print(600 + 35234)
print(67 // 12)
print(56329 % 982)
print(34 ** 5)

#coding exercise 3.12

my_age = 22
mom_age = 61
sister_age = 29

print(mom_age < sister_age and my_age == 22)
print(mom_age == 61)
print(mom_age > 34 or sister_age == 22)
print(mom_age >= 54)
print(not(sister_age <= 400 and my_age == 22))

#coding exercise 4.4

x = 332
y = 2031
if x >= y:
    print("x is greater than or equal to y.")
elif x == y:
    print("x is equal to y.")
else:
    print("x is less than y.")


#coding exercise 4.8

furniture = ["table", "chair", "cabinet", "desk", "couch"]
for x in furniture:
    if x == "cabinet":
        continue
    print(x)


#-----------------------------------------------------

#Programming for Intermediate Users Using Python

#coding exercise 1.5

class Customers:
    greeting = "Welcome to Coffee Palace!"

    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total


c_1 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
c_2 = Customers("Elaine", "Strawberry frappuccino", "Tuna wrap", 270)
c_3 = Customers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
c_4 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c_5 = Customers("Paz", "Iced tea", "Blueberry pancakes", 315)

print(Customers.greeting)
print(c_2.name)
print(c_2.beverage)
print(c_2.food)
print(c_2.total)
print(c_4.name)
print(c_4.beverage)
print(c_4.food)
print(c_4.total)

#coding exercise 1.9

class ClubMembers:
    def __init__(self, birthday: object, age: object, favorite_food: object, goal: object) -> object:
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display1(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite food:", self.favorite_food)
        print("Goal:", self.goal)

class ClubOfficers(ClubMembers):
    #__init__ method of Admin subclass overrides __lnIt_method of User base class

    def __init__(self, name, birthday, age, favorite_food, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, favorite_food, goal)

    def display2(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite food:", self.favorite_food)
        print("Goal:", self.goal)
        print("Position:", self.position)

m_1 = ClubMembers("Tom", "January 16", 14, 'Ice cream', "To be happy")
o_4 = ClubOfficers("Vera", 'June 22', 16, 'Beef stroganoff', "To be the world's greatest chef", 'Treasurer')

m_1.display1()
o_4.display2()

#coding exercise 2.4

flavors = ["boots", "chocolate", "strawberry", "cookies n' cream", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"]
ice_cream = dict(zip(flavors, toppings))
print(ice_cream)

ice_cream["chocolate"] = "blueberries"
ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})
print(ice_cream)

#coding exercise 2.8

tryout_result = {"Carl": "passed", "Quentin": "failed", "John Y.": "passed", "Peter": "failed", "Max T.": "passed", "Joseph": "passed", "Jone": "failed", "Jorge": "failed", "George": "passed", "Ben": "passed", "Jerome": "passed", "Rick": "failed", "Max G.": "failed", "John P.": "failed", "Vince": "passed"}

print(tryout_result.get("Jorge"))

#coding exercise 3.4

f = open("pythonessay.txt", "w")
f.write("I like Python because it's very interesting.")
f = open("pythonessay.txt", "a")
f.write("\nI plan to learn data visualization.")
f.write("\nI want to work in the field of data science.")
f.write("\nI plan to make a better world for the future generation.")
f = open("pythonessay.txt", "r")
f.close()

#coding exercise 3.8
#Solution Step1
f = open("pythonessay.txt", "r")

#Solution Step2
f = open("pythonessay.txt", "r")
print(f.read())

#Solution Step3
f = open("pythonessay.txt", "r")
print(f.readline())

#Solution Step4
f = open("pythonessay.txt", "r")
for x in f:
    print(x)

#Solution Step5
import os
if os.path.exist("pythonessay.txt")
    os.remove("pythonessay.txt")
else:
    print("The file does not exist")

#coding exercise 3.12

#1
x = 500
if x > 100:
    raise Exception("This code will result in an error if x is bigger than 100")

#2
try:
    print(variable_1)
except:
    print("variable_1 is not yet defined")

#3
for ii in range(6):
    print("I'm so happy!")

#4
try:
    print(12*6)
except:
    print("This operation can't be performed.")
else:
    print("This operation can be performed.")

#5
best_burger = "Burger King"
number_2_burger = "McDonald's"

assert best_burger == "Burger King"
assert best_burger == "McDonald's"

#coding exercise 4.4


f = open("functionfile.py", "x")

def general_greeting():
    print("Hello, everyone!")

def personal_greeting(name):
    print("Hi," + name + "!")

def your_province(province):
    print("Oh, I heard " + province + "is a nice place!")

def get_Sum(x,y):
    print(x+y)

def get_Diff(x,y):
    print(x-y)

from functionfile import personal_greeting
from functionfile import your_province

personal_greetiing("Anna")
your_province("Pampanga")

#coding exercise 4.8
#1
help("modules")

#2
help("sched")


