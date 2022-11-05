## Python3 script to assist with manual review and organization of text files
## Uses Linux OS commands to print contents/preview of a text file
## and gives user the option to copy the file to a directory

import os
import shutil

# Get and display current directory
curDir = os.getcwd();
print('Current Working Directory is ' + curDir)

# ask user for directory path files should be copied too
copyDir = input('Enter path of directory to copy files\n')

# Check if user specified path exists
if os.path.exists(copyDir):
    print('Files will be copied to ' + copyDir)
else:
    print('Would you like to create a new directory at ' + copyDir + '?\n')
    newDirAnswer = input('Y/N?\n')
    newDirAnswer = newDirAnswer.upper()
    if newDirAnswer[0] == 'Y':
        print('Creating new directory ' + copyDir)
        os.mkdir(copyDir)
    else:
        print('New directory not created.\nNo destination to copy files to.\n Exiting...')
        exit()

# list files in current directory
print('Files in CWD;\n')
os.system('ls')
print('\n\n')

# Loop over every file in curDir, run 'head' to preview contents
# ask user if file should be copied
for file in os.listdir(curDir):
    f = os.path.join(curDir, file)
    # Check that it is a file
    if os.path.isfile(f):
        name = os.path.basename(f)
        
        # print name of current file in loop
        print('-------- Head of ' + name + '--------\n')
        
        # build HEAD command to pass to os.system()
        cmd = 'head ' + name
        os.system(cmd)
                
        # Ask if file should be copied
        answer = input('\nWould you like to copy ' + f + ' to ' + copyDir + '?\nY/N?\n')
        answer = answer.upper()
        
        # if Yes, copy file to copyDir. shutil.copy syntax is src, dst
        if answer[0] == 'Y':
            print('Copying ' + f + '\nto ' + copyDir + '\n')
            shutil.copy(f, copyDir)
            print('\n\n\n---Next File--->\n\n\n')
        else:
            print(f + ' not copied\n')
            print('\n\n\n---Next File--->\n\n\n')
            continue