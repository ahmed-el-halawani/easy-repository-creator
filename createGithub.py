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
        commands = [r'cd /D ' + repoDir + '&',
                    'git init &',
                    'echo ' + str(repoName) + ' >> README.md &',
                    'git add README.md &',
                    'git add * &'
                    'git commit -m "init commit" &',
                    'git remote add origin ' + str(url) + ' &',
                    'git push -u origin master &',
                    'exit'
                    ]
        cmdText = ""
        for i in commands:
            cmdText += i
        os.system(cmdText)
        self.updateRepo(repoDir)

    def updateRepo(self, repoDir):
        commands = [r'cd /D ' + repoDir + '&',
                    'git pull origin master &'
                    'git add * &',
                    'git commit -m "init commit" &',
                    'git push -u origin master &',
                    'exit'
                    ]
        cmdText = ""
        for i in commands:
            cmdText += i
        os.system(cmdText)
        while True:
            cmdText = str(input("1) update \n2) exit\n---enter choice: "))
            if cmdText == "1":
                self.updateRepo(repoDir)
                break
            else:
                break


if __name__ == "__main__":
    x = str(input("1- for create new repo \n2- for update repo\n---enter choice: "))
    if x == "1":
        inputMessage = "repo name: "
        projectName = ""
        count = 0
        while True:
            count += 1
            projectName = str(input(inputMessage))
            if len(projectName) == 0:
                inputMessage = "repo name" + count * " plz" + ": "
            else:
                inputMessage = "project dir: "
                projectDir = ""
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
        projectDir = ""
        count = 0
        while True:
            count += 1
            projectDir = str(input(inputMessage))
            if len(projectDir) == 0:
                inputMessage = "project dir" + count * " plz" + ": "
            else:
                repoCreator().updateRepo(projectDir)
                break
    else:
        print("error choice")
