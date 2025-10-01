#3 - Lists
#3.1
fav_food = ['pasta', 'pizza', 'sushi', 'burrito', 'hummus']
# print(fav_food[1])
# print(fav_food[-1])
# fav_food.append ("mango")
# fav_food.insert(0,"apple")
# fav_food.remove("sushi")
# print(len(fav_food))
# # print(fav_food)

# for food in fav_food:
    # print (food.upper())


# new_fav_food = [fav_food[0], fav_food[-1]]
# print (new_fav_food)


# if "potato" in fav_food  or "Potato" in fav_food :
        # print ("A potato!")
# else:
        # print("No Potato")

#3.2
numbers = list(range(0,21))
# print(numbers)
def get_first_15(numbers):
       return (numbers[:15])
# print(get_first_15(numbers))

list1 = get_first_15(numbers)

def get_every_5th(lst):
       return (lst[::5])
# print(get_every_5th(list1))

list2 = get_every_5th(list1)

def reverse_and_stride(lst):
       reversed_list = list2[::-1]
       every_third_element = reversed_list[::3]
       return every_third_element

# print(reverse_and_stride(list2))

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)
# print(step3)

#3.3
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

# print(numbers[2])
# print(numbers[1][1])
# numbers.append ([10, 11, 12])
# # print (numbers)

def sum_nested (numbers):
       total = 0
       for row in numbers:
              for digit in row:
                     total += digit
       return(print(total))

# sum_nested(numbers)

# 3.4
def create_matrix ():
       matrix = []
       num = 1
       for i in range (5):
              row = []
              for j in range (5):
                     row.append(num)
                     num += 1
              matrix.append (row)
       return matrix

matrix1 = create_matrix()
# print(matrix1)

def replace_with_question (matrix1):
       for row in matrix1:
              for i in range(len(row)):
                     if row[i] % 3 == 0:
                            row[i] = "?"

       return (matrix1)

# updated_matrix1 = replace_with_question(matrix1)
# print(updated_matrix1)

def sum_non_question (updated_matrix1):
       total = 0
       for rows in updated_matrix1:
              for i in range (len(rows)):
                     if rows [i] != "?":
                            total += rows[i]
       
       return total

# print(sum_non_question(updated_matrix1))

#4

#4.1 
ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

# print (ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
# 
del ages["Mariam"]
# print(ages)
# for key, value in ages.items():
#     print(f"{key} = {value}"  )

for key in ages:
    print(f"{key}")