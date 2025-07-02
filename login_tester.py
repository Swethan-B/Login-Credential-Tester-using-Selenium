from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Smart result checker (no expected message required)
def check_login_result(driver):
    page_text = driver.page_source.lower()

    success_keywords = ["logout"]
    failure_keywords = ["invalid", "incorrect", "try again", "wrong", "error","login","sign up"]

    if any(word in page_text for word in success_keywords):
        return "✅ Login Successful"
    elif any(word in page_text for word in failure_keywords):
        return "❌ Login Failed: Invalid Credentials"
    else:
        return "⚠️ Login may be successful, but no known indicators were found"

# Try to logout after success
def attempt_logout(driver):
    try:
        logout_links = driver.find_elements(By.XPATH, "//a[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'logout')]")
        if not logout_links:
            logout_links = driver.find_elements(By.XPATH, "//button[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'logout')]")
        if logout_links:
            logout_links[0].click()
            time.sleep(2)
            print("↪️ Logged out after login.")
        else:
            print("⚠️ Logout link/button not found.")
    except Exception as e:
        print(f"⚠️ Error during logout: {e}")

# ---------- MAIN SCRIPT ----------
url = input("🔗 Enter the full login page URL: ")
num_sets = int(input("🧪 How many credential sets to test? "))

credentials = []
for i in range(num_sets):
    print(f"\n🧾 Credential Set {i+1}")
    username = input("👤 Username: ")
    password = input("🔒 Password: ")
    credentials.append((username, password))

driver = webdriver.Chrome()
print("\n================= 🔍 Running Tests =================")

for idx, (username, password) in enumerate(credentials):
    print(f"\n🧪 Test {idx+1}: {username} / {password}")
    driver.get(url)
    time.sleep(2)

    try:
        inputs = driver.find_elements(By.TAG_NAME, "input")
        user_field = None
        pass_field = None

        for input_field in inputs:
            input_type = input_field.get_attribute("type")
            if input_type in ["text", "email"] and not user_field:
                user_field = input_field
            elif input_type == "password" and not pass_field:
                pass_field = input_field

        if not user_field or not pass_field:
            print("❌ Could not find username/password fields.")
            continue

        user_field.clear()
        user_field.send_keys(username)
        pass_field.clear()
        pass_field.send_keys(password)

        # Try various submit button options
        try:
            submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        except:
            try:
                submit_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
            except:
                try:
                    submit_btn = driver.find_element(By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'login')]")
                except:
                    print("❌ Submit button not found.")
                    continue

        submit_btn.click()
        time.sleep(3)

        result = check_login_result(driver)
        print(result)

        if "✅" in result:
            attempt_logout(driver)

    except Exception as e:
        print(f"⚠️ Error during test {idx+1}: {e}")

driver.quit()
print("\n✅ All tests completed.")
