#--------------------------------------------------------------------------------------------------------------------------------------------
#Introductory Info
#--------------------------------------------------------------------------------------------------------------------------------------------
import random
import time
correct_Answers = 0
wrong_Answers = 0

print('---' *40)
print("~~ \('v')/ Welcome to our game - PYTHONS and LADDERS \('v')/ ~~")
print('---' *40)
time.sleep(1)

print('~~~' *10)
print("YOUR OBJECTIVE:")
print('~~~' *10)
time.sleep(1)
print('Your goal is to reach the end of the board as fast as you can through dice rolls, answering questions on Python variables along the way!')
time.sleep(1)
print('Alternatively, if you manage to answer all the questions, the game also ends.') 
print('\n')
print('The number of questions you got right or wrong would also be displayed to you along the way ~')
print('\n')
time.sleep(1)

print('~~~' *20)
print("Before we start, here is some introductory info:")
print('~~~' *20)
print('...')
time.sleep(1)
print("Variables are values which are stored in reserved memory locations.")
print("This means that when you create a variable you reserve some space in the memory."+"\n")
time.sleep(1)

#--------------------------------------------------------------------------------------------------------------------------------------------
#Introduction to Python variables - By Derrick
#--------------------------------------------------------------------------------------------------------------------------------------------

flag = True
question_list = ["question_1", "question_2", "question_3", "question_4", "question_5"]

"""This function reacts to correct and incorrect answer"""
def result(answer):
    global correct_Answers
    global wrong_Answers 
    if answer == "True":
        correct_Answers += 1
        print("Correct !!! You are such a genius!")
        print('\n')
    else:
        wrong_Answers += 1
        print("You are wrong, mate.")
        print('\n')
     

"""This user checks the answer of the question asked.
The 'user_input' is the answer given by the user and the 'mode' is the type of question it belongs to.
There are two types of question in this part, the first type is 'y' is the correct answer, the second type is 'n' is the correct answer."""
def check(userinput, mode):
    global flag
    if mode == 1:
        if userinput == "y":
            result("False")
            flag = False
        elif userinput == "n":
            result("True")
            flag = False
        else:
            print("\n"+"Can you read the instruction properly? Try again !!!")
            flag = True
    elif mode == 2:
        if userinput == "y":
            result("True")
        elif userinput == "n":
            result("False")
        else:
            print("\n"+"Can you read the instruction properly? Try again !!!")
    else:
        print("Error when calling check function(mode).")

