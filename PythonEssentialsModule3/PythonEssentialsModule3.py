#3.2.1.3 lab
message = """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""

#from intro paragraph
secret_number = 777

print(message)

userNumber = int(input("Enter an integer Number"))
#ask the user to enter an integer number;

while userNumber != secret_number:
#will use a while loop;
#will check whether the number entered by the user is the 
#same as the number picked by the magician.
#If the number chosen by the user is different
#than the magician's secret number, 

    print("Ha ha! You're stuck in my loop!")
    #the user 
    #should see the message "Ha ha! You're stuck in my loop!" 


    #and be prompted to enter a number again.
    userNumber = int(input("Enter an integer Number"))

print("Well done, muggle! You are free now.")
#If the number entered by the user matches the 
#number picked by the magician, 
#the number should be printed to the screen,
#and the magician should say the following words: 
#"Well done, muggle! You are free now."



#lab on miissipi
import time

for i in range(1,6):
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(i,"Mississippi")
    time.sleep(1)

# Write a print function with the final message.

#lab on chupacabra
exitWord = "chu"
inputWord = ""

while True:
    inputWord = input("Please input a word")
    if inputWord == exitWord:
        break
    
print("You've successfully left the loop.")




#word eater

# Prompt the user to enter a word
# and assign it to the user_word variable.
#ask the user to enter a word;
user_word = input("Enter a word please")

#use user_word = user_word.upper() to convert 
#the word entered by the user to upper case; 
#we'll talk about the so-called string methods 
#and the upper() method very soon - don't worry;
user_word = user_word.upper()

for letter in user_word: 
    if letter in "AEIOU":continue
    print(letter)
    
    #use conditional execution and the continue 
    #statement to "eat" the following vowels 
    #A, E, I, O, U from the inputted word;
    #print the uneaten letters to the screen, 
    #each one of them on a separate line.


    # Complete the body of the for loop.




#posh word eater

word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word")

#use user_word = user_word.upper() 
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the loop.
    #use conditional execution and the 
    #continue statement to "eat" the following 
    #vowels A, E, I, O, U from the inputted word;
    if letter in "AEIOU":
        continue
    
    #assign the uneaten letters to the word_without_vowels 
    #variable and print the variable to the screen.
    word_without_vowels = word_without_vowels + letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)

   




#take any non-negative and non-zero integer number and name it c0;
co = 15
steps = 0

#if c0 ≠ 1, skip to point 2.
while co != 1:
    steps = steps + 1
    #if it's even, evaluate a new c0 as c0 ÷ 2;
    if co % 2 == 0:
        co = co // 2
    else:
        #otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
        co = 3 * co + 1
    print(co)
print("steps", steps)
        


