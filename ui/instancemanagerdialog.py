# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instancemanagerdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QVBoxLayout, QWidget)
import ui.resources_rc

class Ui_InstanceManagerDialog(object):
    def setupUi(self, InstanceManagerDialog):
        if not InstanceManagerDialog.objectName():
            InstanceManagerDialog.setObjectName(u"InstanceManagerDialog")
        InstanceManagerDialog.resize(884, 539)
        self.verticalLayout_6 = QVBoxLayout(InstanceManagerDialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_8 = QWidget(InstanceManagerDialog)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.createNew = QPushButton(self.widget_8)
        self.createNew.setObjectName(u"createNew")
        icon = QIcon()
        icon.addFile(u":/MO/gui/add", QSize(), QIcon.Normal, QIcon.Off)
        self.createNew.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.createNew)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.whatis = QLabel(self.widget_8)
        self.whatis.setObjectName(u"whatis")
        self.whatis.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.whatis)


        self.verticalLayout_6.addWidget(self.widget_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_4 = QWidget(InstanceManagerDialog)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.widget_4)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget_2 = QWidget(self.splitter)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.list = QListView(self.widget_2)
        self.list.setObjectName(u"list")
        self.list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.list.setResizeMode(QListView.Adjust)
        self.list.setUniformItemSizes(True)

        self.verticalLayout.addWidget(self.list)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.filter = QLineEdit(self.widget_5)
        self.filter.setObjectName(u"filter")

        self.horizontalLayout_4.addWidget(self.filter)


        self.verticalLayout.addWidget(self.widget_5)

        self.splitter.addWidget(self.widget_2)
        self.widget_3 = QWidget(self.splitter)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout = QGridLayout(self.widget_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.name = QLineEdit(self.widget_7)
        self.name.setObjectName(u"name")
        self.name.setReadOnly(True)

        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.exploreLocation = QPushButton(self.widget_7)
        self.exploreLocation.setObjectName(u"exploreLocation")

        self.gridLayout.addWidget(self.exploreLocation, 4, 2, 1, 1)

        self.label_8 = QLabel(self.widget_7)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.gameName = QLineEdit(self.widget_7)
        self.gameName.setObjectName(u"gameName")
        self.gameName.setReadOnly(True)

        self.gridLayout.addWidget(self.gameName, 6, 1, 1, 1)

        self.location = QLineEdit(self.widget_7)
        self.location.setObjectName(u"location")
        self.location.setReadOnly(True)

        self.gridLayout.addWidget(self.location, 4, 1, 1, 1)

        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.rename = QPushButton(self.widget_7)
        self.rename.setObjectName(u"rename")

        self.gridLayout.addWidget(self.rename, 0, 2, 1, 1)

        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)

        self.label_6 = QLabel(self.widget_7)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.baseDirectory = QLineEdit(self.widget_7)
        self.baseDirectory.setObjectName(u"baseDirectory")
        self.baseDirectory.setReadOnly(True)

        self.gridLayout.addWidget(self.baseDirectory, 5, 1, 1, 1)

        self.exploreBaseDirectory = QPushButton(self.widget_7)
        self.exploreBaseDirectory.setObjectName(u"exploreBaseDirectory")

        self.gridLayout.addWidget(self.exploreBaseDirectory, 5, 2, 1, 1)

        self.gameDir = QLineEdit(self.widget_7)
        self.gameDir.setObjectName(u"gameDir")
        self.gameDir.setReadOnly(True)

        self.gridLayout.addWidget(self.gameDir, 7, 1, 1, 1)

        self.exploreGame = QPushButton(self.widget_7)
        self.exploreGame.setObjectName(u"exploreGame")

        self.gridLayout.addWidget(self.exploreGame, 7, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.widget_9 = QWidget(self.widget_3)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout = QHBoxLayout(self.widget_9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.convertToPortable = QPushButton(self.widget_9)
        self.convertToPortable.setObjectName(u"convertToPortable")

        self.horizontalLayout.addWidget(self.convertToPortable)

        self.convertToGlobal = QPushButton(self.widget_9)
        self.convertToGlobal.setObjectName(u"convertToGlobal")

        self.horizontalLayout.addWidget(self.convertToGlobal)

        self.openINI = QPushButton(self.widget_9)
        self.openINI.setObjectName(u"openINI")

        self.horizontalLayout.addWidget(self.openINI)

        self.deleteInstance = QPushButton(self.widget_9)
        self.deleteInstance.setObjectName(u"deleteInstance")
        icon1 = QIcon()
        icon1.addFile(u":/MO/gui/remove", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteInstance.setIcon(icon1)

        self.horizontalLayout.addWidget(self.deleteInstance)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.widget_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(3, 1)
        self.splitter.addWidget(self.widget_3)

        self.verticalLayout_4.addWidget(self.splitter)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.verticalLayout_5.setStretch(0, 1)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.widget = QWidget(InstanceManagerDialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.switchToInstance = QPushButton(self.widget)
        self.switchToInstance.setObjectName(u"switchToInstance")
        icon2 = QIcon()
        icon2.addFile(u":/MO/gui/next", QSize(), QIcon.Normal, QIcon.Off)
        self.switchToInstance.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.switchToInstance)

        self.close = QPushButton(self.widget)
        self.close.setObjectName(u"close")

        self.horizontalLayout_3.addWidget(self.close)


        self.verticalLayout_6.addWidget(self.widget)


        self.retranslateUi(InstanceManagerDialog)

        self.close.setDefault(True)


        QMetaObject.connectSlotsByName(InstanceManagerDialog)
    # setupUi

    def retranslateUi(self, InstanceManagerDialog):
        InstanceManagerDialog.setWindowTitle(QCoreApplication.translate("InstanceManagerDialog", u"Instance manager", None))
        self.createNew.setText(QCoreApplication.translate("InstanceManagerDialog", u"Create new instance", None))
        self.whatis.setText(QCoreApplication.translate("InstanceManagerDialog", u"<html><head/><body><p><a href=\"https://github.com/ModOrganizer2/modorganizer/wiki/Instances\">What is an instance?</a></p></body></html>", None))
        self.filter.setPlaceholderText(QCoreApplication.translate("InstanceManagerDialog", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("InstanceManagerDialog", u"Name", None))
        self.exploreLocation.setText(QCoreApplication.translate("InstanceManagerDialog", u"Explore", None))
        self.label_8.setText(QCoreApplication.translate("InstanceManagerDialog", u"Game", None))
        self.label_4.setText(QCoreApplication.translate("InstanceManagerDialog", u"Location", None))
        self.rename.setText(QCoreApplication.translate("InstanceManagerDialog", u"Rename", None))
        self.label.setText(QCoreApplication.translate("InstanceManagerDialog", u"Game location", None))
        self.label_6.setText(QCoreApplication.translate("InstanceManagerDialog", u"Base folder", None))
        self.exploreBaseDirectory.setText(QCoreApplication.translate("InstanceManagerDialog", u"Explore", None))
        self.exploreGame.setText(QCoreApplication.translate("InstanceManagerDialog", u"Explore", None))
        self.convertToPortable.setText(QCoreApplication.translate("InstanceManagerDialog", u"Convert to portable", None))
        self.convertToGlobal.setText(QCoreApplication.translate("InstanceManagerDialog", u"Convert to global", None))
        self.openINI.setText(QCoreApplication.translate("InstanceManagerDialog", u"Open INI", None))
        self.deleteInstance.setText(QCoreApplication.translate("InstanceManagerDialog", u"Delete instance...", None))
        self.switchToInstance.setText(QCoreApplication.translate("InstanceManagerDialog", u"Switch to this instance", None))
        self.close.setText(QCoreApplication.translate("InstanceManagerDialog", u"Close", None))
    # retranslateUi

