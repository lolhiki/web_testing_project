import sys
import os

# Добавляем корень проекта в путь (для прямого запуска)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import pytest
from common.api_steps import APISteps
from config.settings import TestSettings


class TestAPITemplate:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Настройка перед каждым тестом
        Создаёт экземпляр API шагов (аналог подключения к CAN)
        """
        self.api = APISteps()
    
    # ============================================================
    # ТВОЙ ТЕСТ НАЧИНАЕТСЯ ЗДЕСЬ
    # ============================================================
    
    # @pytest.mark.smoke      # Укажи маркер для группировки и раскомментируй
    # @pytest.mark.api        # Доступные маркеры: smoke, regression, api, ui
    def test_example(self):
        """
        TODO: Кратко опиши, что проверяет тест
        """
        
        # Шаг 1: TODO — укажи название шага
        # response = self.api.get("/users/1")
        # assert response.status_code == 200
        
        # Шаг 2: TODO — укажи название шага
        # data = response.json()
        # assert data["id"] == 1
        
        print("✅ Тест пройден")
    
    # ============================================================
    # КОНЕЦ ТЕСТА
    # ============================================================


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])