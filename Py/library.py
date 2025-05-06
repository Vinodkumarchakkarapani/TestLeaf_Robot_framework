import time
import os
import webcolors
# from appium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
# from appium import webdriver
import properties as properties

# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_arguments('--incognito')
# web_driver=webdriver.chrome(chrome_options=chrome_options)

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# web_driver = webdriver.Chrome(options=options)

# serv = Service("C:/Users/vinow/PycharmProjects/Sharepoint/Sharepoint/Drivers/chromedriver.exe")

# web_driver = webdriver.Chrome(executable_path='C:/Users/vinow/PycharmProjects/Sharepoint/Sharepoint/Drivers/chromedriver.exe')
# serv = Service("C:/Users/vinod/PycharmProjects/CSC/Drivers/chromedriver.exe")

# web_driver = webdriver.Chrome(service=serv)

cur_dir = os.getcwd()

web_driver = webdriver.Chrome()




def open_browser(url):
    web_driver.get(url)
    web_driver.maximize_window()


# def open_browser(url):

# webdriver.Chrome()
def page_refresh():
    web_driver.refresh()



def wait_and_find(element, locator):
    try:
        wait = WebDriverWait(web_driver, 120)
        if locator == 'ID':
            return wait.until(EC.presence_of_element_located((By.ID, element)))
        elif locator == 'XPATH':

            return wait.until(EC.presence_of_element_located((By.XPATH, element)))
        elif locator == 'CSS':
            return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
        else:
            print(f"Unsupported locator type: {locator}")
    except Exception as e:
        print(f"Error finding element using {locator}={element}: {e}")
    return None

def wait_and_find_elements_list(element, locator):
    if locator == 'ID':
        waitElements = WebDriverWait(web_driver, 30).until(
            EC.presence_of_all_elements_located((By.ID, element)))
    elif locator == 'XPATH':
        waitElements = WebDriverWait(web_driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, element)))
    elif locator =='TAG_NAME':
        waitElements=WebDriverWait(web_driver,30).until(EC.presence_of_element_located((By.TAG_NAME,element)))
    return waitElements


def string_equals(string1, string2):
    return string1 == string2


def is_displayed(element):
    return web_driver.find_element(By.XPATH, element).is_displayed()


def is_selectByallvisibletext(element, locator):
    try:
        if locator == 'ID':
            visiblealltext = WebDriverWait(web_driver, 30).until(
                EC.visibility_of_all_elements_located((By.ID, element)))
        elif locator == 'XPATH':
            visiblealltext = WebDriverWait(web_driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, element)))
        elif locator == 'CSS':
            visiblealltext = WebDriverWait(web_driver, 30).until(
                EC.visibility_of_element_located(By.CSS_SELECTOR, element))
    except:
        print("No element present for the locator " + element)

    return visiblealltext

def is_selectByvisibletext(element, locator):
    try:
        if locator == 'ID':
            visibletext = WebDriverWait(web_driver, 30).until(
                Select.select_by_visible_text((By.ID, element)))
        elif locator == 'XPATH':
            visibletext = WebDriverWait(web_driver, 30).until(
                Select.select_by_visible_text((By.XPATH, element)))
        elif locator == 'CSS':
            visibletext = WebDriverWait(web_driver, 30).until(Select.select_by_visible_text(By.CSS_SELECTOR, element))
    except:
        print("No element present for the locator " + element)

    return visibletext

def textbox_element():
    wait_and_find(properties.element_tile,'XPATH').click()
    wait_and_find(properties.textbox_tile,'XPATH').click()
def interact_type_your_name():
    title=wait_and_find(properties.type_your_name_title,'XPATH')
    print(title.text)

    Textbox_variable=wait_and_find(properties.type_your_name_textbox,'XPATH')
    matchtext=Textbox_variable.get_attribute("placeholder")
    if matchtext:"Babu Manickam"
    print("Text is matched")
    Textbox_variable.send_keys("Hi Vinod")

    disabled_textbox_field=wait_and_find(properties.disabled_textbox,'XPATH')
    if not disabled_textbox_field.is_enabled():
        print("Field is disabled")
    else:
        print("Field is enabled")

    clear_field=wait_and_find(properties.clear_textbox,'XPATH')
    clear_field.clear()
    clear_field.send_keys("Hi Vinod")

def retrieve_text():
    retrieve=wait_and_find(properties.retrieve_textbox,'XPATH')
    match_Text=retrieve.get_attribute("value")
    if match_Text:"My learning is superb so far."
    print("Given text is matched")

