'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Riegel
email: honzikriegel@gmail.com
'''

import random
import os

mezernik = 40*'-'

def uvodni_text():
    '''
    funkce zobrazí úvodní text
    výstup:
    text...
    -------
    text...
    -------
    '''
    print(f'Hi there!\n{mezernik}\nI have generated a random 4 digit number for you.\nLet´s play a bulls and cows game.\n{mezernik}')
    
def vytoreni_tajného_cisla():
    '''
    program vybere číslo na 1. pozici v int.(1;9)
    na zbylé pozice z intervalu(0;9)
    spojí je do řetězce
    '''
    while True:
        first_digit = random.randint(1, 9) 
        remaining_digits = random.sample(range(10), 3) 
        number = [first_digit] + remaining_digits    
        tip = ''.join(map(str, number)) 
        if len(tip) == len(set(tip)):
            break   
    return tip 
            
def zadani_čísla():
    '''
    vyžádá číslo a ověří jeho platnost
    '''
    while True:
        cislo = input('Enter a number: ')
        if len(set(cislo)) == 4 and cislo.isnumeric():
            if cislo[0] != 0:
                break
        else:
            print('Not omptimal number')
            continue
                      
    return cislo                      

def vyhodnot_tip(cislo, tajne_c):
    '''
    spočte bulls a cows
    '''
    
    bulls = 0
    for i in range(4):
        if cislo[i] == tajne_c[i]:
            bulls += 1
    cow = 0
    for c in tajne_c:
         if c in cislo:
            cow += 1
            cows = cow - bulls
            
    return [bulls, cows]        
    
def zobrazeni_bulls_cows(seznam):
    bulls_text = "bull" if seznam[0] == 1 else "bulls"
    cows_text = "cow" if seznam[1] == 1 else "cows"
    print(f"{seznam[0]} {bulls_text}, {seznam[1]} {cows_text}")

def hra():
    '''
    Program hry
    '''
    os.system('cls')
    uvodni_text()
    tip = vytoreni_tajného_cisla()
    pokusy = 0
    while True:
        
        
        cislo = zadani_čísla()
        seznam_2 = vyhodnot_tip(cislo,tip)
        zobrazeni_bulls_cows(seznam_2)
        print(mezernik)
        pokusy += 1
        
        if seznam_2[0]  == 4:
            print(f'Correct, you´ve guessed the right number in {pokusy} guesses!\n{mezernik}\nThat´s amazing!')
            break
        else:
            continue




hra()      