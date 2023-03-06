import selenium

def login_intomark( id:str, pw:str)

    #로그인 파트

    input_field = driver.find_element("id", "username")
    input_field.send_keys("omipc2")

    input_field = driver.find_element("id", "password")
    input_field.send_keys("omipc2.com")

    link = driver.find_element("link text", "로그인")
    link.click()

    link = driver.find_element("link text", "국가별검색")
    link.click()

    link = driver.find_element("xpath", "//li[2]/button")
    link.click()

    input_field = driver.find_element("id", "tmarkNmArea")
    input_field.send_keys("test")

    input_field = driver.find_element("id", "smlrCdArea")
    input_field.send_keys("S1200")

    link = driver.find_element("id", "dpmaxs_c")
    link.click()

    link = driver.find_element("css", ".ico_search")
    link.click()