# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def note(name):
    return "Hey " + name + "," + """
    I am currently looking to expand my network as I build out my software consultancy. I came across your profile while looking for project managers just outside of my network.
    """

def type_message(elem, name):
    elem.send_keys("Hey " + name + ",")
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.ENTER)
    elem.send_keys("Often, there is a great deal of waste in the IT consulting and project development industry due to flaky, unpredictable implementations and misalignment of business goals.")
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.ENTER)
    elem.send_keys("I have experienced this firsthand with my parents’ Amazon business where a project went way over budget from steep hourly pay rates, and they received a solution that missed the mark on the original problem. I have felt this pain enough to know that choosing the right Software & IT consultant can be challenging.")
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.ENTER)
    elem.send_keys("Projects like these leave people like yourself with never-ending maintenance costs, complexity in your tech stack, and an overall waste of time and resources. For example, for my parents’ business, they spent over $5000 in additional maintenance fees for an original budget of $950. This is due to developer error and shaky implementations, favoring the developer's business goals of recurring revenue, instead of the customer’s goals. Once I took over development and used a better-reasoned toolset, I reduced their maintenance to $0.")
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.ENTER)
    elem.send_keys("That's why my consultancy, SolveX, completely takes the blame and financial burden for all maintenance issues. We do this to ensure that our goals actually align with yours: creating high-quality and productive software that is so unlikely to be flaky or buggy that we can guarantee covering maintenance costs. We are not married to any tool; every toolset is wholly dependent on the unique business problem and customer-defined constraints, allowing us to put your needs first and deliver a solution that fits what you're looking for. You can check out my previous projects here:https://galenthehooman.ninja/ - feel free to ask any questions about our process; we encourage it!  ")
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.ENTER)
    elem.send_keys("If this sounds like something that would be a good fit for your business, let's book a 30-minute consultation call:https://calendly.com/galen-sprout/30min. In this call, we will discuss your business objectives, processes, current challenges, and operational constraints so that I may understand whether or not we are a fit to help your unique business case.")
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.ENTER)
    elem.send_keys("Cheers,")
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.ENTER)
    elem.send_keys("Galen")

driver = webdriver.Firefox()

driver.maximize_window()
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

username = driver.find_element("xpath", "//input[@id='username']")
password = driver.find_element("xpath", "//input[@id='password']")

username.send_keys("galen@aceinterviewprep.io")
password.send_keys("Warhawks58")

driver.find_element("xpath", "//button[@type='submit']").click()

######################################################################################################################################################################################################################


# lastMessaged = open('lastMessaged.txt', 'r').read().strip()

# driver.find_element("xpath", "//a[@href='https://www.linkedin.com/mynetwork/?']").click()

# sleep(3)

# driver.find_element("xpath", "//a[@href='/mynetwork/invite-connect/connections/']").click()

# sleep(5)

# # Determine how many messages to send 
# count = 0
# for elem in driver.find_elements("xpath", "//span[@class='mn-connection-card__name t-16 t-black t-bold']"):
#     if lastMessaged.lower() in elem.get_attribute('innerText').lower():
#         break
#     else:
#         count += 1

# # "//h2[descendant::span[contains(text(),'See results about')]]")[0].innerText
        
# # Send the messages
# for i in range(count):

#     driver.find_elements("xpath", "//div[@class='mn-connection-card__action-container']//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")[i].click()
#     sleep(5)
#     nameElems = driver.find_elements("xpath","//span[@class='mn-connection-card__name t-16 t-black t-bold']")
#     firstName = nameElems[i].get_attribute('innerText').split()[0]
#     print(firstName)
#     # You must use ENTER key on linked in messages

#     if "Neharika" not in firstName:
    
#     # Type the message, expand in case the button does not render, then click button
#         type_message(driver.find_element("xpath", "//div[@aria-label='Write a message…']"), firstName)
#         driver.find_element("xpath", "//button[@aria-expanded='false']").click()
#         driver.find_element("xpath", "//button[@class='msg-form__send-button artdeco-button artdeco-button--1']").click()
#         sleep(10)
#         #close the chat
#         driver.find_element("xpath", "//button[@class='msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view']").click()
#         sleep(2)

    
# lastMessaged = driver.find_elements("xpath","//span[@class='mn-connection-card__name t-16 t-black t-bold']")[0].get_attribute('innerText').strip()


    
# #write lastMessaged name
# with open('lastMessaged.txt', 'w') as f:
#     f.write(lastMessaged)
#     f.close()


######################################################################################################################################################################################################################


### Harvest more connections

# Loop until profile pages run (and thus connects sent) is equal to 80
 # so no "Pending" cases 

 