def error_message_text():
    error_msg=wait_and_find(properties.error_message,'XPATH')
    error_msg.send_keys(Keys.ENTER)
    error_alert=wait_and_find(properties.error_alert_text,'XPATH')
    print(error_alert.text)

# Alert page functions
def alert_simple_dialog():
    time.sleep(3)
    wait_and_find(properties.browser_tile,'XPATH').click()
    wait_and_find(properties.alert_tile,'XPATH').click()
    wait_and_find(properties.alert_simple_dialog_show,'XPATH').click()
    time.sleep(1)
    alert=web_driver.switch_to.alert
    alert_text=alert.text

    if alert_text == "I am simple alert.":
        print("Text is matched")
    else:
        print("Text does not match")
    alert.accept()


def alert_confirm_dialog():
    time.sleep(1)
    wait_and_find(properties.alert_confirm_dialog_show,'XPATH').click()
    alert=web_driver.switch_to.alert
    alert_text=alert.text
    if alert_text == "Did you call me?":
        print("Text is matched")
    else:
        print("Text does not match")

    alert.dismiss()

def sweet_alert_dialog():
    time.sleep(1)
    wait_and_find(properties.alert_sweetalert_dialog_show,'XPATH').click()
    alert=wait_and_find(properties.sweet_alert_content,'XPATH')
    alert_text=alert.text
    if alert_text == "You have clicked and open a dialog that can be inspectable.":
        print("Text is matched")
    else:
        print("Text does not match")

    wait_and_find(properties.sweet_alert_dismiss,'XPATH').click()
    wait_and_find(properties.alert_sweetalert_dialog_show, 'XPATH').click()
    wait_and_find(properties.sweet_alert_cross_icon,'XPATH').click()

def sweet_model_dialog():
    time.sleep(1)
    wait_and_find(properties.alert_sweetmodel_dialog_show, 'XPATH').click()
    header = wait_and_find(properties.sweet_model_header, 'XPATH')
    print(header.text)
    alert = wait_and_find(properties.sweet_model_content, 'XPATH')
    alert_text = alert.text
    if alert_text == "Unless you close this, you cannot interact with other element. But am inspectable !":
        print("Text is matched")
    else:
        print("Text does not match")

    time.sleep(1)
    wait_and_find(properties.sweet_model_cross_icon, 'XPATH').click()
    # alert.dismiss()
    # actions = ActionChains(web_driver)
    # actions.double_click(sweet_Cross).perform()

def alert_prompt_dialog():
    time.sleep(2)
    wait_and_find(properties.alert_promptdialog_show, 'XPATH').click()
    alert = web_driver.switch_to.alert
    alert_text = alert.text
    if alert_text == "Type your name and click OK":
        print("Text is matched")
        alert.send_keys("Vinod")
    else:
        print("Text does not match")
    alert.accept()
    user_entered_prompt=wait_and_find(properties.user_entered_prompt_alert_prompt,'XPATH').text
    if user_entered_prompt=='User entered name as: Vinod':
        print("Text is matched")



def sweet_alert_confirmation_dialog():
    time.sleep(2)
    wait_and_find(properties.sweet_alert_confirm_delete_button, 'XPATH').click()
    alert = wait_and_find(properties.sweet_alert_confirm_content, 'XPATH')
    alert_text = alert.text
    if alert_text == "Are you sure you want to proceed?":
        print("Text is matched")
    else:
        print("Text does not match")

    wait_and_find(properties.sweet_alert_confirm_yes, 'XPATH').click()
    wait_and_find(properties.sweet_alert_confirm_delete_button, 'XPATH').click()
    wait_and_find(properties.sweet_alert_confirm_no, 'XPATH').click()
    wait_and_find(properties.sweet_alert_confirm_delete_button, 'XPATH').click()
    wait_and_find(properties.sweet_alert_confirm_cross_icon, 'XPATH').click()




