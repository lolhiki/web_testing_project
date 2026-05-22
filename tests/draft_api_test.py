"""
  ШАБЛОН API ТЕСТА
====================================

  Как использовать:
   1. Скопируй этот файл в tests/api/test_xxx.py
   2. Переименуй класс TestAPITemplate в TestЧтоTesting
   3. Переименуй функцию test_example в test_что_тестируем
   4. Добавь шаги через self.api.метод()

  Что можно копировать в тест (из common/api_steps.py):
   response = self.api.get(USER_GET.format(user_id=1))
   assert response.status_code == 200
   data = response.json()
   assert data["id"] == 1
"""

import sys
import os

# Добавляем корень проекта в путь (для прямого запуска)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import pytest
from common.api_steps import APISteps
from config.settings import TestSettings


class TestAPITemplate:
    
    @pytest.fixture(autouse=True)
    def setup(self, request):
        """
        Настройка перед каждым тестом
        Создаёт экземпляр API шагов (аналог подключения к CAN)
        """
        #   Создаём логгер с именем теста
        from common.logger import setup_logger
        self.logger = setup_logger(request.node.name)
        
        #   Передаём логгер в APISteps
        self.api = APISteps(logger=self.logger)
    
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
        
        self.logger.info("✅ Тест пройден")
        print("✅ Тест пройден")
    
    # ============================================================
    # КОНЕЦ ТЕСТА
    # ============================================================


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])