"""This function shows the question and asks for the answer from the user.
The parameter 'number' is obtained from the random shuffle of the list that contains 5 questions."""
def introduction(number):
    global flag
    flag = True
    if number == 1:
        while flag:
            print('~~~' *10)
            print("Loading your question.")
            print('~~~' *10)
            time.sleep(1)
            print("...")
            time.sleep(1)
            question1 = input("Since variables store values in the memory, this suggests that variables can only store numbers. Is this right? (y/n): ")
            print('\n')
            check(question1,1)
            flag
        print('~~~' *15)    
        print("Loading the explanation.")
        print('~~~' *15)
        time.sleep(1)
        print("\n"+"Explanation:")
        time.sleep(1)
        print("Variables can store any data types ranging from integers, floating numbers to lists.")
        print("")

    elif number == 2:
        while flag:
            print('~~~' *10)
            print("Loading your question.")
            print('~~~' *10)
            time.sleep(1)
            print("...")
            time.sleep(1)
            
            question2 = input("An integer (eg 100) can be assigned to a variable. But when a string (e.g 'apple') is assigned to it, the Python shell will cause an error. Is this true? (y/n): ")
            print('\n')
            check(question2,1)
        print('~~~' *15)    
        print("Loading the explanation...")
        print('~~~' *15)
        time.sleep(1)
        print("\n"+"Explanation:")
        time.sleep(1)
        print("It will not cause an error because the type of the variable is not fixed. Values of different types can be assigned freely.")
        print("")

    elif number == 3:
        while flag:
            print('~~~' *10)
            print("Loading your question.")
            print('~~~' *10)
            time.sleep(1)
            print("...")
            time.sleep(1)
            
            print("Let's say we want to assign 5 to a variable. Check if the following assignment statements are true. Enter 'y' if true and 'n' if false.")
            print('\n')
            question3 = input("'value <= 5' : ")
            check(question3,1)

            question4 = input("'value == 5' : ")
            check(question4,1)

            question5 = input("'value = 5' : ")
            check(question5,2)
        print('~~~' *15)    
        print("Loading the explanation...")
        print('~~~' *15)
        time.sleep(1)
        print("\n"+"Explanation:")
        time.sleep(1)
        print("We only put one equal sign. One equal sign is a proper away of assigning a value to a variable.")
        print("")

    elif number == 4:
        while flag:
            print('~~~' *10)
            print("Loading your question.")
            print('~~~' *10)
            time.sleep(1)
            print("...")
            time.sleep(1)
            
            print("Check if the variable assignment below uses a valid name. Enter 'y' if valid and 'n' if invalid.")
            print('\n')
            question6 = input("Let's say we want to assign 5 to the variable: 'None = 5'. Is this right? (y/n): ")
            print('\n')
            check(question6,1)
            time.sleep(1)
        #Flag is set to true here because the value of flag is false after the above part
        #We now initiate following question
        flag = True
        while flag:
            question7 = input("Let's say we want to assign 5 to the variable: '2number = 10'. Is this right? (y/n): ")
            print('\n')
            check(question7,1)
        print('~~~' *15)
        print("Loading the explanation...")
        print('~~~' *15)
        time.sleep(1)
        print("\n"+"Explanation:")
        time.sleep(1)
        print("For the first question, you cannot use None as a variable because None is a reserved word.")
        print("For the second question, you cannot start a variable name with a digit.")
        print("")

    elif number == 5:
        while flag:
            print('~~~' *10)
            print("Loading your question.")
            print('~~~' *10)
            time.sleep(1)
            print("...")
            time.sleep(1)
            
            print("Check if the variable assignment below uses a valid name. Enter 'y' if valid and 'n' if invalid.")
            print('\n')
            question8 = input("Let's say we want to assign 5 to the variable: 'pass = 5'. Is this right? (y/n): ")
            print('\n')
            check(question8,1)
        #Flag is set to true here because the value of flag is false after the above part
        #We now initiate following question
        flag = True
        while flag:    
            question9 = input("Let's say we want to assign 5 to variable: 'value5.0 = 5'. Is this right? (y/n): ")
            print('\n')
            check(question9,1)
        print('~~~' *15)    
        print("Loading the explanation...")
        print('~~~' *15)
        time.sleep(1)
        print("\n"+"Explanation:")
        time.sleep(1)
        print("For the first question, you cannot use 'pass' as a variable because 'pass' is a reserved word in Python.")
        print("For the second question, a variable name cannot have any element other than letters, digits and underscore.")
        print("")
    else:
        print("Error when calling introduction function")


"""This function shuffles the 'question_list' and get any random question.
This function then removes the question off the list to prevent repetition of the similar question."""
def choose_question():
    question_num = random.choice(question_list)
    if question_num == "question_1":
        introduction(1)
        
    elif question_num == "question_2":
        introduction(2)

    elif question_num == "question_3":
        introduction(3)
           
    elif question_num == "question_4":
        introduction(4)

    elif question_num == "question_5":
        introduction(5)
           
    question_list.remove(question_num)

    

#--------------------------------------------------------------------------------------------------------------------------------------------
#Variable names - By Nicholas
#--------------------------------------------------------------------------------------------------------------------------------------------

#This section lists the questions with matching multiple choice-answers.

#This question focuses on the case-sensitivity of variables.
question_1 = "Given these variables: variable_name = 0, Variable_Name = 0, and VARIABLE_NAME = 0, which one of these statements is true?"
options_1 = ['A: All three variables are the same.','B: All three variables are different.','C: variable_name = 0 and Variable_Name = 0 are the same.', 'D: Variable_Name = 0 and VARIABLE_NAME = 0 are the same.']



#This question focuses on the relationship between in-built functions and variables.    
question_2 = "Given these variables: False = 10 and World = 10, which one of these statements is true?"
options_2 = ['A: Both variables are valid.','B: Both variables are not valid.','C: World = 10 is valid, False = 10 returns an error.', 'D: False = 10 is valid, World = 10 returns an error.']



#This question focuses on the naming conventions of variables, specifically beginning them with numbers or symbols.
question_3 = "Given these variables: 2018_Monash = 'Hello!' and @_Monash = 'Hello!', which one of these statements is true?" 
options_3 = ['A: Both variables are not valid.','B: Both variables are valid.','C: 2018_Monash = "Hello!" is valid, #_Monash = "Hello!" returns an error.', 'D: #_Monash = "Hello!" is valid, 2018_Monash = "Hello!" returns an error.']



#This question focuses on the naming conventions of variables, specifically beginning them with letters or underscores.
question_4 = "Given these variables: _Python = 'Snake!' and A_Python = 'Snake!', which one of these statements is true?" 
options_4 = ['A: Both variables are not valid.','B: Both variables are valid.','C: _Python = "Snake!" is valid, A_Python = "Snake!" returns an error.', 'D: A_Python = "Snake!" is valid, _Python = "Snake!" returns an error.']


