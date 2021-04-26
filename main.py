import os
import time
import random
import requests
from shutil import move
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import ibm_watson
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#############################################################################################################################
#This is just a testing script, does nothing on its own. To implement this inside your own project, follow further comments.#
#############################################################################################################################
chrome_options = Options()
chrome_options.add_argument("--mute-audio")#nobody wants to hear creepy sounds when botting
driver = webdriver.Chrome(options=chrome_options)

#put your private stuff here, you can also import it from a txt file if youre a big brain
apikeywatson = '' #pretty obvious lol
urlwatson = '' #service url

authibm = IAMAuthenticator(apikeywatson)#just config stuff
stt = SpeechToTextV1(authenticator=authibm)
stt.set_service_url(urlwatson)

driver.get('https://client-demo.arkoselabs.com/github') #this is just a testing site
time.sleep(4)#                                                                             #when selecting the iframe, first you need to select a iframe named something like "whatever-api.arkoselabs.com/v2/" and then the "fc/gc/" one
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src^='https://client-api.arkoselabs.com/fc/gc/']")))#if you want to implement this inside your own project, copy everything from this line
print('this project uses ArkoseBuster by xuehue on GitHub') #dont remove this unless youre a big poo-poo
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='fc_meta_audio_btn']"))).click()
time.sleep(1.5)
def captcha():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "audio_play"))).click()
    time.sleep(1)
    
    audio_src = driver.find_element_by_id('fc_audio_el').get_attribute('src')#saves the audio file into captcha.wav, which is then read by watson
    content = requests.get(audio_src).content
    open('captcha.wav', 'wb').write(content)
    
    with open ('captcha.wav', 'rb') as cap:
        res = stt.recognize(audio=cap, content_type='audio/wav', model='en-US_NarrowbandModel', continuous=True).get_result() #this does something
        captcharesult = res['results'][0]['alternatives'][0]['transcript']
        confidence = res['results'][0]['alternatives'][0]['confidence']
        if float(confidence) < 1.0:#just a safety check so it doesnt bug out when it gets 100%, it almost never gets 100% confidence, but happended once to me
            confidencesplit = str(confidence).split('0.')
            confidenceprint = confidencesplit[1]
        else:
            confidenceprint = str(100)
        print('Captcha broken with ' + confidenceprint + '% confidence')#this defines a string that is then sent
        captcharesult = captcharesult.replace(' ', '')
        captcharesult = captcharesult.replace('one', '1')
        captcharesult = captcharesult.replace('two', '2')
        captcharesult = captcharesult.replace('three', '3')
        captcharesult = captcharesult.replace('four', '4')
        captcharesult = captcharesult.replace('five', '5')
        captcharesult = captcharesult.replace('six', '6')
        captcharesult = captcharesult.replace('seven', '7')
        captcharesult = captcharesult.replace('eight', '8')
        captcharesult = captcharesult.replace('nine', '9')
        captcharesult = captcharesult.replace('zero', '0')
        captcharesult = captcharesult.replace('%HESITATION', '')#i have no idea what hesitation is but i stumbled upon it once
        print('Captcha broken! The result is ' + captcharesult)

    driver.find_element_by_class_name('response_field.audio_response').send_keys(captcharesult)
    time.sleep(0.5)#adjust the timings as you wish, many sites will block audio captcha when they see bot-like behavior even if you beat it, it gets reall tricky
    driver.find_element_by_id('audio_submit').click()
    time.sleep(0.5)
    
    os.remove('captcha.wav')#and end here if you are implementing it inside your own project. you also need to set the variables to
    time.sleep(4)

captcha()

try:#this is a check if it failed
    driver.find_element_by_id('fail-button').click()
    time.sleep(3)
    captcha()
    print('there is some issue with the captcha, trying again')
except NoSuchElementException:
    pass

print('get fucked arkose labs')