def min_and_max_dialog():
    time.sleep(2)
    wait_and_find(properties.alert_mini_maximize_show, 'XPATH').click()
    time.sleep(1)
    header = wait_and_find(properties.min_and_max_header, 'XPATH')
    if header.text == "Min and Max":
        print("Text is matched")
    else:
        print("Text does not match")
    content=wait_and_find(properties.min_and_max_content,'XPATH')
    if content.text=="I am Sweet Alert and can be maximized or minimized. By the way, am not a new window.":
        print("Text is matched")
    else:
        print("Text does not match")

    min=wait_and_find(properties.min_and_max_minimize_icon,'XPATH')
    min.click()
    time.sleep(2)
    min_expand=wait_and_find(properties.min_and_max_minimize_expand,'XPATH')
    min_expand.click()
    time.sleep(1)
    max=wait_and_find(properties.min_and_max_maximize_icon,'XPATH')
    max.click()
    time.sleep(1)
    max_expand=wait_and_find(properties.min_and_max_maximize_expand,'XPATH')
    max_expand.click()
    time.sleep(1)

    wait_and_find(properties.min_and_max_close_icon,'XPATH').click()

# Frame page

def page_frame():
    wait_and_find(properties.browser_tile,'XPATH').click()
    time.sleep(1)
    wait_and_find(properties.frame_tile,'XPATH').click()
    first_iframe = web_driver.find_element(By.XPATH, "(//iframe)[1]")
    web_driver.switch_to.frame(first_iframe)
    frame_text=wait_and_find(properties.frame_click_me_single_frame,'XPATH')
    frame_text.click()
    print(frame_text.text)

    web_driver.switch_to.default_content()
    time.sleep(1)
    second_iframe = web_driver.find_element(By.XPATH, "(//iframe)[2]")
    web_driver.switch_to.frame(second_iframe)
    second_frame_text=wait_and_find(properties.frame_click_me_single_frame,'XPATH')
    second_frame_text.click()
    print(second_frame_text.text)
    web_driver.switch_to.default_content()
    print("Number of frames:",len(web_driver.find_elements(By.TAG_NAME,"iframe")))
    # third_iframe = web_driverdriver.find_element(By.XPATH, "(//iframe)[3]")
    # web_driver.switch_to.frame(third_iframe)
    # wait_and_find(properties.frame_click_me_triple_frame,'XPATH').click()


#Windows Page

def page_single_window():
    wait_and_find(properties.browser_tile,'XPATH').click()
    wait_and_find(properties.window_tile,'XPATH').click()
    main_window=web_driver.current_window_handle
    current_window=wait_and_find(properties.single_window_button,'XPATH')
    current_window.click()
    print(web_driver.title)
    time.sleep(2)
    new_window=web_driver.window_handles
    for handle in new_window:
        if handle!=main_window:
            web_driver.switch_to.window(handle)
            print(web_driver.title)
            web_driver.close()
    web_driver.switch_to.window(main_window)
    print(web_driver.title)

def page_multiple_window():
    # main_window = web_driver.current_window_handle
    current_window = wait_and_find(properties.mulitple_window_button, 'XPATH')
    current_window.click()
    print(web_driver.title)
    time.sleep(2)
    all_tabs = web_driver.window_handles
    print("Number of tabs:", len(all_tabs))
    main_tab = web_driver.current_window_handle
    for handle in all_tabs:
        if handle != main_tab:
            web_driver.switch_to.window(handle)
            web_driver.close()

    # Return to main tab
    web_driver.switch_to.window(main_tab)
    print("Back to main tab:", web_driver.title)

def except_main_window():
    main_window = web_driver.current_window_handle
    current_window = wait_and_find(properties.close_windows_button, 'XPATH')
    current_window.click()
    print(web_driver.title)
    time.sleep(2)
    all_window = web_driver.window_handles
    print("Number of tabs:", len(all_window))

    for handle in all_window:
        if handle != main_window:
            web_driver.switch_to.window(handle)
            web_driver.close()
    web_driver.switch_to.window(main_window)
    print(web_driver.title)


def drag_and_drop():
    wait_and_find(properties.browser_tile,'XPATH').click()
    wait_and_find(properties.drag_tile,'XPATH').click()
    time.sleep(1)
    draggable=wait_and_find(properties.drag_and_drop,'XPATH')
    actions=ActionChains(web_driver)
    actions.drag_and_drop_by_offset(draggable,100,50).perform()

def drag_drop_target():
    source=wait_and_find(properties.drag_to_target,'XPATH')
    target=wait_and_find(properties.droppable_target,'XPATH')
    actions=ActionChains(web_driver)
    actions.drag_and_drop(source,target).perform()
    target_word=wait_and_find(properties.target_word,locator='XPATH').text
    if target_word=='Dropped!':
        print("Text is matched")



# Button page

