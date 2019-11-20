# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, re
import winsound
import pyautogui
import pyperclip
ur = ""
class ZD:
    def __init__(self,fromInput,fromOutput,date):
        self.fromInput=fromInput
        self.fromOutput=fromOutput
        self.date=date
        
    def poisk(self):
        global ur
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        base_url = "http://rzd.ru/"
        verificationErrors = []
                

        driver.get(base_url)

        datin=driver.find_element_by_id("date0")
        datin.click()
        for i in range(13):
            pyautogui.press('backspace')
        datin.send_keys(self.date)
        inp=driver.find_element_by_id("name0")

        inp.send_keys(str(self.fromInput))
        inp.click()
        time.sleep(1.3)
        pyautogui.press('down')
        time.sleep(0.8)
        pyautogui.press('enter')
        outp=driver.find_element_by_id('name1')

        outp.send_keys(str(self.fromOutput))
        outp.click()
        time.sleep(0.6)
        pyautogui.press('down')
        time.sleep(0.6)
        pyautogui.press('enter')
        button=driver.find_element_by_xpath('//*[@id="Submit"]')
        time.sleep(0.4)
        button.click()
        ur=driver.current_url
        
        try:
        	mb=driver.find_element_by_xpath('//*[@id="Page0"]/div/div[2]/div[1]/div[3]/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/span')
        	mb.click()
        except:
        	driver.quit()
        	return("не найдены")
        else:
        	driver.quit()
        	return(ur)

        