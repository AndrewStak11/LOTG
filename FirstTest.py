from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time  # Добавлен импорт time

# Настройка сервиса
service = Service(ChromeDriverManager().install())

# Настройка опций для полноэкранного режима
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--start-maximized")

# Инициализация драйвера
driver = webdriver.Chrome(service=service, options=options)

# Открытие сайта
driver.get("https://www.lotgchurch.com/en/light-of-gospel-home-page-english/")

# Ожидание и клик по элементу
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-24858"]/a'))
)

# Клик через JavaScript
driver.execute_script("arguments[0].click();", element)

# Ожидание результата
time.sleep(5)

# Закрытие браузера
driver.quit()