# PySide2 Project
Примеры проектов, созданных с помощью Qt Designer и библиотеки PySide2. Дизайн создаётся в Qt Designer и сохраняется в .ui файл, который затем конвертируется в .py файл для добавления логики на Python.

Подготовка и установка на Windows
1. Установка Python
Скачайте Python для Windows:

👉 https://www.python.org/downloads/windows/

⚠️ Важно: используйте версию Python не новее 3.10, так как PySide2 поддерживает только старые версии. В моём случае использовалась версия Python 3.10.0.

Во время установки обязательно включите опцию "Add Python to PATH", чтобы можно было запускать Python из терминала.

2. Установка PySide2
Откройте терминал и выполните команду:

pip install PySide2

3. Установка Qt Designer
Скачайте Qt Designer по ссылке:

👉 https://build-system.fman.io/qt-designer-download

Установите программу обычным способом.

Как работает процесс?
Шаг 1: Создание интерфейса
Разрабатываем графический интерфейс в Qt Designer и сохраняем его в формате .ui.

Шаг 2: Конвертация .ui в .py
Откройте терминал и выполните команду:

pyside2-uic file.ui -o file.py

⚠️ Убедитесь, что вы находитесь в той же директории, где лежит файл file.ui.

Если команда не распознаётся, можно указать полный путь к pyside2-uic, например:

"C:\Users\username\AppData\Local\Programs\Python\Python310\Scripts\pyside2-uic.exe" file.ui -o file.py
Шаг 3: Запуск
Теперь можно открыть и запустить файл file.py. Готово!
