# small things can destroy big ambitions 
# MSQ for a desired person
import random
from random import choice
from time import sleep
from ANSI import CR,C,BrightGreen,BrightBlue,BrightYellow,un,SL
from qs import Anatomy_ph,Biology_questions,Biology_ph

wrong_questions = []

objects = {
      "1": "Anatomy", "2": "Biology", "3": "Chemistry",
      "4": "LLM",     "5": "PPC",     "6": "NIT"
      }


print(C,CR)
name = input(f"{BrightGreen}Hey, what you should be called: {un}")

def object_pick():
      print(C,CR)
      print(f"{BrightYellow}Okay {name} What would you test yourself with?{un} {SL}")
      for index, object in enumerate(objects.values(), start=1):
            sleep(0.64)
            print(f"{index}- {BrightBlue}{object}{un}")
      while True:
            get_object = input(f"{SL}to choose enter the object number: ")
            if get_object in objects:
                  print(f"{SL}Good, Your score is 0 Let's start and let it rise{SL}")
                  sleep(2)
                  break
            else: print(f"{SL}Please enter A VALID object{SL}")
      sleep(1)
      print(f" \n{BrightYellow}So {name} after you have chose one from the above objects\nyou will get to answer some questions and and you can see your\nmark at the end and wich questions you answerd wrong.{un}")
      return get_object

class roll_questions:
     def Anatomy(self):
           print(C,CR)
           sleep(1)
           print(BrightGreen,choice(Anatomy_ph),un, SL)
           overall_score = 0 
           for q in Anatomy_questions:
               while True:
                   print(SL,"Question:", q['question'],SL)
                   
                   # Combine correct and wrong answers
                   all_options = [q['correct_answer']] + q['wrong_answers']
                   
                   # Shuffle the options
                   random.shuffle(all_options)
                   
                   # Print numbered and shuffled options
                   for index, option in enumerate(all_options, start=1):
                       print(f"{SL}{index}. {option}")
                   
                   # Prompt the user for a number input
                   user_answer_input = input("{SL}Enter the number of your answer: ")
           
                   if user_answer_input.strip() == "":
                       # If the user pressed only enter, repeat the question
                       print("{SL}Please enter a valid number.{SL}")
                       continue
           
                   try:
                       user_answer_number = int(user_answer_input)
                   except ValueError:
                       print("{SL}Invalid input. Please enter a valid number.{SL}")
                       continue
           
                   # Check if the entered number is a valid option
                   if 1 <= user_answer_number <= len(all_options):
                       # Convert the user's number to an index (0-based) in the list of options
                       user_answer_index = user_answer_number - 1
           
                       # Retrieve the selected option
                       user_answer = all_options[user_answer_index]
           
                       if user_answer == q['correct_answer']:
                           overall_score += 1
                           break  # Break the loop if the answer is correct
                       else:
                           wrong_questions.append(q['question'])
                           q['score'] = 1
                           break  # Break the loop if the answer is incorrect
                   else:
                       print("{SL}Invalid option number. Please enter a valid number.{SL}")

           print(f"{SL}Your score is: {overall_score}")
     def Biology(self):
           print(C,CR)
           sleep(1)
           print(BrightGreen,choice(Biology_ph),un, SL)
           overall_score = 0 
           for q in Biology_questions:
               while True:
                   print(SL,"Question:", q['question'],SL)
                   
                   # Combine correct and wrong answers
                   all_options = [q['correct_answer']] + q['wrong_answers']
                   
                   # Shuffle the options
                   random.shuffle(all_options)
                   
                   # Print numbered and shuffled options
                   for index, option in enumerate(all_options, start=1):
                       print(f"{SL}{index}. {option}")
                   
                   # Prompt the user for a number input
                   user_answer_input = input("{SL}Enter the number of your answer: ")
           
                   if user_answer_input.strip() == "":
                       # If the user pressed only enter, repeat the question
                       print("{SL}Please enter a valid number.{SL}")
                       continue
           
                   try:
                       user_answer_number = int(user_answer_input)
                   except ValueError:
                       print("{SL}Invalid input. Please enter a valid number.{SL}")
                       continue
           
                   # Check if the entered number is a valid option
                   if 1 <= user_answer_number <= len(all_options):
                       # Convert the user's number to an index (0-based) in the list of options
                       user_answer_index = user_answer_number - 1
           
                       # Retrieve the selected option
                       user_answer = all_options[user_answer_index]
           
                       if user_answer == q['correct_answer']:
                           overall_score += 1
                           break  # Break the loop if the answer is correct
                       else:
                           wrong_questions.append(q['question'])
                           q['score'] = 1
                           break  # Break the loop if the answer is incorrect
                   else:
                       print("{SL}Invalid option number. Please enter a valid number.{SL}")

           print(f"{SL}Your score is: {overall_score}")
      


def main():
      object = object_pick()
      
      Q = roll_questions()
      
      if object == "1":
            Q.Anatomy()

      if object == "2":
            Q.Biology()

            
      
      maybe = input(f"{SL}{name}, wanna repeat? 0 for no 1 for yes{SL}")
      if maybe == "1":
            main()
      else:
            print(C,CR)
            print(f"See you then {name.upper()}")
            sleep(5)
      
            
main()

