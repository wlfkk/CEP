# ВКРБ на тему: “Проектирование высоконагруженного отказоустойчивого сервиса рекомендаций в банковских приложениях”

Выполнил студент группы М8О-401Б-21: Филимонов Николай Николаевич

Научный руководитель: Бахиркин Михаил Васильевич

Консультант: Мазаев Артемий Сергеевич

## Структура проекта
Для удобства реализации и анализа проект организован следующим образом:

-  **k8s/**  
Содержит манифесты сущностей kubernetes, требуемые для развертывания всех микросервисов

-  **infra/**  
Содержит стандартную структуру репозитория ansible-скриптов.
В частности, здесь находятся:
    - переменные
    - отдельные задачи
    - полноценные плейбуки