#This question combines concepts of the case-sensitivity and in-built functions with variables.
question_5 = "Given these variables: Break = 'Stop the loop!', break = 'Stop the loop!', which one of these statements is true?"
options_5 = ['A: Both variables are not valid.','B: Both variables are valid.','C: break = "Stop the loop!" is valid, Break = "Stop the loop!" returns an error.', 'D: Break = "Stop the loop!" is valid, break = "Stop the loop!" returns an error.']


input_Statement = 'Please type in the letter of the option you selected (A, B, C, or D): '

    
#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#This section compiles the questions and multiple choice into functions.
#print('\n') is used as spacing between printed lines in the IDLE while time.sleep() is used to provide delays between the printed statements.
#This is done to improve readability in the IDLE.

def Question_One():
    global correct_Answers
    global wrong_Answers
    
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
        
    print(question_1)
    print('\n')
    time.sleep(1)
    for answers in options_1:
        print(answers)
    print('\n' )
    time.sleep(1)
    user_Input = input(input_Statement)
    print('\n')

    if user_Input.lower() == 'b':
        correct_Answers += 1 
        print("Correct!")
        print('\n')
        time.sleep(1)
       
    elif user_Input.lower() != 'b':
        wrong_Answers += 1
        print("Incorrect!")
        print('\n')
        time.sleep(1)

    print('~~~' *15)
    print("Loading your explanation.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print('Correct answer: B. Variables are case sensitive, so different usage of capitals would indicate a different variable.')
    print('\n')
    time.sleep(1)
    
        

def Question_Two():
    global correct_Answers
    global wrong_Answers
    
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print(question_2)
    print('\n')
    time.sleep(1)
    for answers in options_2:
        print(answers)
    print('\n')
    time.sleep(1)
    user_Input = input(input_Statement)
    print('\n')

    if user_Input.lower() == 'c':
        correct_Answers += 1
        print("Correct!")
        print('\n')
        time.sleep(1)
    
    elif user_Input.lower() != 'c':
        wrong_Answers += 1
        print("Incorrect!")
        print('\n')
        time.sleep(1)

    print('~~~' *15)
    print("Loading your explanation.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Correct answer: C. False is an in-built function of Python, so it cannot be used as a variable. World = 10 can be used as a variable as there is no in-built function for it.")
    print('\n')
    time.sleep(1)

    
def Question_Three():
    global correct_Answers
    global wrong_Answers
    
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print(question_3)
    print('\n')
    time.sleep(1)
    for answers in options_3:
        print(answers)
    print('\n')
    time.sleep(1)
    user_Input = input(input_Statement)
    print('\n')

    if user_Input.lower() == 'a':
        correct_Answers += 1
        print("Correct!")
        print('\n')
        time.sleep(1)
    
    elif user_Input.lower() != 'a':
        wrong_Answers += 1
        print("Incorrect!")
        print('\n')
        time.sleep(1)

    print('~~~' *15)
    print("Loading your explanation.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Correct answer: A. When naming variables in Python, you cannot begin them with a number or symbol/special character.")
    print('\n')
    time.sleep(1)
    

def Question_Four():
    global correct_Answers
    global wrong_Answers
    
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print(question_4)
    print('\n')
    time.sleep(1)
    for answers in options_4:
        print(answers)
    print('\n')
    time.sleep(1)
    user_Input = input(input_Statement)
    print('\n')

    if user_Input.lower() == 'b':
        correct_Answers += 1
        print("Correct!")
        print('\n')
        time.sleep(1)
    
    elif user_Input.lower() != 'b':
        wrong_Answers += 1
        print("Incorrect!")
        print('\n')
        time.sleep(1)
    
    print('~~~' *15)
    print("Loading your explanation.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Correct answer: B. When naming variables in Python, you can start them with an underscore (_) or letter.")
    print('\n')
    time.sleep(1)
    

def Question_Five():
    global correct_Answers
    global wrong_Answers
    
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print(question_5)
    print('\n')
    time.sleep(1)
    for answers in options_5:
        print(answers)
    print('\n')
    time.sleep(1)
    user_Input = input(input_Statement)
    print('\n')

    if user_Input.lower() == 'd':
        correct_Answers += 1
        print("Correct!")
        print('\n')
        time.sleep(1)
    
    elif user_Input.lower() != 'd':
        wrong_Answers += 1
        print("Incorrect!")
        print('\n')
        time.sleep(1)
        
    print('~~~' *15)
    print("Loading your explanation.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Correct answer: D. break = 'Stop the loop!' is invalid as it is an in-built function. Break = 'Stop the loop' is valid because variables are case sensitive.")
    print('\n')
    time.sleep(1)
#_______________________________________________________________________________________________________________________________________________________

#This function randomly selects a question to be displayed for the user to answer. The questions would not be repeated when already asked.

i = 0
question_List = [question_1, question_2, question_3, question_4, question_5]

def variable_Names():
    i = 0
    while i < 1:
        random.shuffle(question_List)

        if question_List[0] == question_1:
            Question_One()
            
        elif question_List[0] == question_2:
            Question_Two()
            
        elif question_List[0] == question_3:
            Question_Three()
           
        elif question_List[0] == question_4:
            Question_Four()
            
        elif question_List[0] == question_5:
            Question_Five()
           
        del question_List[0]
        i += 1


        
#--------------------------------------------------------------------------------------------------------------------------------------------
# Code by JuhWan
#--------------------------------------------------------------------------------------------------------------------------------------------
        
#Added
import random
questionlist = ["question_1", "question_2", "question_3", "question_4", "question_5"]
    
#Question No.1
def Quest1():
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)

    Question1=input("Is it possible to use special characters(Ex. @, %, & etc.) in variables? (True/False): ").lower()
    print('\n')
    time.sleep(1)

    def answer1(x):
        global correct_Answers
        global wrong_Answers
    
        while True:
            if x == "true":
                wrong_Answers += 1
                print("Unfortunately, you got the wrong answer.")
                print('\n')
                time.sleep(1)
                break
            elif x == "false":
                correct_Answers += 1
                print("Congratulations! You are correct!.")
                print('\n')
                time.sleep(1)
                break
            else:
                print("Please try again.")
                print('\n')
                time.sleep(1)
                x = input('Type "true" or "false" as your answer')
            
    answer1(Question1)
    print('~~~' *15)
    print("Loading your explanation.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Variables cannot contain special characters.")
    print('\n')
    time.sleep(1)
  

