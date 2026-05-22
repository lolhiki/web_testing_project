"""
Страница логина (SauceDemo)
====================================

  Что здесь хранится:
   - Локаторы элементов на странице логина
   - Тестовые данные (логины, пароли, ожидаемые сообщения)

  Как использовать в тестах:
   from pages.login_page import Locators, TestData
   
   self.ui.fill(Locators.USERNAME_INPUT, TestData.VALID_USER["username"])
   self.ui.fill(Locators.PASSWORD_INPUT, TestData.VALID_USER["password"])
   self.ui.click(Locators.SUBMIT_BUTTON)
   self.ui.check_text(Locators.SUCCESS_MESSAGE, TestData.Messages.LOGIN_SUCCESS)

  Базовый URL берётся из config/urls.py
   Полный URL = Urls.LOGIN_PAGE
"""

# ============================================================
# ЛОКАТОРЫ ЭЛЕМЕНТОВ
# ============================================================

class Locators:
    """CSS-селекторы элементов на странице логина"""
    
    # Поля ввода
    USERNAME_INPUT = "#user-name"          # поле ввода логина
    PASSWORD_INPUT = "#password"           # поле ввода пароля
    
    # Кнопки
    SUBMIT_BUTTON = "#login-button"        # кнопка входа
    
    # Сообщения
    ERROR_MESSAGE = "[data-test='error']"  # сообщение об ошибке
    SUCCESS_MESSAGE = ".title"             # заголовок "Products" после входа


# ============================================================
# ТЕСТОВЫЕ ДАННЫЕ
# ============================================================

class TestData:
    """Данные для тестирования страницы логина"""
    
    # Учётные записи пользователей
    VALID_USER = {"username": "standard_user", "password": "secret_sauce"}
    LOCKED_USER = {"username": "locked_out_user", "password": "secret_sauce"}
    PROBLEM_USER = {"username": "problem_user", "password": "secret_sauce"}
    INVALID_USER = {"username": "wrong_user", "password": "wrong_pass"}
    
    # Ожидаемые сообщения
    class Messages:
        LOGIN_SUCCESS = "Products"                                          # успешный вход
        LOGIN_ERROR = "Epic sadface: Username and password do not match"    # ошибка входа
        LOCKED_ERROR = "Epic sadface: Sorry, this user has been locked out." # заблокирован


# ============================================================
# ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ В ТЕСТАХ
# ============================================================

# 📋 Тест успешного логина:
#    self.ui.go_to_url(Urls.LOGIN_PAGE)
#    self.ui.fill(Locators.USERNAME_INPUT, TestData.VALID_USER["username"])
#    self.ui.fill(Locators.PASSWORD_INPUT, TestData.VALID_USER["password"])
#    self.ui.click(Locators.SUBMIT_BUTTON)
#    self.ui.check_text(Locators.SUCCESS_MESSAGE, TestData.Messages.LOGIN_SUCCESS)

# 📋 Тест ошибки при невалидных данных:
#    self.ui.go_to_url(Urls.LOGIN_PAGE)
#    self.ui.fill(Locators.USERNAME_INPUT, TestData.INVALID_USER["username"])
#    self.ui.fill(Locators.PASSWORD_INPUT, TestData.INVALID_USER["password"])
#    self.ui.click(Locators.SUBMIT_BUTTON)
#    self.ui.check_text(Locators.ERROR_MESSAGE, TestData.Messages.LOGIN_ERROR)

# 📋 Тест заблокированного пользователя:
#    self.ui.go_to_url(Urls.LOGIN_PAGE)
#    self.ui.fill(Locators.USERNAME_INPUT, TestData.LOCKED_USER["username"])
#    self.ui.fill(Locators.PASSWORD_INPUT, TestData.LOCKED_USER["password"])
#    self.ui.click(Locators.SUBMIT_BUTTON)
#    self.ui.check_text(Locators.ERROR_MESSAGE, TestData.Messages.LOCKED_ERROR)