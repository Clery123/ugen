import sys, getopt
from os.path import exists
import os
import argparse

def main(argv):
    input_files = []
    try:
        opt= argv[0] # -o or -h
        if(opt == '-h' or opt == '--help'): #diplay help
            print('py -3 ugen.py -o [output file] [input file] ...\npy ugen.pykkdlfdflk -o [output file] [input file] ...')
            return "help"
        if(len(argv) <3): #passed less then 3 arguments
            print('py -3 ugen.py -o [output file] [input file] ...\npy ugen.learray -o [output file] [input file] ...')
            return "no input"
    except : #wrong arguments
        print('py -3 ugen.py -o [output file] [input file] ...\npy ugen.py -o [output file] [input file] ...')
        return
    output_file = argv[1]
    for arg in argv[2:]:#for every input file
        if (opt == "-o" or opt == "--output"):
            input_files.append(arg) #append to list
        else:
            print('py -3 ugen.py -o [output file] [input file] ...\npy ugen.py -o [output file] [input file] ...')
            return
        #return
    write_output(output_file, input_files)

def from_files_to_list(input_fs): #open files and append everything to the list
    lstF = []
    for i in input_fs: #foreach file
        fil = open(i, "r")
        for x in fil: #append lines to list
            lstF.append(x)
        fil.close()
    return lstF

def generate_username(lstF):
    lst = []
    for y in lstF:
        y = y.strip('\n')
        try:
            x_split = y.split(':')
            if(len(x_split) <4 or len(x_split) >5 ): #Something is missing or there is an extra data
                raise Exception()
            if(len(x_split[2]) == 0): #middle name missing
                temp_string = (x_split[1][0] + x_split[3]).lower()
            else: #with middle name
                temp_string = (x_split[1][0] + x_split[2][0] + x_split[3]).lower()
            x_split.insert(1, temp_string) #insert username
            str1 = ''
            remove_empty = list(filter(None, x_split)) #remove empty middle name
            

            for xsp in x_split: #combine data into 1 string separated with ':'
                str1 += xsp+":"
            lst.append(str1[:-1]) #append it to the list without ':' at the end
        except:
            print("File structure does not match the template:\nID:forename:middle_name(optional):surname:department")
            return "MatchError"
    return lst

def write_output(output_f, input_fs): 
    if(check_files(input_fs)):
        liststFile = from_files_to_list(input_fs)
        lst = generate_username(liststFile)
        
        with open(output_f, 'w') as f: #write data to file output
            for li in lst:
                f.write(li+'\n')
            f.close()
    else:
        print("File does not exist\n")
        return "Does not exist"
    
def check_files(input_files, k = 0): #if file does not exist return False else True
    #checking multiple files if they exist with recursion
    if(exists(input_files[k]) and k == len(input_files)-1):
        return True
    k+=1
    return False if exists(input_files[k])==False else check_files(input_files, k) 
        

        
    
if __name__ == '__main__':
    main(sys.argv[1:])