import time
from selenium.webdriver.common.keys import Keys

def find_fields_and_button(driver):
    forms = driver.find_elements_by_tag_name('form')
    # print('count form: ' + str(len(forms)))
    for form in forms:
        inputs = form.find_elements_by_tag_name('input')
        inputs_and_button = []
        for i in inputs:
            is_displayed = i.is_displayed()
            if is_displayed:
                inputs_and_button.append(i)

        if len(inputs_and_button) == 2:
            return inputs_and_button
    raise Exception('The elements was not found')


def login(inputs_and_pass, login_word, password):
    inputs_and_pass[0].send_keys(login_word)
    inputs_and_pass[1].send_keys(password)
    inputs_and_pass[1].send_keys(Keys.RETURN)


def special_action(driver, query_num):
    if query_num == 1:
        button_label = input('Enter a label>>: ')
        buttons = driver.find_elements_by_xpath('//*[contains(text(),"' + button_label + '")]')
        for button in buttons:
            if button.text.upper() == button_label.upper() and button.is_displayed():
                button.click()
                time.sleep(3)


def find_fields(driver):
    forms = driver.find_elements_by_tag_name('form')
    # print('count form: ' + str(len(forms)))
    for form in forms:
        inputs = form.find_elements_by_tag_name('input')
        ins = []
        for i in inputs:
            if i.is_displayed():
                ins.append(i)

            if len(ins) == 2:
                return ins
    print('Inputs not found')
