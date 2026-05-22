import sys
import os

# Добавляем корень проекта в путь (для прямого запуска)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import pytest
from common.ui_steps import UISteps
from config.urls import Urls


class TestUITemplate:
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        """
        Настройка перед каждым тестом
        Создаёт экземпляр UI шагов (аналог подключения к CAN)
        """
        self.ui = UISteps(page)
    
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
        
        print("✅ Тест пройден")
    
    # ============================================================
    # КОНЕЦ ТЕСТА
    # ============================================================


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])