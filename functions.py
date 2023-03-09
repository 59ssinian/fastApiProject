from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def login_intomark():

    #로그인 파트

    driver = webdriver.Chrome()
    driver.get("https://www.intomark.com/service/mai/main.wips")

    input_field = driver.find_element("id", "username")
    input_field.send_keys("omipc2")

    input_field = driver.find_element("id", "password")
    input_field.send_keys("omipc2.com")

    link = driver.find_element("link text", "로그인")
    link.click()

    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("pop up is clear")
    except Exception:
        print("no pop up")


    print("login")

    return driver

def search_word_similar(driver, mark1, class1, group1):

    link = driver.find_element("link text", "국가별검색")
    link.click()

    #유사검색
    link = driver.find_element("xpath", "//li[2]/button")
    link.click()

    input_field = driver.find_element("id", "tmarkNmArea")
    input_field.send_keys(mark1)

    input_field = driver.find_element("id", "smlrCdArea")
    input_field.send_keys(group1)

    link = driver.find_element("xpath", "//div[2]/a/span")
    link.click()

    wait = WebDriverWait(driver, 10)
    xpath = "/html/body/div[1]/div[2]/div[2]/div[7]/div[1]/article[1]/div"
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    return driver


def search_word_identical(driver, mark1, class1, group1):
        link = driver.find_element("link text", "국가별검색")
        link.click()

        # 일반검색
        link = driver.find_element("xpath", "//li/button")
        link.click()

        input_field = driver.find_element("id", "tmarkNmArea")
        input_field.send_keys(mark1)

        input_field = driver.find_element("id", "smlrCdArea")
        input_field.send_keys(group1)

        link = driver.find_element("xpath", "//div[2]/a/span")
        link.click()

        wait = WebDriverWait(driver, 10)
        xpath = "/html/body/div[1]/div[2]/div[2]/div[7]/div[1]/article[1]/div"
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

        return driver

def if_noresults(driver):

    # fine element by id
    element = driver.find_element("id", "devTableNoResult")

    is_visible = element.is_displayed()

    return is_visible




def results_count(driver):

    wait = WebDriverWait(driver, 10)
    xpath = "//article/div/div/div/span"
    wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath),"총"))

    # fine element by id
    element = driver.find_element("xpath", xpath)
    counts_text = element.text
    numbers = int(counts_text[2:-2].replace(",",""))

    return numbers

def logout_intomark(driver):

    link = driver.find_element("xpath", "//span[contains(.,'로그아웃')]")
    link.click()

    print("logoout")
    return driver


def get_trademarks(driver):

    trademarks = set()

    status_element = driver.find_element("xpath", "//span/span/span")
    app_number_element = driver.find_element("xpath", "//label/span/a")
    url_element = driver.find_element("xpath", "//td/img")

    if status_element:
        status = status_element.text
        app_number = app_number_element.text
        url = url_element.get_attribute('src')

        trademarks.add((status, app_number, url))
    else:
        return trademarks

    for i in range(2,10):
        status_xpath = "//li["+str(i)+"]/div/div[3]/span/span/span"
        app_number_xpath = "//li["+str(i)+"]/div/div[3]/label/span/a"
        url_xpath = "//li["+str(i)+"]/div/div/ul/li/table/tbody/tr/td/img"

        status_element = driver.find_element("xpath", status_xpath)

        if status_element:
            app_number_element = driver.find_element("xpath", app_number_xpath)
            url_element = driver.find_element("xpath", url_xpath)

            status = status_element.text
            app_number = app_number_element.text
            url=url_element.get_attribute('src')

            trademarks.add((status, app_number, url))
        else:
            break

    print(trademarks)

    return trademarks

