"""
Pytest фикстуры для всего проекта
====================================

  Что здесь хранится:
   - Фикстура page — создаёт браузер и страницу для UI тестов
   - Фикстура test_logger — автоматическое логирование тестов

  Как использовать:
   # Фикстура page автоматически доступна в UI тестах
   def test_example(self, page):
       self.ui = UISteps(page)
       self.ui.go_to_url(Urls.LOGIN_PAGE)
   
   # Фикстура test_logger подключается автоматически (autouse=True)
   # Логгер будет создан для каждого теста
"""

import pytest
from playwright.sync_api import sync_playwright
from config.settings import TestSettings
from common.logger import setup_logger


@pytest.fixture(scope="function")
def page(request):
    """
    Фикстура Playwright — создаёт новую страницу для каждого теста
    
      Как использовать в тесте:
        def test_example(self, page):
            self.ui = UISteps(page)
            self.ui.go_to_url(Urls.LOGIN_PAGE)
    
      Что делает:
        - Открывает браузер (Chromium)
        - Создаёт новую страницу
        - После теста закрывает браузер автоматически
    
      Настройки браузера:
        headless = TestSettings.HEADLESS (True — без UI, False — с UI)
    """
    with sync_playwright() as p:
        # Запускаем браузер (видимый или нет — из настроек)
        browser = p.chromium.launch(headless=TestSettings.HEADLESS)
        
        # Создаём контекст и страницу
        context = browser.new_context()
        page = context.new_page()
        
        # 🔥 Сохраняем логгер в атрибут page
        page.logger = setup_logger(request.node.name)
        
        # Передаём страницу в тест
        yield page
        
        # После теста закрываем браузер
        browser.close()


@pytest.fixture(autouse=True)
def test_logger(request):
    """
    Фикстура для автоматического логирования тестов
    
      Что делает:
        - Создаёт логгер для каждого теста
        - Пишет в лог начало и конец теста
        - Логи сохраняются в results/logs/
    
      Используется автоматически (autouse=True)
        Не нужно вызывать в тесте — подключается сама
    """
    # Создаём логгер с именем теста
    logger = setup_logger(request.node.name)
    
    # Логируем начало теста
    logger.info("=" * 60)
    logger.info(f"Запуск теста: {request.node.name}")
    logger.info("=" * 60)
    
    # Передаём управление тесту
    yield
    
    # Логируем завершение теста
    logger.info(f"Завершение теста: {request.node.name}")
    logger.info("=" * 60)