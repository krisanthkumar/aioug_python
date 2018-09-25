#Open and write to file
f = open('Todo.txt','a')
f.write("Hello World\n")
f.close()

"""****************************************************************"""
import os
os.getcwd() #print current working directory
os.chdir('E:\\Learning\\AIOUG\\September\\scripts')
os.listdir()
"""
r	To read a file (default)
w	To write a file; Creates a new file if it doesn’t exist, truncates if it does
x	Exclusive creation; fails if a file already exists
a	To append at the end of the file; create if doesn’t exist
t	Text mode (default)
b	Binary mode
+	To open a file for updating (reading or writing)
"""

"""****************************************************************"""
#Open and write to file
f = open('Todo.txt','a')
f.write("Hello World\n")
f.write("This is second line\n")
f.write("Third line here\n")
f.write("Last line on the file\n")
f.close()

"""****************************************************************"""
#Read the file all together
todo=open('Todo.txt',mode='r',encoding='utf-8')
todo.read()
todo.close()

"""****************************************************************"""
#Read the file line by line
todo=open('Todo.txt',mode='r',encoding='utf-8')
todo.readline()
todo.readline()
todo.close()

"""****************************************************************"""
#Read the whole file to a list per line
todo=open('Todo.txt',mode='r',encoding='utf-8')
todo.readlines()
todo.close()

"""****************************************************************"""
#Ignore the work of opening and closing the files
with open('Todo.txt') as todo:
    todo.read()

"""****************************************************************"""
#Write multple lines
fh = open('Todo2.txt','a')
lines_of_text = ['One line of text here\n', 'and another line here\n', 'and yet another here\n', 'and so on and so forth\n'] 
fh.writelines(lines_of_text) 
fh.close()

"""****************************************************************"""
#Issue when file is not closed
todo=open('Todo.txt',mode='r',encoding='utf-8')
todo.readlines()

todo.close()

"""****************************************************************"""
#Read a non avaiable file
todo=open('IAmNotThere.txt',mode='r',encoding='utf-8')
todo.readlines()

"""****************************************************************"""
#Try to read the unavailable file case failure
try:
    todo=open('IAmNotThere.txt',mode='r',encoding='utf-8')
    todo.readlines()
except IOError:
    print("Sorry, file not available")
except:
    print("Some other error")
finally:
    todo.close()
