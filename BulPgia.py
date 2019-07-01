from collections import defaultdict
import re
import math

def choose_random_number():
    from random import randint
    counter = defaultdict(int)
    mone = 0
    degel = 0
    while mone < 4:
            x = randint(0, 9)
            if not counter[x]:
                counter [x] = 1
                mone+=1
    return counter


def check_pgia(guess, computer_num):
    regex = r'['+computer_num + r']'
    x = re.findall(regex, guess)
    return len(x)

def check_bul (guess, computer_num):
    mone = 0
    if(int (guess)//1000) == (int (computer_num)//1000):
        mone+=1
    if((int (guess)//100) %10) == ((int (computer_num)//100) %10):
        mone+=1
    if((int (guess)%100)//10) == ((int (computer_num)%100)//10):
        mone+=1
    if(int (guess)%10) == (int (computer_num)%10):
        mone+=1
    return mone


def save_file (computer_num, iterations):
    save_file_name = input("Enter file name: ")
    with open(f'{save_file_name}.txt','r+', encoding='UTF-8') as f:
        f.seek(0)
        f.write(f'computer_num={computer_num}\n')
        f.write(f'iterations={iterations}\n')
        f.truncate()


def open_file ():
    open_file_name = input("Enter file name: ")
    try:
        with open(f'{open_file_name}.txt', 'r', encoding='UTF-8') as f:
            x = f.read().split()
            return x


    except FileNotFoundError:
       print("The file not exist")
       return 0


guess_iterate = 0
while True:
    your_chooose = input("please choose: 1 = new game, 2 = open saved game ")
    if your_chooose == '2':
        saved_results = open_file()
        if (saved_results):
            try:
                computer_num_string = saved_results[0].split("=")[1]
                guess_iterate = int (saved_results[1].split("=")[1])
                #print(computer_num_string, guess_iterate)
                break;

            except Exception:
                print ("It's not a saved game file")
    elif your_chooose == '1':
        break;


if your_chooose == '1':
    x = choose_random_number()
    computer_num_string = ''
    for item in x:
        computer_num_string +=str(item)

#print(computer_num_string)


while guess_iterate < 20:
    your_guess = input("enter 4 numbers: (or 'save' to save the game) ")
    if (your_guess == 'save'):
        save_file(computer_num_string, guess_iterate)
        break;
    if re.search(r'^(\d{4})$', your_guess):
        guess_iterate +=1
        bul = check_bul(your_guess, computer_num_string)
        if (bul == 4):
            print("You Win!")
            break;
        pgia = check_pgia(your_guess, computer_num_string)
        print(f"bul = {bul}, pgia = {pgia - bul}")
    else:
        print("your enter is invalid, please enter 4 numbers")
if your_guess != 'save':
    if bul != 4:
        print("You over the game iterations, please try again...")
