"""
UI STEPS — методы для UI тестов
====================================

  Что здесь хранится:
   - Обёртка над Playwright Page для удобного использования в тестах
   - Все базовые действия: клики, ввод текста, проверки

  Как использовать в тестах:
   from common.ui_steps import UISteps
   
   self.ui = UISteps(page)
   self.ui.go_to_url(Urls.LOGIN_PAGE)
   self.ui.click(Locators.SUBMIT_BUTTON)
   self.ui.fill(Locators.USERNAME_INPUT, "user")
   self.ui.check_text(Locators.TITLE, "Products")

  Что можно копировать в тест:
   # Навигация
   self.ui.go_to_url(Urls.LOGIN_PAGE)
   self.ui.get_current_url()
   
   # Действия с элементами
   self.ui.click("#button")
   self.ui.fill("#input", "text")
   self.ui.get_text(".title")
   
   # Проверки
   self.ui.check_text(".title", "Products")
   self.ui.check_text_contains(".message", "добро")
   self.ui.check_element_visible(".logo")
   self.ui.check_url_contains("/cart")
   
   # Вспомогательные
   self.ui.take_screenshot("after_login")
   self.ui.wait_for_element("#spinner")
"""

import logging
from datetime import datetime

class UISteps:
    def __init__(self, page, logger=None):
        """
        Инициализация UI шагов
        
          Копировать в тест:
            self.ui = UISteps(page)
            # или с логгером:
            self.ui = UISteps(page, logger=self.logger)
        """
        self.page = page
        if logger:
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)
    
    # ============================================================
    # 1. НАВИГАЦИЯ
    # ============================================================
    
    def go_to_url(self, url: str):
        """
        Перейти по URL
        
          Копировать в тест:
            self.ui.go_to_url("https://example.com")
            self.ui.go_to_url(Urls.LOGIN_PAGE)  # из config/urls.py
        
          Что можно поменять:
            url — адрес страницы (строку или переменную из Urls)
        """
        self.logger.info(f"Переход на {url}")
        self.page.goto(url)
        self.logger.info("✅ Страница загружена")
    
    def get_current_url(self) -> str:
        """
        Получить текущий URL страницы
        
          Копировать в тест:
            current_url = self.ui.get_current_url()
            assert "cart" in current_url
        
          Что можно поменять:
            Ничего — просто получаешь значение и проверяешь
        """
        url = self.page.url
        self.logger.info(f"Текущий URL: {url}")
        return url
    
    # ============================================================
    # 2. РАБОТА С ЭЛЕМЕНТАМИ
    # ============================================================
    
    def wait_for_element(self, selector: str, timeout: int = 10):
        """
        Ожидать появление элемента на странице
        
          Копировать в тест:
            self.ui.wait_for_element("#loading-spinner")
            self.ui.wait_for_element(".popup", timeout=15)
        
          Что можно поменять:
            selector — CSS-селектор элемента (str)
            timeout — время ожидания в секундах (int, по умолчанию 10)
        """
        self.logger.info(f"Ожидание элемента {selector} ({timeout} сек)")
        self.page.wait_for_selector(selector, timeout=timeout * 1000)
        self.logger.info(f"✅ Элемент {selector} появился")
    
    def click(self, selector: str):
        """
        Кликнуть по элементу (кнопка, ссылка, чекбокс)
        
          Копировать в тест:
            self.ui.click("#submit-btn")
            self.ui.click(Locators.SUBMIT_BUTTON)  # из pages/login_page.py
        
          Что можно поменять:
            selector — CSS-селектор элемента (str)
        """
        self.logger.info(f"Клик по {selector}")
        self.wait_for_element(selector)
        self.page.click(selector)
        self.logger.info(f"✅ Клик выполнен")
    
    def fill(self, selector: str, text: str):
        """
        Ввести текст в поле ввода
        
          Копировать в тест:
            self.ui.fill("#username", "my_login")
            self.ui.fill(Locators.USERNAME_INPUT, "standard_user")
        
          Что можно поменять:
            selector — CSS-селектор поля ввода (str)
            text — текст для ввода (str)
        """
        self.logger.info(f"Ввод '{text}' в {selector}")
        self.wait_for_element(selector)
        self.page.fill(selector, text)
        self.logger.info(f"✅ Текст введен")
    
    def clear(self, selector: str):
        """
        Очистить поле ввода
        
          Копировать в тест:
            self.ui.clear("#username")
        
          Что можно поменять:
            selector — CSS-селектор поля ввода (str)
        """
        self.logger.info(f"Очистка поля {selector}")
        self.page.fill(selector, "")
        self.logger.info(f"✅ Поле очищено")
    
    def get_text(self, selector: str) -> str:
        """
        Получить текст элемента
        
          Копировать в тест:
            text = self.ui.get_text(".title")
            assert text == "Products"
        
          Что можно поменять:
            selector — CSS-селектор элемента (str)
        """
        self.logger.info(f"Получение текста из {selector}")
        self.wait_for_element(selector)
        text = self.page.text_content(selector)
        self.logger.info(f"✅ Получен текст: '{text}'")
        return text
    
    def get_attribute(self, selector: str, attribute: str) -> str:
        """
        Получить атрибут элемента (href, src, value, class, id)
        
          Копировать в тест:
            href = self.ui.get_attribute("a", "href")
            src = self.ui.get_attribute("img", "src")
        
          Что можно поменять:
            selector — CSS-селектор элемента (str)
            attribute — имя атрибута (str)
        """
        self.logger.info(f"Получение атрибута {attribute} из {selector}")
        value = self.page.get_attribute(selector, attribute)
        self.logger.info(f"✅ Получено: '{value}'")
        return value
    
    def get_element_count(self, selector: str) -> int:
        """
        Получить количество элементов (для списков)
        
          Копировать в тест:
            count = self.ui.get_element_count(".cart-item")
            assert count == 3  # в корзине 3 товара
        
          Что можно поменять:
            selector — CSS-селектор элементов (str)
        """
        count = self.page.locator(selector).count()
        self.logger.info(f"Найдено {count} элементов {selector}")
        return count
    
    # ============================================================
    # 3. ПРОВЕРКИ
    # ============================================================
    
    def check_text(self, selector: str, expected: str):
        """
        Проверить, что текст элемента СОВПАДАЕТ с ожидаемым (точное совпадение)
        
          Копировать в тест:
            self.ui.check_text(".title", "Products")
            self.ui.check_text(Locators.SUCCESS_MESSAGE, "Добро пожаловать")
        
          Что можно поменять:
            selector — CSS-селектор элемента (str)
            expected — ожидаемый текст (str)
        """
        actual = self.get_text(selector)
        self.logger.info(f"Проверка текста: ожидалось '{expected}', получено '{actual}'")
        assert actual == expected, f"Текст не совпадает: '{actual}' != '{expected}'"
        self.logger.info("✅ Текст совпадает")
    
    def check_text_contains(self, selector: str, expected_part: str):
        """
        Проверить, что текст элемента СОДЕРЖИТ ожидаемую подстроку
        
          Копировать в тест:
            self.ui.check_text_contains(".title", "Products")
            self.ui.check_text_contains(".message", "добро пожаловать")
        
          Что можно поменять:
            selector — CSS-селектор элемента (str)
            expected_part — ожидаемая подстрока (str)
        """
        actual = self.get_text(selector)
        self.logger.info(f"Проверка наличия '{expected_part}' в '{actual}'")
        assert expected_part in actual, f"'{expected_part}' не найдено в '{actual}'"
        self.logger.info("✅ Подстрока найдена")
    
    def check_element_visible(self, selector: str):
        """
        Проверить, что элемент ВИДЕН на странице
        
          Копировать в тест:
            self.ui.check_element_visible(".logo")
            self.ui.check_element_visible(Locators.SUCCESS_MESSAGE)
        
          Что можно поменять:
            selector — CSS-селектор элемента (str)
        """
        self.logger.info(f"Проверка видимости {selector}")
        self.wait_for_element(selector)
        is_visible = self.page.is_visible(selector)
        assert is_visible, f"Элемент {selector} не виден"
        self.logger.info("✅ Элемент виден")
    
    def check_element_hidden(self, selector: str):
        """
        Проверить, что элемент СКРЫТ или отсутствует
        
          Копировать в тест:
            self.ui.check_element_hidden(".loading-spinner")
        
          Что можно поменять:
            selector — CSS-селектор элемента (str)
        """
        self.logger.info(f"Проверка что элемент {selector} скрыт")
        is_hidden = self.page.is_hidden(selector)
        assert is_hidden, f"Элемент {selector} виден (а должен быть скрыт)"
        self.logger.info("✅ Элемент скрыт")
    
    def check_url_contains(self, expected_part: str):
        """
        Проверить, что текущий URL содержит ожидаемую подстроку
        
          Копировать в тест:
            self.ui.check_url_contains("/cart")    # проверка перехода в корзину
            self.ui.check_url_contains("/login")   # проверка что на странице логина
        
          Что можно поменять:
            expected_part — часть URL (str)
        """
        current_url = self.page.url
        self.logger.info(f"Проверка URL: '{expected_part}' в '{current_url}'")
        assert expected_part in current_url, f"'{expected_part}' не найдено в '{current_url}'"
        self.logger.info("✅ URL содержит ожидаемую часть")
    
    # ============================================================
    # 4. ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ
    # ============================================================
    
    def scroll_to_element(self, selector: str):
        """
        Прокрутить страницу до элемента
        
          Копировать в тест:
            self.ui.scroll_to_element("#footer")
            self.ui.scroll_to_element(Locators.CHECKOUT_BUTTON)
        
          Что можно поменять:
            selector — CSS-селектор элемента (str)
        """
        self.logger.info(f"Скролл к {selector}")
        self.page.locator(selector).scroll_into_view_if_needed()
        self.logger.info("✅ Скролл выполнен")
    
    def take_screenshot(self, name: str = "screenshot"):
        """
        Сделать скриншот страницы (сохраняется в results/screenshots/)
        
          Копировать в тест:
            self.ui.take_screenshot("after_login")
            self.ui.take_screenshot("error_" + test_name)
        
          Что можно поменять:
            name — имя файла скриншота (str)
        """
        import os
        os.makedirs("results/screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results/screenshots/{name}_{timestamp}.png"
        self.page.screenshot(path=filename)
        self.logger.info(f"✅ Скриншот сохранен: {filename}")