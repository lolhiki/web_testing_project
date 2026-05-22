"""
User API Endpoints — все адреса для работы с пользователями
====================================

  Что здесь хранится:
   - Все эндпоинты API для пользователей
   - Используются в API тестах вместе с api_steps.py

  Как использовать в тестах:
   from endpoints.user_endpoints import USER_GET, USER_CREATE, USER_UPDATE, USER_DELETE
   
   response = self.api.get(USER_GET.format(user_id=1))
   response = self.api.post(USER_CREATE, json=new_user)
   response = self.api.put(USER_UPDATE.format(user_id=1), json=update_data)
   response = self.api.delete(USER_DELETE.format(user_id=1))

  Базовый URL берётся из config/settings.py
   Полный URL = base_url + endpoint
"""

# ============================================================
# USER ENDPOINTS
# ============================================================

# GET — получение данных
USER_GET = "/users/{user_id}"           # получить пользователя по ID
USER_LIST = "/users"                     # получить список всех пользователей

# POST — создание
USER_CREATE = "/users"                   # создать нового пользователя

# PUT — полное обновление
USER_UPDATE = "/users/{user_id}"         # обновить пользователя целиком

# PATCH — частичное обновление
USER_PATCH = "/users/{user_id}"          # обновить часть данных пользователя

# DELETE — удаление
USER_DELETE = "/users/{user_id}"         # удалить пользователя

# ============================================================
# ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ В ТЕСТАХ
# ============================================================

# 📋 GET запрос:
#    response = self.api.get(USER_GET.format(user_id=1))
#    assert response.status_code == 200
#    data = response.json()
#    assert data["id"] == 1

# 📋 POST запрос:
#    new_user = {"name": "Test User", "email": "test@example.com"}
#    response = self.api.post(USER_CREATE, json=new_user)
#    assert response.status_code == 201

# 📋 PUT запрос:
#    update_data = {"name": "New Name", "email": "new@example.com"}
#    response = self.api.put(USER_UPDATE.format(user_id=1), json=update_data)
#    assert response.status_code == 200

# 📋 DELETE запрос:
#    response = self.api.delete(USER_DELETE.format(user_id=1))
#    assert response.status_code in [200, 204]