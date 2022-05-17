#usr/bin/python/python3.8.10
# IMPORT RANDOM MUDULES AND SLQITE3
# beast Game for python3.8.10 utf-8
 
import random
from colorama import Fore , Style
from os import system
import numpy
from requests import get , ConnectionError
import webbrowser

def logo_start(): 
   system("clear")
   logs = f"""{Fore.RED}
████████╗██╗░░░██╗░█████╗░██╗░░██╗              ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
╚══██╔══╝██║░░░██║██╔══██╗██║░██╔╝              ┃ Information                    ┃ Version ┃
░░░██║░░░██║░░░██║██║░░╚═╝█████═╝░              ┃ https://github.com/ahSiber/    ┃         ┃    
░░░██║░░░██║░░░██║██║░░██╗██╔═██╗░              ┃ https://twitter.com/AhSibe     ┃  1.1.1  ┃
░░░██║░░░╚██████╔╝╚█████╔╝██║░╚██╗              ╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇
░░░╚═╝░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝   

{Fore.BLACK}▀{Fore.BLUE}▀{Fore.CYAN}▀{Fore.GREEN}▀{Fore.RED}▀{Fore.YELLOW}▀{Fore.WHITE}▀{Fore.LIGHTBLACK_EX}▀{Fore.LIGHTGREEN_EX}▀{Fore.LIGHTMAGENTA_EX}▀{Fore.LIGHTRED_EX}▀{Fore.MAGENTA}▀{Fore.RESET}▀{Fore.LIGHTRED_EX}▀{Fore.CYAN}
"""
   print(logs)


def main_vers():
   print(f"""
{Fore.GREEN}
{Fore.CYAN}1 - {Fore.RED}➟ {Fore.GREEN}Cat Game                  {Fore.BLUE}&{Fore.CYAN} fun games search cat 
{Fore.CYAN}2 - {Fore.RED}➟ {Fore.GREEN}Guess number              {Fore.BLUE}&{Fore.CYAN} Guess numbers! fun 
{Fore.CYAN}3 - {Fore.RED}➟ {Fore.GREEN}Name Games                {Fore.BLUE}&{Fore.CYAN} games names ! to
{Fore.CYAN}4 - {Fore.RED}➟ {Fore.GREEN}Multiplication table      {Fore.BLUE}&{Fore.CYAN} Multiplication + number
{Fore.CYAN}5 - {Fore.RED}➟ {Fore.GREEN}Multiplication 3          {Fore.BLUE}&{Fore.CYAN} Multiplication to power 3
{Fore.CYAN}6 - {Fore.RED}➟ {Fore.GREEN}Muangin!                  {Fore.BLUE}&{Fore.CYAN} mingin the number
{Fore.CYAN}7 - {Fore.RED}➟ {Fore.GREEN}Duplicate                 {Fore.BLUE}&{Fore.CYAN} Find the number of duplicate numbers
{Fore.CYAN}8 - {Fore.RED}➟ {Fore.GREEN}power 2                   {Fore.BLUE}&{Fore.CYAN} pwo two number !
{Fore.CYAN}9 - {Fore.RED}➟ {Fore.GREEN} / two                    {Fore.BLUE}&{Fore.CYAN} number / two!

{Fore.CYAN}99 - {Fore.RED}➟ {Fore.GREEN}Creator!                 {Fore.BLUE}&{Fore.CYAN} Creator Games Tuch
""")


logo_start() 
main_vers() 

try: 
   main =  int(input('➬ Enter,Games number : '))
except:
   exit()

if main == 1: 
   def tuch():
      print(f"{Fore.RED}The game has started (: Let's play")
      # animal list to python --> cheack list txt for input anmials 
      anmials = str(input(f'{Fore.GREEN}[+] Write the name of an animal : ')) 
      # Check the list to find the name of the desired animal

      with open("animal.txt" , mode='r') as file: 
         cheack_read = file.read() 

         if anmials not in cheack_read:
            print(f"{Fore.GREEN}Well done you said (:")
            ask_ = str(input(f'{Fore.YELLOW}[-] Do you want to play again? [yes:no] : '))
            if ask_ == "yes": 
               tuch() 
            else:
               pass
         else:
            print(f"{Fore.RED}[+]You said something wrong ((:")
            ask_ = str(input(f'{Fore.YELLOW}[-] Do you want to play again? [yes:no] : '))
            
            if ask_ == "yes":
               tuch() 
            else:
               pass
   tuch()


