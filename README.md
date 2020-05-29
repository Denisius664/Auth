# Auth
Can get authorized cookies that are needed for requests to the site on your behalf

# 🌐 How to run 🌐 #
```
Follow to project folder
pip3 install -r requirements.txt
python3 Main.py
```

# For Ubuntu run in terminal
```
sudo apt install firefox-geckodriver
```

# On other systems and Windows 10 download file from 'https://github.com/mozilla/geckodriver/releases' and do that under
```
change the line 'driver = webdriver.Firefox()' to 'driver = webdriver.Firefox(executable_path="path for geckodriver")'
```
# If you have Google Chrome on other systems download file from 'https://chromedriver.chromium.org/downloads' for your version:
```
change the line 'driver = webdriver.Firefox()' to 'driver = webdriver.Chrome(executable_path="path for chromedriver")'
```
