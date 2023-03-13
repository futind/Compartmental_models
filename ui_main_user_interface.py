# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_user_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from mpl_widget import MPLWidget
import main_window_resources_rc

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(880, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QSize(880, 600))
        self.perform_action = QAction(main_window)
        self.perform_action.setObjectName(u"perform_action")
        self.clear_action = QAction(main_window)
        self.clear_action.setObjectName(u"clear_action")
        self.reset_action = QAction(main_window)
        self.reset_action.setObjectName(u"reset_action")
        self.quit_action = QAction(main_window)
        self.quit_action.setObjectName(u"quit_action")
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.poluation_groupBox = QGroupBox(self.central_widget)
        self.poluation_groupBox.setObjectName(u"poluation_groupBox")
        self.poluation_groupBox.setGeometry(QRect(20, 10, 191, 101))
        self.layoutWidget = QWidget(self.poluation_groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 171, 62))
        self.population_params_layout = QHBoxLayout(self.layoutWidget)
        self.population_params_layout.setObjectName(u"population_params_layout")
        self.population_params_layout.setContentsMargins(0, 0, 0, 0)
        self.pop_params_label_layout = QVBoxLayout()
        self.pop_params_label_layout.setObjectName(u"pop_params_label_layout")
        self.population_size_label = QLabel(self.layoutWidget)
        self.population_size_label.setObjectName(u"population_size_label")

        self.pop_params_label_layout.addWidget(self.population_size_label)

        self.infectious_size_label = QLabel(self.layoutWidget)
        self.infectious_size_label.setObjectName(u"infectious_size_label")

        self.pop_params_label_layout.addWidget(self.infectious_size_label)


        self.population_params_layout.addLayout(self.pop_params_label_layout)

        self.pop_params_spinBox_layout = QVBoxLayout()
        self.pop_params_spinBox_layout.setObjectName(u"pop_params_spinBox_layout")
        self.population_size_spinBox = QSpinBox(self.layoutWidget)
        self.population_size_spinBox.setObjectName(u"population_size_spinBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.population_size_spinBox.sizePolicy().hasHeightForWidth())
        self.population_size_spinBox.setSizePolicy(sizePolicy1)

        self.pop_params_spinBox_layout.addWidget(self.population_size_spinBox)

        self.infections_size_spinBox = QSpinBox(self.layoutWidget)
        self.infections_size_spinBox.setObjectName(u"infections_size_spinBox")
        sizePolicy1.setHeightForWidth(self.infections_size_spinBox.sizePolicy().hasHeightForWidth())
        self.infections_size_spinBox.setSizePolicy(sizePolicy1)

        self.pop_params_spinBox_layout.addWidget(self.infections_size_spinBox)


        self.population_params_layout.addLayout(self.pop_params_spinBox_layout)

        self.infection_parameters_groupBox = QGroupBox(self.central_widget)
        self.infection_parameters_groupBox.setObjectName(u"infection_parameters_groupBox")
        self.infection_parameters_groupBox.setGeometry(QRect(20, 120, 191, 131))
        self.layoutWidget1 = QWidget(self.infection_parameters_groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 171, 94))
        self.infection_params_layout = QHBoxLayout(self.layoutWidget1)
        self.infection_params_layout.setObjectName(u"infection_params_layout")
        self.infection_params_layout.setContentsMargins(0, 0, 0, 0)
        self.inf_param_label_layout = QVBoxLayout()
        self.inf_param_label_layout.setObjectName(u"inf_param_label_layout")
        self.vitality_rate_label = QLabel(self.layoutWidget1)
        self.vitality_rate_label.setObjectName(u"vitality_rate_label")

        self.inf_param_label_layout.addWidget(self.vitality_rate_label)

        self.contact_rate_label = QLabel(self.layoutWidget1)
        self.contact_rate_label.setObjectName(u"contact_rate_label")

        self.inf_param_label_layout.addWidget(self.contact_rate_label)

        self.recovery_rate_label = QLabel(self.layoutWidget1)
        self.recovery_rate_label.setObjectName(u"recovery_rate_label")

        self.inf_param_label_layout.addWidget(self.recovery_rate_label)


        self.infection_params_layout.addLayout(self.inf_param_label_layout)

        self.inf_param_dspinBox_layout = QVBoxLayout()
        self.inf_param_dspinBox_layout.setObjectName(u"inf_param_dspinBox_layout")
        self.vitality_rate_dSpinBox = QDoubleSpinBox(self.layoutWidget1)
        self.vitality_rate_dSpinBox.setObjectName(u"vitality_rate_dSpinBox")
        sizePolicy1.setHeightForWidth(self.vitality_rate_dSpinBox.sizePolicy().hasHeightForWidth())
        self.vitality_rate_dSpinBox.setSizePolicy(sizePolicy1)

        self.inf_param_dspinBox_layout.addWidget(self.vitality_rate_dSpinBox)

        self.contact_rate_dSpinBox = QDoubleSpinBox(self.layoutWidget1)
        self.contact_rate_dSpinBox.setObjectName(u"contact_rate_dSpinBox")
        sizePolicy1.setHeightForWidth(self.contact_rate_dSpinBox.sizePolicy().hasHeightForWidth())
        self.contact_rate_dSpinBox.setSizePolicy(sizePolicy1)

        self.inf_param_dspinBox_layout.addWidget(self.contact_rate_dSpinBox)

        self.recovery_rate_dSpinBox = QDoubleSpinBox(self.layoutWidget1)
        self.recovery_rate_dSpinBox.setObjectName(u"recovery_rate_dSpinBox")
        sizePolicy1.setHeightForWidth(self.recovery_rate_dSpinBox.sizePolicy().hasHeightForWidth())
        self.recovery_rate_dSpinBox.setSizePolicy(sizePolicy1)

        self.inf_param_dspinBox_layout.addWidget(self.recovery_rate_dSpinBox)


        self.infection_params_layout.addLayout(self.inf_param_dspinBox_layout)

        self.plotting_widget = QTabWidget(self.central_widget)
        self.plotting_widget.setObjectName(u"plotting_widget")
        self.plotting_widget.setGeometry(QRect(240, 10, 631, 541))
        self.dynamics_graphpane = QWidget()
        self.dynamics_graphpane.setObjectName(u"dynamics_graphpane")
        self.dynamics_graph = MPLWidget(self.dynamics_graphpane)
        self.dynamics_graph.setObjectName(u"dynamics_graph")
        self.dynamics_graph.setGeometry(QRect(10, 10, 611, 491))
        self.plotting_widget.addTab(self.dynamics_graphpane, "")
        self.phase_graphpane = QWidget()
        self.phase_graphpane.setObjectName(u"phase_graphpane")
        self.phase_graph = MPLWidget(self.phase_graphpane)
        self.phase_graph.setObjectName(u"phase_graph")
        self.phase_graph.setGeometry(QRect(10, 10, 611, 491))
        self.plotting_widget.addTab(self.phase_graphpane, "")
        self.sir_model_label = QLabel(self.central_widget)
        self.sir_model_label.setObjectName(u"sir_model_label")
        self.sir_model_label.setGeometry(QRect(10, 310, 231, 131))
        self.sir_model_label.setPixmap(QPixmap(u":/computational_models/SIR_classic_endemic_model.png"))
        self.function_display_groupBox = QGroupBox(self.central_widget)
        self.function_display_groupBox.setObjectName(u"function_display_groupBox")
        self.function_display_groupBox.setGeometry(QRect(20, 430, 191, 121))
        self.layoutWidget2 = QWidget(self.function_display_groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 30, 86, 83))
        self.function_display_layout = QVBoxLayout(self.layoutWidget2)
        self.function_display_layout.setObjectName(u"function_display_layout")
        self.function_display_layout.setContentsMargins(0, 0, 0, 0)
        self.suseptible_checkBox = QCheckBox(self.layoutWidget2)
        self.suseptible_checkBox.setObjectName(u"suseptible_checkBox")

        self.function_display_layout.addWidget(self.suseptible_checkBox)

        self.infectious_checkBox = QCheckBox(self.layoutWidget2)
        self.infectious_checkBox.setObjectName(u"infectious_checkBox")

        self.function_display_layout.addWidget(self.infectious_checkBox)

        self.recovered_checkBox = QCheckBox(self.layoutWidget2)
        self.recovered_checkBox.setObjectName(u"recovered_checkBox")

        self.function_display_layout.addWidget(self.recovered_checkBox)

        self.layoutWidget3 = QWidget(self.central_widget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 260, 191, 58))
        self.buttons_layout = QVBoxLayout(self.layoutWidget3)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.perform_button = QPushButton(self.layoutWidget3)
        self.perform_button.setObjectName(u"perform_button")

        self.buttons_layout.addWidget(self.perform_button)

        self.clear_button = QPushButton(self.layoutWidget3)
        self.clear_button.setObjectName(u"clear_button")

        self.buttons_layout.addWidget(self.clear_button)

        main_window.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 880, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.perform_action)
        self.menuFile.addAction(self.clear_action)
        self.menuFile.addAction(self.reset_action)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.quit_action)

        self.retranslateUi(main_window)

        self.plotting_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.perform_action.setText(QCoreApplication.translate("main_window", u"Perform the calculation", None))