elif main == 2 : 
   def Guess(): 
      print(f"""
{Fore.GREEN}
Welcome to the numbers guess game in this game you have to choose and play a number between a range selected by
""")
      try:
         ranger = int(input(f"{Fore.GREEN}[+] Write a number larger than '3' : "))
         number_random = random.randrange(0,ranger)

         print(number_random) # <-----
         
         number_offical =int(input(f'{Fore.WHITE}[+] Enter number Guess : '))
      except: 
         pass
      if ranger <= 3: 
         print(f"{Fore.RED}Must be a number greater than 3")
         Agin_ranger = input('[+] You want to play again:[yes:no] ')
         if Agin_ranger == 'yes':
            system("clear")
            Guess() 
         else: 
            pass
      
      elif (number_random == number_offical):
         print(f"{Fore.GREEN}Well done, you guessed it right.")
      else: 
         print(F"{Fore.RED}You guessed wrong.")

   try: 
      Guess()
   except: 
      print(f"{Fore.RED}") 

elif main == 3: 
   def name_games(): 
      print(f"""
We'll give you two words to make a name with, provided that these names you make should start with these two words first.
""") 
      chrs_one = random.randrange(65,91)
      chrs_two = random.randrange(65,91)

      print(f"{Fore.BLUE}chrs one : {chr(chrs_one)}{chr(chrs_two)}{chr(chrs_one)}")  # <-----
      print(f"{Fore.BLUE}chrs one : {chr(chrs_two)}{chr(chrs_one)}{chr(chrs_two)}")  # <-----
      
      print(f"{Fore.YELLOW}Make a word with these two words : {chr(chrs_one)} and {chr(chrs_two)}")

      value = str(input(f'{Fore.RED}[+] The first word with {chr(chrs_one)} Drink the start : '))
      value_2 = str(input(f"{Fore.RED}[+] The two word with {chr(chrs_two)} Drink the start : ")) 

      if value[0] == chr(chrs_two).lower(): 
         print(f"{Fore.GREEN}Well done, you wrote correctly.")
      elif value_2[0] == chr(chrs_two).lower(): 
         print(f"{Fore.GREEN}Well done, you wrote correctly.")
      else: 
         print(f"{Fore.RED}You've written wrong.") 

   try:
      name_games()
   except: 
      print(f"{Fore.RED}") 

elif main == 4: 
   def table(): 
      randint  = random.randint(1,10)
      x = random.randint(1,10) 
      print(randint * x)
      print(F"{x} × {randint} = ? ")
      number_ok = int(input(f'{Fore.GREEN}[+] Enter number : '))
      if number_ok == randint * x: 
         yes_and_no = input(f"{Fore.GREEN}[+] ITS True! let's play again [Yes:NO] :")
      
         if yes_and_no == "yes".lower(): 
            table() 
         else: 
            pass
      else: 
         print(F"{Fore.RED} Flase Sorry")
   try:
      table() 
   except: 
      print(f"{Fore.RED}Error!") 

elif main == 5 : 
   def Multiplication_3(): 
      randints_1 = random.randint(1,10) 
      randintts_2 = random.randint(1,10) 
      randintts_3 = random.randint(1,10) 

      if randints_1 % 2 == 0: 
         print(randints_1 * randintts_2 + randintts_3)
         print(f"{Fore.GREEN}{randints_1} × {randintts_2} + {randintts_3} = ? ") 
         chaling = int(input(f'{Fore.GREEN}Enter number : '))


         if chaling == randints_1 * randintts_2 + randintts_3: 
            yes_and = input(F"{Fore.GREEN}[+] ITs true lets play again [yes:no] ")
            if yes_and == "yes".lower(): 
               Multiplication_3() 
            else: 
               pass 
         else: 
            ye_end_else = input(f"{Fore.GREEN}[+] ITs true lets play again [yes:no] ")
            if ye_end_else == "yes".lower():
               Multiplication_3()
      else: 
         print(randints_1 + randintts_2 * randintts_3)
         print(F"{Fore.YELLOW}{randints_1} + {randintts_2} × {randintts_3} = ? ") 
         chaling_r = int(input(f'{Fore.GREEN}[+] Enter number : '))
         if chaling_r == randints_1 + randintts_2 * randintts_3: 
            ye_end  = input(f"{Fore.GREEN}[+] ITs true lets play again [yes:no] ")
            if ye_end == "yes".lower(): 
               Multiplication_3() 
            else:
               pass
         else: 
            ye_end_else = input(f"{Fore.GREEN}[+] ITs true lets play again [yes:no] ")
            if ye_end_else == "yes".lower():
               Multiplication_3()
            else:
               pass
   try: 
      Multiplication_3() 
   except: 
      print(f"{Fore.RED}Error")

