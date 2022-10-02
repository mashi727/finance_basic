# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'financeUi.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

from pyqtgraph.dockarea import DockArea

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1692, 1262)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionOpenDialog = QAction(MainWindow)
        self.actionOpenDialog.setObjectName(u"actionOpenDialog")
        self.actionQuit2 = QAction(MainWindow)
        self.actionQuit2.setObjectName(u"actionQuit2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_search = QLabel(self.centralwidget)
        self.label_search.setObjectName(u"label_search")
        sizePolicy.setHeightForWidth(self.label_search.sizePolicy().hasHeightForWidth())
        self.label_search.setSizePolicy(sizePolicy)
        self.label_search.setMaximumSize(QSize(140, 23))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_search.setFont(font1)
        self.label_search.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_search.setMargin(0)
        self.label_search.setIndent(15)

        self.horizontalLayout_3.addWidget(self.label_search)

        self.search_ticker_symbol = QLineEdit(self.centralwidget)
        self.search_ticker_symbol.setObjectName(u"search_ticker_symbol")
        sizePolicy.setHeightForWidth(self.search_ticker_symbol.sizePolicy().hasHeightForWidth())
        self.search_ticker_symbol.setSizePolicy(sizePolicy)
        self.search_ticker_symbol.setMinimumSize(QSize(180, 23))
        self.search_ticker_symbol.setMaximumSize(QSize(180, 23))
        self.search_ticker_symbol.setFont(font1)

        self.horizontalLayout_3.addWidget(self.search_ticker_symbol)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_SMA = QLabel(self.centralwidget)
        self.label_SMA.setObjectName(u"label_SMA")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_SMA.sizePolicy().hasHeightForWidth())
        self.label_SMA.setSizePolicy(sizePolicy1)
        self.label_SMA.setMinimumSize(QSize(40, 0))
        self.label_SMA.setMaximumSize(QSize(40, 16777215))
        self.label_SMA.setFont(font1)
        self.label_SMA.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_SMA.setIndent(10)

        self.horizontalLayout_2.addWidget(self.label_SMA)

        self.label_Short = QLabel(self.centralwidget)
        self.label_Short.setObjectName(u"label_Short")
        sizePolicy1.setHeightForWidth(self.label_Short.sizePolicy().hasHeightForWidth())
        self.label_Short.setSizePolicy(sizePolicy1)
        self.label_Short.setMinimumSize(QSize(47, 0))
        self.label_Short.setMaximumSize(QSize(47, 16777215))
        self.label_Short.setFont(font1)
        self.label_Short.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_Short.setIndent(0)

        self.horizontalLayout_2.addWidget(self.label_Short)

        self.SB_sma_short = QSpinBox(self.centralwidget)
        self.SB_sma_short.setObjectName(u"SB_sma_short")
        self.SB_sma_short.setMinimumSize(QSize(50, 0))
        self.SB_sma_short.setMaximumSize(QSize(50, 16777215))
        self.SB_sma_short.setFont(font1)
        self.SB_sma_short.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_sma_short.setMinimum(1)
        self.SB_sma_short.setMaximum(500)
        self.SB_sma_short.setValue(5)

        self.horizontalLayout_2.addWidget(self.SB_sma_short)

        self.label_Med = QLabel(self.centralwidget)
        self.label_Med.setObjectName(u"label_Med")
        sizePolicy1.setHeightForWidth(self.label_Med.sizePolicy().hasHeightForWidth())
        self.label_Med.setSizePolicy(sizePolicy1)
        self.label_Med.setMaximumSize(QSize(40, 16777215))
        self.label_Med.setFont(font1)
        self.label_Med.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_Med.setIndent(0)

        self.horizontalLayout_2.addWidget(self.label_Med)

        self.SB_sma_med = QSpinBox(self.centralwidget)
        self.SB_sma_med.setObjectName(u"SB_sma_med")
        sizePolicy.setHeightForWidth(self.SB_sma_med.sizePolicy().hasHeightForWidth())
        self.SB_sma_med.setSizePolicy(sizePolicy)
        self.SB_sma_med.setMinimumSize(QSize(50, 0))
        self.SB_sma_med.setMaximumSize(QSize(50, 16777215))
        self.SB_sma_med.setFont(font1)
        self.SB_sma_med.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_sma_med.setMinimum(1)
        self.SB_sma_med.setMaximum(500)
        self.SB_sma_med.setValue(20)

        self.horizontalLayout_2.addWidget(self.SB_sma_med)

        self.label_Long = QLabel(self.centralwidget)
        self.label_Long.setObjectName(u"label_Long")
        sizePolicy1.setHeightForWidth(self.label_Long.sizePolicy().hasHeightForWidth())
        self.label_Long.setSizePolicy(sizePolicy1)
        self.label_Long.setMaximumSize(QSize(40, 16777215))
        self.label_Long.setFont(font1)
        self.label_Long.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_Long.setIndent(0)

        self.horizontalLayout_2.addWidget(self.label_Long)

        self.SB_sma_long = QSpinBox(self.centralwidget)
        self.SB_sma_long.setObjectName(u"SB_sma_long")
        self.SB_sma_long.setMinimumSize(QSize(50, 0))
        self.SB_sma_long.setMaximumSize(QSize(50, 16777215))
        self.SB_sma_long.setFont(font1)
        self.SB_sma_long.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_sma_long.setMinimum(1)
        self.SB_sma_long.setMaximum(500)
        self.SB_sma_long.setValue(60)

        self.horizontalLayout_2.addWidget(self.SB_sma_long)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_time_span = QLabel(self.centralwidget)
        self.label_time_span.setObjectName(u"label_time_span")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_time_span.sizePolicy().hasHeightForWidth())
        self.label_time_span.setSizePolicy(sizePolicy2)
        self.label_time_span.setMaximumSize(QSize(150, 16777215))
        self.label_time_span.setFont(font1)
        self.label_time_span.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_time_span.setIndent(10)

        self.horizontalLayout_4.addWidget(self.label_time_span)

        self.combobox_time_span = QComboBox(self.centralwidget)
        self.combobox_time_span.addItem("")
        self.combobox_time_span.addItem("")
        self.combobox_time_span.addItem("")
        self.combobox_time_span.addItem("")
        self.combobox_time_span.addItem("")
        self.combobox_time_span.setObjectName(u"combobox_time_span")
        self.combobox_time_span.setMaximumSize(QSize(200, 16777215))
        self.combobox_time_span.setFont(font1)

        self.horizontalLayout_4.addWidget(self.combobox_time_span)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.tableView_ticker_symbols = QTableView(self.centralwidget)
        self.tableView_ticker_symbols.setObjectName(u"tableView_ticker_symbols")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableView_ticker_symbols.sizePolicy().hasHeightForWidth())
        self.tableView_ticker_symbols.setSizePolicy(sizePolicy3)
        self.tableView_ticker_symbols.setMinimumSize(QSize(370, 0))
        self.tableView_ticker_symbols.setMaximumSize(QSize(370, 16777215))
        self.tableView_ticker_symbols.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_5.addWidget(self.tableView_ticker_symbols)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphicsView = DockArea(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(600, 0))

        self.verticalLayout_2.addWidget(self.graphicsView)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_Zaimu = QLabel(self.centralwidget)
        self.label_Zaimu.setObjectName(u"label_Zaimu")
        self.label_Zaimu.setMinimumSize(QSize(150, 0))
        font2 = QFont()
        font2.setFamilies([u".AppleJapaneseFont"])
        font2.setPointSize(18)
        self.label_Zaimu.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_Zaimu)

        self.tableView_zaimu_shohyou = QTableView(self.centralwidget)
        self.tableView_zaimu_shohyou.setObjectName(u"tableView_zaimu_shohyou")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableView_zaimu_shohyou.sizePolicy().hasHeightForWidth())
        self.tableView_zaimu_shohyou.setSizePolicy(sizePolicy4)
        self.tableView_zaimu_shohyou.setMinimumSize(QSize(350, 0))
        self.tableView_zaimu_shohyou.setMaximumSize(QSize(350, 16777215))

        self.verticalLayout_3.addWidget(self.tableView_zaimu_shohyou)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_df = QLabel(self.centralwidget)
        self.label_df.setObjectName(u"label_df")
        sizePolicy2.setHeightForWidth(self.label_df.sizePolicy().hasHeightForWidth())
        self.label_df.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u".AppleSystemUIFont"])
        font3.setPointSize(18)
        self.label_df.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_df)

        self.tableview_df = QTableView(self.centralwidget)
        self.tableview_df.setObjectName(u"tableview_df")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tableview_df.sizePolicy().hasHeightForWidth())
        self.tableview_df.setSizePolicy(sizePolicy5)
        self.tableview_df.setMinimumSize(QSize(200, 0))
        self.tableview_df.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_4.addWidget(self.tableview_df)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(765, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.quitButton = QPushButton(self.centralwidget)
        self.quitButton.setObjectName(u"quitButton")
        sizePolicy.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy)
        self.quitButton.setFont(font3)

        self.horizontalLayout.addWidget(self.quitButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1692, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpenDialog)
        self.menuFile.addAction(self.actionQuit2)

        self.retranslateUi(MainWindow)
        self.quitButton.clicked.connect(MainWindow.close)
        self.actionQuit2.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionOpenDialog.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionQuit2.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9298\u67c4\u6307\u5b9a", None))
        self.label_search.setText(QCoreApplication.translate("MainWindow", u"Search NASDAQ", None))
        self.label_SMA.setText(QCoreApplication.translate("MainWindow", u"SMA :", None))
        self.label_Short.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.label_Med.setText(QCoreApplication.translate("MainWindow", u"Med.", None))
        self.label_Long.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.label_time_span.setText(QCoreApplication.translate("MainWindow", u"Time Span", None))
        self.combobox_time_span.setItemText(0, QCoreApplication.translate("MainWindow", u"Daily", None))
        self.combobox_time_span.setItemText(1, QCoreApplication.translate("MainWindow", u"60min", None))
        self.combobox_time_span.setItemText(2, QCoreApplication.translate("MainWindow", u"30min", None))
        self.combobox_time_span.setItemText(3, QCoreApplication.translate("MainWindow", u"15min", None))
        self.combobox_time_span.setItemText(4, QCoreApplication.translate("MainWindow", u"5min", None))

        self.label_Zaimu.setText(QCoreApplication.translate("MainWindow", u"\u8ca1\u52d9\u8af8\u8868", None))
        self.label_df.setText(QCoreApplication.translate("MainWindow", u"dataframe", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

