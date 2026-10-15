# ------------------------------------------------------
#        Name: Ella
#       Peers: None
#  References: Powerpoint Slides
# ------------------------------------------------------
import sys

secret_word = "food"


# Task 1
def check_text():
    """ ask for a sentence from the user, then check whether it contains certain words"""
    
    while True: #create a loop
        user_input = input("Give me a sentence: ") #ask for user input
        
        if secret_word in user_input: #check if the user uses the word "food"
            print("You used the secret word!")
            break
        
        elif "Dog" in user_input or "dog" in user_input: #check if the user uses the word "dog" or "Dog"
            print('You used the word "dog" or the word "Dog"!')
            break
    
        else:
            print("Try again")

# Task 2
def check_greater():
    """ ask for two integers from the user, then compare them """
    
    while True: #create a loop
        user_int1 = int(input("Give me an integer: "))
        user_int2 = int(input("Give me an integer: ")) #ask for user input
    
        if user_int1 > user_int2: #check which num is greater
            print("First is Greater") 
            break
        elif user_int2 > user_int1: 
            print("Second is Greater")
            break
        else:
            print ("Try again")


# Task 3
def get_special_numbers():
    """ print every num between 0 and 40 that is not even or a mutiple of 5 but is a mutiple of 3 """
    
    for num in range(1,41): #check every num that is between 1 and 40, including 1 and 40
        if num%2 == 0: #check if the num is even
            pass
        elif num%3 != 0: #check if it is not a multiple of 3
            pass
        elif num%5 == 0: #check if it is a multiple of 5
            pass
        else:
            print(num)

# Task 4.a
def my_for_loop():
    
    """ get a string from the user and return the function if it is not between 2 and 5 characters or has space,
        then check for vowels and consonant in the string """
    
    vowel = ["A","a","E","e","I","i","O","o","U","u"] #set up an array for the vowels
    user_str = input("Give me a word: ")
    if not 2 <= len(user_str) <= 5: #check if user's string in within the 2-5 character limit
        print("bad word")
        return
    elif " " in user_str: #check if there is space in the user's string
        print("bad word")
        return
    
    letter = list(user_str) #set up a new array for user's string
    
    for idx in letter: #for every element in the array of user's string
        if idx in vowel: #if the element also shows up in the array of vowels
            print(idx,"is a vowel") #then this letter is a vowel
        else:
            print(idx,"is a consonant")

# Task 4.b
def my_while_loop():
    """ Display a menu with three options for the user to select from and respond accordingly.
        If user input is out of the scope of these three options, then ask the user to try again """
    
    user_choice = input("---menu---\na: repeat the menu\nb: goodbye\nc: exit\nWhat's your choice? ") #display a menu with options
    while True: #create a loop
        if user_choice == "a": #if user input is a, repeat the menu
            user_choice = input("---menu---\na: repeat the menu\nb: goodbye\nc: exit\nWhat's your choice? ")
        elif user_choice == "b": #if user input is b, say goodbye then return the function
            print("Goodbye")
            return
        elif user_choice == "c": #exit the program when user input os c
            sys.exit()
        else: #if any other letters are selected, say try again and repeat the menu
            print("try again")
            user_choice = input("---menu---\na: repeat the menu\nb: goodbye\nc: exit\nWhat's your choice? ") 

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
