# os module functions

import os

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

#--------
#path in Linux uses forward slashes
# usr/bin/spam

os.makedirs('C:\\delicious\\walnut\\waffles')

# base name and dir name

path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path)

os.path.dirname(path)

#file properties


os.path.getsize('C:\\Windows\\System32\\calc.exe')
os.listdir('C:\\Windows\\System32')

# validity
os.path.exists('C:\\Windows')

os.path.exists('C:\\some_made_up_folder')

os.path.isdir('C:\\Windows\\System32')

os.path.isfile('C:\\Windows\\System32')

os.path.isdir('C:\\Windows\\System32\\calc.exe')

os.path.isfile('C:\\Windows\\System32\\calc.exe')

# reading files

sonnetFile = open('sonnet29.txt')
sonnetFile.readlines()

#write files

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)




