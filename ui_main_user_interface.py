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
        main_window.resize(1000, 743)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QSize(1000, 700))
        self.perform_action = QAction(main_window)
        self.perform_action.setObjectName(u"perform_action")
        self.clear_action = QAction(main_window)
        self.clear_action.setObjectName(u"clear_action")
        self.reset_action = QAction(main_window)
        self.reset_action.setObjectName(u"reset_action")
        self.quit_action = QAction(main_window)
        self.quit_action.setObjectName(u"quit_action")
        self.sir_classic_action = QAction(main_window)
        self.sir_classic_action.setObjectName(u"sir_classic_action")
        self.sir_vitality_action = QAction(main_window)
        self.sir_vitality_action.setObjectName(u"sir_vitality_action")
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.plotting_widget = QTabWidget(self.central_widget)
        self.plotting_widget.setObjectName(u"plotting_widget")
        self.plotting_widget.setGeometry(QRect(240, 10, 751, 681))
        self.dynamics_graphpane = QWidget()
        self.dynamics_graphpane.setObjectName(u"dynamics_graphpane")
        self.dynamics_graph = MPLWidget(self.dynamics_graphpane)
        self.dynamics_graph.setObjectName(u"dynamics_graph")
        self.dynamics_graph.setGeometry(QRect(10, 10, 731, 631))
        self.plotting_widget.addTab(self.dynamics_graphpane, "")
        self.phase_graphpane = QWidget()
        self.phase_graphpane.setObjectName(u"phase_graphpane")
        self.phase_graph = MPLWidget(self.phase_graphpane)
        self.phase_graph.setObjectName(u"phase_graph")
        self.phase_graph.setGeometry(QRect(10, 10, 731, 631))
        self.plotting_widget.addTab(self.phase_graphpane, "")
        self.sir_classic_label = QLabel(self.central_widget)
        self.sir_classic_label.setObjectName(u"sir_classic_label")
        self.sir_classic_label.setGeometry(QRect(10, 10, 221, 121))
        self.sir_classic_label.setPixmap(QPixmap(u":/Models/resources/images/SIR_classic_epidemic_model.png"))
        self.sir_classic_label.setScaledContents(True)
        self.function_display_groupBox = QGroupBox(self.central_widget)
        self.function_display_groupBox.setObjectName(u"function_display_groupBox")
        self.function_display_groupBox.setGeometry(QRect(20, 500, 201, 121))
        self.layoutWidget = QWidget(self.function_display_groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 86, 83))
        self.function_display_layout = QVBoxLayout(self.layoutWidget)
        self.function_display_layout.setObjectName(u"function_display_layout")
        self.function_display_layout.setContentsMargins(0, 0, 0, 0)
        self.suseptible_checkBox = QCheckBox(self.layoutWidget)
        self.suseptible_checkBox.setObjectName(u"suseptible_checkBox")
        self.suseptible_checkBox.setChecked(True)

        self.function_display_layout.addWidget(self.suseptible_checkBox)

        self.infectious_checkBox = QCheckBox(self.layoutWidget)
        self.infectious_checkBox.setObjectName(u"infectious_checkBox")
        self.infectious_checkBox.setChecked(True)

        self.function_display_layout.addWidget(self.infectious_checkBox)

        self.recovered_checkBox = QCheckBox(self.layoutWidget)
        self.recovered_checkBox.setObjectName(u"recovered_checkBox")
        self.recovered_checkBox.setChecked(True)

        self.function_display_layout.addWidget(self.recovered_checkBox)

        self.layoutWidget1 = QWidget(self.central_widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 630, 201, 58))
        self.buttons_layout = QVBoxLayout(self.layoutWidget1)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.perform_button = QPushButton(self.layoutWidget1)
        self.perform_button.setObjectName(u"perform_button")

        self.buttons_layout.addWidget(self.perform_button)

        self.clear_button = QPushButton(self.layoutWidget1)
        self.clear_button.setObjectName(u"clear_button")

        self.buttons_layout.addWidget(self.clear_button)

        self.observation_time_groupBox = QGroupBox(self.central_widget)
        self.observation_time_groupBox.setObjectName(u"observation_time_groupBox")
        self.observation_time_groupBox.setGeometry(QRect(20, 390, 201, 71))
        self.layoutWidget2 = QWidget(self.observation_time_groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(9, 30, 181, 28))
        self.observation_time_layout = QHBoxLayout(self.layoutWidget2)
        self.observation_time_layout.setObjectName(u"observation_time_layout")
        self.observation_time_layout.setContentsMargins(0, 0, 0, 0)
        self.ovservation_time_label = QLabel(self.layoutWidget2)
        self.ovservation_time_label.setObjectName(u"ovservation_time_label")

        self.observation_time_layout.addWidget(self.ovservation_time_label)

        self.observation_time_spinBox = QSpinBox(self.layoutWidget2)
        self.observation_time_spinBox.setObjectName(u"observation_time_spinBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.observation_time_spinBox.sizePolicy().hasHeightForWidth())
        self.observation_time_spinBox.setSizePolicy(sizePolicy1)
        self.observation_time_spinBox.setMaximum(9999999)
        self.observation_time_spinBox.setValue(365)

        self.observation_time_layout.addWidget(self.observation_time_spinBox)

        self.poluation_groupBox = QGroupBox(self.central_widget)
        self.poluation_groupBox.setObjectName(u"poluation_groupBox")
        self.poluation_groupBox.setGeometry(QRect(20, 130, 201, 101))
        self.layoutWidget3 = QWidget(self.poluation_groupBox)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 30, 180, 62))
        self.population_params_layout = QHBoxLayout(self.layoutWidget3)
        self.population_params_layout.setObjectName(u"population_params_layout")
        self.population_params_layout.setContentsMargins(0, 0, 0, 0)
        self.pop_params_label_layout = QVBoxLayout()
        self.pop_params_label_layout.setObjectName(u"pop_params_label_layout")
        self.population_size_label = QLabel(self.layoutWidget3)
        self.population_size_label.setObjectName(u"population_size_label")

        self.pop_params_label_layout.addWidget(self.population_size_label)

        self.infectious_size_label = QLabel(self.layoutWidget3)
        self.infectious_size_label.setObjectName(u"infectious_size_label")

        self.pop_params_label_layout.addWidget(self.infectious_size_label)


        self.population_params_layout.addLayout(self.pop_params_label_layout)

        self.pop_params_spinBox_layout = QVBoxLayout()
        self.pop_params_spinBox_layout.setObjectName(u"pop_params_spinBox_layout")
        self.population_size_spinBox = QSpinBox(self.layoutWidget3)
        self.population_size_spinBox.setObjectName(u"population_size_spinBox")
        sizePolicy1.setHeightForWidth(self.population_size_spinBox.sizePolicy().hasHeightForWidth())
        self.population_size_spinBox.setSizePolicy(sizePolicy1)
        self.population_size_spinBox.setMaximum(99999999)
        self.population_size_spinBox.setValue(10000)

        self.pop_params_spinBox_layout.addWidget(self.population_size_spinBox)

        self.infections_size_spinBox = QSpinBox(self.layoutWidget3)
        self.infections_size_spinBox.setObjectName(u"infections_size_spinBox")
        sizePolicy1.setHeightForWidth(self.infections_size_spinBox.sizePolicy().hasHeightForWidth())
        self.infections_size_spinBox.setSizePolicy(sizePolicy1)
        self.infections_size_spinBox.setMaximum(99999998)
        self.infections_size_spinBox.setValue(1)

        self.pop_params_spinBox_layout.addWidget(self.infections_size_spinBox)


        self.population_params_layout.addLayout(self.pop_params_spinBox_layout)

        self.infection_parameters_groupBox = QGroupBox(self.central_widget)
        self.infection_parameters_groupBox.setObjectName(u"infection_parameters_groupBox")
        self.infection_parameters_groupBox.setGeometry(QRect(20, 240, 201, 101))
        self.layoutWidget4 = QWidget(self.infection_parameters_groupBox)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 30, 181, 61))
        self.v_2 = QHBoxLayout(self.layoutWidget4)
        self.v_2.setObjectName(u"v_2")
        self.v_2.setContentsMargins(0, 0, 0, 0)
        self.inf_param_label_layout = QVBoxLayout()
        self.inf_param_label_layout.setObjectName(u"inf_param_label_layout")
        self.contact_rate_label = QLabel(self.layoutWidget4)
        self.contact_rate_label.setObjectName(u"contact_rate_label")

        self.inf_param_label_layout.addWidget(self.contact_rate_label)

        self.recovery_rate_label = QLabel(self.layoutWidget4)
        self.recovery_rate_label.setObjectName(u"recovery_rate_label")

        self.inf_param_label_layout.addWidget(self.recovery_rate_label)


        self.v_2.addLayout(self.inf_param_label_layout)

        self.inf_param_dspinBox_layout = QVBoxLayout()
        self.inf_param_dspinBox_layout.setObjectName(u"inf_param_dspinBox_layout")
        self.contact_rate_dSpinBox = QDoubleSpinBox(self.layoutWidget4)
        self.contact_rate_dSpinBox.setObjectName(u"contact_rate_dSpinBox")
        sizePolicy1.setHeightForWidth(self.contact_rate_dSpinBox.sizePolicy().hasHeightForWidth())
        self.contact_rate_dSpinBox.setSizePolicy(sizePolicy1)
        self.contact_rate_dSpinBox.setValue(3.000000000000000)

        self.inf_param_dspinBox_layout.addWidget(self.contact_rate_dSpinBox)

        self.recovery_rate_dSpinBox = QDoubleSpinBox(self.layoutWidget4)
        self.recovery_rate_dSpinBox.setObjectName(u"recovery_rate_dSpinBox")
        sizePolicy1.setHeightForWidth(self.recovery_rate_dSpinBox.sizePolicy().hasHeightForWidth())
        self.recovery_rate_dSpinBox.setSizePolicy(sizePolicy1)
        self.recovery_rate_dSpinBox.setValue(1.000000000000000)

        self.inf_param_dspinBox_layout.addWidget(self.recovery_rate_dSpinBox)


        self.v_2.addLayout(self.inf_param_dspinBox_layout)

        self.basic_reproduction_number_label = QLabel(self.central_widget)
        self.basic_reproduction_number_label.setObjectName(u"basic_reproduction_number_label")
        self.basic_reproduction_number_label.setGeometry(QRect(20, 460, 191, 41))
        self.sir_vitality_label = QLabel(self.central_widget)
        self.sir_vitality_label.setObjectName(u"sir_vitality_label")
        self.sir_vitality_label.setEnabled(False)
        self.sir_vitality_label.setGeometry(QRect(10, 10, 221, 121))
        self.sir_vitality_label.setPixmap(QPixmap(u":/Models/resources/images/SIR_classic_endemic_model.png"))
        self.sir_vitality_label.setScaledContents(True)
        self.layoutWidget5 = QWidget(self.central_widget)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(30, 350, 181, 28))
        self.vitality_rate_layout = QHBoxLayout(self.layoutWidget5)
        self.vitality_rate_layout.setSpacing(6)
        self.vitality_rate_layout.setObjectName(u"vitality_rate_layout")
        self.vitality_rate_layout.setContentsMargins(0, 0, 0, 0)
        self.vitality_rate_label = QLabel(self.layoutWidget5)
        self.vitality_rate_label.setObjectName(u"vitality_rate_label")
        self.vitality_rate_label.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.vitality_rate_label.sizePolicy().hasHeightForWidth())
        self.vitality_rate_label.setSizePolicy(sizePolicy2)

        self.vitality_rate_layout.addWidget(self.vitality_rate_label)

        self.vitality_rate_dSpinBox = QDoubleSpinBox(self.layoutWidget5)
        self.vitality_rate_dSpinBox.setObjectName(u"vitality_rate_dSpinBox")
        self.vitality_rate_dSpinBox.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.vitality_rate_dSpinBox.sizePolicy().hasHeightForWidth())
        self.vitality_rate_dSpinBox.setSizePolicy(sizePolicy3)
        self.vitality_rate_dSpinBox.setValue(0.020000000000000)

        self.vitality_rate_layout.addWidget(self.vitality_rate_dSpinBox)

        main_window.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuModel = QMenu(self.menubar)
        self.menuModel.setObjectName(u"menuModel")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuModel.menuAction())
        self.menuFile.addAction(self.perform_action)
        self.menuFile.addAction(self.clear_action)
        self.menuFile.addAction(self.reset_action)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.quit_action)
        self.menuModel.addAction(self.sir_classic_action)
        self.menuModel.addAction(self.sir_vitality_action)

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
        self.sir_classic_action.setText(QCoreApplication.translate("main_window", u"Classic SIR model", None))
        self.sir_vitality_action.setText(QCoreApplication.translate("main_window", u"SIR model with vitality", None))