#if QT_CONFIG(statustip)
        self.perform_action.setStatusTip(QCoreApplication.translate("main_window", u"Perform the calculation and plot the graphics", None))
#endif // QT_CONFIG(statustip)
        self.clear_action.setText(QCoreApplication.translate("main_window", u"Clear the graph panels", None))
#if QT_CONFIG(statustip)
        self.clear_action.setStatusTip(QCoreApplication.translate("main_window", u"Clear the graphics", None))
#endif // QT_CONFIG(statustip)
        self.reset_action.setText(QCoreApplication.translate("main_window", u"Reset the parameters", None))
#if QT_CONFIG(statustip)
        self.reset_action.setStatusTip(QCoreApplication.translate("main_window", u"Reset the parameters to their default values", None))
#endif // QT_CONFIG(statustip)
        self.quit_action.setText(QCoreApplication.translate("main_window", u"Quit", None))
#if QT_CONFIG(statustip)
        self.quit_action.setStatusTip(QCoreApplication.translate("main_window", u"Quit the application", None))
#endif // QT_CONFIG(statustip)
        self.poluation_groupBox.setTitle(QCoreApplication.translate("main_window", u"Population parameters", None))
#if QT_CONFIG(statustip)
        self.population_size_label.setStatusTip(QCoreApplication.translate("main_window", u"Population size (N) is the total number of people in a population being observed", None))
