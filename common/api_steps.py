"""
API STEPS — методы для API тестов
"""

import logging
from common.api_client import APIClient
from config.settings import TestSettings


class APISteps:
    def __init__(self, logger):
        self.client = APIClient(TestSettings.API_BASE_URL)
        self.logger = logger
    
    # ============================================================
    # ОСНОВНЫЕ HTTP МЕТОДЫ
    # ============================================================
    
    def get(self, endpoint: str, **kwargs):
        """
        GET запрос — получить данные
        
          Копировать в тест:
            response = self.api.get(USER_GET.format(user_id=1))
            assert response.status_code == 200, f"Ошибка: статус {response.status_code}"
            data = response.json()
            assert data["id"] == 1, f"Неверный id: {data['id']}"
            assert "name" in data, "В ответе нет поля name"
            assert "email" in data, "В ответе нет поля email"
            self.logger.info(f"✅ Пользователь получен: {data['name']}")
        
          Источники эндпоинтов:
            - USER_GET = "/users/{user_id}" (из endpoints/user_endpoints.py)
        """
        self.logger.info(f"  GET {endpoint}")
        response = self.client.get(endpoint, **kwargs)
        self.logger.info(f"  Response status: {response.status_code}")
        return response
    
    def post(self, endpoint: str, json: dict = None, **kwargs):
        """
        POST запрос — создать ресурс
        
          Копировать в тест:
            new_user = {"name": "Test User", "email": "test@example.com"}
            response = self.api.post(USER_CREATE, json=new_user)
            assert response.status_code == 201, f"Ошибка: статус {response.status_code}"
            data = response.json()
            assert data["name"] == new_user["name"], "Имя не совпадает"
            assert data["email"] == new_user["email"], "Email не совпадает"
            self.logger.info(f"✅ Пользователь создан: {data}")
        
          Источники эндпоинтов:
            - USER_CREATE = "/users" (из endpoints/user_endpoints.py)
        """
        self.logger.info(f"  POST {endpoint}")
        response = self.client.post(endpoint, json=json, **kwargs)
        self.logger.info(f"  Response status: {response.status_code}")
        return response
    
    def put(self, endpoint: str, json: dict = None, **kwargs):
        """
        PUT запрос — полное обновление ресурса
        
          Копировать в тест:
            update_data = {"name": "Updated Name", "email": "updated@example.com"}
            response = self.api.put(USER_UPDATE.format(user_id=1), json=update_data)
            assert response.status_code == 200, f"Ошибка: статус {response.status_code}"
            self.logger.info(f"✅ Пользователь обновлён")
        
          Источники эндпоинтов:
            - USER_UPDATE = "/users/{user_id}" (из endpoints/user_endpoints.py)
        """
        self.logger.info(f"  PUT {endpoint}")
        response = self.client.put(endpoint, json=json, **kwargs)
        self.logger.info(f"  Response status: {response.status_code}")
        return response
    
    def delete(self, endpoint: str, **kwargs):
        """
        DELETE запрос — удалить ресурс
        
          Копировать в тест:
            response = self.api.delete(USER_DELETE.format(user_id=1))
            assert response.status_code in [200, 204], f"Ошибка: статус {response.status_code}"
            self.logger.info(f"✅ Пользователь удалён")
        
          Источники эндпоинтов:
            - USER_DELETE = "/users/{user_id}" (из endpoints/user_endpoints.py)
        """
        self.logger.info(f"  DELETE {endpoint}")
        response = self.client.delete(endpoint, **kwargs)
        self.logger.info(f"  Response status: {response.status_code}")
        return response
    
    def patch(self, endpoint: str, json: dict = None, **kwargs):
        """
        PATCH запрос — частичное обновление ресурса
        
          Копировать в тест:
            patch_data = {"email": "new@example.com"}
            response = self.api.patch(USER_UPDATE.format(user_id=1), json=patch_data)
            assert response.status_code == 200, f"Ошибка: статус {response.status_code}"
            self.logger.info(f"✅ Пользователь обновлён (частично)")
        """
        self.logger.info(f"  PATCH {endpoint}")
        response = self.client.patch(endpoint, json=json, **kwargs)
        self.logger.info(f"  Response status: {response.status_code}")
        return response
    
    # ============================================================
    # РАБОТА С ЗАГОЛОВКАМИ
    # ============================================================
    
    def add_header(self, key: str, value: str):
        """
        Добавить заголовок ко всем запросам (для авторизации)
        
          Копировать в тест:
            self.api.add_header("Authorization", f"Bearer {token}")
        """
        self.client.add_header(key, value)
        self.logger.info(f"  Добавлен заголовок: {key}: {value}")
    
    def clear_headers(self):
        """
        Очистить все заголовки
        
          Копировать в тест:
            self.api.clear_headers()
        """
        self.client.clear_headers()
        self.logger.info("  Заголовки очищены")