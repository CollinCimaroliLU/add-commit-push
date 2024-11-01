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
    # Print the first and second argument
    print(f"The first argument is: {sys.argv[1]}")
    print(f"The second argument is: {sys.argv[2]}")
    
else:
    print("No arguments were provided.")
    
gitCommit="git commit -m \"Update files.\""
executeCommand(gitCommit)
executeCommand("git push")
