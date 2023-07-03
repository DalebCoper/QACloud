# readme
Проект решения тестового задания QACloud  
https://github.com/QACloudCamp/test-assignment
# Процесс тестирования нового функционала
## Функциональное тестирование:
- Создать таблицу, заполнив все необходимые данные корректными значениями.
- Проверить создается ли база данных без введенного одного или двух обязательных полей.
- Ввести некорректные данные в вводимые поля.
- Попробовать создать одинаковые базы данных.
- Создать базу данных с минимальным, максимальным и более чем максимальным размером.
## Интеграционное тестирование 
- Удостовериться, что при создании базы в веб-интерфейсе она действительно создается на сервере.
- Проверить взаимодействие с другими функциями облачного сервиса.
## Протестировать производительность базы данных:
- Попробовать создать несколько баз данных одновременно.
- Проверить скорость создания баз с различным размером данных.
- Проверить время отклика на запросы веб-интерфейса.
# Автоматизация тестирования API. Часть 1
Инструкция по поднятию автотестов:
1. Скачать папку "Автоматизация тестирования API" из этого репозитория.
2. Необходимо установить python 3+, а также библиотеки pytest, requests и jsonschema.
Для установки библиотеки необходимо в терминал прописать pip instal pytest requests jsonschema.
3. Запустить тест выполнив команду в терминале:
pytest "путь:\к\папке\Автоматизация тестирования API\test.py"

# Автоматизация тестирования API. Часть 2
Для запуска dockerfile необходимо прописать в консоле папки с автотестами:
- docker build -t apitest .  

После создания образа в контейнере, запустить команду:  

    
          
            
    

          
          Expand Down
    
    
  
- docker run --rm pytest-image
