import os

def executeCommand(cmd):
    print(cmd)
    os.system(cmd)
    print("")

print("Add Commit Push")
print("")
executeCommand("git status")
executeCommand("git add -A")
executeCommand("git commit -m \"Update files.\"")
executeCommand("git push")
