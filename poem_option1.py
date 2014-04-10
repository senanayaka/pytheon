from sys import version_info,exit

## This function filters the user given words
def filterWords(word_list):
    
    output = ''
    f = open('poem.rtf','rU')
    for line in f:
	line_mod = line
        for word in word_list:
	    line_mod = line_mod.replace(word,'')
	output = output+line_mod
    return output

print '\n\tWhat would you like to do ?\
\n\n\t1. Fileter file with selected words\
\n\t2. Show the word counts of the file\
\n\t3. Filter file by the most popular words in the file\
\n\t4. Quit\n'

## check python version
if version_info[0] <= 2:
    choice = raw_input("Choice?  ")
elif version_info[0] == 3:
    choice = input("Choice? ")

## We have only 4 options
if not int(choice) in [1,2,3,4]:
    print 'Invalid Choice'
    exit(0)

## Option 1
if choice == '1':
    print 'Enter the words you like filtered from the text.'
    words = raw_input('Words: ')
    word_list = words.split()
#    print word_list
    print 'Here\'s your filtered text :\n\n'
    filtered_output = filterWords(word_list)
    print filtered_output
    print 

