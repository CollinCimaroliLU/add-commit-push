import os
import sys

def executeCommand(cmd):
    print(cmd)
    os.system(cmd)
    print("")

print("Add Commit Push")
print("")
executeCommand("git status")

response=input("Would you like to add commit and push (Y/N)? ")

# check if the input is not equal to "y"
if response != "Y":
    print("You did not respond with Y")
    sys.exit()


executeCommand("git add -A")

# Check if there are two arguments
CommitMessage="Update files."
if len(sys.argv) > 2:
   CommitMessage=sys.argv[2]
    
gitCommit="git commit -m \""+CommitMessage+"\"" 
executeCommand(gitCommit)
executeCommand("git push")
