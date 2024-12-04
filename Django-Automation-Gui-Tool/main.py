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
        global window_x
        txt = self.form.lineEdit.text()
        url = f"{txt}" + f"{text}"
        #os.system(f"start {url}")
        
        window_x = window_designer()
        window_x.show()
        window_x.form_designer.lineEdit.setText(url)
        window_x.form_designer.webEngineView_5.setUrl(url)
        
    
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
#---------------------------x----------------------------------

from PySide6.QtCore import Qt
class window_designer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        from window2 import Ui_designer
        from PySide6.QtWebEngineCore import ( QWebEngineSettings,QWebEngineProfile)
        from PySide6.QtGui import QIcon
        
        self.form_designer = Ui_designer()
        self.form_designer.setupUi(self)
        
        self.resizeEvent = self.on_resize10
        


        self.form_designer.lineEdit.setVisible(True)
        self.form_designer.lineEdit.move(125,1)
        self.form_designer.widget_toolbar.setVisible(True)


        self.form_designer.webEngineView_5.move(0,0)
        
        self.form_designer.widget_toolbar.move(0,0)
        self.form_designer.toolButton_aerrow_left.setVisible(True)
        self.form_designer.toolButton_aerrow_left.move(5,0)
        self.form_designer.toolButton_aerrow_right.setVisible(True)
        self.form_designer.toolButton_aerrow_right.move(30,0)
        self.form_designer.toolButton_refresh.setVisible(True)
        self.form_designer.toolButton_refresh.move(55,0)
        self.form_designer.pushButton_go.setVisible(True)
        self.form_designer.pushButton_go.move(80,0)
        self.form_designer.pushButton_save_page.setVisible(True)
        self.form_designer.pushButton_maximise.setVisible(True)
        self.form_designer.pushButton_go.clicked.connect(self.opener)


        self.form_designer.lineEdit.setStyleSheet("""
            QLineEdit {
                border: 2px solid rgb(0, 0, 0); /* Custom border color */
                border-radius: 8px; /* Optional: Make the corners rounded */
                
                                          
                background-color: rgb(240, 240, 240); /* Background color */
                alternate-background-color: rgb(100, 100, 100); /* Alternate background color */
                selection-background-color: rgb(137, 143, 255); /* Selected text background color */
                selection-color: rgb(0, 0, 0); /* Selected text color */
                color: rgb(0, 0, 0); /* Text color */
            }
        """)


       
        self.form_designer.lineEdit.returnPressed.connect(self.navigate)
    
        

        


        #self.settings = self.form_designer.webEngineView_5.page().profile()
        #self.settings.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        
     

        self.profile = self.form_designer.webEngineView_5.page().profile()
        self.profile.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanAccessClipboard, True)
        self.profile.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanPaste, True)
        #profile.downloadRequested.connect(self.on_downloadRequested)

        #self.form_designer.webEngineView_5.setPage(CustomWebEnginePage(self))
        self.form_designer.webEngineView_5.setZoomFactor(0.8)
       
        profile1 = QWebEngineProfile.defaultProfile()
        profile1.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")




        self.form_designer.toolButton_aerrow_left.clicked.connect(self.form_designer.webEngineView_5.back)
        self.form_designer.toolButton_aerrow_right.clicked.connect(self.form_designer.webEngineView_5.forward)
        self.form_designer.toolButton_refresh.clicked.connect(self.form_designer.webEngineView_5.reload)    
        
        self.form_designer.pushButton_maximise.clicked.connect(self.fulldisplay)
        self.fullscreen = False



    def fulldisplay(self):
        
        if self.fullscreen:
            self.showNormal()
            self.fullscreen = False
        else:
            self.showFullScreen()
            self.fullscreen = True




    def enterEvent(self, event):
        
        # Focus the window when the mouse enters
        self.activateWindow()  # Bring window to the front
        self.setFocus(Qt.OtherFocusReason)  # Set focus explicitly
        super().enterEvent(event)

    def opener(self):
        my_url = self.form_designer.webEngineView_5.url().toString()
        os.system(f"start {my_url}")




    '''def on_downloadRequested(self, download: QWebEngineDownloadRequest):
        # Open file dialog to select download location
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", download.suggestedFileName())
        
        if file_path:
            # Print debug info
            print(f"Download path selected: {file_path}")
            directory = QFileInfo(file_path).absolutePath()
            file_name = QFileInfo(file_path).fileName()

            print(f"Directory: {directory}")
            print(f"File Name: {file_name}")

            if QDir(directory).exists():
                print("Directory exists, proceeding with download.")
            else:
                print("Directory does not exist, creating directory.")
                if QDir().mkpath(directory):
                    print("Directory created successfully.")
                else:
                    print("Failed to create directory.")
                    QMessageBox.critical(self, "Error", f"Failed to create directory: {directory}")
                    return
            
            # Set the download directory and file name
            download.setDownloadDirectory(directory)
            download.setDownloadFileName(file_name)
            download.accept()

            print("Download accepted.")
        else:
            download.cancel()
            print("Download was canceled by the user.")'''

       


    def navigate(self):
        self.form_designer.webEngineView_5.setUrl(self.form_designer.lineEdit.text())
        


    def on_resize10(self, event):
        x,y = self.geometry().width(),self.geometry().height()
        self.form_designer.webEngineView_5.setGeometry(1,23,x-3,y-26)
        self.form_designer.widget_toolbar.setGeometry(0,0,x-2,23)
        self.form_designer.lineEdit.setGeometry(130,0,x-260,22)
        self.form_designer.pushButton_save_page.setGeometry(x-130,1,22,22)
        self.form_designer.pushButton_maximise.setGeometry(x-105,-1,22,22)
    


        
    '''def search(self):
        url = self.form.lineEdit.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.form.webEngineView_5.setUrl(url)'''

    

   

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = window()
    widget.show()
    
    sys.exit(app.exec())