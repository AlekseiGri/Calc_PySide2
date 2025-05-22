pyside2-uic -o new_main_window.py $1
sed -i 's/from PySide2.QtWidgets import \*/from PySide2.QtWidgets import \*\nfrom event_view import \*\n/' new_main_window.py
sed -i 's/QGraphicsView/EventView/g' new_main_window.py
