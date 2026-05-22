"""
UI STEPS — методы для UI тестов
"""

import logging
from datetime import datetime

class UISteps:
    def __init__(self, page, logger):
        self.page = page
        self.logger = logger
    
    # ============================================================
    # НАВИГАЦИЯ
    # ============================================================
    
    def go_to_url(self, url: str):
        """
        Перейти по URL
        
          Копировать в тест:
            self.ui.go_to_url(Urls.LOGIN_PAGE)
        
          Источники URL:
            - Urls.LOGIN_PAGE, Urls.MAIN_PAGE, Urls.CART_PAGE (из config/urls.py)
        """
        self.logger.info(f"Переход на {url}")
        self.page.goto(url)
        self.logger.info("✅ Страница загружена")
        return True
    
    def get_current_url(self) -> str:
        """
        Получить текущий URL
        
          Копировать в тест:
            current_url = self.ui.get_current_url()
            assert "/cart" in current_url
        """
        url = self.page.url
        self.logger.info(f"Текущий URL: {url}")
        return url
    
    # ============================================================
    # РАБОТА С ЭЛЕМЕНТАМИ
    # ============================================================
    
    def wait_for_element(self, selector: str, timeout: int = 10):
        """
        Ожидать появление элемента на странице
        
          Копировать в тест:
            self.ui.wait_for_element(Locators.SOME_ELEMENT, timeout=10)
        """
        self.logger.info(f"Ожидание элемента {selector} ({timeout} сек)")
        self.page.wait_for_selector(selector, timeout=timeout * 1000)
        self.logger.info(f"✅ Элемент {selector} появился")
        return True
    
    def click(self, selector: str):
        """
        Кликнуть по элементу
        
          Копировать в тест:
            self.ui.click(Locators.SUBMIT_BUTTON)
        
          Источники селекторов:
            - Locators.SUBMIT_BUTTON, Locators.CART_ICON (из pages/xxx_page.py)
        """
        self.logger.info(f"Клик по {selector}")
        self.wait_for_element(selector)
        self.page.click(selector)
        self.logger.info(f"✅ Клик выполнен")
        return True
    
    def fill(self, selector: str, text: str):
        """
        Ввести текст в поле ввода
        
          Копировать в тест:
            self.ui.fill(Locators.USERNAME_INPUT, "standard_user")
        
          Источники параметров:
            - selector: Locators.USERNAME_INPUT (из pages/login_page.py)
            - text: "standard_user" или TestData.VALID_USER["username"]
        """
        self.logger.info(f"Ввод '{text}' в {selector}")
        self.wait_for_element(selector)
        self.page.fill(selector, text)
        self.logger.info(f"✅ Текст введен")
        return True
    
    def clear(self, selector: str):
        """
        Очистить поле ввода
        
          Копировать в тест:
            self.ui.clear(Locators.USERNAME_INPUT)
        """
        self.logger.info(f"Очистка поля {selector}")
        self.page.fill(selector, "")
        self.logger.info(f"✅ Поле очищено")
        return True
    
    def get_text(self, selector: str) -> str:
        """
        Получить текст элемента
        
          Копировать в тест:
            text = self.ui.get_text(Locators.SUCCESS_MESSAGE)
            assert text == "Products"
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
            assert count == 3
        """
        count = self.page.locator(selector).count()
        self.logger.info(f"Найдено {count} элементов {selector}")
        return count
    
    # ============================================================
    # ПРОВЕРКИ
    # ============================================================
    
    def check_text(self, selector: str, expected: str):
        """
        Проверить точное совпадение текста
        
          Копировать в тест:
            self.ui.check_text(Locators.SUCCESS_MESSAGE, "Products")
        
          Источники параметров:
            - selector: Locators.SUCCESS_MESSAGE (из pages/login_page.py)
            - expected: "Products" или TestData.Messages.LOGIN_SUCCESS
        """
        actual = self.get_text(selector)
        self.logger.info(f"Проверка текста: ожидалось '{expected}', получено '{actual}'")
        assert actual == expected, f"Текст не совпадает: '{actual}' != '{expected}'"
        self.logger.info("✅ Текст совпадает")
        return True
    
    def check_text_contains(self, selector: str, expected_part: str):
        """
        Проверить, что текст содержит подстроку
        
          Копировать в тест:
            self.ui.check_text_contains(Locators.SUCCESS_MESSAGE, "Products")
        """
        actual = self.get_text(selector)
        self.logger.info(f"Проверка наличия '{expected_part}' в '{actual}'")
        assert expected_part in actual, f"'{expected_part}' не найдено в '{actual}'"
        self.logger.info("✅ Подстрока найдена")
        return True
    
    def check_element_visible(self, selector: str):
        """
        Проверить, что элемент виден
        
          Копировать в тест:
            self.ui.check_element_visible(Locators.SUCCESS_MESSAGE)
        """
        self.logger.info(f"Проверка видимости {selector}")
        self.wait_for_element(selector)
        is_visible = self.page.is_visible(selector)
        assert is_visible, f"Элемент {selector} не виден"
        self.logger.info("✅ Элемент виден")
        return True
    
    def check_element_hidden(self, selector: str):
        """
        Проверить, что элемент скрыт
        
          Копировать в тест:
            self.ui.check_element_hidden(".loading-spinner")
        """
        self.logger.info(f"Проверка что элемент {selector} скрыт")
        is_hidden = self.page.is_hidden(selector)
        assert is_hidden, f"Элемент {selector} виден (а должен быть скрыт)"
        self.logger.info("✅ Элемент скрыт")
        return True
    
    def check_url_contains(self, expected_part: str):
        """
        Проверить, что URL содержит подстроку
        
          Копировать в тест:
            self.ui.check_url_contains("/cart")
        """
        current_url = self.page.url
        self.logger.info(f"Проверка URL: '{expected_part}' в '{current_url}'")
        assert expected_part in current_url, f"'{expected_part}' не найдено в '{current_url}'"
        self.logger.info("✅ URL содержит ожидаемую часть")
        return True
    
    # ============================================================
    # ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ
    # ============================================================
    
    def scroll_to_element(self, selector: str):
        """
        Прокрутить до элемента
        
          Копировать в тест:
            self.ui.scroll_to_element(Locators.CHECKOUT_BUTTON)
        """
        self.logger.info(f"Скролл к {selector}")
        self.page.locator(selector).scroll_into_view_if_needed()
        self.logger.info("✅ Скролл выполнен")
        return True
    
    def take_screenshot(self, name: str = "screenshot"):
        """
        Сделать скриншот
        
          Копировать в тест:
            self.ui.take_screenshot("after_login")
        """
        import os
        os.makedirs("results/screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results/screenshots/{name}_{timestamp}.png"
        self.page.screenshot(path=filename)
        self.logger.info(f"✅ Скриншот сохранен: {filename}")