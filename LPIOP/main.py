import random

MAX_LINES = 3
MAX_BET, MIN_BET = 100 , 1
ROWS, COLS = 3 , 3

def deposit():
    while True:
        amount = input(f"What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: print(f"Amount must be greater than 0.")
        else: print(f"Enter a number please.")
    return amount

def NL():
    while True:
        lines = input(f"Enter number of lines to bet on [ 1 - {MAX_LINES} ]? : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: print(f"lines must be greater than 1 and no more than {MAX_LINES}.")            
        else: print(f"Enter a valid number please.")
    return lines

def BA():
    while True:
        bet = input(f"Enter how much you want to bet on each line [ {MIN_BET} - {MAX_BET} ]? $ ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else: print(f"bet must be between [ {MIN_BET} - {MAX_BET} ].")
        else: print(f"Enter a valid number please.")
    return bet


def main():
    amount = deposit()
    lines = NL()
    while True:
        bet = BA()
        total = bet * lines
        if total > amount:
            print(f"Your budget({amount}) is not enuogh to bet that much") 
        else: break
        
    print(f"You are betting ${bet} on {lines} lines, Total is {total}")
    
main()