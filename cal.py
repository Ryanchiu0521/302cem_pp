# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TaxCalculator(object):
    def setupUi(self, TaxCalculator):
        TaxCalculator.setObjectName("TaxCalculator")
        TaxCalculator.resize(1701, 819)
        self.centralwidget = QtWidgets.QWidget(TaxCalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 267, 32))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 266, 24))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 123, 24))
        self.label_3.setObjectName("label_3")
        self.radio_single = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_single.setGeometry(QtCore.QRect(210, 160, 375, 28))
        self.radio_single.setChecked(True)
        self.radio_single.setObjectName("radio_single")
        self.radio_married = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_married.setGeometry(QtCore.QRect(610, 160, 115, 28))
        self.radio_married.setObjectName("radio_married")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 400, 121, 24))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 510, 154, 24))
        self.label_5.setObjectName("label_5")
        self.total_income_self = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.total_income_self.setGeometry(QtCore.QRect(270, 390, 201, 41))
        self.total_income_self.setObjectName("total_income_self")
        self.total_deduction_self = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.total_deduction_self.setGeometry(QtCore.QRect(270, 500, 201, 41))
        self.total_deduction_self.setObjectName("total_deduction_self")
        self.total_income_spouse = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.total_income_spouse.setGeometry(QtCore.QRect(550, 390, 201, 41))
        self.total_income_spouse.setObjectName("total_income_spouse")
        self.total_deduction_spouse = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.total_deduction_spouse.setGeometry(QtCore.QRect(550, 500, 201, 41))
        self.total_deduction_spouse.setObjectName("total_deduction_spouse")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 250, 141, 111))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 250, 141, 111))
        self.label_7.setObjectName("label_7")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(310, 660, 150, 46))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(540, 660, 150, 46))
        self.btn_submit.setObjectName("btn_submit")
        self.result_married = QtWidgets.QTableWidget(self.centralwidget)
        self.result_married.setGeometry(QtCore.QRect(790, 290, 901, 431))
        self.result_married.setObjectName("result_married")
        self.result_married.setColumnCount(3)
        self.result_married.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.result_married.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_married.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_married.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_married.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_married.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_married.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_married.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_married.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_married.setHorizontalHeaderItem(2, item)
        self.result_single = QtWidgets.QTableWidget(self.centralwidget)
        self.result_single.setGeometry(QtCore.QRect(790, 290, 491, 351))
        self.result_single.setObjectName("result_single")
        self.result_single.setColumnCount(1)
        self.result_single.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.result_single.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_single.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_single.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_single.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_single.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_single.setHorizontalHeaderItem(0, item)
        self.label_self = QtWidgets.QLabel(self.centralwidget)
        self.label_self.setGeometry(QtCore.QRect(1160, 240, 38, 24))
        self.label_self.setObjectName("label_self")
        self.label_spouse = QtWidgets.QLabel(self.centralwidget)
        self.label_spouse.setGeometry(QtCore.QRect(1350, 240, 65, 24))
        self.label_spouse.setObjectName("label_spouse")
        self.label_UST = QtWidgets.QLabel(self.centralwidget)
        self.label_UST.setGeometry(QtCore.QRect(1180, 160, 225, 24))
        self.label_UST.setObjectName("label_UST")
        self.label_UJA = QtWidgets.QLabel(self.centralwidget)
        self.label_UJA.setGeometry(QtCore.QRect(1470, 160, 218, 24))
        self.label_UJA.setObjectName("label_UJA")
        self.label_UST2 = QtWidgets.QLabel(self.centralwidget)
        self.label_UST2.setGeometry(QtCore.QRect(790, 750, 380, 24))
        self.label_UST2.setObjectName("label_UST2")
        self.label_UJA2 = QtWidgets.QLabel(self.centralwidget)
        self.label_UJA2.setGeometry(QtCore.QRect(790, 750, 380, 24))
        self.label_UJA2.setObjectName("label_UJA2")
        TaxCalculator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TaxCalculator)
        self.statusbar.setObjectName("statusbar")
        TaxCalculator.setStatusBar(self.statusbar)

        self.retranslateUi(TaxCalculator)
        self.result_married.hide()
        self.result_single.hide()
        self.label_self.hide()
        self.label_spouse.hide()
        self.label_UJA.hide()
        self.label_UJA2.hide()
        self.label_UST.hide()
        self.label_UST2.hide()
        self.btn_reset.clicked.connect(self.resetButton)
        self.btn_submit.clicked.connect(self.submitButton)
        QtCore.QMetaObject.connectSlotsByName(TaxCalculator)

    def retranslateUi(self, TaxCalculator):
        _translate = QtCore.QCoreApplication.translate
        TaxCalculator.setWindowTitle(_translate("TaxCalculator", "MainWindow"))
        self.label.setText(_translate("TaxCalculator", "<html><head/><body><p><span style=\" font-size:10pt;\">Salaries Tax Computation</span></p></body></html>"))
        self.label_2.setText(_translate("TaxCalculator", "Year of assessment   2018/19"))
        self.label_3.setText(_translate("TaxCalculator", "Marital status"))
        self.radio_single.setText(_translate("TaxCalculator", "Single/Separated/Divorced/Widowed"))
        self.radio_married.setText(_translate("TaxCalculator", "Married"))
        self.label_4.setText(_translate("TaxCalculator", "Total Income"))
        self.label_5.setText(_translate("TaxCalculator", "Total Deductions"))
        self.total_income_self.setPlainText(_translate("TaxCalculator", "0"))
        self.total_deduction_self.setPlainText(_translate("TaxCalculator", "0"))
        self.total_income_spouse.setPlainText(_translate("TaxCalculator", "0"))
        self.total_deduction_spouse.setPlainText(_translate("TaxCalculator", "0"))
        self.label_6.setText(_translate("TaxCalculator", "<html><head/><body><p align=\"center\">Self</p><p align=\"center\">HK$</p><p align=\"center\">(Exclude cents)</p></body></html>"))
        self.label_7.setText(_translate("TaxCalculator", "<html><head/><body><p align=\"center\">Spouse</p><p align=\"center\">HK$</p><p align=\"center\">(Exclude cents)</p></body></html>"))
        self.btn_reset.setText(_translate("TaxCalculator", "Reset"))
        self.btn_submit.setText(_translate("TaxCalculator", "Submit"))
        item = self.result_married.verticalHeaderItem(0)
        item.setText(_translate("TaxCalculator", "Total Income"))
        item = self.result_married.verticalHeaderItem(1)
        item.setText(_translate("TaxCalculator", "Total Deductions"))
        item = self.result_married.verticalHeaderItem(2)
        item.setText(_translate("TaxCalculator", "Total Allowances"))
        item = self.result_married.verticalHeaderItem(3)
        item.setText(_translate("TaxCalculator", "Net Chargeable Income"))
        item = self.result_married.verticalHeaderItem(4)
        item.setText(_translate("TaxCalculator", "Tax Payable"))
        item = self.result_married.verticalHeaderItem(5)
        item.setText(_translate("TaxCalculator", "Total Tax"))
        item = self.result_married.horizontalHeaderItem(0)
        item.setText(_translate("TaxCalculator", "HK$"))
        item = self.result_married.horizontalHeaderItem(1)
        item.setText(_translate("TaxCalculator", "HK$"))
        item = self.result_married.horizontalHeaderItem(2)
        item.setText(_translate("TaxCalculator", "HK$"))
        item = self.result_single.verticalHeaderItem(0)
        item.setText(_translate("TaxCalculator", "Total Income"))
        item = self.result_single.verticalHeaderItem(1)
        item.setText(_translate("TaxCalculator", "Total Deductions"))
        item = self.result_single.verticalHeaderItem(2)
        item.setText(_translate("TaxCalculator", "Total Allowances"))
        item = self.result_single.verticalHeaderItem(3)
        item.setText(_translate("TaxCalculator", "Net Chargeable Income"))
        item = self.result_single.verticalHeaderItem(4)
        item.setText(_translate("TaxCalculator", "Tax Payable"))
        item = self.result_single.horizontalHeaderItem(0)
        item.setText(_translate("TaxCalculator", "HK$"))
        self.label_self.setText(_translate("TaxCalculator", "Self"))
        self.label_spouse.setText(_translate("TaxCalculator", "Spouse"))
        self.label_UST.setText(_translate("TaxCalculator", "Under Separate Taxation"))
        self.label_UJA.setText(_translate("TaxCalculator", "Under Joint Assessment"))
        self.label_UST2.setText(_translate("TaxCalculator", "Under Separate Taxation is recommended"))
        self.label_UJA2.setText(_translate("TaxCalculator", "Under Joint Assessment is recommended"))

    def resetButton(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        self.total_income_self.setPlainText(_translate("MainWindow", "0"))
        self.total_deduction_self.setPlainText(_translate("MainWindow", "0"))
        self.total_income_spouse.setPlainText(_translate("MainWindow", "0"))
        self.total_deduction_spouse.setPlainText(_translate("MainWindow", "0"))

    def submitButton(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate

        if self.radio_single.isChecked():
            self.result_married.hide()
            self.result_single.show()
            self.label_self.show()
            self.label_spouse.hide()
            self.label_UJA.hide()
            self.label_UST.hide()
            self.label_UJA2.hide()
            self.label_UST2.hide()
        else:
            self.result_single.hide()
            self.result_married.show()
            self.label_self.show()
            self.label_spouse.show()
            self.label_UJA.show()
            self.label_UST.show()
            self.label_UJA2.hide()
            self.label_UST2.hide()

        if self.radio_single.isChecked():
            single_income = int(self.total_income_self.toPlainText())
            single_deduction = int(self.total_deduction_self.toPlainText())

            mpf = 0
            if single_income/12 < 7100:
                mpf = 0
            elif single_income/12 >= 7100 and single_income/12 <= 30000:
                mpf = (single_income/12 * 0.05)*12
            elif single_income/12 > 30000:
                mpf = 1500 * 12

            self_net_income = single_income - single_deduction - mpf

            self.result_single.setItem(0, 0, QtWidgets.QTableWidgetItem(str(single_income)))
            self.result_single.setItem(0, 1, QtWidgets.QTableWidgetItem(str(single_deduction)))
            self.result_single.setItem(0, 2, QtWidgets.QTableWidgetItem(str(int(132000))))
            self.result_single.setItem(0, 3, QtWidgets.QTableWidgetItem(str(int(self_net_income - 132000))))

            if self_net_income >= 132000:
                if self_net_income > 2022000:
                    tax = (self_net_income) * 0.15
                    self.result_single.setItem(0, 3, QtWidgets.QTableWidgetItem(str(int(self_net_income + 18000))))
                    self.result_single.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(tax))))
                elif self_net_income - 132000 >= 50000:
                    tax = 50000 * 0.02
                    self_net_income = self_net_income - 132000 - 50000
                    if self_net_income - 50000 - mpf >= 0:
                        tax = tax + 50000 * 0.06
                        self_net_income = self_net_income - 50000
                        self.result_single.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(tax))))
                        if self_net_income - 50000 >= 0:
                            tax = tax + 50000 * 0.10
                            self_net_income = self_net_income - 50000
                            self.result_single.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(tax))))
                            if self_net_income - 50000 >= 0:
                                tax = tax + 50000 * 0.14
                                self_net_income = self_net_income - 50000
                                self.result_single.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(tax))))
                                if self_net_income >= 0:
                                    tax = tax + self_net_income * 0.17
                                    self.result_single.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(tax))))
                                else:
                                    tax = tax + self_net_income * 0.17
                                    self.result_single.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(tax))))
                            else:
                                tax = tax + self_net_income * 0.14
                                self.result_single.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(tax))))
                        else:
                            tax = tax + self_net_income * 0.1
                            self.result_single.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(tax))))
                    else:
                        tax = tax + self_net_income * 0.06
                        self.result_single.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(tax))))
                else:
                    tax = (self_net_income - 132000) * 0.02
                    self.result_single.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(tax))))
            elif self_net_income <= 132000:
                 self.result_single.setItem(0, 3, QtWidgets.QTableWidgetItem(str(int(0))))
                 self.result_single.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(0))))

        if self.radio_married.isChecked():
            single_income = int(self.total_income_self.toPlainText())
            single_deduction = int(self.total_deduction_self.toPlainText())
            spouse_income = int(self.total_income_spouse.toPlainText())
            spouse_deduction = int(self.total_deduction_spouse.toPlainText())

            mpf = 0
            if single_income/12 < 7100:
                mpf = 0
            elif single_income/12 >= 7100 and single_income/12 <= 30000:
                mpf = (single_income/12 * 0.05)*12
            elif single_income/12 > 30000:
                mpf = 1500 * 12

            mpf2 = 0
            if spouse_income/12 < 7100:
                mpf2 = 0
            elif spouse_income/12 >= 7100 and spouse_income/12 <= 30000:
                mpf2 = (spouse_income/12 * 0.05)*12
            elif spouse_income/12 > 30000:
                mpf2 = 1500 * 12

            self_net_income = single_income - single_deduction - mpf
            spouse_net_income = spouse_income - spouse_deduction - mpf2
            Joint_net_income = single_income + spouse_income - single_deduction - mpf - spouse_deduction - mpf2

            self.result_married.setItem(0, 0, QtWidgets.QTableWidgetItem(str(int(single_income))))
            self.result_married.setItem(0, 1, QtWidgets.QTableWidgetItem(str(int(spouse_income))))
            self.result_married.setItem(0, 2, QtWidgets.QTableWidgetItem(str(int(single_income + spouse_income))))
            self.result_married.setItem(0, 3, QtWidgets.QTableWidgetItem(str(single_deduction)))
            self.result_married.setItem(0, 4, QtWidgets.QTableWidgetItem(str(spouse_deduction)))
            self.result_married.setItem(0, 5, QtWidgets.QTableWidgetItem(str(single_deduction + spouse_deduction)))
            self.result_married.setItem(0, 6, QtWidgets.QTableWidgetItem(str(int(132000))))
            self.result_married.setItem(0, 7, QtWidgets.QTableWidgetItem(str(int(132000))))
            self.result_married.setItem(0, 8, QtWidgets.QTableWidgetItem(str(int(264000))))
            self.result_married.setItem(0, 9, QtWidgets.QTableWidgetItem(str(int(self_net_income - 132000))))
            self.result_married.setItem(0, 10, QtWidgets.QTableWidgetItem(str(int(spouse_net_income - 132000))))
            self.result_married.setItem(0, 11, QtWidgets.QTableWidgetItem(str(int(self_net_income + spouse_net_income - 264000 ))))

            tax = int(0)
            tax1 = int(0)
            if self_net_income >= 132000:
                if self_net_income > 2022000:
                    tax = (self_net_income) * 0.15
                    self.result_married.setItem(0, 3, QtWidgets.QTableWidgetItem(str(int(self_net_income + 18000))))
                    self.result_married.setItem(0, 12, QtWidgets.QTableWidgetItem(str(int(tax))))
                elif self_net_income - 132000 >= 50000:
                    tax = 50000 * 0.02
                    self_net_income = self_net_income - 132000 - 50000
                    if self_net_income - 50000 - mpf >= 0:
                        tax = tax + 50000 * 0.06
                        self_net_income = self_net_income - 50000
                        self.result_married.setItem(0, 12, QtWidgets.QTableWidgetItem(str(int(tax))))
                        if self_net_income - 50000 >= 0:
                            tax = tax + 50000 * 0.10
                            self_net_income = self_net_income - 50000
                            self.result_married.setItem(0, 12, QtWidgets.QTableWidgetItem(str(int(tax))))
                            if self_net_income - 50000 >= 0:
                                tax = tax + 50000 * 0.14
                                self_net_income = self_net_income - 50000
                                self.result_married.setItem(0, 12, QtWidgets.QTableWidgetItem(str(int(tax))))
                                if self_net_income >= 0:
                                    tax = tax + self_net_income * 0.17
                                    self.result_married.setItem(0, 12, QtWidgets.QTableWidgetItem(str(int(tax))))
                                else:
                                    tax = tax + self_net_income * 0.17
                                    self.result_married.setItem(0, 12, QtWidgets.QTableWidgetItem(str(int(tax))))
                            else:
                                tax = tax + self_net_income * 0.14
                                self.result_married.setItem(0, 12, QtWidgets.QTableWidgetItem(str(int(tax))))
                        else:
                            tax = tax + self_net_income * 0.1
                            self.result_married.setItem(0, 12, QtWidgets.QTableWidgetItem(str(int(tax))))
                    else:
                        tax = tax + self_net_income * 0.06
                        self.result_married.setItem(0, 12, QtWidgets.QTableWidgetItem(str(int(tax))))
                else:
                    tax = (self_net_income - 132000) * 0.02
                    self.result_married.setItem(0, 12, QtWidgets.QTableWidgetItem(str(int(tax))))
            elif self_net_income <= 132000:
                 self.result_married.setItem(0, 9, QtWidgets.QTableWidgetItem(str(int(0))))
                 self.result_married.setItem(0, 12, QtWidgets.QTableWidgetItem(str(int(0))))

            if spouse_net_income >= 132000:
                if spouse_net_income > 2022000:
                    tax1 = (spouse_net_income) * 0.15
                    self.result_married.setItem(0, 4, QtWidgets.QTableWidgetItem(str(int(spouse_net_income + 18000))))
                    self.result_married.setItem(0, 13, QtWidgets.QTableWidgetItem(str(int(tax1))))
                elif spouse_net_income - 132000 >= 50000:
                    tax1 = 50000 * 0.02
                    spouse_net_income = spouse_net_income - 132000 - 50000
                    if spouse_net_income - 50000 - mpf2 >= 0:
                        tax1 = tax1 + 50000 * 0.06
                        spouse_net_income = spouse_net_income - 50000
                        self.result_married.setItem(0, 13, QtWidgets.QTableWidgetItem(str(int(tax1))))
                        if spouse_net_income- 50000 >= 0:
                            tax1 = tax1 + 50000 * 0.10
                            spouse_net_income = spouse_net_income - 50000
                            self.result_married.setItem(0, 13, QtWidgets.QTableWidgetItem(str(int(tax1))))
                            if spouse_net_income - 50000 >= 0:
                                tax1 = tax1 + 50000 * 0.14
                                spouse_net_income = spouse_net_income - 50000
                                self.result_married.setItem(0, 13, QtWidgets.QTableWidgetItem(str(int(tax1))))
                                if spouse_net_income >= 0:
                                    tax1 = tax1 + spouse_net_income * 0.17
                                    self.result_married.setItem(0, 13, QtWidgets.QTableWidgetItem(str(int(tax1))))
                                else:
                                    tax1 = tax1 + spouse_net_income * 0.17
                                    self.result_married.setItem(0, 13, QtWidgets.QTableWidgetItem(str(int(tax1))))
                            else:
                                tax1 = tax1 + spouse_net_income * 0.14
                                self.result_married.setItem(0, 13, QtWidgets.QTableWidgetItem(str(int(tax1))))
                        else:
                            tax1 = tax1 + spouse_net_income * 0.1
                            self.result_married.setItem(0, 13, QtWidgets.QTableWidgetItem(str(int(tax1))))
                    else:
                        tax1 = tax1 + spouse_net_income * 0.06
                        self.result_married.setItem(0, 13, QtWidgets.QTableWidgetItem(str(int(tax1))))
                else:
                    tax1 = (spouse_net_income - 132000) * 0.02
                    self.result_married.setItem(0, 13, QtWidgets.QTableWidgetItem(str(int(tax1))))
            elif spouse_net_income <= 132000:
                self.result_married.setItem(0, 10, QtWidgets.QTableWidgetItem(str(int(0))))
                self.result_married.setItem(0, 13, QtWidgets.QTableWidgetItem(str(int(0))))
            self.result_married.setItem(0, 15, QtWidgets.QTableWidgetItem(str(int(tax + tax1))))

            tax2 = int(0)
            if Joint_net_income >= 264000:
                if Joint_net_income > 2022000:
                    tax2 = (Joint_net_income) * 0.15
                    self.result_married.setItem(0, 14, QtWidgets.QTableWidgetItem(str(int(tax1 + tax))))
                    self.result_married.setItem(0, 17, QtWidgets.QTableWidgetItem(str(int(tax2))))
                elif Joint_net_income - 264000 >= 50000:
                    tax2 = 50000 * 0.02
                    Joint_net_income = Joint_net_income - 264000 - 50000
                    if Joint_net_income - 50000 >= 0:
                        tax2 = tax2 + 50000 * 0.06
                        Joint_net_income = Joint_net_income - 50000
                        self.result_married.setItem(0, 14, QtWidgets.QTableWidgetItem(str(int(tax2))))
                        self.result_married.setItem(0, 17, QtWidgets.QTableWidgetItem(str(int(tax2))))
                        if Joint_net_income - 50000 >= 0:
                            tax2 = tax2 + 50000 * 0.10
                            Joint_net_income = Joint_net_income - 50000
                            self.result_married.setItem(0, 14, QtWidgets.QTableWidgetItem(str(int(tax2))))
                            self.result_married.setItem(0, 17, QtWidgets.QTableWidgetItem(str(int(tax2))))
                            if Joint_net_income- 50000 >= 0:
                                tax2 = tax2 + 50000 * 0.14
                                Joint_net_income = Joint_net_income - 50000
                                self.result_married.setItem(0, 14, QtWidgets.QTableWidgetItem(str(int(tax2))))
                                self.result_married.setItem(0, 17, QtWidgets.QTableWidgetItem(str(int(tax2))))
                                if Joint_net_income >= 0:
                                    tax2 = tax2 + Joint_net_income * 0.17
                                    self.result_married.setItem(0, 14, QtWidgets.QTableWidgetItem(str(int(tax2))))
                                    self.result_married.setItem(0, 17, QtWidgets.QTableWidgetItem(str(int(tax2))))
                                else:
                                    tax2 = tax2 + Joint_net_income * 0.17
                                    self.result_married.setItem(0, 14, QtWidgets.QTableWidgetItem(str(int(tax2))))
                                    self.result_married.setItem(0, 17, QtWidgets.QTableWidgetItem(str(int(tax2))))
                            else:
                                tax2 = tax2 + Joint_net_income * 0.14
                                self.result_married.setItem(0, 14, QtWidgets.QTableWidgetItem(str(int(tax2))))
                                self.result_married.setItem(0, 17, QtWidgets.QTableWidgetItem(str(int(tax2))))
                        else:
                            tax2 = tax2 + Joint_net_income * 0.1
                            self.result_married.setItem(0, 14, QtWidgets.QTableWidgetItem(str(int(tax2))))
                            self.result_married.setItem(0, 17, QtWidgets.QTableWidgetItem(str(int(tax2))))
                    else:
                        tax2 = tax2 + Joint_net_income * 0.06
                        self.result_married.setItem(0, 14, QtWidgets.QTableWidgetItem(str(int(tax2))))
                        self.result_married.setItem(0, 17, QtWidgets.QTableWidgetItem(str(int(tax2))))
                else:
                    tax2 = (Joint_net_income - 264000) * 0.02
                    self.result_married.setItem(0, 14, QtWidgets.QTableWidgetItem(str(int(tax2))))
                    self.result_married.setItem(0, 17, QtWidgets.QTableWidgetItem(str(int(tax2))))
            elif Joint_net_income < 264000:
                self.result_married.setItem(0, 14, QtWidgets.QTableWidgetItem(str(int(0))))
                self.result_married.setItem(0, 17, QtWidgets.QTableWidgetItem(str(int(0))))

            if tax > tax2:
                self.label_UJA2.show()
                self.label_UST2.hide()
            elif tax == tax2:
                self.label_UST2.hide()
                self.label_UJA2.hide()
            elif tax < tax2:
                self.label_UST2.show()
                self.label_UJA2.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TaxCalculator = QtWidgets.QMainWindow()
    ui = Ui_TaxCalculator()
    ui.setupUi(TaxCalculator)
    TaxCalculator.show()
    sys.exit(app.exec_())
