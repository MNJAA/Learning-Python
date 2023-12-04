# small things can destroy big ambitions 
# MSQ for a desired person

from random import choice
from time import sleep
from ANSI import CR,C,BrightGreen,BrightBlue,BrightYellow,un,SL

questions = [{
      "question": "What is the difference between meiosis I and mitosis?",
      "correct": "Sister chromatids remain joined at their centromeres throughout meiosis I but are apart completely anaphase in mitosis",
      "wrong": [
            "In both meiosis I and mitosis, sister chromatids separate during anaphase, and they are always apart completely from prophase through telophase.",
            "During meiosis I, sister chromatids separate in anaphase similar to mitosis, and they remain joined at their centromeres throughout mitosis."
      ]
}]

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
           

def main():
      object = object_pick()
      
      Q = roll_questions()
      
      if object == "1":
            Q.Anatomy()
            
main()