#Question No.2
def Quest2(): 
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)

    print("Which of these cannot be a variable?")
    print('\n')
    time.sleep(1)
    print("1. p")
    print("2. PYT0N")
    print("3. 5yTon")
    print("4. py_24")
    print('\n')
    time.sleep(1)
    Question2=input('Type in the number of your answer:')
    print('\n')
    time.sleep(1)
    
    def multi2(x):
        global correct_Answers
        global wrong_Answers

        while True:
            if x == "3":
                correct_Answers += 1
                print("Congratulations! You are correct!")
                print('\n')
                time.sleep(1)
                break
            elif x == "1" or x == "2" or x == "4":
                wrong_Answers += 1
                print("Unfortunately, you got the wrong answer.")
                print('\n')
                time.sleep(1)
                break
            else:
                print("Please try again, type the number only.")
                print('\n')
                time.sleep()
                x = input('Type in the number of your answer:')           

    multi2(Question2)
    print('~~~' *15)
    print("Loading your explanation.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Python variable names cannot begin with a number.")
    print('\n')
    time.sleep(1)


#Question No.3
def Quest3():
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print("If 'a = 10' and 'b = a',")
    Question3 = input("is a the same as b'? (True/False): ").lower()
    print('\n')
    time.sleep(1)
    
    def answer3(x):
        global correct_Answers
        global wrong_Answers

        while True:
            if x == "true":
                correct_Answers += 1
                print("Congratulations! You are correct!")
                print('\n')
                time.sleep(1)
                break
            elif x == "false":
                wrong_Answers += 1
                print("Unfortunately, you got the wrong answer.")
                print('\n')
                time.sleep(1)
                break
            else:
                print("Please try again")
                print('\n')
                time.sleep(1)
                x = input('Type "true" or "false" as your answer')
                
    answer3(Question3)
    print('~~~' *15)
    print("Loading your explanation.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("b = a, so a and b are the same. Therefore, a is b.")
    print('\n')
    time.sleep(1)
    

#Question No.4
def Quest4():
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print("If you want to make the variable 'x = 10', to 'x = 20'. What should you do?")
    print('\n')
    time.sleep(1)
    print("1. x + 10")
    print("2. x += 10")
    print("3. 2*x")
    print('\n')
    time.sleep(1)
    Question4 = input('Type in the number of your answer:')
    print('\n')
    time.sleep(1)
    
    def multi4(x):
        global correct_Answers
        global wrong_Answers

        while True:
            if x == "2":
                correct_Answers += 1
                print("Congratulations! You are correct!")
                print('\n')
                time.sleep(1)
                break
            elif x == "1" or x == "3":
                wrong_Answers += 1
                print("Unfortunately, you got the wrong answer.")
                print('\n')
                time.sleep(1)
                break
            else:
                print("Please try again, type the number only.")
                print('\n')
                time.sleep(1)
                x = input('Type in the number of your answer:')
                
    multi4(Question4)
    print('~~~' *15)
    print("Loading your explanation.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Only option 2 changes the value of variable x, the others do not.")
    print('\n')
    time.sleep(1)


#Question No.5
def Quest5():
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print("Given these options:")
    print('\n')
    print("a = [x, y, z]")
    print("b = [x, y, z]")
    print('\n')
    time.sleep(1)
    Question5 = input("Are 'a is b' and 'a == b' same? (True/False) ").lower()
    print('\n')
    time.sleep(1)

    def answer5(x):
        global correct_Answers
        global wrong_Answers

        while True:
            if x == "true":
                wrong_Answers += 1
                print("Unfortunately, you got the wrong answer.")
                print('\n')
                time.sleep(1)
                break
            elif x == "false":
                correct_Answers += 1
                print("Congratulations, you are correct!")
                print('\n')
                time.sleep(1)
                break
            else:
                print("Please try again")
                print('\n')
                time.sleep(1)
                x = input('Type "true" or "false" as your answer')
                

    answer5(Question5)
    print('~~~' *15)
    print("Loading your explanation.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Both variables have the same value assigned to them but they are independent. 'a == b' checks for the SAME VALUE while 'a is b' checks whether both variables are referring to the SAME OBJECT (same memory location).")
    print('\n')
    time.sleep(1)
    
#____________________________________________________________________________________________________________________________________________________________   

#Added
def chooseQuestion():
    question_num = random.choice(questionlist)
    if question_num == "question_1":
        Quest1()
        
    elif question_num == "question_2":
        Quest2()

    elif question_num == "question_3":
        Quest3()
           
    elif question_num == "question_4":
        Quest4()

    elif question_num == "question_5":
        Quest5()
           
    questionlist.remove(question_num)


    
#--------------------------------------------------------------------------------------------------------------------------------------------
#By EuZin
#--------------------------------------------------------------------------------------------------------------------------------------------

questionList = ["question_1", "question_2", "question_3", "question_4", "question_5"]

#Question 1
def question1():
    print('~~~' *15)
    print("Here is some prior info you should know...")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print("CHOICES: 100, 0.1, John")
    print('\n')
    time.sleep(1)
    print("QUESTION REQUIREMENTS: ")
    print('\n')
    time.sleep(1)
    print("Please assign the correct values or names from \n"\
          "the choices above to the questions below: \n")
    time.sleep(1)

    #Question Parts
    partA = "i)The maximum marks you can score in an exam?"
    partB = "ii)The accuracy of a lab thermometer?"
    partC = "iii)The name of a boy \n"

    #Part A Code
    print('~~~' *15)
    print("Loading PART 1 of your question.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print("QUESTION: ")
    print(partA)
    ans = str(100)
    hint = "Make sure you keyed in the actual numbers (integer form) and not spell them. \n"
    guide = " Take note: Integer numbers are numbers which contain no decimals \n"
    explanation = "Correct answer: 100. This is known as integer assignment, where you \n"\
                  "assign integer values to a variable, in this case \n"\
                  "you assigned maximumMarks = 100. It shouldn't be spelled \n"\
                  "out 'one hundred' as that is known as a string. \n"\
                  "The appropriate assignment should be \n"\
                  "written as: maximumMarks = 100 \n"\
            
    life(guide,ans,hint,explanation)
    print('\n')
    time.sleep(1)

    print('~~~' *15)
    print("Loading PART 2 of your question.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)

    print("QUESTION: ")
    time.sleep(1)
    print(partB)
    ans = str(0.1)
    hint = "This is a decimal value answer \n"
    guide = "Take Note: A decimal number is known as a 'float' in Python \n"
    explanation = "Correct answer: 0.1. This is known as a float assignment, where you assign \n"\
                  "a decimal value to a variable. \n"\
                  "The correct syntax when it comes to coding should be written \n"\
                  "as: thermometerAccuracy = float(0.1) or thermometerAccuracy = 0.1.\n"\
                  "You cannot key in an string to a float function as \n"\
                  "this will cause an error."
    life(guide,ans,hint,explanation)
    print('\n')
    time.sleep(1)
    
    print('~~~' *15)
    print("Loading PART 3 of your question.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)

    print("QUESTION: ")
    time.sleep(1)
    print(partC)
    ans = "john"
    hint = "It's a common name"
    guide = "Take Note: A name is which consists of all alphabets is known as \n"\
            "a 'String' in Python"
    explanation = "Correct answer: John. This is known as a String assignment where Strings are \n"\
                  "characters which are enclosed in a single or double colon. \n"\
                  "For instance, 'This is a string' and ''Th1s 15 a1s0'' a string."
    life(guide, ans,hint, explanation)
    
#-------------------------------------------------------------------------------
#QUESTION 2
def question2():
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    a,b,c = "20","99","100"
    print("a,b,c = 20,99,100")
    print('\n')
    time.sleep(1)
    print("What will be printed if the function 'print(b)' is called?")
    time.sleep(1)
    print("Please select A, B, C or D.")
    print(" ")
    time.sleep(1)
    print("A) 20 \n"
          "B) Error \n"
          "C) 99\n"
          "D) 100 \n")
    ans = "c"
    hint = "The index of the variables are corresponded to the values"
    guide = "Take Note: This is multiple assignment of variables"
    explanation = "Correct answer: C. This is known as a multiple assignment of variables. \n"\
                  "The first variable on the LHS of the equation represents \n"\
                  "the first item on the RHS of the equation. You can assign \n"\
                  "as many variables as you like in a single line."
    
    life(guide,ans,hint,explanation)
      

#----------------------------------------------------------------------------------
 #QUESTION 3
def question3():
    print('~~~' *25)
    print("Here is some background info before answering the question.")
    print('~~~' *25)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print("The data stored in memory can be of many types. \n"\
          "For example, a person's age is stored as a numeric \n"\
          "value and his or her address is stored as alphanumeric \n"\
          "characters. Python has various standard data types that \n"\
          "are used to define the operations possible on them and \n"\
          "the storage method for each of them.\n")
    print('\n')
    time.sleep(1)
    print("Python has five standard data types:\n")
    time.sleep(1)
    print("i)  Numbers \n"\
          "ii) Strings \n"\
          "iii)List \n"\
          "iv) Tuple \n"\
          "v)  Dictionary \n")
    time.sleep(1)

    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print("QUESTION: ")
    print("var1,var2,var3,var4,var5 = 1,10,23,89,34")
    print('\n')
    time.sleep(1)
    print("If implied the 'del' function to var3, what will printed?")
    print('\n')
    time.sleep(1)
    print("Please select A, B, C or D")
    print('\n')
    time.sleep(1)
    print("A) 10,23,89,34 \n"\
          "B) 1,23,89,34 \n"\
          "C) 1,10,89,34 \n"\
          "D) 1,10,23,89 \n")
    var1 = 1
    var2 = 10
    var3 = 23
    var4 = 89
    var5 = 34
    varList = [var1,var2,var3,var4,var5]
    del varList[2]
    ans = "c"
    hint = "See what var3 corresponds to on the RHS"
    guide = "Take Note: The 'del' function means delete."
    explanation = "Correct answer: C. Deleting a variable removes the item which was assigned to \n"\
                  "that particular variable."

    life(guide,ans,hint,explanation)
    

#-------------------------------------------------------------------------------
#QUESTION 4
def question4():
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print("This will be a question on lists.")
    print('\n')
    time.sleep(1)
    guide = "Take Note: The beginning item of a list has an index 0. \n"
    time.sleep(1)
    print("QUESTION: ")
    print("In thisList = ['apple','potato','tomato','banana'] \n")
    time.sleep(1)
    print("What is the item in thisList[1] ? \n")
    hint = "thisList[1] means the item in thisList which has a index of 1"
    ans = "potato"
    explanation = "Correct answer: potato. Lists are the most versatile \n"\
                  "of Python's compound data types. A list contains items separated by commas and \n"\
                  "enclosed within square brackets ([]). To some extent, \n"\
                  "lists are similar to arrays in C. One difference between \n"\
                  "them is that all the items belonging to a list can be \n"\
                  "of different data type. The values stored in a list can \n"\
                  "be accessed using the slice operator ([ ] and [:]) with \n"\
                  "indexes starting at 0 in the beginning of the list and \n"\
                  "working their way to end -1. The plus (+) sign is the \n"\
                  "list concatenation operator, and the asterisk (*) is the \n"\
                  "duplication operator."
    life(guide,ans,hint,explanation)
  


#-------------------------------------------------------------------------------
#QUESTION 5
def question5():
    print('~~~' *10)
    print("Loading your question.")
    print('~~~' *10)
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print("This a question on strings in Python. \n")
    time.sleep(1)
    print(" str = 'Hello World' \n")
    time.sleep(1)
    print("What will be the result if 'print str[0:8]' is executed? \n" )
    time.sleep(1)
    print("A) 'HELLO WORLD' \n"\
          "B) 'HELLO' \n"\
          "C) 'HO' \n"\
          "D) 'HELLO WO' \n"\
          "E) 'HELLO WOR' \n")
    guide = "Take Note: Watch out, spaces counts too! \n"
    hint = "Remember the beginning of an item which in this is the first \n"\
           "alphabet has an index of 0."
    ans = "d"
    explanation = "Correct answer: D. Strings in Python are identified as a contiguous set of \n"\
                  "characters represented in the quotation marks. Python \n"\
                  "allows for either pairs of single or double quotes. \n"\
                  "Subsets of strings can be taken using the slice \n"\
                  "operator ([ ] and [:] ) with indexes starting at 0 in \n"\
                  "the beginning of the string and working their way \n"\
                  "from -1 at the end.The plus (+) sign is the string \n"\
                  "concatenation operator and the asterisk (*) is the \n"\
                  "duplication operator."

    life(guide,ans,hint,explanation)

#---------------------------------------------------------------------------------
def life(guide, ans,hint,explanation):
    global correct_Answers
    global wrong_Answers

    lives = 2
    while lives != 0:
        print(guide)
        print()
        userInput = input("PLEASE KEY IN YOUR ANSWER: ").lower()
        print()
        if ans == userInput:
            correct_Answers += 1
            time.sleep(1)
            print("CORRECT! WELL DONE. PLEASE PROCEED FORWARD.")
            print()
            break
        elif userInput == "hint":
            time.sleep(1)
            if lives == 2 :
                print("HINT: " + hint)
                print("YOU HAVE ONE MORE TURN LEFT")
                print()
                lives -= 1
            else:
                print(hint)
                print("YOU HAVE ONE LAST TRY")
                
            
        else:
            lives -= 1
            time.sleep(1)
            if lives == 1:
                wrong_Answers + 1
                print("OH NO, THATS INCORRECT, TRY AGAIN.")
                print(hint)
                print()

            else:
                pass
          
    print('~~~' *15)
    print("Loading your explanation.")
    print('~~~' *15)
    time.sleep(1)
    print("...")
    time.sleep(1)          
    print("EXPLANATION: " + explanation)
    print('\n')
    time.sleep(1)
    
#-----------------------------------------------------------------------
def choose_Question():
    question_num = random.choice(questionList)
    if question_num == "question_1":
        question1()
        
    elif question_num == "question_2":
        question2()

    elif question_num == "question_3":
        question3()
           
    elif question_num == "question_4":
        question4()

    elif question_num == "question_5":
        question5()
           
    questionList.remove(question_num)

    
        
#--------------------------------------------------------------------------------------------------------------------------------------------
#Python and ladders frame
#--------------------------------------------------------------------------------------------------------------------------------------------
board = [0]*30
num_List = [1,2,3,4]*5
current_position = 0
flag = True

"""This function rolls the dice and returns the number obtained."""
def dice_roll():
    print('\n')
    print('~~~' *10)
    print("YOUR SCORE SO FAR IS...")
    print('~~~' *10)
    print('...')
    time.sleep(1)

    print("The number of questions you answered correctly is: " + str(correct_Answers))
    print("The number of questions you answered wrongly is: " + str(wrong_Answers))
    print('\n')
    continue_Input = input("When you're ready, press Enter to receive your dice roll!") 
    print('\n')
    print("\_('O')_/ Drum roll please, your dice is rolling \_('O')_/ ")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("...loading...")
    time.sleep(2)
    number = random.randint(1,5)
    print("Your dice roll is "+ str(number))
    return number


"""This function updates the postion of the board after diceRolls.
'roll_number' is the number obtained from the diceRoll.
current position of the token will be updated after adding the roll_number."""
def update_location(roll_number):
    global flag
    global current_position
    current_position += roll_number
    print("You will move to position "+str(current_position))
    check_for_trap(current_position)
    if current_position >30:
        print("There is not position "+str(current_position)+" therefore you need to move back.")
        move_back = current_position - 30
        current_position = 30 - move_back
        print("You will now move to "+str(current_position))
        board[current_position - 1] = 1
        print("Loading your board")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print("")
        print("--"*45)
        print(" "*35 +"This is your board")
        print("--"*45)
        print(board)
        print("--"*45)
        print("")
    elif current_position == 30:
        board[29] = 1
        print("Loading your board")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print("")
        print("--"*45)
        print(" "*35 +"This is your board")
        print("--"*45)
        print(board)
        print("--"*45)
        print("")
        flag = False
    else:    
        board[current_position-1]=1
        print("Loading your board")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print("")
        print("--"*45)
        print(" "*35 +"This is your board")
        print("--"*45)
        print(board)
        print("--"*45)
        print("")
    return current_position


"""This function removes the '1'(token) from the board,
so that the location of the location can be updated"""
def remove_token():
    for i in range(len(board)):
        if board[i] == 1:
            board[i] =0
            

"""This function is called when the token is on a ladder.
The user will then move his token up to the end of the ladder."""
def promotion(new_position):
    print("Congratulation! You got a ladder")
    print("You are at position "+str(new_position)+" now")



"""This function is called when the token is on a python.
The user will then mvoe his token down to the tail of the python."""
def demotion(new_position):
    print("Ahhh, too bad you met a python and you have to move back")
    print("You are at position "+str(current_position)+" now")


"""This function checks whether the location of the token is a trap or not.
If it is, the token will be moved upwards or downwards,
depending whether the user meets ladder or python."""
def check_for_trap(location):
    global current_position
    if location == 4:
        current_position = 8
        promotion(current_position)
    elif location == 7:
        current_position = 3
        demotion(current_position)
    elif location == 13:
        current_position = 9
        demotion(current_position)
    elif location == 14:
        current_position = 17
        promotion(current_position)
    elif location == 22:
        current_position = 19
        demotion(current_position)
    elif location == 23:
        current_position = 27
        demotion(current_position)
    elif location == 29:
        current_position = 24
        demotion(current_position)
        

def choose_category():
    global num_List

    if num_List == []:
        return False
 
    if num_List[0] == 1:
        del num_List[0]
        choose_question()
        return True
    elif num_List[0] == 2:
        del num_List[0]
        variable_Names()
        return True
    elif num_List[0] == 3:
        del num_List[0]
        chooseQuestion()
        return True
    elif num_List[0]== 4:
        del num_List[0]
        choose_Question()
        return True

   
     
#When to stop the while loop
def start_game():
    global flag
    global current_position
    i = 0
    continue_Loop = True
    while continue_Loop == True:
        end_Check = update_location(dice_roll())
        remove_token()
        if end_Check == 30:
            break
        continue_Loop = choose_category()
        
#--------------------------------------------------------------------------------------------------------------------------------------------
#Running the function and ending outputs.
#--------------------------------------------------------------------------------------------------------------------------------------------
start_game()

#These if statement is for whether the player chooses to continue answering questions after the game ends.
#Only applies if there are remaining questions in num_List.
if num_List != []:
    print('---' *40)
    print("\('v')/ CONGRATULATIONS! YOU'VE MANAGED TO COMPLETE THE GAME! BUT...")
    print('---' *40)
    print('...')
    time.sleep(1)
    print('There are still ' + str(len(num_List)) + ' question(s) left to answer.')
    time.sleep(1)
    continue_Input = input('Would you like to continue answering the remaining questions, but without the board and dice rolls? Type "yes" or "no": ').lower()
    print('\n')
    
    if 'y' in continue_Input:
        loop = True
        while loop == True:
            #The loop breaks when False is returned (no more questions in num_List)
            loop = choose_category()
            
            #Printing out the total score after the game ends.
            print('\n')
            print('~~~' *10)
            print("YOUR SCORE SO FAR IS...")
            print('~~~' *10)
            print('...')
            time.sleep(1)
            print("The number of questions you answered correctly is: " + str(correct_Answers))
            print("The number of questions you answered wrongly is: " + str(wrong_Answers))
            print('\n')

            if len(num_List) > 0:
                #Requests the user whether they want to continue answering questions after the game.
                print('\n')
                print('~~~' *10)
                print("REQUEST TO CONTINUE...")
                print('~~~' *10)
                print('...')
                time.sleep(1)
                print('There are still ' + str(len(num_List)) + ' question(s) left to answer.')
                continue_Input2 = input('Would you like to continue answering the questions? Type "yes" or "no": ').lower()
                print('\n'*2)

                if 'y' in continue_Input2:
                    continue
                elif 'n' in continue_Input2:
                    break
                else:
                    break

            else:
                break
                
        if num_List == []:
            print('~~~' *20)
            print('There are no more questions left to answer!')
            print('~~~' *20)
    else:
        pass
            
elif num_List == []:
    print('~~~' *20)
    print('There are no more questions left to answer!')
    print('~~~' *20)
    time.sleep(1)
    print('\n')
    print('---' *40)
    print("\('v')/ CONGRATULATIONS! YOU'VE MANAGED TO COMPLETE THE GAME! ~~")
    print('---' *40)

    
#Ending outputs:
print('\n')
print('---' *40)
print(' ~~~ THANK YOU FOR PLAYING! HOPE YOU ENJOYED THE GAME! \(^_^)/ ~~~')
print('---' *40)

