# small things can destroy big ambitions 
# MSQ for a desired person

import random
from random import choice
from time import sleep
from ANSI import CR,C,BrightGreen,BrightBlue,BrightYellow,un,SL
from qs import Anatomy_questions,Anatomy_ph,Biology_questions,Biology_ph,Chemistry_questions,Chemistry_ph,NIT_questions,PPC_questions

print(C,CR)
name = input(f"{BrightGreen}Hey, what you should be called: {un}")

wrong_questions = [
    
]
objects = {
    "1": "Anatomy", "2": "Biology","3":
    "Chemistry","4": "PPC","5": "NIT"
    }
class roll_questions:
    def object_pick():
      print(C,CR)
      print(f"{BrightYellow}Okay {name} What would you test yourself with?{un} {SL}")
      for index, object in enumerate(objects.values(), start=1):
            sleep(0.64)
            print(f"{index}- {BrightBlue}{object}{un}")
      while True:
            get_object = input(f"{SL} to choose enter the object number: ")
            if get_object in objects:
                  print(f"{SL} Good, Your score is 0 Let's start and let it rise {SL}")
                  sleep(2)
                  break
            else: print(f"{SL} Please enter A VALID object {SL}")
      sleep(1)
      print(f" \n{BrightYellow}So {name} after you have chose one from the above objects\nyou will get to answer some questions and and you can see your\nmark at the end and wich questions you answerd wrong.{un}")
      return get_object
    
    def Anatomy(self):
        print(C,CR)
        sleep(1)
        print(BrightGreen,choice(Anatomy_ph),un, SL)
        overall_score = 0 
        for q in Anatomy_questions:
           while True:
               q["score"] = 0
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
        print(C,CR)
        print(f"{SL}{SL}Your score is: {overall_score}/{len(Anatomy_questions)}")
        
    def Biology(self):
        print(C,CR)
        sleep(1)
        print(BrightGreen,choice(Biology_ph),un, SL)
        overall_score = 0 
        for q in Biology_questions:
            while True:
                q["score"] = 0
                print(SL,"Question:", q['question'],SL)
                
                # Combine correct and wrong answers
                all_options = [q['correct_answer']] + q['wrong_answers']
                
                # Shuffle the options
                random.shuffle(all_options)
                
                # Print numbered and shuffled options
                for index, option in enumerate(all_options, start=1):
                    print(f"{SL}{index}. {option}")
                
                # Prompt the user for a number input
                user_answer_input = input(f"{SL}Enter the number of your answer: ")
        
                if user_answer_input.strip() == "":
                    # If the user pressed only enter, repeat the question
                    print(f"{SL}Please enter a valid number.{SL}")
                    continue
        
                try:
                    user_answer_number = int(user_answer_input)
                except ValueError:
                    print(f"{SL}Invalid input. Please enter a valid number.{SL}")
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
                    print(f"{SL}Invalid option number. Please enter a valid number.{SL}")
        print(C,CR)
        print(f"{SL}{SL}Your score is: {overall_score}/{len(Biology_questions)}")
        
    def Chemistry(self):
        print(C,CR)
        sleep(1)
        print(BrightGreen,choice(Chemistry_ph),un, SL)
        overall_score = 0 
        for q in Chemistry_questions:
            while True:
                q["score"] = 0
                print(SL,"Question:", q['question'],SL)
                
                # Combine correct and wrong answers
                all_options = [q['correct_answer']] + q['wrong_answers']
                
                # Shuffle the options
                random.shuffle(all_options)
                
                # Print numbered and shuffled options
                for index, option in enumerate(all_options, start=1):
                    print(f"{SL}{index}. {option}")
                
                # Prompt the user for a number input
                user_answer_input = input(f"{SL}Enter the number of your answer: ")
        
                if user_answer_input.strip() == "":
                    # If the user pressed only enter, repeat the question
                    print(f"{SL}Please enter a valid number.{SL}")
                    continue
        
                try:
                    user_answer_number = int(user_answer_input)
                except ValueError:
                    print(f"{SL}Invalid input. Please enter a valid number.{SL}")
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
                    print(f"{SL}Invalid option number. Please enter a valid number.{SL}")
        print(C,CR)
        print(f"{SL}{SL}Your score is: {overall_score}/{len(Chemistry_questions)}")
        
    def NIT(self):
        print(C,CR)
        sleep(1)
        overall_score = 0 
        for q in NIT_questions:
            while True:
                q["score"] = 0
                print(SL,"Question:", q['question'],SL)
                
                # Combine correct and wrong answers
                all_options = [q['correct_answer']] + q['wrong_answers']
                
                # Shuffle the options
                random.shuffle(all_options)
                
                # Print numbered and shuffled options
                for index, option in enumerate(all_options, start=1):
                    print(f"{SL}{index}. {option}")
                
                # Prompt the user for a number input
                user_answer_input = input(f"{SL}Enter the number of your answer: ")
        
                if user_answer_input.strip() == "":
                    # If the user pressed only enter, repeat the question
                    print(f"{SL}Please enter a valid number.{SL}")
                    continue
        
                try:
                    user_answer_number = int(user_answer_input)
                except ValueError:
                    print(f"{SL}Invalid input. Please enter a valid number.{SL}")
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
                    print(f"{SL}Invalid option number. Please enter a valid number.{SL}")
        print(C,CR)
        print(f"{SL}{SL}Your score is: {overall_score}/{len(NIT_questions)}")
        
    def PPC(self):
        print(C,CR)
        sleep(1)
        overall_score = 0 
        for q in PPC_questions:
            while True:
                q["score"] = 0
                print(SL,"Question:", q['question'],SL)
                
                # Combine correct and wrong answers
                all_options = [q['correct_answer']] + q['wrong_answers']
                
                # Shuffle the options
                random.shuffle(all_options)
                
                # Print numbered and shuffled options
                for index, option in enumerate(all_options, start=1):
                    print(f"{SL}{index}. {option}")
                
                # Prompt the user for a number input
                user_answer_input = input(f"{SL}Enter the number of your answer: ")
        
                if user_answer_input.strip() == "":
                    # If the user pressed only enter, repeat the question
                    print(f"{SL}Please enter a valid number.{SL}")
                    continue
        
                try:
                    user_answer_number = int(user_answer_input)
                except ValueError:
                    print(f"{SL}Invalid input. Please enter a valid number.{SL}")
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
                    print(f"{SL}Invalid option number. Please enter a valid number.{SL}")
        print(C,CR)
        print(f"{SL}{SL}Your score is: {overall_score}/{len(PPC_questions)}")
        
def main():
    Q = roll_questions()
    object = Q.object_pick
    if object == "1":
        Q.Anatomy()

    elif object == "2":
        Q.Biology()
            
    elif object == "3":
        Q.Chemistry

    elif object == "4":
        Q.PPC

    elif object == "5":
        Q.NIT



    sleep(5)
    print(C,CR)
    print(f"{SL}Great, now let's see what you should review and do your best in{SL}")
    sleep(0.6),sleep(2.5) ,print("just one second..."), sleep(0.4), print("a mommment.."),sleep(1),print("yup done."),sleep(0.6)
    for index, wq in enumerate(wrong_questions, start=1):
        print(f"{SL}{index}- {wq}")
                

    maybe = input(f"{SL}{name}, wanna repeat? 0 for no 1 for yes{SL}")
    if maybe == "1":
        main()
    else:
        print(C,CR)
        print(f"See you then {name.upper()}")
        sleep(5)
main()
