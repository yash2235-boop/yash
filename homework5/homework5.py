# Git vs. GitHub
# Git is a version control tool used to track code changes. GitHub is a website that hosts Git repositories online for sharing and collaboration.

# Terminal vs. Command Line
# The terminal is the program where you type text commands. The command line is the actual interface inside the terminal where you enter the commands.

# Local vs. Remote Repository
# Local is on your own computer whereas remote is stored online (lke github) so others can access it.

# Version Control
# A system that records changes to files over time, allowing you to go back to earlier versions and work collaboratively without losing progress

# Staging Area
# The space where git keeps track of files that are ready to be committed to the repository.

# git add
# Adds changes from your working directory to the staging area.

# git commit
# Saves the staged changes to the repository with a message describing what was done.

# git push
# Uploads your committed changes from your local repository to the remote repository (like GitHub).

# git status
# Shows which files have been changed, staged, or committed.

# git pull
# Downloads and merges changes from the remote repository into your local repository.

# pwd
# Prints the current working directory (shows where you are in the file system).

# ls 
# Lists all files and folders in the current directory.

# cd
# Changes the current directory (move into another folder).

# nano
# Opens a simple text editor inside the terminal to edit files.

# touch
# Creates a new empty file.

# mv
# Moves or renames a file or folder.

# rm
# Deletes a file or folder.

# cat
# Displays the contents of a file in the terminal.


#Q2
# • You have been plopped into Judy’s directory system. What command will tell you what your current working directory is?
# pwd

# • The terminal responds by saying you are in ∼/python decal/judy decal. What command
# will list all the files in your current working directory?
# ls

# • Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py.
# You will need to pull the brianna repo repository to find the updated file. What command(s)
# will let you move to the correct repository and pull the latest changes?
# cd ../brianna_repo
# git pull


# • How would you move this new homework.py to the homework/ folder in your personal repository?
# mv homework.py ../judy_decal/homework/


# • How would you move yourself to the same repository as homework.py?
# cd ../judy_decal/homework


# • You want to see the contents of homework.py in your terminal, how would you do this?
# cat homework.py


# • Great job! You just finished the homework for this week. What command(s) allow you to
# save the changes and push from your local repository to your remote repository?
# git add .
# git commit -m "Finished homework"
# git push

# • Oh no! Git gave you the following error. What commands should you call to resolve this
# error and push your homework properly? What does the error mean? (i.e. what did “Judy” do wrong when trying to push?)
# The error means someone else pushed changes to GitHub that you don’t have locally. You need to pull those updates before pushing again.
# git pull --rebase
# git push

# • What absolute path will allow you to move to Recents/?
# cd ~/Recent


#4
#4.1
def checkDataType (value):
    return type(value)

# print (checkDataType(3.14))
# print (checkDataType(True))

#4.2
def evenOrOdd(integer):
    if integer % 2 == 0:
        return ("Even")
    else:
        return ("Odd")

# print (evenOrOdd(7))
# print (evenOrOdd(8))

#5
numbers = [1, 2, 3, 4, 5]
def sumWithLoop (numbers):
    total = 0
    for i in numbers:
        total += i
    return total

# print(sumWithLoop(numbers))

#6
# #6.1
list = ["a", "b", "c"]

def duplicateList(list):
    new_list = []
    for item in list:
        new_list.append(item)
        new_list.append(item)
    return new_list

# print (duplicateList(list))

#6.2
def square(num):
    return num * num
#missing a colon after def