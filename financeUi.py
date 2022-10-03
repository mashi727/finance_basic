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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

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
        MainWindow.setTabShape(QTabWidget.Rounded)
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
#ifndef Q_OS_MAC
        self.verticalLayout.setSpacing(-1)
#endif
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, 0)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_search = QLabel(self.centralwidget)
        self.label_search.setObjectName(u"label_search")
        sizePolicy.setHeightForWidth(self.label_search.sizePolicy().hasHeightForWidth())
        self.label_search.setSizePolicy(sizePolicy)
        self.label_search.setMaximumSize(QSize(150, 27))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_search.setFont(font1)
        self.label_search.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_search.setMargin(0)
        self.label_search.setIndent(15)

        self.verticalLayout_7.addWidget(self.label_search)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_search_3 = QLabel(self.centralwidget)
        self.label_search_3.setObjectName(u"label_search_3")
        sizePolicy.setHeightForWidth(self.label_search_3.sizePolicy().hasHeightForWidth())
        self.label_search_3.setSizePolicy(sizePolicy)
        self.label_search_3.setMinimumSize(QSize(150, 0))
        self.label_search_3.setMaximumSize(QSize(150, 27))
        self.label_search_3.setFont(font1)
        self.label_search_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_search_3.setMargin(0)
        self.label_search_3.setIndent(15)

        self.horizontalLayout_8.addWidget(self.label_search_3)

        self.forty_rule_checkBox = QCheckBox(self.centralwidget)
        self.forty_rule_checkBox.setObjectName(u"forty_rule_checkBox")
        self.forty_rule_checkBox.setMinimumSize(QSize(20, 20))
        self.forty_rule_checkBox.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.forty_rule_checkBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_search_5 = QLabel(self.centralwidget)
        self.label_search_5.setObjectName(u"label_search_5")
        sizePolicy.setHeightForWidth(self.label_search_5.sizePolicy().hasHeightForWidth())
        self.label_search_5.setSizePolicy(sizePolicy)
        self.label_search_5.setMinimumSize(QSize(150, 0))
        self.label_search_5.setMaximumSize(QSize(150, 27))
        self.label_search_5.setFont(font1)
        self.label_search_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_search_5.setMargin(0)
        self.label_search_5.setIndent(15)

        self.horizontalLayout_7.addWidget(self.label_search_5)

        self.market_capital_ckeckBox = QCheckBox(self.centralwidget)
        self.market_capital_ckeckBox.setObjectName(u"market_capital_ckeckBox")
        self.market_capital_ckeckBox.setMinimumSize(QSize(20, 20))
        self.market_capital_ckeckBox.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.market_capital_ckeckBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_10.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.search_ticker_symbol = QLineEdit(self.centralwidget)
        self.search_ticker_symbol.setObjectName(u"search_ticker_symbol")
        sizePolicy.setHeightForWidth(self.search_ticker_symbol.sizePolicy().hasHeightForWidth())
        self.search_ticker_symbol.setSizePolicy(sizePolicy)
        self.search_ticker_symbol.setMinimumSize(QSize(150, 27))
        self.search_ticker_symbol.setMaximumSize(QSize(150, 27))
        self.search_ticker_symbol.setFont(font1)

        self.verticalLayout_8.addWidget(self.search_ticker_symbol)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_search_4 = QLabel(self.centralwidget)
        self.label_search_4.setObjectName(u"label_search_4")
        sizePolicy.setHeightForWidth(self.label_search_4.sizePolicy().hasHeightForWidth())
        self.label_search_4.setSizePolicy(sizePolicy)
        self.label_search_4.setMinimumSize(QSize(50, 0))
        self.label_search_4.setMaximumSize(QSize(50, 27))
        self.label_search_4.setFont(font1)
        self.label_search_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_search_4.setMargin(0)
        self.label_search_4.setIndent(15)

        self.horizontalLayout_3.addWidget(self.label_search_4)

        self.search_ticker_symbol_2 = QLineEdit(self.centralwidget)
        self.search_ticker_symbol_2.setObjectName(u"search_ticker_symbol_2")
        sizePolicy.setHeightForWidth(self.search_ticker_symbol_2.sizePolicy().hasHeightForWidth())
        self.search_ticker_symbol_2.setSizePolicy(sizePolicy)
        self.search_ticker_symbol_2.setMinimumSize(QSize(100, 27))
        self.search_ticker_symbol_2.setMaximumSize(QSize(100, 27))
        self.search_ticker_symbol_2.setFont(font1)
        self.search_ticker_symbol_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.search_ticker_symbol_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.combobox_time_span_3 = QComboBox(self.centralwidget)
        self.combobox_time_span_3.addItem("")
        self.combobox_time_span_3.addItem("")
        self.combobox_time_span_3.setObjectName(u"combobox_time_span_3")
        self.combobox_time_span_3.setMinimumSize(QSize(70, 27))
        self.combobox_time_span_3.setMaximumSize(QSize(70, 16777215))
        self.combobox_time_span_3.setFont(font1)

        self.horizontalLayout_9.addWidget(self.combobox_time_span_3)

        self.search_ticker_symbol_3 = QLineEdit(self.centralwidget)
        self.search_ticker_symbol_3.setObjectName(u"search_ticker_symbol_3")
        sizePolicy.setHeightForWidth(self.search_ticker_symbol_3.sizePolicy().hasHeightForWidth())
        self.search_ticker_symbol_3.setSizePolicy(sizePolicy)
        self.search_ticker_symbol_3.setMinimumSize(QSize(60, 27))
        self.search_ticker_symbol_3.setMaximumSize(QSize(60, 27))
        self.search_ticker_symbol_3.setFont(font1)
        self.search_ticker_symbol_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.search_ticker_symbol_3)

        self.label_search_7 = QLabel(self.centralwidget)
        self.label_search_7.setObjectName(u"label_search_7")
        sizePolicy.setHeightForWidth(self.label_search_7.sizePolicy().hasHeightForWidth())
        self.label_search_7.setSizePolicy(sizePolicy)
        self.label_search_7.setMaximumSize(QSize(40, 27))
        self.label_search_7.setFont(font1)
        self.label_search_7.setAlignment(Qt.AlignCenter)
        self.label_search_7.setMargin(0)
        self.label_search_7.setIndent(15)

        self.horizontalLayout_9.addWidget(self.label_search_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_8)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_SMA = QLabel(self.centralwidget)
        self.label_SMA.setObjectName(u"label_SMA")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_SMA.sizePolicy().hasHeightForWidth())
        self.label_SMA.setSizePolicy(sizePolicy1)
        self.label_SMA.setMinimumSize(QSize(55, 0))
        self.label_SMA.setMaximumSize(QSize(45, 27))
        self.label_SMA.setFont(font1)
        self.label_SMA.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_SMA.setIndent(10)

        self.horizontalLayout_2.addWidget(self.label_SMA)

        self.label_Short = QLabel(self.centralwidget)
        self.label_Short.setObjectName(u"label_Short")
        sizePolicy1.setHeightForWidth(self.label_Short.sizePolicy().hasHeightForWidth())
        self.label_Short.setSizePolicy(sizePolicy1)
        self.label_Short.setMinimumSize(QSize(47, 0))
        self.label_Short.setMaximumSize(QSize(47, 27))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_Short.setFont(font2)
        self.label_Short.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_Short.setIndent(0)

        self.horizontalLayout_2.addWidget(self.label_Short)

        self.SB_sma_short = QSpinBox(self.centralwidget)
        self.SB_sma_short.setObjectName(u"SB_sma_short")
        self.SB_sma_short.setMinimumSize(QSize(40, 27))
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
        self.label_Med.setMaximumSize(QSize(40, 27))
        self.label_Med.setFont(font2)
        self.label_Med.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_Med.setIndent(0)

        self.horizontalLayout_2.addWidget(self.label_Med)

        self.SB_sma_med = QSpinBox(self.centralwidget)
        self.SB_sma_med.setObjectName(u"SB_sma_med")
        sizePolicy.setHeightForWidth(self.SB_sma_med.sizePolicy().hasHeightForWidth())
        self.SB_sma_med.setSizePolicy(sizePolicy)
        self.SB_sma_med.setMinimumSize(QSize(50, 27))
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
        self.label_Long.setMaximumSize(QSize(40, 27))
        self.label_Long.setFont(font2)
        self.label_Long.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_Long.setIndent(0)

        self.horizontalLayout_2.addWidget(self.label_Long)

        self.SB_sma_long = QSpinBox(self.centralwidget)
        self.SB_sma_long.setObjectName(u"SB_sma_long")
        self.SB_sma_long.setMinimumSize(QSize(50, 27))
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
        self.label_time_span.setMaximumSize(QSize(150, 27))
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
        self.combobox_time_span.addItem("")
        self.combobox_time_span.setObjectName(u"combobox_time_span")
        self.combobox_time_span.setMinimumSize(QSize(0, 27))
        self.combobox_time_span.setMaximumSize(QSize(200, 16777215))
        self.combobox_time_span.setFont(font1)

        self.horizontalLayout_4.addWidget(self.combobox_time_span)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout_6.setSpacing(-1)
