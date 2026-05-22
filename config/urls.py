"""
Базовые URL для разных окружений
====================================

   Что здесь хранится:
   - URL для разных окружений (dev, staging, prod)
   - Базовые адреса страниц

   Как использовать в тестах:
   from config.urls import Urls
   
   self.ui.go_to_url(Urls.LOGIN_PAGE)
   self.ui.go_to_url(Urls.MAIN_PAGE)

   Как переключить окружение:
   Просто измени CURRENT_ENV на нужное значение
"""

from config.settings import TestSettings

class Urls:
    # ========== БАЗОВЫЕ URL ДЛЯ КАЖДОГО ОКРУЖЕНИЯ ==========
    BASE_URLS = {
        "dev": "https://dev.saucedemo.com",
        "staging": "https://www.saucedemo.com",
        "prod": "https://www.saucedemo.com"
    }
    
    # ========== ТЕКУЩЕЕ ОКРУЖЕНИЕ (берём из settings.py) ==========
    CURRENT_ENV = TestSettings.ENVIRONMENT
    
    # ========== БАЗОВЫЙ URL ДЛЯ ТЕКУЩЕГО ОКРУЖЕНИЯ ==========
    BASE_URL = BASE_URLS[CURRENT_ENV]
    
    # ========== КОНКРЕТНЫЕ СТРАНИЦЫ ==========
    MAIN_PAGE = BASE_URL                     # Главная страница
    LOGIN_PAGE = BASE_URL                    # Страница логина (она же главная)
    INVENTORY_PAGE = f"{BASE_URL}/inventory.html"   # Страница с товарами
    CART_PAGE = f"{BASE_URL}/cart.html"            # Корзина
    CHECKOUT_STEP_ONE = f"{BASE_URL}/checkout-step-one.html"
    CHECKOUT_STEP_TWO = f"{BASE_URL}/checkout-step-two.html"
    CHECKOUT_COMPLETE = f"{BASE_URL}/checkout-complete.html"