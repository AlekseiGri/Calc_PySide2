# PySide2 Project
Примеры проектов, созданных с помощью Qt Designer и библиотеки PySide2. Дизайн создаётся в Qt Designer и сохраняется в .ui файл, который затем конвертируется в .py файл для добавления логики на Python.

## Подготовка и установка на Windows
### 1. Установка Python
Скачайте Python для Windows:

👉 https://www.python.org/downloads/windows/

⚠️ Важно: используйте версию Python не новее 3.10, так как PySide2 поддерживает только старые версии. В моём случае использовалась версия Python 3.10.0.

Во время установки обязательно включите опцию "Add Python to PATH", чтобы можно было запускать Python из терминала.

### 2. Установка PySide2
Откройте терминал и выполните команду:

`pip install PySide2`

### 3. Установка Qt Designer
Скачайте Qt Designer по ссылке:

👉 https://build-system.fman.io/qt-designer-download

Установите программу обычным способом.

## Как работает процесс?
### Шаг 1: Создание интерфейса
Разрабатываем графический интерфейс в Qt Designer и сохраняем его в формате .ui.

### Шаг 2: Конвертация .ui в .py
Откройте терминал и выполните команду:

`pyside2-uic file.ui -o file.py`

⚠️ Убедитесь, что вы находитесь в той же директории, где лежит файл file.ui.

Если команда не распознаётся, можно указать полный путь к pyside2-uic, например:

"C:\Users\username\AppData\Local\Programs\Python\Python310\Scripts\pyside2-uic.exe" file.ui -o file.py
Шаг 3: Запуск
Теперь можно открыть и запустить файл file.py. Готово!

# PySide2 Project
Example projects created using Qt Designer and PySide2 library. The UI design is created in Qt Designer and saved as a .ui file, which is then converted to a .py file for adding Python logic.

## Setup and Installation (Windows)
### 1. Install Python
Download Python for Windows:

👉 https://www.python.org/downloads/windows/

⚠️ Important: Use Python version 3.10 or older, as PySide2 only supports older versions. In my case, I used Python 3.10.0.

During installation, make sure to enable the "Add Python to PATH" option to run Python from the terminal.

### 2. Install PySide2
Open a terminal and run:
`pip install PySide2`

### 3. Install Qt Designer
Download Qt Designer from:

👉 https://build-system.fman.io/qt-designer-download

Install using the standard installation method.

## Workflow
### Step 1: Create Interface
Design the graphical interface in Qt Designer and save it as a .ui file.

### Step 2: Convert .ui to .py
Open a terminal and execute:

`pyside2-uic file.ui -o file.py`

⚠️ Make sure you're in the same directory as your file.ui

If the command isn't recognized, you can specify the full path to pyside2-uic, for example:

"C:\Users\username\AppData\Local\Programs\Python\Python310\Scripts\pyside2-uic.exe" file.ui -o file.py

### Step 3: Run
Now you can open and execute file.py. Done!





