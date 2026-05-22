"""
Логирование для тестов
====================================

  Что здесь хранится:
   - Настройка логгеров для тестов
   - Автоматическое создание папки для логов
   - Сохранение логов в файл с временной меткой

  Как использовать в тестах:
   from common.logger import setup_logger
   
   logger = setup_logger("test_name")
   logger.info("Сообщение")
   logger.error("Ошибка")
"""

import logging
import os
from datetime import datetime

def setup_logger(test_name: str):
    """
    Настройка логгера для теста
    
      Копировать в тест:
        from common.logger import setup_logger
        logger = setup_logger("test_valid_login")
        logger.info("Начинаем тест")
    
      Что можно поменять:
        test_name — имя теста (str), будет использовано в имени файла лога
    """
    
    # Создаём папку для логов (если её нет)
    log_dir = "results/logs"
    os.makedirs(log_dir, exist_ok=True)
    
    # Формируем имя файла с временной меткой
    timestamp = datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
    log_file = f"{log_dir}/{test_name}_{timestamp}.log"
    
    # Создаём логгер
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)
    
    # Если у логгера уже есть обработчики — не добавляем новые (чтобы не дублировать)
    if not logger.handlers:
        # Обработчик для записи в файл
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        ))
        
        # Обработчик для вывода в консоль
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            '%(levelname)s - %(message)s'
        ))
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger