
from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap ={
    "platformName": "Android",
    "deviceName": "3695d818",
    "appPackage": "com.android.messaging",
    "appActivity": "com.android.messaging.ui.conversationlist.ConversationListActivity"

}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

driver.find_element(By.XPATH,"//android.widget.TextView[@text='Vk']").click()
sms=driver.find_element(By.ID,"com.android.messaging:id/message_text").text
print(sms)
# def textbox

Str = sms
N = 8
print(Str)
length = len(Str)
OTP = Str[length - N:]
print(OTP)

















































































# import os
# from subprocess import PIPE, run
#
#
# def out(command):
#     result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
#     return result.stdout
#
#
# get_current_device = out("adb devices").split("attached")[1].split("device")[0].strip()
# cur_dir = os.getcwd()
#
#
# desired_cap_b2b = {
#     "appium:deviceName": "Android Emulator",
#     "platformName": "Android",
#     "appium:app": cur_dir + "/APK/GrabB2B.apk",
#     "appium:automationName": "UIAutomator2",
#     "appium:platformVersion": "11",
#     "appium:appActivity": "com.grab.grabrider.Activity.MainActivity",
#     "appium:appPackage": "com.grab.grabrider",
#     "appium:udid": get_current_device,
#     "appium:uiautomator2ServerInstallTimeout": "25000"
# }
# #
# # desired_cap={
# #     "deviceName": "3695d818",
# #     "platformName": "Android"
# # }
# # driver.open_notifications()
# #
# # try:
# #     notification = driver.find_element_by_id("com.android.systemui:id/clear_notifications")
# #
# #     if notification.is_displayed():
# #         notification.click()
# #         return EnterPhoneNumber(driver)
# #
# # except Exception as e:
# #     print(e)
# #     driver.press_keycode(4)
# #



# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)


def quit_app():
    driver.reset()


def open_notifications():
    driver.open_notifications()


def clear_notifications():
    driver.clear_notifications()


def string_contains(first, second):
    flag = False

    if str(second) in str(first):
        flag = True

    return bool(flag)


def find(element, locator):
    if locator == 'ID':
        webelement = driver.find_element(By.ID, element)
    elif locator == 'XPATH':
        webelement = driver.find_element(By.XPATH, element)

    return webelement


def wait_and_find(element, locator):
    try:
        if locator == 'ID':
            waitElement = WebDriverWait(driver, 30).until(
                EC.element_to_be_selected((By.ID, element)))
        elif locator == 'XPATH':
            waitElement = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, element)))
    except:
        print("No element present for the locator " + element)

    return waitElement


def wait_and_find_elements_list(element, locator):
    if locator == 'ID':
        waitElements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.ID, element)))
    elif locator == 'XPATH':
        waitElements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, element)))
    return waitElements


def is_element_displayed(element, locator):
    flag = False
    try:
        find(element, locator)
        flag = True
    except:
        time.sleep(2)

    return flag