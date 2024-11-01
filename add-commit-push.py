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

# Check if there is at least one argument
if len(sys.argv) > 1:
    first_arg = sys.argv[1]  # The first argument (after the script name)
    print(f"The first argument is: {first_arg}")
else:
    print("No arguments were provided.")
    
executeCommand("git commit -m \"Update files.\"")
executeCommand("git push")
