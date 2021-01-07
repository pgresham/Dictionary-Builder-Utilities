#!/usr/bin/python3

import os
from termcolor import colored
import sys

#This program was tested on the Hunspell
#( https://hunspell.github.io/ ) dictionary.
#This assumes that '/' is used to split the
#dictionary entries where applicable. 



#clears screen, returns nothing.
def clear():
    os.system('clear')

#takes in string
#retunrs green [ ok ] followed by string
def okay(string):
    ok = colored('ok','green')
    print('[ '+ok+' ] '+string)

#takes in string
#returns red [error] followed by string
def error(string):
    error = colored('error','red')
    print('['+error+'] '+string)

#takes in string on stdin. 
#loops until y/n entered.
#returns True for y, False for n.
def tryagain():
    entry = str(input('try again? y/n >'))
    if entry == 'y':
        return True
    elif entry == 'n':
        return False
    else:
        tryagain()

#takes in list,split symbol (optional)
#returns list without dictionary markup
#Hunspell uses / at end of each word
#but this can be changed for other cases
def cleanup(dictionary,splitter='/'):
    cleaned = []
    for i in dictionary:
        cleaned.append(i.split(splitter)[0])
    return cleaned

#takes in list
#returns list with no entries
#containing upper case characters
def remove_proper(dictionary):
    improper = []
    for i in dictionary:
        if any(x.isupper() for x in i):
            pass
        else:
            improper.append(i)
    return improper

#takes in filename as string
#returns a list stripped of newlines
def dictionary_load():
    dictionary = []
    try:
        dic_file = str(input('Dictionary filename >'))
        with open(dic_file,'r',encoding='latin-1') as f:
            for i in f:
                dictionary.append(i.strip('\n'))
            f.close()
        clear()
        return dictionary
    except:
        error(dic_file+' could not be loaded.')
        if tryagain():
            return dictionary_load()
        else:
            exit()
        
#takes in list
#returns dictionary stripped of numbers
#this likely does not pertain most dictionaries
def remove_digits(dictionary):
    undigit = []
    for i in dictionary:
        if any(x.isdigit() for x in i):
            pass
        else:
            undigit.append(i)
    return undigit
#takes in dictionary
#returns filename string

def writedown(dictionary):
    filename = str(input('Enter filename [output.txt]'))
    if filename == '':
        filename = 'output.txt'
    with open(filename,'w') as f:
        for i in dictionary:
            f.write(i+'\n')
        f.close()
    return filename        

def main(dictionary,di_flag=1,cl_flag=0,up_flag=0,dt_flag=0,sa_flag=0,filename=''):
    c = ''
   # di_flag Dictionary Loaded Flag
   # cl_flag Cleanup Flag
   # up_flag Uppercase Flag
   # dt_flag Digits Removed Flag
   # sa_flag Saved Flag
   # filename is the output file name

    while c != '00':
        print('.dic to .txt converter\n')
        print('1  Clean dictionary markup (Do this first)')
        print('2  Remove Uppercase (Proper names, etc.)')
        print('3  Remove Digits (Sometimes applicable)')
        print('4  Save Dictionary')
        print('00 Exit')

        print('------------------------------------------')
        if di_flag ==1:
            okay(' dictionary loaded')
        if cl_flag ==1:
            okay(' dictionary cleaned')
        if up_flag ==1:
            okay(' uppercase-containing words removed')
        if dt_flag ==1:
            okay(' digit-containing words removed')
        if sa_flag ==1:
            okay(' dictionary saved '+filename)
        
        c = str(input('> '))
        if c == '1':
            splitter = str(input('Split character [/] > '))
            if splitter == '':
                splitter = '/'
                
            dictionary = cleanup(dictionary,splitter)
            cl_flag=1
            clear()
        elif c =='2':
            dictionary = remove_proper(dictionary)
            clear()
            up_flag = 1
        elif c =='3':
            dictionary = remove_digits(dictionary)
            clear()
            dt_flag = 1
        elif c =='4':
            filename = writedown(dictionary)
            clear()
            sa_flag = 1
        elif c =='00':
            pass
        else:
            clear()

if __name__ == '__main__':
    clear()
    dictionary = dictionary_load()
    main(dictionary)

