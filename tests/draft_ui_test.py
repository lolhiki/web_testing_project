"""
  ШАБЛОН UI ТЕСТА
====================================

  Как использовать:
   1. Скопируй этот файл в tests/ui/test_xxx.py
   2. Переименуй класс TestUITemplate в TestЧтоTesting
   3. Переименуй функцию test_example в test_что_тестируем
   4. Добавь шаги через self.ui.метод()

  Что можно копировать в тест (из common/ui_steps.py):
   self.ui.go_to_url(Urls.LOGIN_PAGE)
   self.ui.click(Locators.BUTTON)
   self.ui.fill(Locators.INPUT, "text")
   self.ui.check_text(Locators.TEXT, "expected")
"""

import sys
import os

# Добавляем корень проекта в путь (для прямого запуска)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import pytest
from common.ui_steps import UISteps
from config.urls import Urls


class TestUITemplate:
    
    @pytest.fixture(autouse=True)
    def setup(self, page, request):
        """
        Настройка перед каждым тестом
        Создаёт экземпляр UI шагов (аналог подключения к CAN)
        """
        #   Создаём логгер с именем теста
        from common.logger import setup_logger
        self.logger = setup_logger(request.node.name)
        
        #   Передаём логгер в UISteps
        self.ui = UISteps(page, logger=self.logger)
    
    # ============================================================
    # ТВОЙ ТЕСТ НАЧИНАЕТСЯ ЗДЕСЬ
    # ============================================================
    
    # @pytest.mark.smoke      # Укажи маркер для группировки и раскомментируй
    # @pytest.mark.ui         # Доступные маркеры: smoke, regression, api, ui
    def test_example(self):
        """
        TODO: Кратко опиши, что проверяет тест
        """
        
        # Шаг 1: TODO — укажи название шага
        # self.ui.go_to_url(Urls.LOGIN_PAGE)
        
        # Шаг 2: TODO — укажи название шага
        # self.ui.fill("#username", "standard_user")
        
        # Шаг 3: TODO — укажи название шага
        # self.ui.click("#submit")
        
        # Шаг 4: TODO — укажи название шага
        # self.ui.check_text(".title", "Products")
        
        self.logger.info("✅ Тест пройден")
        print("✅ Тест пройден")
    
    # ============================================================
    # КОНЕЦ ТЕСТА
    # ============================================================


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])