# I should send a note too


#TODO(galen): Testing system of different messages


# this is defective cuz I cant just access all 10, i must continuously scroll

# this also fell down cuz I expect there to be zero pending

# I could fix this the easiest by expanding the XPATH selector to be either button

page_number = 45
driver.get('https://www.linkedin.com/search/results/people/?keywords=software%20project%20manager&origin=SWITCH_SEARCH_VERTICAL&page=' + str(page_number) + '&sid=_-')
sleep(5)
connects = 80
while connects > 0:
    #take i where i++ after goBack
    
    for i in range (0,10): # 10 results per page
        # current or past occupation. Our target is Software PM
        # NOTE: we get the elems every time cuz they can refresh in selenium - ugggggh
        
            
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(("xpath", "//div[@class='entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light']//p"))
            )
        except: # TimeoutException
            driver.back()
            driver.forward()
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(("xpath", "//div[@class='entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light']//p"))
            )

        currentOrPastEls = driver.find_elements("xpath", "//div[@class='entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light']//p")
        currentOrPastElsText = [ e.get_attribute('innerText') for e in currentOrPastEls ]
        try:
            elTexto = currentOrPastElsText[i].lower()
        except IndexError:
            sleep(10)
            elTexto = driver.find_elements("xpath", "//div[@class='entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light']//p")[i].get_attribute('innerText').lower()
        
        if 'current:' in elTexto and 'project manager' in elTexto and 'at' in elTexto:
            #then get the same element idx for profile and click it
            buttons = driver.find_elements("xpath", "//div[@class='entity-result__actions entity-result__divider']//button")
            print(len(buttons), i)

            try:
                connectBUTTon = buttons[i]
            except IndexError:
                print('trying again for connect buttons...ugh')
                sleep(10)
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(("xpath", "//div[@class='entity-result__actions entity-result__divider']//button"))
                )
                connectBUTTon = driver.find_elements("xpath", "//div[@class='entity-result__actions entity-result__divider']//button")[i]
            connectHow = connectBUTTon.get_attribute('innerText').lower()
            if "pending" in connectHow or "message" in connectHow or "follow" in connectHow:
                pass
            else:
                print(connectBUTTon)
                connectBUTTon.click()

                maybeModal = driver.find_elements("xpath", "//button[@class='artdeco-pill artdeco-pill--slate artdeco-pill--3 artdeco-pill--choice ember-view mt2']")
                
                if len(maybeModal) != 0:
                    modalButton = maybeModal[4] # is the 5th pill option
                    modalButton.click()
                    driver.find_element("xpath", "//div[@class='artdeco-modal__actionbar ember-view display-flex justify-flex-end']//button[@aria-label='Connect']").click()
                    driver.find_element("xpath", "//div[@class='artdeco-modal__actionbar ember-view display-flex justify-flex-end']//button[@aria-label='Connect']").click()
                    driver.find_element("xpath", "//button[@aria-label='Send now']").click()
                #driver.find_element("xpath", "//button[@aria-label='Add a note']").click()
                #driver.find_element("xpath", "//textarea[@id='custom-message']").send_keys(note)
                else:
                    # for now I assume that if an unknown dialog pops up, its some verification
                    # by the connectee and so we say fuck it
                    emailConnectRequest = driver.find_elements("xpath", "//button[@aria-label='Dismiss']")
                    if len(emailConnectRequest) != 0:
                        emailConnectRequest[0].click()
                    else:
                        driver.find_element("xpath", "//button[@aria-label='Send now']").click()
                x = driver.find_elements("xpath","//span[@class='entity-result__title-line entity-result__title-line--2-lines']//a")[i].get_attribute('innerText')
                connects -= 1
                print("connects", connects)
                print("with", x.split()[:2])

        # scroll after the 5th result on the page and the 10th to bring up the next 5 and then
        # the click next button
        if (i + 1) % 5 == 0: driver.find_element("xpath","//body").send_keys(Keys.PAGE_DOWN)
    #driver.get('https://www.linkedin.com/search/results/people/?keywords=software%20project%20manager&origin=SWITCH_SEARCH_VERTICAL&sid=_-')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)
    # go to next page 
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(("xpath", "//button[@aria-label='Next']"))
    ).click()
    sleep(5)

print('done') 
    
# subject = ""



# find their name, click
# find their job title and check if 'Project Manager' AND 'at' in Current job note (may also say past)

# IF SO:
#     click message
#     paste message
#     pause after each sentence - if needed
    

# - lets alternate between 3 messages + subjects to test what works best


# - neeeed already messaged





# -- 1 : go check recent connections and send the message
# -- 2 : go add 80 people a day

