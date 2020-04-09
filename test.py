import os
import subprocess

projectName = "new project"

comands = [r'cd C:\Users\ahmed\PycharmProjects\createGithub\ahmed &',
           'git init &',
           'echo ahmed >> README.md &',
           'git add README.md &',
           'git add * &'
           'git commit -m "init commit" &',
           'git remote add origin https://github.com/mano1997max/firstpro &',
           'git push -u origin master &'
           'exit'
           ]
x = ""
for i in comands:
    x += i
os.system(x)
