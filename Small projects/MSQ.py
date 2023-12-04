# small things can destroy big ambitions 
# MSQ for a desired person
import random
from random import choice
from time import sleep
from ANSI import CR,C,BrightGreen,BrightBlue,BrightYellow,un,SL
from qs import Anatomy_questions

wrong_questions = []

objects = {
      "1": "Anatomy", "2": "Biology", "3": "Chemistry",
      "4": "LLM",     "5": "PPC",     "6": "NIT"
      }

Anatomy_ph = ["Join the Body Party: Where Bones and Friends Hang Out!", "Anatomy Antics: Fun with Organs and Friends!",
              "Anatomy Quest: Where Cells and Smiles Collide!", "Anatomy Aces: Where Learning Meets Limb-rary!",
              "Anatomy Excellence: Charting the Course to Success!", "Body Brilliance Begins with Anatomy Excellence!",
              ]

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
                print("Question:", q['question'])
                all_options = [q['correct_answer']] + q['wrong_answers']
                random.shuffle(all_options)
                for index, option in enumerate(all_options, start=1):
                      print(f"{index}. {option}")
                user_answer_number = int(input("Enter the number of your answer: "))
                if 1 <= user_answer_number <= len(all_options):
                      user_answer_index = user_answer_number - 1
                      user_answer = all_options[user_answer_index]
                      if user_answer == q['correct_answer']:
                            overall_score += 1
                      else:
                            wrong_questions.append(q['question'])
                            q['score'] = 1
                else:
                      print("Invalid option number. Please enter a valid number.")

            
           print(f"Your score is: {overall_score}")



def main():
      object = object_pick()
      
      Q = roll_questions()
      
      if object == "1":
            Q.Anatomy()
      
            
main()