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
    def __init__(self, projectName: str, projectDir: str):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 30)
        self.projectName = projectName
        self.projectsPath = projectDir
        self.email = "agomaa528.ag@gmail.com"
        self.password = "Aa01097033133"
        self.makeRepo()

    def makeRepo(self):
        self.driver.get("https://github.com/login")

        # auth
        self.driver.find_element_by_id("login_field").send_keys(self.email)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_id("password").send_keys(Keys.ENTER)
        self.driver.get("https://github.com/new")

        # create repo
        create = self.driver.find_element_by_id("repository_name")
        create.send_keys(self.projectName)
        time.sleep(1)
        self.driver.find_element_by_css_selector("button.btn.btn-primary.first-in-line").submit()
        print("submit...")

        # after create repo
        self.wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "body")))
        repoUrl = self.driver.current_url
        self.createLocalRepo(repoUrl)

    def createLocalRepo(self,url):
        # push file
        comands = [r'cd /D ' + self.projectsPath + '&',
                   'git init &',
                   'echo ' + str(self.projectName) + ' >> README.md &',
                   'git add README.md &',
                   'git add * &'
                   'git commit -m "init commit" &',
                   'git remote add origin '+str(url)+' &',
                   'git push -u origin master &'
                   'exit'
                   ]
        x = ""
        for i in comands:
            x += i
        os.system(x)

    # def updateLocalRepo(self):
    #     commands = ['git add * &'
    #                 'git commit -m "init commit" &',
    #                 'git remote add origin ' + str(self.repoUrl) + '&',
    #                 'git push -u origin master &'
    #                 'exit'
    #                 ]
    #     x = ""
    #     for i in commands:
    #         x += i
    #     os.system(x)


if __name__ == "__main__":
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
                    repoCreator(projectName, projectDir)
                    break