#if QT_CONFIG(statustip)
        self.dynamics_graph.setStatusTip(QCoreApplication.translate("main_window", u"Dynamics of compartments S, I and R is displayed here", None))
#endif // QT_CONFIG(statustip)
        self.plotting_widget.setTabText(self.plotting_widget.indexOf(self.dynamics_graphpane), QCoreApplication.translate("main_window", u"Compartmental dynamics", None))
#if QT_CONFIG(statustip)
        self.phase_graph.setStatusTip(QCoreApplication.translate("main_window", u"Phase plane I(S) is displayed here", None))
#endif // QT_CONFIG(statustip)
        self.plotting_widget.setTabText(self.plotting_widget.indexOf(self.phase_graphpane), QCoreApplication.translate("main_window", u"Phase plane", None))
#if QT_CONFIG(statustip)
        self.sir_classic_label.setStatusTip(QCoreApplication.translate("main_window", u"The classic endemic model described in a form of a differential equations system", None))
#endif // QT_CONFIG(statustip)
        self.sir_classic_label.setText("")
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
        self.observation_time_groupBox.setTitle(QCoreApplication.translate("main_window", u"Observation time of a population", None))
#if QT_CONFIG(statustip)
        self.ovservation_time_label.setStatusTip(QCoreApplication.translate("main_window", u"Number of days (T) is the time period in which the population is observed", None))
