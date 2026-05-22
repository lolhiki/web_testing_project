
---

## 📄 Файл №15: `README.md`

```markdown
# Web Testing Project

Проект для автоматизации веб-тестирования с использованием **Playwright + Pytest**.

---

## 📁 Структура проекта

```
web_testing_project/
│
├── common/                         # Базовые механизмы (настраиваем 1 раз)
│   ├── api_client.py               # Базовый API клиент (requests)
│   ├── api_steps.py                # API методы (get, post, put, delete)
│   ├── ui_steps.py                 # UI методы (click, fill, check_text)
│   ├── logger.py                   # Логирование
│   └── conftest.py                 # Pytest фикстуры
│
├── endpoints/                      # API адреса (как Swagger)
│   ├── user_endpoints.py           # /users, /users/{id}
│   ├── product_endpoints.py        # /products, /products/{id}
│   └── auth_endpoints.py           # /login, /logout
│
├── pages/                          # UI локаторы (для каждой страницы)
│   ├── login_page.py               # Locators + TestData для логина
│   ├── cart_page.py                # Locators для корзины
│   └── product_page.py             # Locators для товара
│
├── config/                         # Глобальные настройки
│   ├── settings.py                 # HEADLESS, таймауты, окружение
│   └── urls.py                     # Базовые URL стендов
│
├── tests/                          # Твои тесты
│   ├── draft_api_test.py           # Шаблон API теста
│   ├── draft_ui_test.py            # Шаблон UI теста
│   ├── api/                        # API тесты
│   │   └── test_users.py
│   └── ui/                         # UI тесты
│       └── test_login.py
│
├── data/                           # Тестовые данные (JSON, CSV)
├── results/                        # Логи и скриншоты
│   ├── logs/
│   └── screenshots/
│
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Установка браузеров Playwright

```bash
playwright install chromium
```

### 3. Запуск тестов

```bash
# Все тесты
pytest tests/ -v -s

# Только API тесты
pytest tests/api/ -v -s

# Только UI тесты
pytest tests/ui/ -v -s

# С маркером
pytest -m smoke -v -s
```

---

## 📝 Как создать новый тест

### UI тест:

1. **Скопируй шаблон:**
   ```bash
   cp tests/draft_ui_test.py tests/ui/test_my_feature.py
   ```

2. **Переименуй класс** (TestUITemplate → TestMyFeature)

3. **Переименуй функцию** (test_example → test_my_scenario)

4. **Добавь шаги** (копируй из `common/ui_steps.py`):
   ```python
   self.ui.go_to_url(Urls.LOGIN_PAGE)
   self.ui.click(Locators.BUTTON)
   self.ui.fill(Locators.INPUT, "text")
   self.ui.check_text(Locators.TEXT, "expected")
   ```

5. **Запусти:**
   ```bash
   pytest tests/ui/test_my_feature.py -v -s
   ```

### API тест:

1. **Скопируй шаблон:**
   ```bash
   cp tests/draft_api_test.py tests/api/test_my_api.py
   ```

2. **Переименуй класс** (TestAPITemplate → TestMyAPI)

3. **Переименуй функцию** (test_example → test_get_data)

4. **Добавь запрос** (копируй из `common/api_steps.py`):
   ```python
   response = self.api.get(USER_GET.format(user_id=1))
   assert response.status_code == 200
   data = response.json()
   ```

5. **Запусти:**
   ```bash
   pytest tests/api/test_my_api.py -v -s
   ```

---

## 📚 Доступные методы

### UI методы (`common/ui_steps.py`)

| Метод | Описание | Пример |
|-------|----------|--------|
| `go_to_url(url)` | Открыть страницу | `self.ui.go_to_url(Urls.LOGIN_PAGE)` |
| `click(selector)` | Кликнуть | `self.ui.click("#submit")` |
| `fill(selector, text)` | Ввести текст | `self.ui.fill("#username", "user")` |
| `get_text(selector)` | Получить текст | `text = self.ui.get_text(".title")` |
| `check_text(selector, expected)` | Проверить текст | `self.ui.check_text(".title", "Products")` |
| `check_element_visible(selector)` | Проверить видимость | `self.ui.check_element_visible(".logo")` |
| `take_screenshot(name)` | Скриншот | `self.ui.take_screenshot("after_login")` |

### API методы (`common/api_steps.py`)

| Метод | Описание | Пример |
|-------|----------|--------|
| `get(endpoint)` | GET запрос | `self.api.get(USER_GET.format(user_id=1))` |
| `post(endpoint, json)` | POST запрос | `self.api.post(USER_CREATE, json=data)` |
| `put(endpoint, json)` | PUT запрос | `self.api.put(USER_UPDATE, json=data)` |
| `delete(endpoint)` | DELETE запрос | `self.api.delete(USER_DELETE)` |

---

## 🌐 Тестовые стенды

| Тип | Стенд | Назначение |
|-----|-------|------------|
| **API** | https://jsonplaceholder.typicode.com | Бесплатное API для тестов |
| **UI** | https://www.saucedemo.com | Тестовый интернет-магазин |

### Учётные данные для UI:

| Логин | Пароль |
|-------|--------|
| `standard_user` | `secret_sauce` |
| `locked_out_user` | `secret_sauce` |

---

## ⚙️ Настройка окружения

### `config/settings.py`:

```python
HEADLESS = False      # True — браузер не виден (для CI)
ENVIRONMENT = "dev"   # dev, staging, prod
WAIT_TIMEOUT = 10
```

### `config/urls.py`:

```python
CURRENT_ENV = "dev"   # Переключение между стендами
```


---

## 📦 Зависимости

```
pytest==8.4.2          # Фреймворк тестирования
playwright==1.40.0     # Браузерная автоматизация
pytest-playwright==0.4.4 # Интеграция Playwright
requests==2.31.0       # HTTP клиент для API
pytest-html==4.1.1     # HTML отчёты
pytest-xdist==3.5.0    # Параллельный запуск
```

---

**Удачного тестирования! 🚀**
```

