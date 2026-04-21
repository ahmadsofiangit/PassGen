# Made In Malaysia
############################# Sector 0 (Import) ################################
import random
from sys import argv 
import string 
from pyfiglet import *
from wonderwords import *

font = Figlet(font='slant')
ranword = RandomWord()

############################ Sector 1 (Data Structure) ###########################
# Options Main, A class use to storing data for banner menu_banner.
class options_main():
    about = "Wordlist generator, Fast and effective! made in 2 day"
    version = "0.0.1.10"
    language_based = "python"
    banner = argv[0]

    info = f"[i] Description: {about}\n[i] Version: {version}\n[i] Based On: {language_based}"

class command():
    arguments = (
        "-h", 
        "-l", 
        "-c", 
        "-m")
    
    meaning = (
    "Showing a command arguments", 
    "Set the line length of password", 
    "Set the character length of password", 
    "Mode options: Weak, Strong, Medium")
    
    example = (
    f'python3 {argv[0]} -l 10 -c 10 -m weak', 
    f'python3 {argv[0]} -l 10 -c 10 -m strong', 
    f'python3 {argv[0]} -l 10 -c 10 -m medium')
    
############################ Sector 2 (Functions) ###########################
# Banner menu_banner, Use to displaying the lists in consoles.
def menu_banner():
    print(font.renderText(options_main.banner))
    print(f"{options_main.info}\n")

ERROR_MSG = f"Invalid argument, Please use {command.arguments[0]} for displaying all commands and examples"

# Show commands.
def help_command():
    for numbers_pre_arg, pre_arg in enumerate(command.arguments):
        print(f"{pre_arg}\t| {command.meaning[numbers_pre_arg]}")
    
    print("\nUsage:")
    for pre_example in command.example:
        print(f'\t{pre_example}')

# Generating a password into file depends on mode.
def generate_wordlist(length, line, mode):
    try:
        with open("wordlist.txt", "x", encoding="utf-8") as file:
            pass
    except FileExistsError:
        pass
    
    if mode == "weak":
        with open("wordlist.txt", "w", encoding="utf-8") as file:
            for i in range(0, line):
                passwords = ''.join(random.choices(string.digits, k=length))
                n_password = ''.join(passwords) + '\n'
                file.write(n_password)
        file.close()
    elif mode == "strong":
        with open("wordlist.txt", "w", encoding="utf-8") as file:
            for i in range(0, line):
                passwords = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k=length))
                n_password = ''.join(passwords) + '\n'
                file.write(n_password)
        file.close()
    elif mode == "medium":
        with open("wordlist.txt", "w", encoding="utf-8") as file:
            for i in range(0, line):
                passwords = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
                n_password = ''.join(passwords) + '\n'
                file.write(n_password)
        file.close()
    else:
        print(ERROR_MSG)
        exit(1)

# Error Handling if first argument is empty print error message.
try:
    argv[1]
except IndexError:
    print(ERROR_MSG)
    exit(1)

# Check and Handle.
if argv[1] == command.arguments[0]:
    # Function being calling here.
    help_command()
    exit() # Exit after calling the help command()
elif argv[1] == command.arguments[1]: # Else if argv[1] is equal to command_arg.arg2
    try:
        argv[2]
        argv[3]
        argv[4]
        argv[5]
        argv[6]
    except IndexError: #if index is empty print error message.
        print(ERROR_MSG)
        exit(1) # Exit if error happen

    try:    
        int(argv[2])
        int(argv[4])
        str(argv[6])
    except ValueError:
        print(f'Simplify traceback: Invalid type {type(argv[2])} {type(argv[4])} {type(argv[6])}\n{ERROR_MSG}') 
        exit(1)

    lengths = int(argv[2])
    lines = int(argv[4])
    set_mode = str(argv[6]).lower()
    
    if argv[3] == command.arguments[2]:
        if argv[5] == command.arguments[3]: # Function being calling here.
            menu_banner()
            generate_wordlist(lengths, lines, set_mode)
    else:
        print(ERROR_MSG)
        exit(1)
else:
    print(ERROR_MSG)
    exit(1)

print(f"[Log] Successfully created a wordlist, Check it out!\n[Log] wordlist.txt > Lengths: {lengths} Lines: {lines}")