#endif // QT_CONFIG(statustip)
        self.population_size_label.setText(QCoreApplication.translate("main_window", u"Population size", None))
#if QT_CONFIG(statustip)
        self.infectious_size_label.setStatusTip(QCoreApplication.translate("main_window", u"Infectious size (I_{0}) is the initial number of infectious people in population", None))
#endif // QT_CONFIG(statustip)
        self.infectious_size_label.setText(QCoreApplication.translate("main_window", u"Infectious size", None))
        self.infection_parameters_groupBox.setTitle(QCoreApplication.translate("main_window", u"Infection parameters", None))
#if QT_CONFIG(statustip)
        self.vitality_rate_label.setStatusTip(QCoreApplication.translate("main_window", u"Vitality rate (\\mu) is the rate of inflow into S, I and R classes (in this model the deaths calance the births)", None))
#endif // QT_CONFIG(statustip)
        self.vitality_rate_label.setText(QCoreApplication.translate("main_window", u"Vitality rate", None))
#if QT_CONFIG(statustip)
        self.contact_rate_label.setStatusTip(QCoreApplication.translate("main_window", u"Contact rate (\\beta) is the average number of adequate contacts (meaning contacts that are sufficient for transmission)", None))
#endif // QT_CONFIG(statustip)
        self.contact_rate_label.setText(QCoreApplication.translate("main_window", u"Contact rate", None))
