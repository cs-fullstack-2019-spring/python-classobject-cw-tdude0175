def main():

    # problem1()
    # problem2()
    # problem3()
    # problem4()
    challenge()
# Create a class Dog.
# Make sure it has the attributes name, breed, color, gender.
# Create a function that will print all attributes of the class.
# Create an object of Dog in your problem1 function and print all of it's attributes.
class Dog:
    def __init__(self,name,breed,color,gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender
    def dogInfo(self):
        print(f"{self.name} is a {self.gender} {self.breed} with a {self.color} coat")
#         make it look pretty
def problem1():
    dogge = Dog("Dogge", "shishu","yellow","male")
    dogge.dogInfo()
#Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign,
# ask them to input another string
def problem2():
    userInput="-"
    while(userInput != "="):
        userInput = input("AND SO THERE WERE LOOPS AND WE WERE ALL CAUGHT IN THEM")
# you can check for type with [type(variable)] against the arguments [str] and [int]

# In your main file create three Person objects.
# Change the weight and height of each one.
# Afterwards, print the BMI (body mass index) of each Person.
# If you don’t know how to calculate BMI, look at the code I provided for you.
#
# Hint: BMI is (weight / (height * height)) x 703. Weight is in pounds and height is in inches.
#
# Extra:Put the three person objects in an array and use a loop to print out their BMIs.
class Person:
    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height
    def calBMI(self):
        print ((self.weight / (self.height * self.height))*703)

def problem3():
    person1 = Person("george", 220 , 67)
    person2 = Person("Rocky" , 300 , 60)
    person3 = Person("Mac" , 150 , 53)
    person1.calBMI()
    person2.calBMI()
    person3.calBMI()
    personlist = []
    personlist.append(person1)
    personlist.append(person2)
    personlist.append(person3)

    for person in personlist:
        person.calBMI()

#  Create a class Product that represents a product sold online.
#  A product has a name, price, and quantity.
#
# The class should have changeProduct:
# a) If changeProduct has one parameter, it can change the name of the product.
#
# b) If changeProduct has two parameters it can change the name and price of the product.
#
# c) If changeProduct has three parameters it can change the name, price, and quantity of the product.
#
# Create an object of Product in your problem4 function and print all of it's attributes.
class Product:
    def __init__(self,name ="",price = 0,quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def productInfo(self):
        print(f"{self.name} costs ${self.price} \n We have {self.quantity} in stock")
def problem4():
    cheese = Product("cheese",3,35)
    cheese.productInfo()
# Use a standard JavaScript template. In your main function create the array below:
# var squad = ["Bob", "John", "Bob", "Kenn", "Bob", "Kevin", "John", "Kevin"];
# Print how many times each name is present in the array.
def challenge():
    squad = ["Bob", "John", "Bob", "Kenn", "Bob", "Kevin", "John", "Kevin"];
    bobcount = 0
    johncount= 0
    kenncount= 0
    kevincount = 0
    for name in squad:
        if(name == "Bob"):
            bobcount +=1
        elif(name == "John"):
            johncount +=1
        elif(name == "Kenn"):
            kenncount +=1
        elif(name == "Kevin"):
            kevincount +=1
    print(f"Bob = {bobcount}\nJohn = {johncount}\nKenn = {kenncount}\nKevin = {kevincount}")
if __name__ == '__main__':
    main()