# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import os
import threading
import os,django,time
import pandas
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

import subprocess
   
        
from window1 import Ui_master
class window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_master()
        self.form.setupUi(self)
        
        self.form.pushButton_runserver.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        
        self.form.pushButton_show_databse.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        self.form.pushButton_admin.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        self.form.pushButton_open_shell.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        self.form.pushButton_check.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        self.form.pushButton_create_new_app.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        self.form.pushButton_make_migration.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        
        self.form.pushButton_apply_migration.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        self.form.pushButton_show_migration.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        self.form.pushButton_flush_databse.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        self.form.pushButton_clear.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        self.form.pushButton_open_site.setStyleSheet("QPushButton{background-color: rgb(152, 222, 218);; border: 1px solid cyan; border-radius: 5px; padding: 5px;}"
        "QPushButton:hover{background-color: #e0e0e0; border: 1px solid #aaa;}"
        "QPushButton:pressed{background-color: #ccc; border: 1px solid #777;}")
        
        self.form.pushButton_show_databse.clicked.connect(self.database_show)
        self.form.pushButton_runserver.clicked.connect(self.abhi)
        self.form.pushButton_clear.clicked.connect(self.clear)
        self.form.pushButton_open_site.clicked.connect(lambda: self.open_site(''))
        self.form.pushButton_admin.clicked.connect(lambda: self.open_site('/admin'))
        self.form.pushButton_execute.clicked.connect(self.execute)
        self.form.pushButton_open_shell.clicked.connect(self.shell)
        self.form.pushButton_check.clicked.connect(self.check)
        self.form.pushButton_make_migration.clicked.connect(self.make_migration)
        self.form.pushButton_apply_migration.clicked.connect(self.apply_migration)
        self.form.pushButton_show_migration.clicked.connect(self.show_migration)
        self.form.pushButton_flush_databse.clicked.connect(self.flush_databse)
        
        
    def flush_databse(self):
        os.system('python manage.py flush')
    def show_migration(self):
        os.system('python manage.py showmigrations')
    def apply_migration(self):
        os.system('python manage.py migrate')
    def make_migration(self):
        os.system('python manage.py makemigrations')
    def check(self):
        os.system('python manage.py check')
    def shell(self):
        subprocess.Popen('start cmd /K "py manage.py shell"', shell=True)
    def execute(self):
        
        cmd = self.form.lineEdit_command.text()
        if 'runserver' in cmd:
            self.abhi()
        else:
            
            os.system(f"{cmd}")
    def open_site(self,text):
        txt = self.form.lineEdit.text()
        url = f"{txt}" + f"{text}"
        os.system(f"start {url}")
    
    def clear(self):
        os.system('cls')
        
        
    def abhi(self):
    # Open a new command prompt and run a specific command
        subprocess.Popen('start cmd /K "py manage.py runserver"', shell=True)
        
        
        
    def database_show(self):
        print('----------------------------Django Database----------------------------')
        # Set the correct settings module
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')
        django.setup()
        
        from login.models import User

        users = User.objects.values()
        #for user in users:
        #    print(f"Name: {user.name}, Phone: {user.phone}, Email: {user.email},password:{user.password}")

        print(pandas.DataFrame(list(users)))


        





        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = window()
    widget.show()
    sys.exit(app.exec())