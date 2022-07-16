# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './main_app_windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setProperty("CurrentFilePath", "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 531))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Key")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plist_xmlview = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.plist_xmlview.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.plist_xmlview.setObjectName("plist_xmlview")
        self.verticalLayout_2.addWidget(self.plist_xmlview)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setDefaultUp(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_recent = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_recent.setObjectName("menuOpen_recent")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSort = QtWidgets.QMenu(self.menuEdit)
        self.menuSort.setObjectName("menuSort")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menumacOS_Plits_tools = QtWidgets.QMenu(self.menuHelp)
        self.menumacOS_Plits_tools.setObjectName("menumacOS_Plits_tools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_new = QtWidgets.QAction(MainWindow)
        self.actionCreate_new.setObjectName("actionCreate_new")
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionCreat_tempate = QtWidgets.QAction(MainWindow)
        self.actionCreat_tempate.setObjectName("actionCreat_tempate")
        self.actionPrint_XML = QtWidgets.QAction(MainWindow)
        self.actionPrint_XML.setObjectName("actionPrint_XML")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPaste_as_plaint_text = QtWidgets.QAction(MainWindow)
        self.actionPaste_as_plaint_text.setObjectName("actionPaste_as_plaint_text")
        self.actionAdd_plist_group = QtWidgets.QAction(MainWindow)
        self.actionAdd_plist_group.setObjectName("actionAdd_plist_group")
        self.actionAdd_plist_key = QtWidgets.QAction(MainWindow)
        self.actionAdd_plist_key.setObjectName("actionAdd_plist_key")
        self.actionDelete_selected = QtWidgets.QAction(MainWindow)
        self.actionDelete_selected.setObjectName("actionDelete_selected")
        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionReplace = QtWidgets.QAction(MainWindow)
        self.actionReplace.setObjectName("actionReplace")
        self.action_by_name = QtWidgets.QAction(MainWindow)
        self.action_by_name.setObjectName("action_by_name")
        self.action_by_key_types = QtWidgets.QAction(MainWindow)
        self.action_by_key_types.setObjectName("action_by_key_types")
        self.actionVisual_editor = QtWidgets.QAction(MainWindow)
        self.actionVisual_editor.setObjectName("actionVisual_editor")
        self.actionXML_editor = QtWidgets.QAction(MainWindow)
        self.actionXML_editor.setObjectName("actionXML_editor")
        self.actionSplit_view = QtWidgets.QAction(MainWindow)
        self.actionSplit_view.setObjectName("actionSplit_view")
        self.actionHide = QtWidgets.QAction(MainWindow)
        self.actionHide.setObjectName("actionHide")
        self.actionChange_size = QtWidgets.QAction(MainWindow)
        self.actionChange_size.setObjectName("actionChange_size")
        self.actionPyPLIST_Editor_Documentation = QtWidgets.QAction(MainWindow)
        self.actionPyPLIST_Editor_Documentation.setObjectName("actionPyPLIST_Editor_Documentation")
        self.actionplist_documentation = QtWidgets.QAction(MainWindow)
        self.actionplist_documentation.setObjectName("actionplist_documentation")
        self.actionLaunch_Agents_Daemons_tool = QtWidgets.QAction(MainWindow)
        self.actionLaunch_Agents_Daemons_tool.setObjectName("actionLaunch_Agents_Daemons_tool")
        self.actionCLOVER_Bootloader_config_tool = QtWidgets.QAction(MainWindow)
        self.actionCLOVER_Bootloader_config_tool.setObjectName("actionCLOVER_Bootloader_config_tool")
        self.menuOpen_recent.addSeparator()
        self.menuFile.addAction(self.actionCreate_new)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.menuOpen_recent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionCreat_tempate)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint_XML)
        self.menuSort.addAction(self.action_by_name)
        self.menuSort.addAction(self.action_by_key_types)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionPaste_as_plaint_text)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAdd_plist_group)
        self.menuEdit.addAction(self.actionAdd_plist_key)
        self.menuEdit.addAction(self.actionDelete_selected)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionReplace)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuSort.menuAction())
        self.menuView.addAction(self.actionVisual_editor)
        self.menuView.addAction(self.actionSplit_view)
        self.menuView.addAction(self.actionXML_editor)
        self.menuWindow.addAction(self.actionHide)
        self.menuWindow.addAction(self.actionChange_size)
        self.menumacOS_Plits_tools.addAction(self.actionLaunch_Agents_Daemons_tool)
        self.menumacOS_Plits_tools.addAction(self.actionCLOVER_Bootloader_config_tool)
        self.menuHelp.addAction(self.actionPyPLIST_Editor_Documentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionplist_documentation)
        self.menuHelp.addAction(self.menumacOS_Plits_tools.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyPLIST Editor"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Value"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_recent.setTitle(_translate("MainWindow", "Open recent..."))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSort.setTitle(_translate("MainWindow", "Sort"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menumacOS_Plits_tools.setTitle(_translate("MainWindow", "macOS Plits tools"))
        self.actionCreate_new.setText(_translate("MainWindow", "Create new"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionCreat_tempate.setText(_translate("MainWindow", "Creat tempate"))
        self.actionPrint_XML.setText(_translate("MainWindow", "Print XML"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste_as_plaint_text.setText(_translate("MainWindow", "Paste as plaint text"))
        self.actionAdd_plist_group.setText(_translate("MainWindow", "Add plist group"))
        self.actionAdd_plist_key.setText(_translate("MainWindow", "Add plist key"))
        self.actionDelete_selected.setText(_translate("MainWindow", "Delete selected"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionReplace.setText(_translate("MainWindow", "Replace"))
        self.action_by_name.setText(_translate("MainWindow", "by name"))
        self.action_by_key_types.setText(_translate("MainWindow", "by key types"))
        self.actionVisual_editor.setText(_translate("MainWindow", "Visual handlers"))
        self.actionXML_editor.setText(_translate("MainWindow", "XML handlers"))
        self.actionSplit_view.setText(_translate("MainWindow", "Split view"))
        self.actionHide.setText(_translate("MainWindow", "Hide"))
        self.actionChange_size.setText(_translate("MainWindow", "Change size"))
        self.actionPyPLIST_Editor_Documentation.setText(_translate("MainWindow", "PyPLIST Editor Documentation"))
        self.actionplist_documentation.setText(_translate("MainWindow", "Plist Documentation"))
        self.actionLaunch_Agents_Daemons_tool.setText(_translate("MainWindow", "Launch Agents/Daemons config tool"))
        self.actionCLOVER_Bootloader_config_tool.setText(_translate("MainWindow", "CLOVER Bootloader config tool"))