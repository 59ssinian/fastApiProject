from selenium import webdriver

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
    except:
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

        return driver

def if_noresults(driver):

    # fine element by id
    element = driver.find_element("id", "devTableNoResult")

    is_visible = element.is_displayed()

    return is_visible

def logout_intomark(driver):

    link = driver.find_element("xpath", "//span[contains(.,'로그아웃')]")
    link.click()

    print("logoout")
    return driver
