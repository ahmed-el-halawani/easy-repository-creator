# !/usr/bin/python
import os
import time
import subprocess

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class repoCreator:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 30)

        self.email = "agomaa528.ag@gmail.com"
        self.password = "Aa01097033133"

    def auth(self):
        # auth
        self.driver.get("https://github.com/login")
        self.driver.find_element_by_id("login_field").send_keys(self.email)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_id("password").send_keys(Keys.ENTER)

    def makeRepo(self, repoName: str):
        time.sleep(1)
        self.driver.get("https://github.com/new")
        # create repo
        create = self.driver.find_element_by_id("repository_name")
        create.send_keys(repoName)
        time.sleep(1)
        self.driver.find_element_by_css_selector("button.btn.btn-primary.first-in-line").submit()
        print("submit...")

        # after create repo
        self.wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "body")))
        repoUrl = self.driver.current_url
        return repoUrl

    def uploadRepo(self, repoName: str, repoDir: str):
        self.auth()
        url = self.makeRepo(repoName)
        # push file
        comands = [r'cd /D ' + repoDir + '&',
                   'git init &',
                   'echo ' + str(repoName) + ' >> README.md &',
                   'git add README.md &',
                   'git add * &'
                   'git commit -m "init commit" &',
                   'git remote add origin ' + str(url) +' &',
                   'git push -u origin master &',
                   'exit'
                   ]
        x = ""
        for i in comands:
            x += i
        os.system(x)
        self.updateRepo(url,repoDir)

    def updateRepo(self,repoUrl,repoDir):
        commands = [r'cd /D ' + repoDir + '&',
                    'git pull origin master &'
                    'git add * &',
                    'git commit -m "init commit" &',
                    # 'git remote add origin http://' + str(repoUrl) + '&',
                    'git push -u origin master &',
                    'exit'
                    ]
        x = ""
        for i in commands:
            x += i
        os.system(x)
        while True:
            x = str(input("1) update \n2) exit"))
            if x == "1":
                self.updateRepo(repoUrl,repoDir)
                break
            else:
                break


if __name__ == "__main__":
    x = str(input("1- for create new repo \n2- for update repo\n enter choice:  "))
    if x=="1":
        inputMessage = "repo name: "
        count = 0
        while True:
            count += 1
            projectName = str(input(inputMessage))
            if len(projectName) == 0:
                inputMessage = "repo name" + count * " plz" + ": "
            else:
                inputMessage = "project dir: "
                count = 0
                while True:
                    count += 1
                    projectDir = str(input(inputMessage))
                    if len(projectDir) == 0:
                        inputMessage = "project dir" + count * " plz" + ": "
                    else:
                        repoCreator().uploadRepo(projectName, projectDir)
                        break
    elif x == "2":
        inputMessage = "project dir: "
        count = 0
        while True:
            count += 1
            projectDir = str(input(inputMessage))
            if len(projectDir) == 0:
                inputMessage = "project dir" + count * " plz" + ": "
            else:
                inputMessage = "repo url: "
                count = 0
                while True:
                    count += 1
                    projectUrl = str(input(inputMessage))
                    if len(projectUrl) == 0:
                        inputMessage = "repo url" + count * " plz" + ": "
                    else:
                        repoCreator().updateRepo(projectUrl,projectDir)
                        break
    else:
        print("error choice")