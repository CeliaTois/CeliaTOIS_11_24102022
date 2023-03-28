from selenium import webdriver
from selenium.webdriver.common.by import By


def test_full_user_login_logout():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/")
    driver.implicitly_wait(20)

    email_input = driver.find_element(By.TAG_NAME, "input")
    email_input.clear()
    email_input.send_keys("john@simplylift.co")
    login_button = driver.find_element(By.TAG_NAME, "button")
    login_button.click()

    driver.implicitly_wait(20)

    booking_link = driver.find_element(By.TAG_NAME, "ul").find_element(By.TAG_NAME, "a")
    booking_link.click()

    driver.implicitly_wait(20)

    nb_places_input = driver.find_element(By.NAME, "places")
    nb_places_input.clear()
    nb_places_input.send_keys(2)
    book_button = driver.find_element(By.TAG_NAME, "button")
    book_button.click()

    driver.implicitly_wait(20)

    links = driver.find_elements(By.TAG_NAME, "a")
    logout_link = [link for link in links if link.text == "Logout"][0]
    logout_link.click()
