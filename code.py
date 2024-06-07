import requests, time, qdarktheme
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from github import Github, Auth
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QListView, QFileDialog, QMessageBox
from PyQt6.QtGui import QStandardItem
from PyQt6.QtCore import Qt

class CustomListView(QListView):
    def mousePressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            # If CTRL is pressed, allow multi-selection
            self.setSelectionMode(QListView.SelectionMode.MultiSelection)
        else:
            # Otherwise, enforce single selection
            self.setSelectionMode(QListView.SelectionMode.SingleSelection)
        super().mousePressEvent(event)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 588)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(0, 0, 901, 561))
        self.TabWidget.setAutoFillBackground(False)
        self.TabWidget.setObjectName("TabWidget")
        self.QRadarTab = QtWidgets.QWidget()
        self.QRadarTab.setObjectName("QRadarTab")
        self.ImportButton = QtWidgets.QPushButton(parent=self.QRadarTab)
        self.ImportButton.setGeometry(QtCore.QRect(630, 170, 81, 31))
        self.ImportButton.setStyleSheet("")
        self.ImportButton.setObjectName("ImportButton")
        self.RuleView = CustomListView(parent=self.QRadarTab)
        self.RuleView.setGeometry(QtCore.QRect(10, 120, 501, 341))
        self.RuleView.setAutoFillBackground(False)
        self.RuleView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.RuleView.setObjectName("RuleView")
        self.ExportButton = QtWidgets.QPushButton(parent=self.QRadarTab)
        self.ExportButton.setGeometry(QtCore.QRect(630, 290, 81, 31))
        self.ExportButton.setStyleSheet("")
        self.ExportButton.setObjectName("ExportButton")
        self.SECTokenEntry = QtWidgets.QLineEdit(parent=self.QRadarTab)
        self.SECTokenEntry.setGeometry(QtCore.QRect(10, 40, 321, 20))
        self.SECTokenEntry.setAutoFillBackground(False)
        self.SECTokenEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SECTokenEntry.setObjectName("SECTokenEntry")
        self.SECTokenLabel = QtWidgets.QLabel(parent=self.QRadarTab)
        self.SECTokenLabel.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.SECTokenLabel.setAutoFillBackground(False)
        self.SECTokenLabel.setObjectName("SECTokenLabel")
        self.FileSelectionLine = QtWidgets.QLineEdit(parent=self.QRadarTab)
        self.FileSelectionLine.setGeometry(QtCore.QRect(530, 140, 261, 21))
        self.FileSelectionLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FileSelectionLine.setObjectName("FileSelectionLine")
        self.BrowseButton = QtWidgets.QPushButton(parent=self.QRadarTab)
        self.BrowseButton.setEnabled(True)
        self.BrowseButton.setGeometry(QtCore.QRect(800, 140, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BrowseButton.setFont(font)
        self.BrowseButton.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.BrowseButton.setFlat(False)
        self.BrowseButton.setObjectName("BrowseButton")
        self.GetRulesButton = QtWidgets.QPushButton(parent=self.QRadarTab)
        self.GetRulesButton.setGeometry(QtCore.QRect(210, 470, 81, 31))
        self.GetRulesButton.setStyleSheet("")
        self.GetRulesButton.setObjectName("GetRulesButton")
        self.FiletoImportLabel = QtWidgets.QLabel(parent=self.QRadarTab)
        self.FiletoImportLabel.setGeometry(QtCore.QRect(530, 120, 71, 16))
        self.FiletoImportLabel.setObjectName("FiletoImportLabel")
        self.QRadarURL = QtWidgets.QLineEdit(parent=self.QRadarTab)
        self.QRadarURL.setGeometry(QtCore.QRect(10, 90, 321, 20))
        self.QRadarURL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.QRadarURL.setObjectName("QRadarURL")
        self.QRadarURLLabel = QtWidgets.QLabel(parent=self.QRadarTab)
        self.QRadarURLLabel.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.QRadarURLLabel.setObjectName("QRadarURLLabel")
        self.FileSelectionLine_Export = QtWidgets.QLineEdit(parent=self.QRadarTab)
        self.FileSelectionLine_Export.setGeometry(QtCore.QRect(530, 260, 261, 20))
        self.FileSelectionLine_Export.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FileSelectionLine_Export.setObjectName("FileSelectionLine_Export")
        self.BrowseButton_Export = QtWidgets.QPushButton(parent=self.QRadarTab)
        self.BrowseButton_Export.setEnabled(True)
        self.BrowseButton_Export.setGeometry(QtCore.QRect(800, 260, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BrowseButton_Export.setFont(font)
        self.BrowseButton_Export.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.BrowseButton_Export.setFlat(False)
        self.BrowseButton_Export.setObjectName("BrowseButton_Export")
        self.ExportLocationLabel = QtWidgets.QLabel(parent=self.QRadarTab)
        self.ExportLocationLabel.setGeometry(QtCore.QRect(530, 240, 91, 16))
        self.ExportLocationLabel.setObjectName("ExportLocationLabel")
        self.TabWidget.addTab(self.QRadarTab, "")
        self.GithubTab = QtWidgets.QWidget()
        self.GithubTab.setObjectName("GithubTab")
        self.GithubRulesView = QtWidgets.QListView(parent=self.GithubTab)
        self.GithubRulesView.setGeometry(QtCore.QRect(260, 60, 311, 311))
        self.GithubRulesView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GithubRulesView.setObjectName("GithubRulesView")
        self.ImportToQRadarButton = QtWidgets.QPushButton(parent=self.GithubTab)
        self.ImportToQRadarButton.setGeometry(QtCore.QRect(580, 60, 131, 31))
        self.ImportToQRadarButton.setObjectName("ImportToQRadarButton")
        self.GithubRuleDescription = QtWidgets.QTextBrowser(parent=self.GithubTab)
        self.GithubRuleDescription.setGeometry(QtCore.QRect(130, 380, 571, 141))
        self.GithubRuleDescription.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GithubRuleDescription.setReadOnly(True)
        self.GithubRuleDescription.setObjectName("GithubRuleDescription")
        self.DescriptionLabel = QtWidgets.QLabel(parent=self.GithubTab)
        self.DescriptionLabel.setGeometry(QtCore.QRect(130, 360, 61, 16))
        self.DescriptionLabel.setObjectName("DescriptionLabel")
        self.TacticLabel = QtWidgets.QLabel(parent=self.GithubTab)
        self.TacticLabel.setGeometry(QtCore.QRect(580, 210, 301, 16))
        self.TacticLabel.setObjectName("TacticLabel")
        self.TechniqueLabel = QtWidgets.QLabel(parent=self.GithubTab)
        self.TechniqueLabel.setGeometry(QtCore.QRect(580, 230, 301, 16))
        self.TechniqueLabel.setObjectName("TechniqueLabel")
        self.SubtechniqueLabel = QtWidgets.QLabel(parent=self.GithubTab)
        self.SubtechniqueLabel.setGeometry(QtCore.QRect(580, 250, 301, 16))
        self.SubtechniqueLabel.setObjectName("SubtechniqueLabel")
        self.AvailableRulesLabel = QtWidgets.QLabel(parent=self.GithubTab)
        self.AvailableRulesLabel.setGeometry(QtCore.QRect(260, 40, 81, 16))
        self.AvailableRulesLabel.setObjectName("AvailableRulesLabel")
        self.RequiredTelemetryMainLabel = QtWidgets.QLabel(parent=self.GithubTab)
        self.RequiredTelemetryMainLabel.setGeometry(QtCore.QRect(580, 290, 301, 16))
        self.RequiredTelemetryMainLabel.setObjectName("RequiredTelemetryMainLabel")
        self.TelemetryLabel1 = QtWidgets.QLabel(parent=self.GithubTab)
        self.TelemetryLabel1.setGeometry(QtCore.QRect(580, 310, 121, 16))
        self.TelemetryLabel1.setText("")
        self.TelemetryLabel1.setObjectName("TelemetryLabel1")
        self.TelemetryLabel2 = QtWidgets.QLabel(parent=self.GithubTab)
        self.TelemetryLabel2.setGeometry(QtCore.QRect(580, 330, 121, 16))
        self.TelemetryLabel2.setText("")
        self.TelemetryLabel2.setObjectName("TelemetryLabel2")
        self.TelemetryLabel3 = QtWidgets.QLabel(parent=self.GithubTab)
        self.TelemetryLabel3.setGeometry(QtCore.QRect(580, 350, 121, 16))
        self.TelemetryLabel3.setText("")
        self.TelemetryLabel3.setObjectName("TelemetryLabel3")
        self.GithubTokenLabel = QtWidgets.QLabel(parent=self.GithubTab)
        self.GithubTokenLabel.setGeometry(QtCore.QRect(90, 50, 71, 16))
        self.GithubTokenLabel.setObjectName("GithubTokenLabel")
        self.GithubTokenLineEdit = QtWidgets.QLineEdit(parent=self.GithubTab)
        self.GithubTokenLineEdit.setGeometry(QtCore.QRect(20, 70, 211, 20))
        self.GithubTokenLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GithubTokenLineEdit.setObjectName("GithubTokenLineEdit")
        self.GithubAuthenticateButton = QtWidgets.QPushButton(parent=self.GithubTab)
        self.GithubAuthenticateButton.setGeometry(QtCore.QRect(70, 160, 111, 23))
        self.GithubAuthenticateButton.setObjectName("GithubAuthenticateButton")
        self.RepoNameLine = QtWidgets.QLineEdit(parent=self.GithubTab)
        self.RepoNameLine.setGeometry(QtCore.QRect(20, 130, 211, 20))
        self.RepoNameLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.RepoNameLine.setObjectName("RepoNameLine")
        self.RepoNameLabel = QtWidgets.QLabel(parent=self.GithubTab)
        self.RepoNameLabel.setGeometry(QtCore.QRect(90, 110, 71, 16))
        self.RepoNameLabel.setObjectName("RepoNameLabel")
        self.TabWidget.addTab(self.GithubTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        app.setStyle("Fusion")
        app.setStyleSheet("""
        QLineEdit, QTextEdit, QPlainTextEdit, QListView {
            color: #2E2E2E; /* Dark color for user input text */
        }
    """)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BrowseButton.clicked.connect(self.browseFiles)
        self.BrowseButton_Export.clicked.connect(self.browseFilesExport)
        self.GetRulesButton.clicked.connect(self.getRules)  
        self.ExportButton.clicked.connect(self.exportRules)
        self.ImportButton.clicked.connect(self.importRules)
        self.GithubAuthenticateButton.clicked.connect(self.github)
        self.ImportToQRadarButton.clicked.connect(self.importRulesFromGithub)


        self.model = QtGui.QStandardItemModel(self.RuleView)
        self.githubModel = QtGui.QStandardItemModel(self.GithubRulesView)
        self.RuleView.setModel(self.model)
        self.GithubRulesView.setModel(self.githubModel)
        self.GithubRulesView.selectionModel().selectionChanged.connect(self.on_directory_selected)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QRadar Rule Manager"))
        self.ImportButton.setText(_translate("MainWindow", "Import"))
        self.ExportButton.setText(_translate("MainWindow", "Export"))
        self.SECTokenLabel.setText(_translate("MainWindow", "SEC Token"))
        self.BrowseButton.setText(_translate("MainWindow", "Browse"))
        self.GetRulesButton.setText(_translate("MainWindow", "Get Rules"))
        self.FiletoImportLabel.setText(_translate("MainWindow", "File to import"))
        self.QRadarURLLabel.setText(_translate("MainWindow", "QRadar URL"))
        self.BrowseButton_Export.setText(_translate("MainWindow", "Browse"))
        self.ExportLocationLabel.setText(_translate("MainWindow", "Export Location"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.QRadarTab), _translate("MainWindow", "QRadar"))
        self.ImportToQRadarButton.setText(_translate("MainWindow", "Import to QRadar"))
        self.DescriptionLabel.setText(_translate("MainWindow", "Description"))
        self.TacticLabel.setText(_translate("MainWindow", "Tactic"))
        self.TechniqueLabel.setText(_translate("MainWindow", "Technique"))
        self.SubtechniqueLabel.setText(_translate("MainWindow", "Sub-technique"))
        self.AvailableRulesLabel.setText(_translate("MainWindow", "Available Rules"))
        self.RequiredTelemetryMainLabel.setText(_translate("MainWindow", "Required Telemetry"))
        self.GithubTokenLabel.setText(_translate("MainWindow", "Github Token"))
        self.GithubAuthenticateButton.setText(_translate("MainWindow", "Authenticate"))
        self.RepoNameLabel.setText(_translate("MainWindow", "Repo Name"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.GithubTab), _translate("MainWindow", "Github"))

    def showMessageBox(self, title, message):
          msgBox = QMessageBox()
          msgBox.setWindowTitle(title)
          msgBox.setText(message)
          msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
          msgBox.exec()

    def browseFiles(self):
        fileName , _ = QFileDialog.getOpenFileName(None, "Select File", "", "ZIP Files (*.zip)")
        if fileName:
                self.FileSelectionLine.setText(fileName)  # Display the selected file path in the QLineEdit
    def browseFilesExport(self):
        fileName = QFileDialog.getExistingDirectory(None, "Select Directory")
        if fileName:
                self.FileSelectionLine_Export.setText(fileName)  # Display the selected file path in the QLineEdit

    def github(self):
        self.auth = Auth.Token(self.GithubTokenLineEdit.text())
        self.g = Github(auth=self.auth)
        self.repo =  self.g.get_user().get_repo(self.RepoNameLine.text())
        contents = self.repo.get_contents("")
        while len(contents) > 1:
                content_item = contents.pop(0)
                if content_item.type == "dir":
                        item = QStandardItem(content_item.name)
                        self.githubModel.appendRow(item)

    def on_directory_selected(self, selected):
        
        for index in selected.indexes():
            # Get the selected directory path
            directory_path = self.githubModel.itemFromIndex(index).text()
            
            # Get the contents of the selected directory
            contents = self.repo.get_contents(directory_path)
            

            for content_item in contents:
                if content_item.name == "Description.md":
                    # Read the content of Description.md
                    description_content = content_item.decoded_content.decode('utf-8')
                    # Set the text in GithubRuleDescription
                    self.GithubRuleDescription.setText(description_content)
                if content_item.name == "README.md":
                    readme_content = content_item.decoded_content.decode('utf-8')
                    readme_content_lines = readme_content.splitlines()
                    # We are incrementing the index by 2 everytime to skip the newlines
                    self.TacticLabel.setText(readme_content_lines[0])
                    self.TechniqueLabel.setText(readme_content_lines[2])
                    self.SubtechniqueLabel.setText(readme_content_lines[4])
                    self.RequiredTelemetryMainLabel.setText(readme_content_lines[6])
                    
    def buildRequest(self):
            BASE_URL = self.QRadarURL.text()
            header = {
                'SEC': self.SECTokenEntry.text(),
                'Content-type':'application/json',
                'accept':'application/json'
            }  

            r = requests.get(BASE_URL+'/api/analytics/rules?fields=name,enabled,id', headers=header, verify=False)
            PRE = r.json()
            return PRE

    def getRules(self):
                response = self.buildRequest()
                rules = []
                for rule in response:
                        rules.append(rule['name'])
        
                # Insert rules into the listbox
                for rule in rules:
                        item = QStandardItem(rule)
                        self.model.appendRow(item)

    def importRulesGithub(self,file_name):
        BASE_URL = self.QRadarURL.text()
        headers = {
                'SEC': self.SECTokenEntry.text(),
                'Content-Type': 'application/zip',
                'Version': '20.0',
                'Accept': 'application/json',
        }

        params = {
                'action_type': 'INSTALL',
                'overwrite': 'true' # Change this to 'false' if you want to preserve existing items
        }


        with open(file_name, 'rb') as f:
                data = f.read()
                f.close()
              

        response = requests.post(BASE_URL+'/api/config/extension_management/extensions', data=data, headers=headers,verify=False)
        response_body = response.json()
        app_id = str(response_body['id'])
        

        print("Extension uploaded successfully with ID: " + app_id)

        url_install = BASE_URL+'/api/config/extension_management/extensions/' + app_id
        response_install = requests.post(url_install, headers=headers, params=params, verify=False)
        response_install_body = response_install.json()
        status_location = response_install_body["status_location"]

        response_install = requests.get(status_location, headers=headers, verify=False)
        response_install_body = response_install.json()

        self.showMessageBox("Installing", "Installation in-progress...")
        while response_install_body["status"] != "COMPLETED":
                response_install = requests.get(status_location, headers=headers, verify=False)
                response_install_body = response_install.json()
                
        self.showMessageBox("Completed", "Sucessfully Installed")
    def importRules(self):
        BASE_URL = self.QRadarURL.text()
        headers = {
                'SEC': self.SECTokenEntry.text(),
                'Content-Type': 'application/zip',
                'Version': '20.0',
                'Accept': 'application/json',
        }

        params = {
                'action_type': 'INSTALL',
                'overwrite': 'true' # Change this to 'false' if you want to preserve existing items
        }


        with open(self.FileSelectionLine.text(), 'rb') as f:
                data = f.read()
                f.close()
              
        response = requests.post(BASE_URL+'/api/config/extension_management/extensions', data=data, headers=headers,verify=False)
        response_body = response.json()
        app_id = str(response_body['id'])

        print("Extension uploaded successfully with ID: " + app_id)

        url_install = BASE_URL+'/api/config/extension_management/extensions/' + app_id
        response_install = requests.post(url_install, headers=headers, params=params, verify=False)
        response_install_body = response_install.json()
        status_location = response_install_body["status_location"]

        response_install = requests.get(status_location, headers=headers, verify=False)
        response_install_body = response_install.json()

        self.showMessageBox("Installing", "Installation in-progress...")
        while response_install_body["status"] != "COMPLETED":
                response_install = requests.get(status_location, headers=headers, verify=False)
                response_install_body = response_install.json()
                
        self.showMessageBox("Completed", "Sucessfully Installed")

    def exportRules(self):
        response = self.buildRequest()
        BASE_URL = self.QRadarURL.text()
        SEC_TOKEN = self.SECTokenEntry.text()

        headers_json = {
                'SEC': SEC_TOKEN,
                'Content-type': 'application/json',
                'accept': 'application/json'
        }

        headers_zip = {
                'SEC': SEC_TOKEN,
                'Content-type': 'application/zip',
                'accept': 'application/zip'
        }

        selected_indexes = self.RuleView.selectedIndexes()
        selected_items = [self.model.itemFromIndex(index).text() for index in selected_indexes]
        selected_values_ids = [
                str(item['id'])
                for name in selected_items
                for item in response
                if item['name'].strip() == name.strip()
        ]
        
        data = str({
                "export_contents": [
                { 
                        "content_item_ids": selected_values_ids, 
                        "content_type": "CUSTOM_RULES", 
                        "related_content": [ { "content_type": "FGROUP_LINKS"} ] 
                        }
                ]
                }
        )
        try:
                export_response = requests.post(
                f'{BASE_URL}/api/config/extension_management/extension_export_tasks',
                data=data,
                headers=headers_json,
                verify=False
                )
                export_response.raise_for_status()
                task_id = export_response.json().get('task_id')

                task_status_url = f'{BASE_URL}/api/config/extension_management/extensions_task_status/{task_id}'
                while True:
                        status_response = requests.get(task_status_url, headers=headers_json, verify=False)
                        status_response.raise_for_status()
                        status = status_response.json().get('status')
                        if status == "COMPLETED":
                                break
                time.sleep(1)

                download_url = f'{BASE_URL}/api/config/extension_management/extension_export_tasks/{task_id}/extension_export'
                download_response = requests.get(download_url, headers=headers_zip, verify=False)
                download_response.raise_for_status()

                with open(self.FileSelectionLine_Export.text() + '\\output.zip', 'wb') as file:
                        file.write(download_response.content)

                self.showMessageBox("Export Complete", "Export rules have been saved to output.zip")
                

        except requests.RequestException as e:
                self.showMessageBox("Export Failed", str(e))

    def importRulesFromGithub(self):
        if self.QRadarURL.text() == "":
              self.showMessageBox("Error", "QRadar URL Must not be empty!")
        else:
                selected_indexes = self.GithubRulesView.selectionModel().selectedIndexes()
                if selected_indexes:
                        selected_item = self.githubModel.itemFromIndex(selected_indexes[0]).text()
                        contents = self.repo.get_contents(selected_item)
                        for item in contents:
                                if item.type == "file" and item.name.endswith(".zip"):
                                        download_url = item.download_url
                                        response = requests.get(download_url)
                                        if response.status_code == 200:
                                                file_name = item.name
                                                with open(file_name, 'wb') as file:
                                                        file.write(response.content)
                                                        self.importRulesGithub(file_name)

            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    qdarktheme.load_stylesheet("dark")
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
 