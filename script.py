import os
import sys
os.path.dirname(sys.executable)
from selenium.webdriver.common.by import By

from time import sleep
from selenium import webdriver
# this is tested on Firefox or you can use "webdriver.Chrome()"
driver = webdriver.Chrome()
# driver.get('https://cumsdtu.in/registration_student/login/login.jsp?courseRegistration')
# user= driver.find_element(By.XPATH,"//input[@name='userName']")
# user.send_keys('2K20/EP/95')
# passw= driver.find_element(By.XPATH,"//input[@name='password']")
# passw.send_keys('9013844884')
# login= driver.find_element(By.XPATH,"//input[@value='Log In']")
# login.click()
# # user.send_keys('2K20/EP/95')
# # passw= driver.find_element(By.XPATH,"//input[@name='password']")
# # passw.send_keys('9013844884')
# # login= driver.find_element(By.XPATH,"//input[@value='Log In']")
# # login.click()
# sleep(4)
# l= driver.find_element(By.XPATH,"//div[@title='MACHINE LEARNING']")
# # reg1=driver.find_element(By.XPATH,"//button[@class='narrow mat-button mat-save']")
# # register= driver.find_element(By.XPATH,"//button[@ng-reflect-color='save']")
# l[3].click()
# register.click()
# reg1.click()
# l.click()
while True:
    try:
        driver.get('https://cumsdtu.in/registration_student/login/login.jsp?courseRegistration')
        user= driver.find_element(By.XPATH,"//input[@name='userName']")
        user.send_keys('2K20/EP/96')
        passw= driver.find_element(By.XPATH,"//input[@name='password']")
        passw.send_keys('11112001S@k')
        login= driver.find_element(By.XPATH,"//input[@value='Log In']")
        login.click()
        # user.send_keys('2K20/EP/95')
        # passw= driver.find_element(By.XPATH,"//input[@name='password']")
        # passw.send_keys('9013844884')
        # login= driver.find_element(By.XPATH,"//input[@value='Log In']")
        # login.click()
        sleep(10)
        dl= driver.find_element(By.XPATH,"(//div[@title='Deep Learning'])[1]")


        ic= driver.find_element(By.XPATH,"//div[@title='Laser and Instrumentation']")
        # bp= driver.find_element(By.XPATH,"(//div[@title='BIOPHYSICS'])[2]")
        # ps= driver.find_element(By.XPATH,"//div[@title='Probability Statistics']")

        for i in range(1000):
            try:
                dl.click()
                
                reg1=driver.find_element(By.XPATH,"//button[@class='narrow mat-button mat-save']")
                register= driver.find_element(By.XPATH,"//button[@ng-reflect-color='save']")
                try:
                    ic.click()
                    sleep(0.4)
                    register.click()
                    reg1.click()
                except:
                    print("IC registered or Not available")
                sleep(0.4)
                try:
                    dl.click()
                    sleep(0.4)
                    register.click()
                    reg1.click()
                except:
                    print("Deep Learning Already registered or Not available")
                sleep(0.4)
                
                # try:
                #     bp.click()
                #     sleep(0.4)
                #     register.click()
                #     reg1.click()
                # except:
                #     print("BioPhysics Already registered or Not available")
                # sleep(0.4)
                # try:
                #     ps.click()
                #     sleep(0.4)
                #     register.click()
                #     reg1.click()
                # except:
                #     print("Probability Statistics Already registered or Not available")
                # sleep(0.4)
            except:
              print("Registration Closed")
    except:
              print("Site Down")
