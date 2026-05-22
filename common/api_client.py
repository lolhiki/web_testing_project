"""
Базовый API клиент
====================================

  Что здесь хранится:
   - Базовый класс для отправки HTTP запросов
   - Методы GET, POST, PUT, DELETE, PATCH
   - Методы для работы с заголовками (авторизация)

  Как использовать в тестах:
   # Обычно не используем напрямую, а через api_steps.py
   from common.api_client import APIClient
   
   client = APIClient("https://jsonplaceholder.typicode.com")
   response = client.get("/users/1")
"""

import requests
import logging

class APIClient:
    def __init__(self, base_url: str):
        """
        Инициализация API клиента
        
          Копировать в тест:
            client = APIClient(TestSettings.API_BASE_URL)
        
          Что можно поменять:
            base_url — базовый адрес API (берём из config/settings.py)
        """
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
    
    def _build_url(self, endpoint: str) -> str:
        """Формирует полный URL из базового и эндпоинта"""
        return f"{self.base_url}{endpoint}"
    
    def get(self, endpoint: str, **kwargs):
        """
        GET запрос — получение данных
        
          Копировать в тест:
            from endpoints.user_endpoints import USER_GET
            
            response = client.get(USER_GET.format(user_id=1))
            assert response.status_code == 200
            data = response.json()
        
          Что можно поменять:
            endpoint — путь к ресурсу (берём из папки endpoints/)
            Пример: USER_GET.format(user_id=123)
        """
        url = self._build_url(endpoint)
        self.logger.info(f"GET {url}")
        response = self.session.get(url, timeout=30, **kwargs)
        self.logger.info(f"Response status: {response.status_code}")
        return response
    
    def post(self, endpoint: str, data: dict = None, json: dict = None, **kwargs):
        """
        POST запрос — создание нового ресурса
        
          Копировать в тест:
            from endpoints.user_endpoints import USER_CREATE
            
            new_user = {"name": "Test", "email": "test@mail.com"}
            response = client.post(USER_CREATE, json=new_user)
            assert response.status_code == 201
        
          Что можно поменять:
            endpoint — путь к ресурсу (берём из папки endpoints/)
            data — данные в формате form-data
            json — данные в формате JSON (создаём в тесте)
        """
        url = self._build_url(endpoint)
        self.logger.info(f"POST {url}")
        response = self.session.post(url, data=data, json=json, timeout=30, **kwargs)
        self.logger.info(f"Response status: {response.status_code}")
        return response
    
    def put(self, endpoint: str, **kwargs):
        """
        PUT запрос — полное обновление ресурса
        
          Копировать в тест:
            from endpoints.user_endpoints import USER_UPDATE
            
            update_data = {"name": "New Name", "email": "new@mail.com"}
            response = client.put(USER_UPDATE.format(user_id=1), json=update_data)
            assert response.status_code == 200
        
          Что можно поменять:
            endpoint — путь к ресурсу (берём из папки endpoints/)
            Пример: USER_UPDATE.format(user_id=123)
        """
        url = self._build_url(endpoint)
        self.logger.info(f"PUT {url}")
        response = self.session.put(url, timeout=30, **kwargs)
        self.logger.info(f"Response status: {response.status_code}")
        return response
    
    def delete(self, endpoint: str, **kwargs):
        """
        DELETE запрос — удаление ресурса
        
          Копировать в тест:
            from endpoints.user_endpoints import USER_DELETE
            
            response = client.delete(USER_DELETE.format(user_id=1))
            assert response.status_code in [200, 204]
        
          Что можно поменять:
            endpoint — путь к ресурсу (берём из папки endpoints/)
            Пример: USER_DELETE.format(user_id=123)
        """
        url = self._build_url(endpoint)
        self.logger.info(f"DELETE {url}")
        response = self.session.delete(url, timeout=30, **kwargs)
        self.logger.info(f"Response status: {response.status_code}")
        return response
    
    def patch(self, endpoint: str, **kwargs):
        """
        PATCH запрос — частичное обновление ресурса
        
          Копировать в тест:
            from endpoints.user_endpoints import USER_UPDATE
            
            patch_data = {"email": "new@mail.com"}
            response = client.patch(USER_UPDATE.format(user_id=1), json=patch_data)
        
          Что можно поменять:
            endpoint — путь к ресурсу (берём из папки endpoints/)
        """
        url = self._build_url(endpoint)
        self.logger.info(f"PATCH {url}")
        response = self.session.patch(url, timeout=30, **kwargs)
        self.logger.info(f"Response status: {response.status_code}")
        return response
    
    # ============================================================
    # РАБОТА С ЗАГОЛОВКАМИ (для авторизации)
    # ============================================================
    
    def add_header(self, key: str, value: str):
        """
        Добавить заголовок ко всем последующим запросам (например, для авторизации)
        
          КОГДА НУЖНО:
           - API требует Bearer token (JWT)
           - API требует API-ключ в заголовке
           - Нужно указать Content-Type для всех запросов
        
          Копировать в тест:
            from endpoints.auth_endpoints import AUTH_LOGIN
            
            # Шаг 1: Получаем токен
            login_response = client.post(AUTH_LOGIN, json={
                "username": "user@example.com",
                "password": "pass123"
            })
            token = login_response.json()["access_token"]
            
            # Шаг 2: Добавляем токен в заголовки
            client.add_header("Authorization", f"Bearer {token}")
            
            # Шаг 3: Теперь все запросы будут авторизованы
            response = client.get("/users/me")
            assert response.status_code == 200
        
          Что можно поменять:
            key — название заголовка (str)
            value — значение заголовка (str)
            Примеры заголовков:
                - "Authorization": "Bearer eyJhbGciOiJIUzI1NiIs..."
                - "X-API-Key": "abc123"
                - "Content-Type": "application/json"
        """
        self.session.headers.update({key: value})
        self.logger.info(f"✅ Добавлен заголовок: {key}: {value}")
    
    def clear_headers(self):
        """
        Очистить все заголовки из сессии
        
          КОГДА НУЖНО:
           - Между разными тестами с разными пользователями
           - После теста на выход (logout)
           - Чтобы сбросить авторизацию перед публичными запросами
        
          Копировать в тест:
            from endpoints.user_endpoints import USER_DELETE
            
            # Шаг 1: Очищаем старые заголовки
            client.clear_headers()
            
            # Шаг 2: Делаем запрос без авторизации
            response = client.get("/public/info")
            assert response.status_code == 200
        
          Пример сценария:
            # Тест 1: авторизованный запрос
            client.add_header("Authorization", "Bearer token1")
            response = client.get("/users/me")  # ✅ пойдёт с токеном
            
            # Очищаем перед следующим тестом
            client.clear_headers()
            
            # Тест 2: публичный запрос
            response = client.get("/public/data")  # ✅ без токена
            assert response.status_code == 200
        """
        self.session.headers.clear()
        self.logger.info("✅ Все заголовки очищены")