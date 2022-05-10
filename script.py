from selenium import webdriver
import sys
import time

# set default download location
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : r"C:\Users\victo\Downloads\Test\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "chromedriver.exe"

# function to convert a list into string
def convert(s):
    str1 = ""
    return(str1.join(s))
		
# Assign the arguments passed to a variable search_string
search_string = sys.argv[1:]

# The argument passed to the program is accepted
# as list, it is needed to convert that into string
search_string = convert(search_string)

# This is done to structure the string
# into search url.(This can be ignored)
search_string = search_string.replace(' ', '+')


# Assigning the browser variable with chromedriver of Chrome.
# Any other browser and its respective webdriver
# like geckodriver for Mozilla Firefox can be used
browser = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

# keywords list
keywordsList = ["\"emergency+response\"", "digital+democracy"]

# get searched term in google scholar and maximize window
# allow time to fill out captcha
for keyword in keywordsList:
    matched_elements = browser.get("https://scholar.google.com/scholar?as_ylo=2022&q=" + keyword + "&hl=en&as_sdt=0,48")
    browser.maximize_window()
    time.sleep(10)
    
    # get all cite buttons, download all refmans, repeat for multiple pages
    for i in range(2):
      citeButtons = browser.find_elements_by_css_selector("a.gs_or_cit.gs_or_btn.gs_nph")
      for x in citeButtons:
          button = x
          button.click()
          time.sleep(1)
          button = browser.find_element_by_css_selector("#gs_citi > a:nth-child(3)")
          button.click()
          time.sleep(1)
          button = browser.find_element_by_css_selector("#gs_cit-x")
          button.click()
          time.sleep(1)

      nextButton = browser.find_element_by_css_selector("#gs_n > center > table > tbody > tr > td:nth-child(12) > a")
      nextButton.click()
      time.sleep(3)

# for i in range(1):
#     matched_elements = browser.get("https://scholar.google.com/scholar?as_ylo=2022&q=" + search_string + "&hl=en&as_sdt=0,48")
#     browser.maximize_window()
#     time.sleep(10)

# py -3 -m venv .venv
# .venv\scripts\activate

