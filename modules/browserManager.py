from selenium import webdriver
import json

def getBrowserInstance():
    chrome_options = webdriver.ChromeOptions()
    settings = {"recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}], "selectedDestinationId": "Save as PDF", "version": 2}
    prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--kiosk-printing')

    browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options)
    return browser