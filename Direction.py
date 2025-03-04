from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка сервиса
service = Service(ChromeDriverManager().install())

# Настройка опций для полноэкранного режима
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--start-maximized")  # Попробуем ещё раз
options.add_argument("--disable-extensions")  # Отключаем расширения для стабильности
options.add_argument("--no-sandbox")  # Для macOS иногда помогает

# Инициализация драйвера
driver = webdriver.Chrome(service=service, options=options)

# Открытие сайта
driver.get("https://www.lotgchurch.com/en/light-of-gospel-home-page-english/")

# Явное ожидание полной загрузки страницы (например, основного контента)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "post-24650"))
)

# Ожидание кликабельности элемента
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="post-24650"]/div/div/section[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/a'))
)

# Скролл к элементу
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

# Небольшая пауза после скролла для стабильности
time.sleep(1)

# Клик через JavaScript
driver.execute_script("arguments[0].click();", element)

# Ожидание результата
time.sleep(5)

# Закрытие браузера
driver.quit()