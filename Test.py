from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:
    # Step 1: Open the hotel booking application
    driver.get("https://example-hotel-booking.com") 

    # Step 2: Search for hotels in “New York” for dates April 10 - April 15
    wait.until(EC.presence_of_element_located((By.ID, "location"))).send_keys("New York")
    driver.find_element(By.ID, "checkin").send_keys("04/10/2025")
    driver.find_element(By.ID, "checkout").send_keys("04/15/2025")
    driver.find_element(By.ID, "search-button").click()

    # Step 3: Select the first hotel from the search results
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".hotel-card")))
    first_hotel = driver.find_elements(By.CSS_SELECTOR, ".hotel-card")[0]
    first_hotel.click()

    # Step 4: Apply the coupon code "SUMMER25"
    wait.until(EC.presence_of_element_located((By.ID, "coupon-code"))).send_keys("SUMMER25")
    driver.find_element(By.ID, "apply-coupon").click()

    # Step 5: Verify that the discount is applied correctly
    discount_msg = wait.until(EC.presence_of_element_located((By.ID, "discount-applied-msg")))
    assert "Discount Applied" in discount_msg.text

    # Optionally, validate price change
    original_price = driver.find_element(By.ID, "original-price").text
    final_price = driver.find_element(By.ID, "final-price").text
    print(f"Original Price: {original_price}, Final Price: {final_price}")

    # Step 6: Proceed to checkout (but do not complete payment)
    driver.find_element(By.ID, "proceed-checkout").click()
    wait.until(EC.presence_of_element_located((By.ID, "payment-page")))
    print("Reached payment page successfully.")

finally:
    time.sleep(3)
    driver.quit()