#endif
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_data_source = QLabel(self.centralwidget)
        self.label_data_source.setObjectName(u"label_data_source")
        sizePolicy2.setHeightForWidth(self.label_data_source.sizePolicy().hasHeightForWidth())
        self.label_data_source.setSizePolicy(sizePolicy2)
        self.label_data_source.setMaximumSize(QSize(150, 27))
        self.label_data_source.setFont(font1)
        self.label_data_source.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_data_source.setIndent(10)

        self.horizontalLayout_6.addWidget(self.label_data_source)

        self.combobox_time_span_2 = QComboBox(self.centralwidget)
        self.combobox_time_span_2.addItem("")
        self.combobox_time_span_2.addItem("")
        self.combobox_time_span_2.addItem("")
        self.combobox_time_span_2.addItem("")
        self.combobox_time_span_2.setObjectName(u"combobox_time_span_2")
        self.combobox_time_span_2.setMinimumSize(QSize(0, 27))
        self.combobox_time_span_2.setMaximumSize(QSize(200, 16777215))
        self.combobox_time_span_2.setFont(font1)

        self.horizontalLayout_6.addWidget(self.combobox_time_span_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


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
        self.tableView_ticker_symbols.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableView_ticker_symbols.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_5.addWidget(self.tableView_ticker_symbols)

        self.growth_rate_button = QPushButton(self.centralwidget)
        self.growth_rate_button.setObjectName(u"growth_rate_button")
        sizePolicy.setHeightForWidth(self.growth_rate_button.sizePolicy().hasHeightForWidth())
        self.growth_rate_button.setSizePolicy(sizePolicy)
        self.growth_rate_button.setMinimumSize(QSize(370, 0))
        self.growth_rate_button.setMaximumSize(QSize(370, 16777215))
        font3 = QFont()
        font3.setFamilies([u".AppleSystemUIFont"])
        font3.setPointSize(20)
        self.growth_rate_button.setFont(font3)

        self.verticalLayout_5.addWidget(self.growth_rate_button)


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
        font4 = QFont()
        font4.setFamilies([u".AppleJapaneseFont"])
        font4.setPointSize(20)
        self.label_Zaimu.setFont(font4)

        self.verticalLayout_3.addWidget(self.label_Zaimu)

        self.tableView_zaimu_shohyou = QTableView(self.centralwidget)
        self.tableView_zaimu_shohyou.setObjectName(u"tableView_zaimu_shohyou")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableView_zaimu_shohyou.sizePolicy().hasHeightForWidth())
        self.tableView_zaimu_shohyou.setSizePolicy(sizePolicy4)
        self.tableView_zaimu_shohyou.setMinimumSize(QSize(600, 0))
        self.tableView_zaimu_shohyou.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout_3.addWidget(self.tableView_zaimu_shohyou)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_df = QLabel(self.centralwidget)
        self.label_df.setObjectName(u"label_df")
        sizePolicy2.setHeightForWidth(self.label_df.sizePolicy().hasHeightForWidth())
        self.label_df.setSizePolicy(sizePolicy2)
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
        self.label_search.setText(QCoreApplication.translate("MainWindow", u"Search NASDAQ :", None))
        self.label_search_3.setText(QCoreApplication.translate("MainWindow", u"Fourty Rule :", None))
        self.forty_rule_checkBox.setText("")
        self.label_search_5.setText(QCoreApplication.translate("MainWindow", u"Market capital. :", None))
        self.market_capital_ckeckBox.setText("")
        self.label_search_4.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.search_ticker_symbol_2.setText(QCoreApplication.translate("MainWindow", u"0.4", None))
        self.combobox_time_span_3.setItemText(0, QCoreApplication.translate("MainWindow", u">", None))
        self.combobox_time_span_3.setItemText(1, QCoreApplication.translate("MainWindow", u"<", None))

        self.search_ticker_symbol_3.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_search_7.setText(QCoreApplication.translate("MainWindow", u"M$", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u8a08\u7b97\u8af8\u5143", None))
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
        self.combobox_time_span.setItemText(5, QCoreApplication.translate("MainWindow", u"1min", None))

        self.label_data_source.setText(QCoreApplication.translate("MainWindow", u"Data Source", None))
        self.combobox_time_span_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Alpha Vantage", None))
        self.combobox_time_span_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Yahoo Finance", None))
        self.combobox_time_span_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Quandl", None))
        self.combobox_time_span_2.setItemText(3, QCoreApplication.translate("MainWindow", u"CSV(Local file)", None))

        self.growth_rate_button.setText(QCoreApplication.translate("MainWindow", u"Growth Rate", None))
        self.label_Zaimu.setText(QCoreApplication.translate("MainWindow", u"\u8ca1\u52d9\u8af8\u8868", None))
        self.label_df.setText(QCoreApplication.translate("MainWindow", u"dataframe", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

