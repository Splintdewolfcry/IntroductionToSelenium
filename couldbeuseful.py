# wait until we see a skill
login_button = wait.until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'I ALREADY HAVE AN ACCOUNT')]"))
)

# click the login button (it says "I ALREADY HAVE AN ACCOUNT")
login_button.click()