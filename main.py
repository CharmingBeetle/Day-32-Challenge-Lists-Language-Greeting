import random
import os
import time

greeting = ["Hello!",
 "Bonjour!",
 "Konnichiwa!", 
 "Hola!", 
 "Ciao!", 
 "Namaste!", 
 "Ni hao!",
 "Ahn-young-ha-se-yo!", 
 "Ola!", 
 "Merhaba!",
 "Guten Tag!",
 "Geia!"]

emoji = ["🖐🏾","👨🏼‍🦰","👨‍🦱","👧🏾","👨🏽‍🦱","👳🏿‍♂️", "🧑🏻","🧒🏻","👩🏽","👳🏽‍♂️","👩🏻‍🦰","👴🏽"]

def greet():
  randNum = random.randint(0,11) # Generate a random number
  # could also use random.randint(0, len(greeting)-1)
  # plug in the random number as an index value
  print(f"{emoji[randNum]}{greeting[randNum]}") 
  time.sleep(3)
  os.system("clear")

greet()

