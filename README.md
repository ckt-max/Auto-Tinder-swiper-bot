# Auto-Tinder-swiper-bot
 A bot to swipe right on profiles displayed by Tinder

A bot that right swipes on all profiles that tinder shows using Selenium

The code is basically divided into two parts: Logging in, and Swiping.See the code to understand how it works

Notes:

--- LOGGING IN --- 
-- Set up a tinder account( or login if you already have one), and make sure to login using Facebook(I have used Facebook to avoid any OTP verification, and also logging in using Google is a tedious process) 
-- Tinder remembers the device, so you will have to do phone number verification only once.That 's why I have asked you to go through the above step 
-- If the bot gives an output 'Please Retry'. It 's because Tinder's website uses two different login pages.And this code avoids one of them.So just run the code again in your IDE(you might require to do it 3 - 4 times at times.My apologies for the inconvenience caused)

--- BROWSER --- 
-- So I have used 'Edge' for this project.If you want to use another browser such as Safari, or Chrome or Firefox just replace the respective selenium libraries.You can look for in documentation.For chrome, just change 'edge' to 'chrome' everywhere.Such as change 'selenium.webdriver.edge' to 'selenium.webdriver.chrome'

--- SLEEP ---
-- I have used the 'sleep' keyword wherever I felt it was necessary.If you think your PC can run the code faster or slower, then adjust the delays accordingly
