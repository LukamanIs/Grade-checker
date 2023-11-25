
#This is what I use to tell the user if they want to start the code again or quit it
def start():
    start = True
    while start == True:
        ver = ''
        ver = input("do you wish to continue? [ yes or no ]: ")
        if ver == "yes":
            break
        if ver == "no":
            quit()

#This function is to ask the useer for the number of assignment they have or what to check    
def number_of_assign():
    asig = int()
    asig = int(input('Enter the number of assignment: '))
    return asig

#This will fill the grade that the user will type manual
def fill_grades(grade,assignment):
    for index in range(0,assignment):
        grade[index] = float(input("Enter your assignment grades: "))
    return grade[index]

#This function is calulating the grade between all the grade that got fill in and getting the total 
def calulate_grades(grade):
    total1 = 0.0
    for num in grade:
        total1 += num
    return total1

# This is finding the average of the grade
def find_average(total,assignment):
    average = total/assignment
    rounded_average = round(average,2)
    return rounded_average

# I use this to tell the user what grade they got in the class with the assignment they did
def find_grade(average):
    if average >= 90.0:
        print("A")
    elif average >= 80.0:
        print("B")
    elif average >= 70.0:
        print("C")
    elif average >= 60.0:
        print("D")
    else:
        print("F")

#This main is for what grade the user got in the class and I put it all here to look better together        
def main():
    assignment = number_of_assign()
    grade = [float()] * assignment
    fill_grades(grade,assignment)
    total = calulate_grades(grade)
    average = find_average(total,assignment)
    print(average)
    f_grade = find_grade(average)
    
#I am now going to start writing a different code that will find what you will get in the simulator for all the classes you took and get the GPA from it.

# This is finding how much class I took
def class_taken():
    class_1 = int(input("how much classes did you take? : "))
    return class_1

# This is asking the user for the grades they got for each classes
def simister_grade(classes):
    letter_grade = [""] * classes
    for index in range(0,classes):
        letter_grade[index] = input("What grade did you get in the class: ").upper()
    return letter_grade

#I am now replacing my value with a new value that people use to calulate their grades with
def replace_value(my_list, old_value, new_value):
   index = my_list.index(old_value)
   my_list[index] = new_value

# This code checks I have the letter in my list
def check_value_in_list(my_list, value_to_check):
    return value_to_check in my_list


# This is the second main function I use to put all the code in 
def main2():
    classes = class_taken()
    letter = simister_grade(classes)
    
    for i in range(0,classes):
        value_to_check = 'A'
        if check_value_in_list(letter, value_to_check):
            replace_value(letter,"A",4)
    
    for i in range(0,classes):
        value_to_check = 'B'
        if check_value_in_list(letter, value_to_check):
            replace_value(letter,"B",3)

    for i in range(0,classes):
        value_to_check = 'C'
        if check_value_in_list(letter, value_to_check):
            replace_value(letter,"C",2)
            
    for i in range(0,classes):
        value_to_check = 'D'
        if check_value_in_list(letter, value_to_check):
            replace_value(letter,"D",1)
    
    for i in range(0,classes):
        value_to_check = 'F'
        if check_value_in_list(letter, value_to_check):
            replace_value(letter,"F",0)

    total = calulate_grades(letter)
    average = find_average(total,classes)
    print("Your GPA is",average)



# I made my third and last main function to put both the main function in to ask the user to choose from both of them 
def main3(main,main2):
    ask = ""
    for ask in range(0,2):
        ask = input("what do you want to check (G for Grade or PA for GPA): ").upper()
        if ask == "G":
            main()
        elif ask == "PA":
            main2()
        else:
            print("You Enter the wrong thing try again")
        start()
main3(main,main2)







