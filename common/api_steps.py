"""
API STEPS — методы для API тестов
====================================

  Что здесь хранится:
   - Обёртка над APIClient для удобного использования в тестах
   - Берёт базовый URL из настроек автоматически

  Как использовать в тестах:
   from common.api_steps import APISteps
   
   self.api = APISteps()
   response = self.api.get(USER_GET.format(user_id=1))
   assert response.status_code == 200

  Что можно копировать в тест:
   response = self.api.get(USER_GET.format(user_id=1))
   response = self.api.post(USER_CREATE, json=new_user)
   response = self.api.put(USER_UPDATE.format(user_id=1), json=update_data)
   response = self.api.delete(USER_DELETE.format(user_id=1))
"""

from common.api_client import APIClient
from config.settings import TestSettings

class APISteps:
    def __init__(self, logger=None):
        """
        Инициализация API шагов
        
        📋 Копировать в тест:
            self.api = APISteps()
            # или с логгером:
            self.api = APISteps(logger=self.logger)
        """
        from common.api_client import APIClient
        from config.settings import TestSettings
        
        self.client = APIClient(TestSettings.API_BASE_URL)
        
        if logger:
            self.logger = logger
        else:
            import logging
            self.logger = logging.getLogger(__name__)
    
    def get(self, endpoint: str, **kwargs):
        """
        GET запрос — получение данных
        
          Копировать в тест:
            from endpoints.user_endpoints import USER_GET
            
            response = self.api.get(USER_GET.format(user_id=1))
            assert response.status_code == 200
            data = response.json()
        
          Что можно поменять:
            endpoint — путь к ресурсу (берём из папки endpoints/)
        """
        return self.client.get(endpoint, **kwargs)
    
    def post(self, endpoint: str, data: dict = None, json: dict = None, **kwargs):
        """
        POST запрос — создание нового ресурса
        
          Копировать в тест:
            from endpoints.user_endpoints import USER_CREATE
            
            new_user = {"name": "Test", "email": "test@mail.com"}
            response = self.api.post(USER_CREATE, json=new_user)
            assert response.status_code == 201
        
          Что можно поменять:
            endpoint — путь к ресурсу (берём из папки endpoints/)
            json — данные для создания (создаём в тесте)
        """
        return self.client.post(endpoint, data=data, json=json, **kwargs)
    
    def put(self, endpoint: str, **kwargs):
        """
        PUT запрос — полное обновление ресурса
        
          Копировать в тест:
            from endpoints.user_endpoints import USER_UPDATE
            
            update_data = {"name": "New Name", "email": "new@mail.com"}
            response = self.api.put(USER_UPDATE.format(user_id=1), json=update_data)
            assert response.status_code == 200
        
          Что можно поменять:
            endpoint — путь к ресурсу (берём из папки endpoints/)
        """
        return self.client.put(endpoint, **kwargs)
    
    def delete(self, endpoint: str, **kwargs):
        """
        DELETE запрос — удаление ресурса
        
          Копировать в тест:
            from endpoints.user_endpoints import USER_DELETE
            
            response = self.api.delete(USER_DELETE.format(user_id=1))
            assert response.status_code in [200, 204]
        
          Что можно поменять:
            endpoint — путь к ресурсу (берём из папки endpoints/)
        """
        return self.client.delete(endpoint, **kwargs)
    
    def patch(self, endpoint: str, **kwargs):
        """
        PATCH запрос — частичное обновление ресурса
        
          Копировать в тест:
            from endpoints.user_endpoints import USER_UPDATE
            
            patch_data = {"email": "new@mail.com"}
            response = self.api.patch(USER_UPDATE.format(user_id=1), json=patch_data)
        
          Что можно поменять:
            endpoint — путь к ресурсу (берём из папки endpoints/)
        """
        return self.client.patch(endpoint, **kwargs)
    
    def add_header(self, key: str, value: str):
        """
        Добавить заголовок ко всем последующим запросам
        
          Копировать в тест:
            # Получаем токен
            response = self.api.post(AUTH_LOGIN, json={"username": "user", "password": "pass"})
            token = response.json()["access_token"]
            
            # Добавляем токен в заголовки
            self.api.add_header("Authorization", f"Bearer {token}")
        
          Что можно поменять:
            key — название заголовка (str)
            value — значение заголовка (str)
        """
        self.client.add_header(key, value)
    
    def clear_headers(self):
        """
        Очистить все заголовки
        
          Копировать в тест:
            self.api.clear_headers()
        """
        self.client.clear_headers()