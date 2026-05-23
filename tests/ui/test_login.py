import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from common.logger import setup_logger
from common.ui_steps import UISteps
from config.urls import Urls
from pages.login_page import *


TEST_NAME = "VALID_LOGIN"


class TestUITemplate:
    
    @pytest.fixture(autouse=True)
    def setup(self, page, request):
        self.logger = setup_logger(request.node.name)
        self.ui = UISteps(page, logger=self.logger)
    
    # @pytest.mark.smoke
    # @pytest.mark.ui
    def test_example(self):
        self.logger.info("=" * 60)
        self.logger.info(f"  ТЕСТ: {TEST_NAME}")
        self.logger.info("=" * 60)
        
        # 👉 ТВОИ ШАГИ НАЧИНАЮТСЯ ЗДЕСЬ
        
        # Шаг 1: Открыть страницу логина
        self.ui.go_to_url(Urls.LOGIN_PAGE)

        # Шаг 2% Ввести логин
        self.ui.fill(Locators.USERNAME_INPUT, "standard_user")

        # Шаг 3: Ввести пароль
        self.ui.fill(Locators.PASSWORD_INPUT, TestData.VALID_USER["password"])

        # Шаг 4: Нажать на кнопку входа
        self.ui.click(Locators.SUBMIT_BUTTON)

        # Шаг 5: Проверить результат
        self.ui.check_text(Locators.SUCCESS_MESSAGE, "Products")


        
        self.logger.info("=" * 60)
        self.logger.info(f"✅ ТЕСТ {TEST_NAME} ПРОЙДЕН УСПЕШНО")
        self.logger.info("=" * 60)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])