#endif // QT_CONFIG(statustip)
        self.ovservation_time_label.setText(QCoreApplication.translate("main_window", u"Number of days", None))
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
        self.contact_rate_label.setStatusTip(QCoreApplication.translate("main_window", u"Contact rate (\\beta) is the average number of adequate contacts (meaning contacts that are sufficient for transmission)", None))
#endif // QT_CONFIG(statustip)
        self.contact_rate_label.setText(QCoreApplication.translate("main_window", u"Contact rate", None))
#if QT_CONFIG(statustip)
        self.recovery_rate_label.setStatusTip(QCoreApplication.translate("main_window", u"Recovery rate (\\gamma) corresponds to the speed of a person's movement out of the I compartment into R", None))
#endif // QT_CONFIG(statustip)
        self.recovery_rate_label.setText(QCoreApplication.translate("main_window", u"Recovery rate", None))
        self.basic_reproduction_number_label.setText(QCoreApplication.translate("main_window", u"Basic reproduction number:", None))
        self.sir_vitality_label.setText("")
#if QT_CONFIG(statustip)
        self.vitality_rate_label.setStatusTip(QCoreApplication.translate("main_window", u"Vitality rate (\\mu) is the rate of inflow into S, I and R classes (in this model the deaths calance the births)", None))
#endif // QT_CONFIG(statustip)
        self.vitality_rate_label.setText(QCoreApplication.translate("main_window", u"Vitality rate", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
        self.menuModel.setTitle(QCoreApplication.translate("main_window", u"Model", None))
    # retranslateUi
