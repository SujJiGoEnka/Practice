from    selenium import webdriver
from    selenium.common.exceptions import TimeoutException
from    selenium.webdriver.support.ui import WebDriverWait
from    selenium.webdriver.common.by import By
from    selenium.webdriver.support import expected_conditions as EC
from     selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import    time
import    base64


START = "start"
END = "end"


browser = webdriver.Chrome("C:/lib/chromedriver/chromedriver.exe")
browser.implicitly_wait(10)
bTitle = 'SwiftALM Login'
browser.get('http://4sight.infrasofttech.com')
print ("Successfully launched Browser with URL [http://4sight.infrasofttech.com]")
loader = EC.presence_of_element_located((By.XPATH,"//iframe[@onloadfired ='true']"))

# Validate Browser Title
assert bTitle in browser.title, "FAIL: Browser title as[" + bTitle + "] not populating."
print ("Successfully verified browser title as[" + bTitle + "]")

browser.maximize_window()
print ("Successfully Maximised window")

username = browser.find_element_by_xpath("//input[@id='loginId']")
password = browser.find_element_by_xpath("//*[@id='password']")
loginbutton = browser.find_element_by_id('QTP_LoginButton')

username.send_keys('suraj.durgaprasad')
password.send_keys(base64.b64decode('U2h1YmhAbTEyMw==').decode("utf-8", "ignore"))
loginbutton.click()
print ("Successfully entered UID/PWD and clicked on login button")

# time.sleep(1)

# Validate page 2
lUserName = 'surajdurgaprasad'
print("Waiting for dashboard...")
try:
    WebDriverWait(browser, 30).until(loader)
    element = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.ID, "UserName")))    
    print ("PASS: Successfully verified UserName visible in home page as[" + lUserName + "]")
except:
    print("FAIL: Unable to load Home page.")

# Click Setup -> Calender
try:
    oSetup = browser.find_element_by_id("LOCK_Setup")
    ActionChains(browser).move_to_element(oSetup).perform()
    browser.find_element_by_id("LOCK_Calendar").click()
    print ("PASS: Successfully clicked menu [SETUP->Calender] is clicked.")
#     verifying calender page
    

except:
    print ("FAIL: Unable to click [SETUP->Calendar].")
    
element = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH, "//li[@class = 'last']//a[contains(text(), 'Calendar')]")))
print("PASS: Calendar page is opened")

print("Waiting for frame to be available....")
WebDriverWait(browser, 30).until(loader)
browser.switch_to_frame("contentframe")
print("Switched to frame")


try:
    browser.find_element_by_css_selector('#tab2').click()           
    element = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='sectiontab2']//legend[@class='popupLegend']")))
    print ("PASS: Successfully loaded object[Daily Exception] tab.")
except:
    print ("FAIL: Unable to load [Daily Exception] Tab.")

print("Selecting Exceptions to [All]")
# browser.switch_to_frame("contentframe")
select = Select(browser.find_element_by_css_selector("#QTP_KEY_LABEL_Daily_Exceptions"))
select.select_by_visible_text("All")
print("Selected Exceptions to [All] successfully")
table_rows_elements_After_today=[]

table_rows_elements_before_today = browser.find_elements_by_xpath("//*[@id='DailyExTable']/tbody/tr[@myattrib='BeforeToday']")
try:
    table_rows_elements_After_today = browser.find_elements_by_xpath("//*[@id='DailyExTable']/tbody/tr[@myattrib='AfterToday']")
except:
    print("There is no exception added today!!!")    


row_no = len(table_rows_elements_before_today) + len(table_rows_elements_After_today)
print("Total no. of Exceptions before today are: {0}".format(len(table_rows_elements_before_today)))
print("Total no. of Exceptions After today are: {0}".format(len(table_rows_elements_After_today)))

plus_button = '//*[@id="img_1_lm_'+str(row_no-1)+'"'+']'
# str(row_no-1)
browser.find_element_by_xpath(plus_button).click()
print("Clicked on [+] button to add new daily exception")

new_row_no =str(row_no+1)
# browser.find_element_by_xpath("//*[@id='DailyExRow_"+new_row_no+"'""]/td[1]/a").click()

  
def calender(calendar_type, year, month, date):
    if(calendar_type=="start"):
        browser.find_element_by_id("fromDate_lm"+new_row_no).send_keys(date+"-"+month+"-"+year)
        print("From date is entered: ["+date+"-"+month+"-"+year+"]")
    elif(calendar_type=="end"):
        browser.find_element_by_id("toDate_lm"+new_row_no).send_keys(date+"-"+month+"-"+year)
        print("To date is entered: ["+date+"-"+month+"-"+year+"]")
    else:
        print("Please Select right format for input date")
        
calender(START,"2019", "Apr", "15")
calender(END,"2019", "Apr", "15")    
# Go to bottom row - Click on Plus to add item
print("Selecting Exception-Type: ")
def exception_type(exception_type):
    exception_type_element = Select(browser.find_element_by_id("exceptionType_lm"+new_row_no))
    exception_type_element.select_by_visible_text(exception_type)
    print("Exception-Type: ["+exception_type+"] selected successfully")
exception_type("Daily-Exception")

print("Selecting Reason-Type: ")
def reason_type(reason_type):
    exception_type_element = Select(browser.find_element_by_id("reasonCode_lm"+new_row_no))
    exception_type_element.select_by_visible_text(reason_type)
    print("Reason-Type: ["+reason_type+"] selected successfully")
    
reason_type("Earned Leave")

browser.find_element_by_id("save").submit()



# Check holiday is added 
time.sleep(10)

browser.close()


"""  

wait = WebDriverWait( browser, 5 )
  
try:
page_loaded = wait.until_not(
lambda browser: browser.current_url == login_page
)
except TimeoutException:
self.fail( "Loading timeout expired" )
  
self.assertEqual(
browser.current_url,
correct_page,
msg = "Successful Login"
)


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('url')
timeout = 5
try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print "Timed out waiting for page to load"
    """
