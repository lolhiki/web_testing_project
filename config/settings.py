"""
Глобальные настройки проекта
====================================

   Что здесь хранится:
   - Настройки браузера (видимый/невидимый)
   - Таймауты ожидания
   - Базовые URL для API и UI
   - Окружение (dev/staging/prod)

   Как использовать в тестах:
   from config.settings import TestSettings
   
   if TestSettings.HEADLESS:
       # браузер не виден
   else:
       # браузер виден
"""

class TestSettings:
    # ========== БРАУЗЕР ==========
    HEADLESS = False           # True — браузер не виден (для CI)
                               # False — браузер виден (для отладки)
    
    # ========== ТАЙМАУТЫ (в секундах) ==========
    WAIT_TIMEOUT = 10          # Ожидание появления элемента
    PAGE_LOAD_TIMEOUT = 30     # Ожидание загрузки страницы
    API_REQUEST_TIMEOUT = 5    # Ожидание ответа API
    
    # ========== ОКРУЖЕНИЕ ==========
    # Доступные: "dev", "staging", "prod"
    ENVIRONMENT = "staging"
    
    # ========== API ==========
    # Базовый URL для API тестов (можно переопределить под окружение)
    API_BASE_URL = "https://jsonplaceholder.typicode.com"
    
    # ========== НАСТРОЙКИ ОТЧЁТОВ ==========
    SCREENSHOT_ON_FAILURE = True   # Делать скриншот при падении теста
    SAVE_LOGS = True               # Сохранять логи в results/logs/