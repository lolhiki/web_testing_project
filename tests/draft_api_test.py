import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from common.logger import setup_logger
from common.api_steps import APISteps
from endpoints.user_endpoints import *


TEST_NAME = "ЗАМЕНИТЕ_НА_НАЗВАНИЕ_ТЕСТА"


class TestAPITemplate:
    
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.logger = setup_logger(request.node.name)
        self.api = APISteps(logger=self.logger)
    
    # @pytest.mark.smoke
    # @pytest.mark.api
    def test_example(self):
        self.logger.info("=" * 60)
        self.logger.info(f"  ТЕСТ: {TEST_NAME}")
        self.logger.info("=" * 60)
        
        # 👉 ТВОИ ШАГИ НАЧИНАЮТСЯ ЗДЕСЬ
        
        # Пример:
        # response = api.get(USER_GET.format(user_id=1))
        # assert response.status_code == 200
        # data = response.json()
        # assert data["id"] == 1
        
        self.logger.info("=" * 60)
        self.logger.info(f"✅ ТЕСТ {TEST_NAME} ПРОЙДЕН УСПЕШНО")
        self.logger.info("=" * 60)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])