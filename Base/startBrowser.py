from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Library import ConfigReader

#Função iniciar navegador
def start_browser():
    #Adicionar opção de personalização ao navegador
    options = Options()
    options.add_argument("--start-maximized")
    #options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    return driver
