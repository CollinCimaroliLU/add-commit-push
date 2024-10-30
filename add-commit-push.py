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
print(response)
sys.exit()


executeCommand("git add -A")
executeCommand("git commit -m \"Update files.\"")
executeCommand("git push")
