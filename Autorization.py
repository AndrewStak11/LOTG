from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка сервиса
service = Service(ChromeDriverManager().install())

# Настройка опций
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")

# Инициализация драйвера
driver = webdriver.Chrome(service=service, options=options)

# Динамическая установка размера окна (90% от размеров экрана)
width = driver.execute_script("return screen.width * 0.9;")
height = driver.execute_script("return screen.height * 0.9;")
driver.set_window_size(int(width), int(height))

# Открытие сайта
driver.get("https://www.lotgchurch.com/en/light-of-gospel-home-page-english/")

# Ожидание загрузки страницы
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "post-24650"))
)

# Первый элемент: клик
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/header/div/section[1]/div/div[3]/div/div/div/div/a'))
)
driver.execute_script("arguments[0].click();", element)
time.sleep(5)

# Второй элемент: клик
element2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="react-container"]/div/header/div/div/div/div[3]/button/div[3]/span'))
)
driver.execute_script("arguments[0].click();", element2)
time.sleep(5)

# Третий элемент: клик
element3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/a/span'))
)
driver.execute_script("arguments[0].click();", element3)
time.sleep(5)

# Закрытие браузера
driver.quit()