#if QT_CONFIG(statustip)
        self.recovery_rate_label.setStatusTip(QCoreApplication.translate("main_window", u"Recovery rate (\\gamma) corresponds to the speed of a person's movement out of the I compartment into R", None))
#endif // QT_CONFIG(statustip)
        self.recovery_rate_label.setText(QCoreApplication.translate("main_window", u"Recovery rate", None))
#if QT_CONFIG(statustip)
        self.dynamics_graph.setStatusTip(QCoreApplication.translate("main_window", u"Dynamics of compartments S, I and R is displayed here", None))
#endif // QT_CONFIG(statustip)
        self.plotting_widget.setTabText(self.plotting_widget.indexOf(self.dynamics_graphpane), QCoreApplication.translate("main_window", u"Compartmental dynamics", None))
#if QT_CONFIG(statustip)
        self.phase_graph.setStatusTip(QCoreApplication.translate("main_window", u"Phase plane I(S) is displayed here", None))
#endif // QT_CONFIG(statustip)
        self.plotting_widget.setTabText(self.plotting_widget.indexOf(self.phase_graphpane), QCoreApplication.translate("main_window", u"Phase plane", None))
#if QT_CONFIG(statustip)
        self.sir_model_label.setStatusTip(QCoreApplication.translate("main_window", u"The classic endemic model described in a form of a differential equations system", None))
#endif // QT_CONFIG(statustip)
        self.sir_model_label.setText("")
        self.function_display_groupBox.setTitle(QCoreApplication.translate("main_window", u"Choose a function to display", None))
#if QT_CONFIG(statustip)
        self.suseptible_checkBox.setStatusTip(QCoreApplication.translate("main_window", u"Suseptible (S) is a compartment that describes the number of people, who are suseptible to an infection", None))
#endif // QT_CONFIG(statustip)
        self.suseptible_checkBox.setText(QCoreApplication.translate("main_window", u"Suseptible", None))
#if QT_CONFIG(statustip)
        self.infectious_checkBox.setStatusTip(QCoreApplication.translate("main_window", u"Infectious (I) is a compartment that describes the number of people who are, at the time, infected", None))
#endif // QT_CONFIG(statustip)
        self.infectious_checkBox.setText(QCoreApplication.translate("main_window", u"Infectious", None))
#if QT_CONFIG(statustip)
        self.recovered_checkBox.setStatusTip(QCoreApplication.translate("main_window", u"Recovered (R) compartment describes the number of people who recovered from the infection or dead because of it", None))
#endif // QT_CONFIG(statustip)
        self.recovered_checkBox.setText(QCoreApplication.translate("main_window", u"Recovered", None))
#if QT_CONFIG(statustip)
        self.perform_button.setStatusTip(QCoreApplication.translate("main_window", u"Perform the calculation and plot the graphics", None))
#endif // QT_CONFIG(statustip)
        self.perform_button.setText(QCoreApplication.translate("main_window", u"Perform the calculation", None))
#if QT_CONFIG(statustip)
        self.clear_button.setStatusTip(QCoreApplication.translate("main_window", u"Clear the graphics", None))
#endif // QT_CONFIG(statustip)
        self.clear_button.setText(QCoreApplication.translate("main_window", u"Clear the graph panels", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
    # retranslateUi

Error: main_user_interface.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget1'.
main_user_interface.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget2'.
main_user_interface.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget3'.

while executing '/home/frostled/.local/lib/python3.10/site-packages/PySide6/Qt/libexec/uic -g python main_user_interface.ui'
