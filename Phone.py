from termcolor import colored
import os
import sys
os.system("clear")
print(colored('''
██████╗░██╗░░██╗░█████╗░███╗░░██╗███████╗
██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝
██████╔╝███████║██║░░██║██╔██╗██║█████╗░░
██╔═══╝░██╔══██║██║░░██║██║╚████║██╔══╝░░
██║░░░░░██║░░██║╚█████╔╝██║░╚███║███████╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝''', 'green', attrs=['>
print(colored(''' by MR.zero

''', 'blue', attrs=['underline']))
def store_phone_info():
    number = input(colored('enter phone number: ','red'))
    name = input(colored('Enter Name: ', 'red'))
    country = input(colored('Enter Country: ','red'))
    city = input(colored('Enter City: ', 'red'))

    with open("phone_info.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Country: {country}\n")
        file.write(f"City: {city}\n")
        file.write("----------\n")

def retrieve_phone_info():
    try:
        with open("phone_info.txt", "r") as file:
            phone_info = file.read()
            print(phone_info)
    except FileNotFoundError:
        print("No phone information found.")

store_phone_info()
retrieve_phone_info()

print(colored('work is done' , 'green'))
