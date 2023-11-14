from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.keys import Keys
import time


from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
'''
# Spécifiez le chemin vers le pilote Edge WebDriver
edge_driver_path = "C:/Users/fibou/cahier_exercice/comparateur_cote/projet1/comparateur_live/msedgedriver"

# Créez une instance du navigateur Edge
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True  # Assurez-vous que cette option est définie pour les versions récentes de Edge
edge_options.binary_location = edge_driver_path

driver = webdriver.Edge(options=edge_options)
'''
from selenium import webdriver
from webdriver_manager.microsoft import EdgeDriverManager

# Créez une instance du navigateur Edge en utilisant le gestionnaire de pilotes
driver = webdriver.Edge(EdgeDriverManager().install())

# Exemple : accédez à une page Web
driver.get("https://www.google.com")

# Exemple : accédez à une page Web
#driver.get("https://www.google.com")

# Faire d'autres opérations avec Selenium...
time.sleep(7)

# Fermez le navigateur Edge
driver.quit()