elif main == 6:
   def mintgin():
      random_size = random.randrange(5,10)
      achtemnt  = numpy.random.randint(1,10 , size=random_size)
      
      print(f"{Fore.YELLOW} show in number : {achtemnt}")
      print(numpy.sum(achtemnt) / len(achtemnt))
      s7 = float(input(f'{Fore.GREEN}[+] manigin numbers write : '))

      if s7 == numpy.sum(achtemnt) / len(achtemnt): 
         yor = input('vergod..play Again [yes:no] ')
         if yor == "yes".lower(): 
            mintgin()
         else:
            pass

      else: 
         very_agin = input(f'{Fore.RED}[-] sorry..play Agine ? [yes:no] ')
         if very_agin == 'yes'.lower(): 
            mintgin() 
         else:
            pass
   
   try: 

      mintgin()
   except: 
      print(F"{Fore.RED} Error!")

if main == 99: 
   def serice_creator():
      try:

         sned = get(url="https://iplogger.com/") 
         webbrowser.open(url="http://github.com/AhSiber")

      except ConnectionError:
         print(f"{Fore.RED}Please connect to the internet (:")
         servix = str(input('[-] Agine ? [Y:N] '))
         
         if servix == "y".lower(): 
            serice_creator() 
         else:
            pass
   
   serice_creator() 

elif main == 7: 
   def Duplicate():
      randomize = random.randrange(10,30)
      Dup = numpy.random.randint(10 , 100 , size=randomize)
      seting = list(set(Dup))
      print(len(seting))
      print("\n")
      print(Dup)
      print("\n")
      


      len_shoir = int(input(f'{Fore.GREEN}[+] Enter Duplicate len : '))
      if len(seting) == len_shoir: 
         print(F"{Fore.GREEN}Well done, you answered correctly.")
         Agin_Dup = str(input(f'{Fore.GREEN}[+] Do you want to play again [y:n] : '))
         if Agin_Dup == "y".lower(): 
            Duplicate() 
         else:
            pass
      else:
         print(f"{Fore.RED}You answered wrong.")
         
         AginDup = str(input(f'{Fore.GREEN}[+] Do you want to play again [y:n] : '))
         
         if AginDup == "y".lower():
            Duplicate()
         else:
            pass
   try:
      Duplicate()
   except: 
      print(f"{Fore.RED}Error")


elif main == 8: 
   def powers(): 
      pows = random.randint(5,50)
      print(F"{Fore.GREEN}{pows} ** {pows} = ?")
      print(pows ** pows) 
      
      shs_ = int(input(f'{Fore.CYAN}Enter number : '))
      if shs_ == pows ** pows: 
         print(F"{Fore.GREEN}Well done, you answered correctly.")
         Agins = input(f"{Fore.GREEN}[+] Do you want to play again [y:n] : ")
         if Agins == 'y'.lower():
            powers() 
         else:
            pass
      else: 
         print(f'{Fore.RED}You answered wrong.')
         Agins = input(f"{Fore.GREEN}[+] Do you want to play again [y:n] : ") 
         if Agins == "y".lower(): 
            powers()
         else:
            pass
   try: 
      powers()
   except: 
      print(f"{Fore.RED}Error")

elif main == 9: 
   def two_number(): 
      umber = random.randrange(10,1002)
      print(f"{Fore.GREEN} {umber} / 2") 
      print(F"ok Quiz : {umber /2}")
      input_me = float(input(f'{Fore.WHITE} Enter number : '))
      if input_me == umber / 2: 
         print(f"{Fore.GREEN}well!") 
         cheack_out = str(input('[+] Do you want to play again [y:n] : '))
         if cheack_out == 'y'.lower(): 
            system('clear') 
            two_number() 
         else:
            pass

      else: 
         print(f"{Fore.RED}oh..sorry!") 
         cheack_out_lossed = str(input('[+] Do you want to play again [y:n] : '))
         if cheack_out_lossed == 'y'.lower(): 
            system('clear')
            two_number()  
         else: 
            pass 
   
   two_number() 
