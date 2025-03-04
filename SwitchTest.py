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
options.add_argument("--start-maximized")  # Оставим для попытки
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")

# Инициализация драйвера
driver = webdriver.Chrome(service=service, options=options)

# Принудительный полноэкранный режим (запасной вариант)
driver.set_window_size(1920, 1080)  # Устанавливаем большой размер окна

# Открытие сайта
driver.get("https://www.lotgchurch.com/en/light-of-gospel-home-page-english/")

# Ожидание загрузки страницы
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "post-24650"))
)

# Ожидание кликабельности элемента (проверяем вложенные элементы слайдера)
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="rev_slider_5_1"]//a | //*[@id="rev_slider_5_1"]//button'))
)

# Скролл к элементу
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

# Пауза после скролла
time.sleep(1)

# Клик через JavaScript
driver.execute_script("arguments[0].click();", element)

# Ожидание результата
time.sleep(5)

# Закрытие браузера
driver.quit()