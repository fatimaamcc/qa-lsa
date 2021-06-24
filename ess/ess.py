# importing selenium
from selenium import webdriver

# Loading chromedriver which is in directory Selenium from the current dir
driver = webdriver.Chrome()

# opening text file
file = open("url.txt")

print("Checking script tag")
# read websites line by line
for website in file:
    # removing trailing spaces from website if exist
    website = website.strip()
    # opening the website using driver.get
    driver.get(website)
    # checking if script /scripts/lsa.min.js exist using try/catch
    try:
        # checking for the script
        source = driver.find_element_by_xpath("//script[@src='/scripts/lsa.min.js']")
        # displaying for exist
        #print("lsa.min.js exists in " + website)
    except:
        print("lsa.min.js doesn't exist in " + website)
        
file.close()
driver.close()