def clickandconfirm_title():
    wait_and_find(properties.element_tile,'XPATH').click()
    wait_and_find(properties.button_title,'XPATH').click()
    wait_and_find(properties.click_and_confirm_title,'XPATH').click()
    confirm_title=web_driver.title
    print(confirm_title)
def confirm_button_disabled():
    wait_and_find(properties.element_tile, 'XPATH').click()
    wait_and_find(properties.button_title, 'XPATH').click()
    disabled_button=wait_and_find(properties.disabled_button,'XPATH')
    is_disabled=disabled_button.get_attribute("Disabled") is not None
    if is_disabled:
        print("Button is disabled")
    else:
        print("Button is enabled")

def button_position():
    submit_button=wait_and_find(properties.position_of_button,'XPATH')
    position=submit_button.location
    x=position['x']
    y=position['y']
    size=submit_button.size
    width=size['width']
    height=size['height']
    is_visible=submit_button.is_displayed()

    print(f"submit button position: X={x},Y={y}")
    print(f"submit button size: Width={width},Height={height}")
    print(f"Submit button visible?{is_visible}")
def find_h_w_button():
    submit_button=wait_and_find(properties.find_height_width_of_button,'XPATH')
    size=submit_button.size
    height=size['height']
    width=size['width']
    print(f"Submit button size: Width={width},Height={height}")
def button_hover_color_change():
    hover_element=wait_and_find(properties.color_button_hover,'XPATH')
    color_before=hover_element.value_of_css_property('background-color')
    color_name_before=rgb_to_color_name(color_before)
    ActionChains(web_driver).move_to_element(hover_element).perform()
    time.sleep(1)
    color_after=hover_element.value_of_css_property('background-color')
    color_name_after=rgb_to_color_name(color_after)
    print(f"Before color: {color_name_before}")
    print(f"After color:{color_name_after}")
    if color_before!=color_after:
        print("Color changes on hover",color_after)
    else:
        print("Color doesn't change")

def rgb_to_color_name(rgb_string):
    # Remove 'rgba' or 'rgb' and split by commas
    rgb_string = rgb_string.strip().lower()
    if rgb_string.startswith('rgba'):
        rgb_string = rgb_string[5:-1]  # Remove "rgba(" and ")"
    elif rgb_string.startswith('rgb'):
        rgb_string = rgb_string[4:-1]  # Remove "rgb(" and ")"

    rgb_values = tuple(map(int, rgb_string.split(",")))

    try:
        return webcolors.rgb_to_name(rgb_values[:3])  # Use only RGB part for matching
    except ValueError:
        # If no exact match, return the closest name
        closest_name = min(
            webcolors.CSS3_NAMES_TO_HEX,
            key=lambda name: sum(
                (a - b) ** 2 for a, b in zip(webcolors.hex_to_rgb(webcolors.CSS3_NAMES_TO_HEX[name]), rgb_values[:3])
            )
        )
        return closest_name

def count_round_button():
    buttons=wait_and_find_elements_list(properties.total_buttons,'XPATH')
    print(f"Number of rounded button:{len(buttons)}")


#dropdown page

def select_tool_dropdown():
    wait_and_find(properties.element_tile,'XPATH').click()
    is_selectByvisibletext(properties.select_tools_dropdown_field,'XPATH')

def select_by_label(label):
    """Select an option from the dropdown by visible text (label)."""
    wait_and_find(properties.element_tile, 'XPATH').click()
    wait_and_find(properties.dropdown_tile, 'XPATH').click()
    dropdown_element = wait_and_find(properties.select_tools_dropdown_field,'XPATH')
    select = Select(dropdown_element)
    select.select_by_visible_text(label)

    print(f"Selected '{label}' by visible text.")

def country_dropdown(label):
    # wait_and_find(properties.dropdown_tile,'XPATH').click()
    time.sleep(2)
    wait_and_find(properties.select_country_dropdown_field,'XPATH').click()
    time.sleep(2)
    country_dropdown_xpath=f"//li[@data-label='{label}']"

    option = WebDriverWait(web_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, country_dropdown_xpath))
    )
    option.click()
    print(f"Selected '{label}' from custom dropdown.")


def course_dropdown(course):
    time.sleep(2)
    course_element=wait_and_find(properties.choose_the_course_dropdown_field,'XPATH')
    course_element.click()
    course_element.send_keys(course)
    course_element.send_keys(Keys.ENTER)
    print(f"Selected '{course}' from custom dropdown.")
