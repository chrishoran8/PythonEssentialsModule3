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




