import pyttsx
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
#phantomjs_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe'
#browser=webdriver.PhantomJS(phantomjs_path)
#browser.set_window_size(1024,768)
chromedriver="D:\\seleniumchromedriver\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
browser.get("https://www.google.co.in/webhp?gfe_rd=cr&ei=YdmxVt_UEMeuogPZ4ZnwCw&gws_rd=ssl#q=Pune+weather")
delay = 10

try:
    WebDriverWait(browser,delay).until(
        EC.presence_of_element_located((By.ID,"wob_loc"))
        )
except TimeoutException:
    print "Loading took too much time!"
	
	
location=browser.find_element_by_id("wob_loc")
day=browser.find_element_by_id("wob_dts")
condition=browser.find_element_by_id("wob_dc")
celcius=browser.find_element_by_id("wob_tm")
precipitation=browser.find_element_by_id("wob_pp")
humidity=browser.find_element_by_id("wob_hm")
wind=browser.find_element_by_id("wob_ws")
engine = pyttsx.init()
engine.setProperty('rate',95)
engine.say("This is just a rather very intelligent system")
engine.say("desinged to assist tanmay sir in his personal work.")
engine.say("WAKING UP NOW")
engine.say("Hello Tanmay Sir. Good Morning.")
engine.say("Your Location is "+location.text)
engine.say("Today is"+day.text)
engine.say("Full weather Report Generated")
engine.say("Weather today looks"+condition.text)
engine.say("Temperature today is"+celcius.text+"degree celicious")
engine.say("Precipitation predicted is"+precipitation.text)
engine.say("Humidity recorded is"+humidity.text)
engine.say("Wind is blowing with"+wind.text)
engine.say("Weather report completed")
engine.say("Thank you sirr. Have a good and wonderful day ahead!")
engine.runAndWait()
