import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

# fb login details
email = os.getenv('EMAIL')
password = os.getenv('PASS')

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach',True)
driver = webdriver.Edge(options=edge_options)

driver.get('https://tinder.com/')
driver.maximize_window()
main_window_handle = driver.current_window_handle
# Auto Tinder swiper bot

# --------- LOGGING IN --------------
# click on the login button
sleep(5)
try:
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button').click()

except NoSuchElementException:
    print('Please retry')
    driver.close()
    sys.exit()

sleep(2)

# Switch to the popup window
for handle in driver.window_handles:
    if handle != main_window_handle:
        popup_window_handle = handle
        break

# switch back to main window after logging in
driver.switch_to.window(popup_window_handle)


# log in with facebook

driver.find_element(By.ID,'email').send_keys(email)
driver.find_element(By.ID,'pass').send_keys(password, Keys.ENTER)
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div').click()

# -------- GETTING TO SWIPING AND SWIPING
# Switch back to the main window
driver.switch_to.window(main_window_handle)

sleep(7)
# allow location access
driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div/div[3]/button[1]').click()

# no notifications
driver.find_element(By.XPATH,'/html/body/div[2]/main/div[1]/div/div/div[3]/button[2]').click()
sleep(15)

# click on 'I accept' to avoid intercept error
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button').click()
sleep(1)

like_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')


i = 0
while True:
    # print(i)
    try:
        like_button.click()
        sleep(1)
        i+=1
    except ElementClickInterceptedException:
        break

print(f'You have right swiped on {i} people today')


