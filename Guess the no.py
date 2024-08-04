
import random
rand1_21=random.randint(1,21)

print("HINT● Number is between 1 and 20")

number=int(input("\nEnter an number:\n"))
print(number)

if number>rand1_21 :
   print("\nThe Number you guessd is greater than the number required .\n\nThat was a good try.\n\n""TRY AGAIN\n")
 
elif number<rand1_21:
   print("\nThe Number you guessd is smaller than the number required.\n\n""That was a good try.\n\n""TRY AGAIN\n")
 
else:
   print("\n♡♡You Guessed it Correct♡♡\n")   
   print("•●♤GREAT♤●•\n")
  
print ("The Number You Should Guess Is",rand1_21 )