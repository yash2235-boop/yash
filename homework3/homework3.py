# 3.1

def say_goodbye(name):
    print("Hello","", name)

# say_goodbye("Yash") 

#3.2

def circle_area(radius):
    return print(3.14 * radius ** 2)

# circle_area(3)

#4.1

#function that subtracts one from another (b from a):
def subtract (a, b):
    difference = a - b
    return difference
# print(subtract(10,5))

# function that multiplies two numbers together
def multiply (a ,b):
    product = a * b
    return product
# print(multiply(10,5))

# function that divides one number by another (a by b)
def divide (a,b):
    quotient = a / b
    return quotient
# print(divide(10,5))

#5.1
readings = [15, 14, 17, 20, 23, 28, 20]
def temp_min_max (readings):
    max_temp = max(readings)
    min_temp = min (readings)
    result = (min_temp, max_temp)
    return (result), type(result)
# print (temp_min_max(readings))

#5.2
def is_weekend (day_number): #takes an input of the day as a number and returns if it is the weekend.
#Does not account for invalid inputs like day_number greater than 7 or less than 1
    if day_number == 6 or day_number == 7:
        return True
    else:
        return False

# print(is_weekend(2))

#5.3



def fuel_efficiency (distance_miles, fuel_gallons): #enter distance in miles and fuel in gallons. Calculates fuel efficiency (miles/gallon)
     efficiency = distance_miles / fuel_gallons
     return efficiency

# print (fuel_efficiency(10, 2), "miles per gallon")

#5.4 
def encrypt_data (number):
    length_number = len(str(number))
    last_digit = number % 10
    remaining_digits = number // 10
    encrypted_data = last_digit * (10 **(length_number-1)) + remaining_digits
    return encrypted_data

# print(encrypt_data(2431))

#6.1
def power_calculator (x, y):
    product = 1
    for i in range (y):
        product *= x
        
    return product

# print (power_calculator(4,3))

#6.2
list_integers = [1,3,6,10,8,5,4]

#6.2.1
def min_with_for (list_integers):
    x_min = list_integers[0]
    for i in list_integers:
        if i < x_min:
            x_min = i
    return x_min

# print ("The result of finding the minimum value using a for loop is:", min_with_for(list_integers))


def max_with_for (list_integers):
    x_max = 0
    for i in list_integers:
        if i > x_max:
            x_max = i
    return x_max

# print (max_with_for(list_integers))

#6.2.2

def min_with_while (list_integers):
    x2_min = list_integers[0]
    i = 1
    while i < len(list_integers):
        if list_integers[i] < x2_min:
            x2_min = list_integers[i]
        
        i+= 1
    return x2_min
# print(min_with_while(list_integers))

def max_with_while (list_integers):
    x2_max = list_integers[0]
    i = 1
    while i < len(list_integers):
        if list_integers[i] > x2_max:
            x2_max = list_integers[i]
        
        i+= 1
    return x2_max
# print(max_with_while(list_integers))

#6.3
def sum_integer (integer_input):
   total = 0
   while integer_input > 0:
       digit = integer_input % 10
       total += digit
       integer_input //= 10
   return total

# print(sum_integer(2488))


