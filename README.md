🔐Login Credential Tester using Selenium (Python)
===============================================

This script allows you to test multiple sets of login credentials on any website with a login form using Selenium. It intelligently detects whether login was successful or not and automatically logs out before attempting the next login.

-------------------------------------------------
✅ Features:
-------------------------------------------------
- Accepts dynamic login page URLs from user input
- Accepts multiple username/password sets to test
- Automatically detects login success or failure
- Logs out automatically if login is successful

-------------------------------------------------
 🧰 Requirements:
-------------------------------------------------
- Python 3.7 or higher
- Google Chrome browser installed
- ChromeDriver that matches your Chrome version
- Python modules:
    - selenium

Install Selenium using pip:
> pip install selenium

-------------------------------------------------
🚀 How to Use:
-------------------------------------------------
1. Run the script:
   > python login_tester.py

2. Provide the required inputs:
   - Full login page URL
   - Number of credential sets
   - Each username and password

3. The script will:
   - Open the page
   - Input credentials
   - Attempt login
   - Display login result
   - Logout if login is successful
   - Repeat for all credentials

-------------------------------------------------
🧪Sample Run:
-------------------------------------------------
🔗 Enter the full login page URL: https://testphp.vulnweb.com/login.php     
🧪 How many credential sets to test? 2

🧾 Credential Set 1
👤 Username: test
🔒 Password: test

🧾 Credential Set 2
👤 Username: wrong
🔒 Password: wrong

================= 🔍 Running Tests =================

🧪 Test 1: test / test    
✅ Login Successful      
↪️ Logged out after login.        

🧪 Test 2: wrong / wrong       
❌ Login Failed: Invalid Credentials      

✅ All tests completed.

-------------------------------------------------
File List:
-------------------------------------------------
- login_tester.py        : Main Python script
- requirements.txt       : Python module list (just contains 'selenium')
- README.txt             : This documentation file

-------------------------------------------------
Author:
-------------------------------------------------
Swethan B  
Security & Automation Enthusiast 🛡️⚙️

License: MIT  
Feel free to use, modify, and distribute with attribution.
