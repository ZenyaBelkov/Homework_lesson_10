from math import pi, sqrt


# TASK 1
print("TASK 1 \n")


class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f"You have a {self.taste} soda"
        else:
            return "You have a simple soda"


taste = str(input("Enter the taste of soda: "))
soda = Soda(taste)
print(soda.__str__())


# TASK2
print("TASK 2 \n")


class Math:

    def addition(self, val_1, val_2):
        return f"The result of addition: {val_1 + val_2}"

    def subtraction(self, val_1, val_2):
        return f"The result of subtraction: {val_1 - val_2}"

    def multiplication(self, val_1, val_2):
        return f"The result of multiplication: {val_1 * val_2}"

    def division(self, val_1, val_2):
        return f"The result of division: {val_1 / val_2}"


result = Math()
print(result.addition(val_1=5, val_2=4))
print(result.subtraction(val_1=5, val_2=4))
print(result.multiplication(val_1=5, val_2=4))
print(result.division(val_1=5, val_2=4))


# TASK 3
print("TASK 3 \n")


class Car:

    def __init__(self, color, type, date):
        self.color = color
        self.type = type
        self.date = date

    def take_on(self):
        return "Your car is taken on"

    def take_off(self):
        return "Your car is taken off"

    def date_of_release(self, date):
        self.date = date
        return f"Your car was released in {self.date}"

    def type_of_car(self, type):
        self.type = type
        return f"The type of your car is {self.type}"

    def color_of_car(self, color):
        self.color = color
        return f"The color of your car is {self.color}"


date = int(input("Enter the year of your car: "))
type = str(input("Enter the type of your car: "))
color = str(input("Enter the color of your car: "))

car = Car(date, type, color)
print(car.take_on())
print(car.take_off())
print(car.date_of_release(date))
print(car.type_of_car(type))
print(car.color_of_car(color))


# TASK 4
print("TASK 4 \n")


class Sphere:
    def __init__(self, radius=None, x=None, y=None, z=None, R=None):
        self.__radius = radius
        self.__x = x
        self.__y = y
        self.__z = z
        self.__R = len(radius) - 1

    def __str__(self):
        if self.__radius and self.__x and self.__y and self.__z:
            return f"Radius: {self.__radius} cm\nx: {self.__x}\ny: {self.__y}\nz: {self.__z}"
        elif self.__radius:
            self.__radius = radius
            self.__x = 0
            self.__y = 0
            self.__z = 0
            return f"Radius: {self.__radius} cm\nx: {self.__x}\ny: {self.__y}\nz: {self.__z}"
        else:
            self.__radius = 1
            self.__x = 0
            self.__y = 0
            self.__z = 0
            self.__R = 0.5
            return f"Radius: {self.__radius} cm\nx: {self.__x}\ny: {self.__y}\nz: {self.__z}"

    def get_volume(self):
        volume = (4/3) * pi * (int(self.__radius) ** 3) - (4/3) * pi * (self.__R ** 3)
        return f"The volume of the sphere is: {volume} cm3"

    def get_square(self):
        square = 4 * pi * (self.__R ** 2)
        return f"The square of the sphere surface is: {square} cm2"

    def get_radius(self):
        return f"The radius of the current sphere: {self.__radius} cm"

    def get_center(self):
        cortege = (self.__x, self.__y, self.__z)
        return f"the center of the sphere is: {cortege}"

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            raise Exception("value can't be less than 0")

    def set_center(self, x, y, z):
        if x and y and z >= 0:
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            raise Exception("value can't be less than 0")

    def is_point_inside(self, point_x=None, point_y=None, point_z=None):
        print("Coordinates of point in the sphere")

        distance = sqrt((int(point_x) - self.__x)**2 + (int(point_y) - self.__y)**2 + (int(point_z) - self.__z)**2)

        if distance < self.__radius:
            print("The point is inside the sphere")
            return True
        elif distance == radius:
            print("The point is on the surface of the sphere")
            return True
        else:
            print("The point is outside the sphere")
            return False


radius = input("Enter the radius of the sphere: ")
x = input("Enter x: ")
y = input("Enter y: ")
z = input("Enter z: ")

sphere = Sphere(radius, x, y, z)

print(sphere.__str__())
print(sphere.get_volume())
print(sphere.get_square())
print(sphere.get_radius())
print(sphere.get_center())

sphere.set_radius(15)
print(sphere.get_radius())
sphere.set_center(5, 6, 7)
print(sphere.get_center())

point_x = input("Enter x: ")
point_y = input("Enter y: ")
point_z = input("Enter z: ")

print(sphere.is_point_inside(point_x, point_y, point_z))


# TASK 5
print("TASK 5 \n")


class SuperStr(str):

    def is_repeatance(self, s):
        if str(self) == "":
            return False
        elif s =="":
            return True
        elif len(str(self)) % len(s) != 0:
            return False
        else:
            num_repeats = len(str(self)) // len(s)
            return str(self) == s * num_repeats

    def is_palindrome(self):
        if str(self).lower() == str(self).lower()[::-1]:
            return True
        else:
            return False


s = SuperStr("hello")
print(s.is_repeatance("lo"))
print(s.is_repeatance("o"))
print(s.is_palindrome())
