# -*- Coding: utf-8 -*-
import pickle
import re
import csv
import os
from time import time
import fitz
import fnmatch
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(824, 377)
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, -40, 812, 421))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.input_type = QComboBox(self.layoutWidget)
        self.input_type.addItem("")
        self.input_type.addItem("")
        self.input_type.addItem("")
        self.input_type.addItem("")
        self.input_type.setObjectName(u"input_type")
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.input_type.setFont(font1)

        self.horizontalLayout_2.addWidget(self.input_type)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.input_text = QLineEdit(self.layoutWidget)
        self.input_text.setObjectName(u"input_text")

        self.horizontalLayout_2.addWidget(self.input_text)

        self.clean_button = QPushButton(self.layoutWidget)
        self.clean_button.setObjectName(u"clean_button")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.clean_button.setFont(font2)

        self.horizontalLayout_2.addWidget(self.clean_button)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 6, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.output_text = QTextEdit(self.layoutWidget)
        self.output_text.setObjectName(u"output_text")
        font3 = QFont()
        font3.setFamilies([u"\u5b8b\u4f53"])
        self.output_text.setFont(font3)

        self.horizontalLayout_4.addWidget(self.output_text)

        self.clean_output = QPushButton(self.layoutWidget)
        self.clean_output.setObjectName(u"clean_output")
        self.clean_output.setFont(font2)

        self.horizontalLayout_4.addWidget(self.clean_output)


        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout.addWidget(self.label_9)

        self.dict_name = QLineEdit(self.layoutWidget)
        self.dict_name.setObjectName(u"dict_name")

        self.horizontalLayout.addWidget(self.dict_name)

        self.clean_dict_name = QPushButton(self.layoutWidget)
        self.clean_dict_name.setObjectName(u"clean_dict_name")
        self.clean_dict_name.setFont(font2)

        self.horizontalLayout.addWidget(self.clean_dict_name)

        self.new_dict = QPushButton(self.layoutWidget)
        self.new_dict.setObjectName(u"new_dict")
        self.new_dict.setFont(font)

        self.horizontalLayout.addWidget(self.new_dict)

        self.append_dict = QPushButton(self.layoutWidget)
        self.append_dict.setObjectName(u"append_dict")
        self.append_dict.setFont(font)

        self.horizontalLayout.addWidget(self.append_dict)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setFamilies([u"\u5b8b\u4f53"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.load_dict = QPushButton(self.layoutWidget)
        self.load_dict.setObjectName(u"load_dict")
        self.load_dict.setFont(font)

        self.horizontalLayout_5.addWidget(self.load_dict)

        self.line_7 = QFrame(self.layoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_7)

        self.start_ner = QPushButton(self.layoutWidget)
        self.start_ner.setObjectName(u"start_ner")
        self.start_ner.setFont(font)

        self.horizontalLayout_5.addWidget(self.start_ner)

        self.line_6 = QFrame(self.layoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_6)

        self.ner_output = QPushButton(self.layoutWidget)
        self.ner_output.setObjectName(u"ner_output")
        self.ner_output.setFont(font)

        self.horizontalLayout_5.addWidget(self.ner_output)


        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 824, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionhelp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Input Type\uff1a", None))
        self.input_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Text", None))
        self.input_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Dictionary", None))
        self.input_type.setItemText(2, QCoreApplication.translate("MainWindow", u"File", None))
        self.input_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Folder", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Input Text or Path\uff1a", None))
        self.clean_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Procedural implementation:", None))
        self.clean_output.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Input Dictionary\uff1a", None))
        self.clean_dict_name.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.new_dict.setText(QCoreApplication.translate("MainWindow", u"Create Dictionary", None))
        self.append_dict.setText(QCoreApplication.translate("MainWindow", u"Add to Dictionary", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Chemical Entity Recognition System for English Literature", None))
        self.load_dict.setText(QCoreApplication.translate("MainWindow", u"Load Dictionary", None))
        self.start_ner.setText(QCoreApplication.translate("MainWindow", u"Start Recognition", None))
        self.ner_output.setText(QCoreApplication.translate("MainWindow", u"Recognize and Output File", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"help", None))


def delete_characters(token_words):
    words_lists = [x.lower() for x in token_words]
    words_lists = [x.replace('.', '') for x in words_lists]
    words_lists = [x.replace('‘', '\'') for x in words_lists]
    words_lists = [x.replace('：', ':') for x in words_lists]
    words_lists = [x.replace(';', '') for x in words_lists]
    words_lists = [x.replace('?', '') for x in words_lists]
    words_lists = [x.replace('\"', '\'') for x in words_lists]
    words_lists = [x.replace('&', '') for x in words_lists]
    words_lists = [x.replace('*', '') for x in words_lists]
    words_lists = [x.replace('@', '') for x in words_lists]
    words_lists = [x.replace('!', '') for x in words_lists]
    words_lists = [x.replace('#', '') for x in words_lists]
    words_lists = [x.replace('%', '') for x in words_lists]
    words_lists = [x.replace('^', '') for x in words_lists]
    words_lists = [x.strip(',') for x in words_lists]
    return words_lists


def delete_characters_upper(token_words):
    words_lists = [x.replace('.', '') for x in token_words]
    words_lists = [x.replace('‘', '\'') for x in words_lists]
    words_lists = [x.replace('：', ':') for x in words_lists]
    words_lists = [x.replace(';', '') for x in words_lists]
    words_lists = [x.replace('?', '') for x in words_lists]
    words_lists = [x.replace('\"', '\'') for x in words_lists]
    words_lists = [x.replace('&', '') for x in words_lists]
    words_lists = [x.replace('*', '') for x in words_lists]
    words_lists = [x.replace('@', '') for x in words_lists]
    words_lists = [x.replace('!', '') for x in words_lists]
    words_lists = [x.replace('#', '') for x in words_lists]
    words_lists = [x.replace('%', '') for x in words_lists]
    words_lists = [x.replace('^', '') for x in words_lists]
    words_lists = [x.strip(',') for x in words_lists]
    return words_lists


def get_pdf_text(filepath):
    with fitz.open(filepath) as pdf:
        file_content = ''
        for page in pdf:
            file_content += page.get_text()
            file_content += ' '
    return file_content


def clean_text(content):
    content = content.strip()
    content = content.replace('\n', ' ')
    return content


class GenerateDict(object):
    """
    The main functions of GenerateDict are to create new dictionaries and append dictionaries,
    which are used to build dictionaries that meet the rules for recognizing named entities in the next step
    """
    def __init__(self, get_filepath, get_dict_name='initial'):
        """
        :param get_filepath: Path to the file you entered to create a new or additional dictionary
        :param get_dict_name: Dictionary series name set, default is 'initial'
        (dictionary series containing 7.85 million chemical names), can be set according to the user's needs
        """
        self.get_filepath = get_filepath
        self.get_dict_name = get_dict_name
        name_sid_cid = {}
        lower_name_upper = {}
        upper_name_lower = {}
        one_chemical_list = []
        two_chemical_list = []
        three_chemical_list = []
        multi_chemical_list = []
        pre_two_chemical = []
        pre_three_chemical = []
        two_repeat_one = []
        three_repeat_one = []
        self.one_chemical_list = one_chemical_list
        self.two_chemical_list = two_chemical_list
        self.three_chemical_list = three_chemical_list
        self.multi_chemical_list = multi_chemical_list
        self.pre_two_chemical = pre_two_chemical
        self.pre_three_chemical = pre_three_chemical
        self.two_repeat_one = two_repeat_one
        self.three_repeat_one = three_repeat_one
        self.name_sid_cid = name_sid_cid
        self.lower_name_upper = lower_name_upper
        self.upper_name_lower = upper_name_lower

    def new_dict(self):
        """
        New dictionary module, the new dictionary file must contain chemical name, CAS, sid, cid and other information,
        if there is no corresponding information can be left blank.
        """
        with open(self.get_filepath, 'r', encoding='utf-8-sig') as f:
            csv_reader = csv.reader(f)
            tmp_i = 0
            for rows in csv_reader:
                if tmp_i != 0:
                    name = rows[0]
                    cas = rows[1]
                    sid = rows[2]
                    cid = rows[3]
                    name = name.replace('[', '(')
                    name = name.replace(']', ')')
                    name_split = name.split()
                    clean_name_list = delete_characters(name_split)
                    if len(clean_name_list) == 1:
                        self.one_chemical_list.append(clean_name_list[0])
                        self.name_sid_cid[clean_name_list[0]] = {'cas': cas, 'sid': sid, 'cid': cid}
                        self.lower_name_upper[clean_name_list[0]] = name
                        self.upper_name_lower[name] = clean_name_list[0]
                    elif len(clean_name_list) == 2:
                        self.pre_two_chemical.append(clean_name_list[0])
                        ture_name = clean_name_list[0] + ' ' + clean_name_list[1]
                        self.two_chemical_list.append(ture_name)
                        self.name_sid_cid[ture_name] = {'cas': cas, 'sid': sid, 'cid': cid}
                        self.lower_name_upper[ture_name] = name
                        self.upper_name_lower[name] = ture_name
                    elif len(clean_name_list) == 3:
                        ture_name = clean_name_list[0] + ' ' + clean_name_list[1] + ' ' + clean_name_list[2]
                        self.pre_three_chemical.append(clean_name_list[0])
                        self.three_chemical_list.append(ture_name)
                        self.name_sid_cid[ture_name] = {'cas': cas, 'sid': sid, 'cid': cid}
                        self.lower_name_upper[ture_name] = name
                        self.upper_name_lower[name] = ture_name
                    elif len(clean_name_list) >= 4:
                        self.multi_chemical_list.append(name)
                        self.name_sid_cid[name] = {'cas': cas, 'sid': sid, 'cid': cid}
                else:
                    tmp_i += 1
        for word in self.pre_two_chemical:
            if word not in self.two_repeat_one and word in self.one_chemical_list:
                self.two_repeat_one.append(word)
        for word in self.pre_three_chemical:
            if word not in self.three_repeat_one and word in self.one_chemical_list:
                self.three_repeat_one.append(word)
        save_path = self.save_file()
        print('---New Dictionary Successfully Created---')
        return save_path

    def append_dict(self):
        """
        Append dictionary module, similar to the new dictionary module, the input file must contain chemical name,
        CAS, sid, cid and other information, if there is no corresponding information can be left blank.
        :return:
        """
        current_path = os.getcwd()
        pkl_filepath = current_path + '\\' + self.get_dict_name + '\\' + 'name_sid_cid.pkl'
        with open(pkl_filepath, 'rb') as r1:
            self.name_sid_cid = pickle.load(r1)
        with open(self.get_filepath, 'r', encoding='utf-8-sig') as f:
            csv_reader = csv.reader(f)
            tmp_i = 0
            for rows in csv_reader:
                if tmp_i != 0:
                    name = rows[0]
                    cas = rows[1]
                    sid = rows[2]
                    cid = rows[3]
                    name = name.replace('[', '(')
                    name = name.replace(']', ')')
                    name_split = name.split()
                    clean_name_list = delete_characters(name_split)
                    if len(clean_name_list) == 1:
                        if clean_name_list[0] not in self.name_sid_cid:
                            self.one_chemical_list.append(clean_name_list[0])
                            self.name_sid_cid[clean_name_list[0]] = {'cas': cas, 'sid': sid, 'cid': cid}
                            self.lower_name_upper[clean_name_list[0]] = name
                            self.upper_name_lower[name] = clean_name_list[0]
                    elif len(clean_name_list) == 2:
                        ture_name = clean_name_list[0] + ' ' + clean_name_list[1]
                        if ture_name not in self.name_sid_cid:
                            self.pre_two_chemical.append(clean_name_list[0])
                            self.two_chemical_list.append(ture_name)
                            self.name_sid_cid[ture_name] = {'cas': cas, 'sid': sid, 'cid': cid}
                            self.lower_name_upper[ture_name] = name
                            self.upper_name_lower[name] = ture_name
                    elif len(clean_name_list) == 3:
                        ture_name = clean_name_list[0] + ' ' + clean_name_list[1] + ' ' + clean_name_list[2]
                        if ture_name not in self.name_sid_cid:
                            self.pre_three_chemical.append(clean_name_list[0])
                            self.three_chemical_list.append(ture_name)
                            self.name_sid_cid[ture_name] = {'cas': cas, 'sid': sid, 'cid': cid}
                            self.lower_name_upper[ture_name] = name
                            self.upper_name_lower[name] = ture_name
                    elif len(clean_name_list) >= 4:
                        self.multi_chemical_list.append(name)
                        self.name_sid_cid[name] = {'cas': cas, 'sid': sid, 'cid': cid}
                else:
                    tmp_i += 1
        for word in self.pre_two_chemical:
            if word not in self.two_repeat_one and word in self.one_chemical_list:
                self.two_repeat_one.append(word)
        for word in self.pre_three_chemical:
            if word not in self.three_repeat_one and word in self.one_chemical_list:
                self.three_repeat_one.append(word)
        save_path = self.save_file()
        print('---Additional Dictionary Success---')
        return save_path

    def save_file(self):
        """
        Save Dictionary File
        """
        set_one_chemical_list = set(self.one_chemical_list)
        set_two_chemical_list = set(self.two_chemical_list)
        set_three_chemical_list = set(self.three_chemical_list)
        set_multi_chemical_list = set(self.multi_chemical_list)
        set_pre_two_chemical = set(self.pre_two_chemical)
        set_pre_three_chemical = set(self.pre_three_chemical)
        set_two_repeat_one = set(self.two_repeat_one)
        set_three_repeat_one = set(self.three_repeat_one)
        folder_name = self.get_dict_name
        current_path = os.getcwd()
        dict_filepath = current_path + '\\' + folder_name
        if not os.path.exists(dict_filepath):
            os.makedirs(dict_filepath)
        one_chemical_list_save_path = dict_filepath + '\\' + 'one_chemical_list' + '.txt'
        two_chemical_list_save_path = dict_filepath + '\\' + 'two_chemical_list' + '.txt'
        three_chemical_list_save_pat = dict_filepath + '\\' + 'three_chemical_list' + '.txt'
        multi_chemical_list_save_pat = dict_filepath + '\\' + 'multi_chemical_list' + '.txt'
        pre_two_chemical_save_pat = dict_filepath + '\\' + 'pre_two_chemical' + '.txt'
        pre_three_chemical_save_pat = dict_filepath + '\\' + 'pre_three_chemical' + '.txt'
        two_repeat_one_save_pat = dict_filepath + '\\' + 'two_repeat_one' + '.txt'
        three_repeat_one_save_pat = dict_filepath + '\\' + 'three_repeat_one' + '.txt'
        name_sid_cid_save_pat = dict_filepath + '\\' + 'name_sid_cid' + '.pkl'
        lower_name_upper_save_pat = dict_filepath + '\\' + 'lower_name_upper' + '.pkl'
        upper_name_lower_save_pat = dict_filepath + '\\' + 'upper_name_lower' + '.pkl'
        with open(one_chemical_list_save_path, 'a', encoding='utf-8') as f1:
            for word in set_one_chemical_list:
                f1.write(word + '\n')
        with open(two_chemical_list_save_path, 'a', encoding='utf-8') as f2:
            for word in set_two_chemical_list:
                f2.write(word + '\n')
        with open(three_chemical_list_save_pat, 'a', encoding='utf-8') as f3:
            for word in set_three_chemical_list:
                f3.write(word + '\n')
        with open(multi_chemical_list_save_pat, 'a', encoding='utf-8') as f4:
            for word in set_multi_chemical_list:
                f4.write(word + '\n')
        with open(pre_two_chemical_save_pat, 'a', encoding='utf-8') as f5:
            for word in set_pre_two_chemical:
                f5.write(word + '\n')
        with open(pre_three_chemical_save_pat, 'a', encoding='utf-8') as f6:
            for word in set_pre_three_chemical:
                f6.write(word + '\n')
        with open(two_repeat_one_save_pat, 'a', encoding='utf-8') as f7:
            for word in set_two_repeat_one:
                f7.write(word + '\n')
        with open(three_repeat_one_save_pat, 'a', encoding='utf-8') as f8:
            for word in set_three_repeat_one:
                f8.write(word + '\n')
        with open(name_sid_cid_save_pat, 'wb') as w1:
            pickle.dump(self.name_sid_cid, w1)
        with open(lower_name_upper_save_pat, 'wb') as w2:
            pickle.dump(self.lower_name_upper, w2)
        with open(upper_name_lower_save_pat, 'wb') as w3:
            pickle.dump(self.upper_name_lower, w3)
        print('---The file was saved successfully, and the storage path is %s---' % dict_filepath)
        return dict_filepath


class ChemicalNER(object):
    def __init__(self, get_dict_name='initial'):
        self.get_dict_name = get_dict_name
        one_chemical_list = {}
        two_chemical_list = {}
        three_chemical_list = {}
        multi_chemical_list = {}
        pre_two_chemical = {}
        pre_three_chemical = {}
        two_repeat_one = {}
        three_repeat_one = {}
        self.one_chemical_list = one_chemical_list
        self.two_chemical_list = two_chemical_list
        self.three_chemical_list = three_chemical_list
        self.multi_chemical_list = multi_chemical_list
        self.pre_two_chemical = pre_two_chemical
        self.pre_three_chemical = pre_three_chemical
        self.two_repeat_one = two_repeat_one
        self.three_repeat_one = three_repeat_one
        self.name_sid_cid = {}
        self.lower_name_upper = {}
        self.upper_name_lower = {}
        self.load_dict()

    def load_dict(self):
        folder_name = self.get_dict_name
        current_path = os.getcwd()
        dict_filepath = current_path + '\\' + folder_name
        one_chemical_list_save_path = dict_filepath + '\\' + 'one_chemical_list' + '.txt'
        two_chemical_list_save_path = dict_filepath + '\\' + 'two_chemical_list' + '.txt'
        three_chemical_list_save_pat = dict_filepath + '\\' + 'three_chemical_list' + '.txt'
        multi_chemical_list_save_pat = dict_filepath + '\\' + 'multi_chemical_list' + '.txt'
        pre_two_chemical_save_pat = dict_filepath + '\\' + 'pre_two_chemical' + '.txt'
        pre_three_chemical_save_pat = dict_filepath + '\\' + 'pre_three_chemical' + '.txt'
        two_repeat_one_save_pat = dict_filepath + '\\' + 'two_repeat_one' + '.txt'
        three_repeat_one_save_pat = dict_filepath + '\\' + 'three_repeat_one' + '.txt'
        name_sid_cid_save_pat = dict_filepath + '\\' + 'name_sid_cid' + '.pkl'
        lower_name_upper_save_pat = dict_filepath + '\\' + 'lower_name_upper' + '.pkl'
        upper_name_lower_save_pat = dict_filepath + '\\' + 'upper_name_lower' + '.pkl'
        with open(one_chemical_list_save_path, 'r', encoding='utf-8') as f1:
            for line in f1.readlines():
                line = line.strip()
                self.one_chemical_list[line] = 1
        with open(two_chemical_list_save_path, 'r', encoding='utf-8') as f2:
            for line in f2.readlines():
                line = line.strip()
                self.two_chemical_list[line] = 1
        with open(three_chemical_list_save_pat, 'r', encoding='utf-8') as f3:
            for line in f3.readlines():
                line = line.strip()
                self.three_chemical_list[line] = 1
        with open(multi_chemical_list_save_pat, 'r', encoding='utf-8') as f4:
            for line in f4.readlines():
                line = line.strip()
                self.multi_chemical_list[line] = 1
        with open(pre_two_chemical_save_pat, 'r', encoding='utf-8') as f5:
            for line in f5.readlines():
                line = line.strip()
                self.pre_two_chemical[line] = 1
        with open(pre_three_chemical_save_pat, 'r', encoding='utf-8') as f6:
            for line in f6.readlines():
                line = line.strip()
                self.pre_three_chemical[line] = 1
        with open(two_repeat_one_save_pat, 'r', encoding='utf-8') as f7:
            for line in f7.readlines():
                line = line.strip()
                self.two_repeat_one[line] = 1
        with open(three_repeat_one_save_pat, 'r', encoding='utf-8') as f8:
            for line in f8.readlines():
                line = line.strip()
                self.three_repeat_one[line] = 1
        with open(name_sid_cid_save_pat, 'rb') as w1:
            self.name_sid_cid = pickle.load(w1)
        with open(lower_name_upper_save_pat, 'rb') as w2:
            self.lower_name_upper = pickle.load(w2)
        with open(upper_name_lower_save_pat, 'rb') as w3:
            self.upper_name_lower = pickle.load(w3)
        print('---Dictionary loading is complete, allowing for the next step of named entity recognition---')

    def double_lookup(self, word, word_list):
        word_index = [i for i, x in enumerate(word_list) if x == word]
        list_outcome = []
        for index in word_index:
            if index != len(word_list) - 1:
                double_word = word + ' ' + word_list[index + 1]
                if double_word in self.two_chemical_list:
                    if double_word not in list_outcome:
                        list_outcome.append((double_word, index))
        return list_outcome

    def three_lookup(self, word, word_list):
        word_index = [i for i, x in enumerate(word_list) if x == word]
        list_outcome = []
        for index in word_index:
            if index != len(word_list) - 2 and index != len(word_list) - 1:
                three_word = word + ' ' + word_list[index + 1] + ' ' + word_list[index + 2]
                if three_word in self.three_chemical_list:
                    if three_word not in list_outcome:
                        list_outcome.append(three_word)
        return list_outcome

    def chemical_match(self, get_text):
        chemicals = []
        get_text = get_text.replace(']', ')')
        get_text = get_text.replace('[', '(')
        word_list = get_text.split()
        upper_token_word = delete_characters_upper(word_list)
        token_word = delete_characters(word_list)
        for word in set(token_word):
            if word in self.pre_three_chemical:
                three_words = self.three_lookup(word, token_word)
                if three_words:
                    for three_word in three_words:
                        if three_word not in chemicals:
                            chemicals.append(three_word)
                else:
                    if word in self.pre_two_chemical:
                        double_words = self.double_lookup(word, token_word)
                        if double_words:
                            for double_word in double_words:
                                if len(double_word[0]) <= 6:
                                    upper_double_word = upper_token_word[double_word[1]] + ' ' + \
                                                        upper_token_word[double_word[1] + 1]
                                    if upper_double_word == self.lower_name_upper[double_word[0]]:
                                        if double_word[0] not in chemicals:
                                            chemicals.append(double_word[0])
                                else:
                                    if double_word[0] not in chemicals:
                                        chemicals.append(double_word[0])
                        else:
                            if word in self.three_repeat_one:
                                if len(word) <= 5:
                                    get_word_index = [num for num, w in enumerate(token_word) if w == word]
                                    for w_i in get_word_index:
                                        upper_word = upper_token_word[w_i]
                                        if upper_word == self.lower_name_upper[word]:
                                            if word not in chemicals:
                                                chemicals.append(word)
                                else:
                                    if word not in chemicals:
                                        chemicals.append(word)
                            else:
                                clean_word = word.strip(')').strip('(').strip(',').strip('\'')
                                if clean_word in self.one_chemical_list:
                                    if len(clean_word) <= 5:
                                        get_word_index = [num for num, w in enumerate(token_word) if w == word]
                                        for w_i in get_word_index:
                                            upper_word = upper_token_word[w_i].strip(')').strip('(').strip(',').strip(
                                                '\'')
                                            if upper_word == self.lower_name_upper[clean_word]:
                                                if clean_word not in chemicals:
                                                    chemicals.append(clean_word)
                                    else:
                                        if clean_word not in chemicals:
                                            chemicals.append(clean_word)
                    else:
                        if word in self.two_repeat_one:
                            if len(word) <= 5:
                                get_word_index = [num for num, w in enumerate(token_word) if w == word]
                                for w_i in get_word_index:
                                    upper_word = upper_token_word[w_i]
                                    if upper_word == self.lower_name_upper[word]:
                                        if word not in chemicals:
                                            chemicals.append(word)
                            else:
                                if word not in chemicals:
                                    chemicals.append(word)
                        else:
                            clean_word = word.strip(')').strip('(').strip(',').strip('\'')
                            if clean_word in self.one_chemical_list:
                                if len(clean_word) <= 5:
                                    get_word_index = [num for num, w in enumerate(token_word) if w == word]
                                    for w_i in get_word_index:
                                        upper_word = upper_token_word[w_i].strip(')').strip('(').strip(',').strip('\'')
                                        if upper_word == self.lower_name_upper[clean_word]:
                                            if clean_word not in chemicals:
                                                chemicals.append(clean_word)
                                else:
                                    if clean_word not in chemicals:
                                        chemicals.append(clean_word)
            elif word in self.pre_two_chemical:
                double_words = self.double_lookup(word, token_word)
                if double_words:
                    for double_word in double_words:
                        if len(double_word[0]) <= 6:
                            upper_double_word = upper_token_word[double_word[1]] + ' ' + \
                                                upper_token_word[double_word[1] + 1]
                            if upper_double_word == self.lower_name_upper[double_word[0]]:
                                if double_word[0] not in chemicals:
                                    chemicals.append(double_word[0])
                        else:
                            if double_word[0] not in chemicals:
                                chemicals.append(double_word[0])
                else:
                    if word in self.two_repeat_one:
                        if len(word) <= 5:
                            get_word_index = [num for num, w in enumerate(token_word) if w == word]
                            for w_i in get_word_index:
                                upper_word = upper_token_word[w_i]
                                if upper_word == self.lower_name_upper[word]:
                                    if word not in chemicals:
                                        chemicals.append(word)
                        else:
                            if word not in chemicals:
                                chemicals.append(word)
                    else:
                        clean_word = word.strip(')').strip('(').strip(',').strip('\'')
                        if clean_word in self.one_chemical_list:
                            if len(clean_word) <= 5:
                                get_word_index = [num for num, w in enumerate(token_word) if w == word]
                                for w_i in get_word_index:
                                    upper_word = upper_token_word[w_i].strip(')').strip('(').strip(',').strip('\'')
                                    if upper_word == self.lower_name_upper[clean_word]:
                                        if clean_word not in chemicals:
                                            chemicals.append(clean_word)
                            else:
                                if clean_word not in chemicals:
                                    chemicals.append(clean_word)
            elif word in self.one_chemical_list:
                if len(word) <= 5:
                    get_word_index = [num for num, w in enumerate(token_word) if w == word]
                    for w_i in get_word_index:
                        upper_word = upper_token_word[w_i]
                        if upper_word == self.lower_name_upper[word]:
                            if word not in chemicals:
                                chemicals.append(word)
                else:
                    if word not in chemicals:
                        chemicals.append(word)
            else:
                clean_word = word.strip(')').strip('(').strip(',').strip('\'')
                if clean_word in self.one_chemical_list:
                    if len(clean_word) <= 5:
                        get_word_index = [num for num, w in enumerate(token_word) if w == word]
                        for w_i in get_word_index:
                            upper_word = upper_token_word[w_i].strip(')').strip('(').strip(',').strip('\'')
                            if upper_word == self.lower_name_upper[clean_word]:
                                if clean_word not in chemicals:
                                    chemicals.append(clean_word)
                    else:
                        if clean_word not in chemicals:
                            chemicals.append(clean_word)
        return chemicals

    def chemical_frequency(self, get_filepath, dict_name):
        chemical_filename = {}
        sid_filename = {}
        filename_chemical = {}
        tmp_count = 1
        for filename in os.listdir(get_filepath):
            print('---Currently processing file %d, filename %s ---' % (tmp_count, filename))
            start = time()
            get_file_path = get_filepath + '\\' + filename
            if fnmatch.fnmatch(get_file_path, '*.pdf') or fnmatch.fnmatch(get_file_path, '*.PDF'):
                get_text = get_pdf_text(get_file_path)
                get_text = clean_text(get_text)
                get_chemicals = self.chemical_match(get_text)
                for chemical in get_chemicals:
                    if dict_name == 'initial':
                        get_sid = self.name_sid_cid[chemical]['dtxsid']
                    else:
                        get_sid = self.name_sid_cid[chemical]['sid']
                    if chemical not in chemical_filename:
                        chemical_filename[chemical] = []
                    if filename not in chemical_filename[chemical]:
                        chemical_filename[chemical].append(filename)
                    if get_sid:
                        if get_sid not in sid_filename:
                            sid_filename[get_sid] = []
                        if filename not in sid_filename[get_sid]:
                            sid_filename[get_sid].append(filename)
                    else:
                        if chemical not in sid_filename:
                            sid_filename[chemical] = []
                        if filename not in sid_filename[chemical]:
                            sid_filename[chemical].append(filename)
                    if filename not in filename_chemical:
                        filename_chemical[filename] = []
                    if chemical not in filename_chemical[filename]:
                        filename_chemical[filename].append(chemical)
            elif fnmatch.fnmatch(get_file_path, '*.txt') or fnmatch.fnmatch(get_file_path, '*.txt'):
                with open(get_file_path, 'r', encoding='utf-8-sig') as f:
                    for line in f.readlines():
                        line = line.strip()
                        get_chemicals = self.chemical_match(line)
                        for chemical in get_chemicals:
                            if dict_name == 'initial':
                                get_sid = self.name_sid_cid[chemical]['dtxsid']
                            else:
                                get_sid = self.name_sid_cid[chemical]['sid']
                            if chemical not in chemical_filename:
                                chemical_filename[chemical] = []
                            if filename not in chemical_filename[chemical]:
                                chemical_filename[chemical].append(filename)
                            if get_sid:
                                if get_sid not in sid_filename:
                                    sid_filename[get_sid] = []
                                if filename not in sid_filename[get_sid]:
                                    sid_filename[get_sid].append(filename)
                            else:
                                if chemical not in sid_filename:
                                    sid_filename[chemical] = []
                                if filename not in sid_filename[chemical]:
                                    sid_filename[chemical].append(filename)
                            if filename not in filename_chemical:
                                filename_chemical[filename] = []
                            if chemical not in filename_chemical[filename]:
                                filename_chemical[filename].append(chemical)
            end = time()
            print('%s Recognition complete, time %.2f' % (filename, (end-start)))
            tmp_count += 1
        return chemical_filename, sid_filename, filename_chemical

    def ner(self, get_filepath, input_type='file'):
        if input_type == 'file':
            if fnmatch.fnmatch(get_filepath, '*.txt'):
                get_chemicals = []
                with open(get_filepath, 'r', encoding='utf-8') as f:
                    for line in f.readlines():
                        line = line.strip()
                        get_chemical = self.chemical_match(line)
                        if get_chemical:
                            get_chemicals += get_chemical
                print('---The named entity recognition is complete and the results are as follows:---')
                print(get_chemicals)
                return get_chemicals
            elif fnmatch.fnmatch(get_filepath, '*.pdf') or fnmatch.fnmatch(get_filepath, '*.PDF'):
                get_content = get_pdf_text(get_filepath)
                get_content = clean_text(get_content)
                get_chemicals = self.chemical_match(get_content)
                print('---The Named entity recognition is complete with the following results:---')
                print(get_chemicals)
                return get_chemicals
            else:
                print('---Currently only support pdf, txt file input---')
        elif input_type == 'text':
            get_chemicals = self.chemical_match(get_filepath)
            print('---The Named entity recognition is complete with the following results:---')
            print(get_chemicals)
            return get_chemicals
        elif input_type == 'folder':
            chemical_filename, sid_filename, filename_chemical = self.chemical_frequency(get_filepath,
                                                                                         self.get_dict_name)
            c_s_f = (chemical_filename, sid_filename, filename_chemical)
            print('---The Named entity recognition is complete with the following results:---')
            print(c_s_f)
            return c_s_f

    def output_file(self, get_filepath, input_type='file'):
        current_path = os.getcwd()
        save_filepath = current_path + '\\' + 'output'
        if not os.path.exists(save_filepath):
            os.makedirs(save_filepath)
        if input_type == 'file':
            get_chemicals = self.ner(get_filepath, input_type='file')
            target_filepath = save_filepath + '\\' + 'chemicals.txt'
            with open(target_filepath, 'a', encoding='utf-8') as w:
                for chemical in get_chemicals:
                    w.write(chemical + '\n')
            print('---The file is saved, and the save path is %s---' % save_filepath)
        elif input_type == 'text':
            get_chemicals = self.ner(get_filepath, input_type='text')
            target_filepath = save_filepath + '\\' + 'chemicals.txt'
            with open(target_filepath, 'a', encoding='utf-8') as w:
                for chemical in get_chemicals:
                    w.write(chemical + '\n')
        elif input_type == 'folder':
            c_s_f = self.ner(get_filepath, input_type='folder')
            chemical_filename = c_s_f[0]
            sid_filename = c_s_f[1]
            filename_chemical = c_s_f[2]
            chemical_filename_save_path = save_filepath + '\\' + 'chemical_filename.csv'
            chemical_filename_save_path_pkl = save_filepath + '\\' + 'chemical_filename.pkl'
            with open(chemical_filename_save_path, 'a', encoding='utf-8', newline='') as w1:
                csv_writer = csv.writer(w1)
                data = ['Chemical', 'Frequency', 'List']
                csv_writer.writerow(data)
                for key in chemical_filename:
                    data = [key, len(chemical_filename[key]), ' | '.join(chemical_filename[key])]
                    csv_writer.writerow(data)
            with open(chemical_filename_save_path_pkl, 'wb') as w1_pkl:
                pickle.dump(chemical_filename, w1_pkl)
            sid_filename_save_path = save_filepath + '\\' + 'sid_filename.csv'
            sid_filename_save_path_pkl = save_filepath + '\\' + 'sid_filename.pkl'
            with open(sid_filename_save_path, 'a', encoding='utf-8', newline='') as w2:
                csv_writer = csv.writer(w2)
                data = ['SID', 'Frequency', 'List']
                csv_writer.writerow(data)
                for key in sid_filename:
                    data = [key, len(sid_filename[key]), ' | '.join(sid_filename[key])]
                    csv_writer.writerow(data)
            with open(sid_filename_save_path_pkl, 'wb') as w2_pkl:
                pickle.dump(sid_filename, w2_pkl)
            filename_chemical_save_path = save_filepath + '\\' + 'filename_chemical.csv'
            filename_chemical_save_path_pkl = save_filepath + '\\' + 'filename_chemical.pkl'
            with open(filename_chemical_save_path, 'a', encoding='utf-8', newline='') as w3:
                csv_writer = csv.writer(w3)
                data = ['Filename', 'Reported Chemicals', 'List']
                csv_writer.writerow(data)
                for key in filename_chemical:
                    data = [key, len(filename_chemical[key]), ' | '.join(filename_chemical[key])]
                    csv_writer.writerow(data)
            with open(filename_chemical_save_path_pkl, 'wb') as w3_pkl:
                pickle.dump(filename_chemical, w3_pkl)
            print('---The file is saved, and the save path is %s---' % save_filepath)
        else:
            print('---This input type is not recognized, please re-enter. Input types include: text, file, folder---')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.band()
        print('---Initialization is in progress, it is expected to take two minutes, please be patient.---')
        self.initial_dict = ChemicalNER()

    def band(self):
        self.ui.new_dict.clicked.connect(self.new_dict)
        self.ui.append_dict.clicked.connect(self.append_dict)
        self.ui.clean_button.clicked.connect(self.clean_text)
        self.ui.clean_output.clicked.connect(self.clean_output)
        self.ui.clean_dict_name.clicked.connect(self.clean_dict)
        self.ui.load_dict.clicked.connect(self.load_dict)
        self.ui.start_ner.clicked.connect(self.start_ner)
        self.ui.ner_output.clicked.connect(self.ner_output)

    def new_dict(self):
        input_text = self.ui.input_text.text()
        input_type = self.ui.input_type.currentText()
        dict_name = self.ui.dict_name.text()
        if input_type == 'Dictionary':
            generate_dict = GenerateDict(input_text, dict_name)
            get_save_path = generate_dict.new_dict()
            tmp_text = '---The new dictionary was created successfully, and the path to save the dictionary is %s' % get_save_path
            self.ui.output_text.setText('')
            self.ui.output_text.setText(tmp_text)
        else:
            self.ui.output_text.setText('')
            self.ui.output_text.setText('The current input type is not a dictionary type, so you cannot create a new dictionary.')

    def append_dict(self):
        input_text = self.ui.input_text.text()
        input_type = self.ui.input_type.currentText()
        dict_name = self.ui.dict_name.text()
        if input_type == 'Dictionary':
            generate_dict = GenerateDict(input_text, dict_name)
            get_save_path = generate_dict.append_dict()
            tmp_text = '---Append dictionary successfully, the dictionary save path is %s---' % get_save_path
            self.ui.output_text.setText('')
            self.ui.output_text.setText(tmp_text)
        else:
            self.ui.output_text.setText('')
            self.ui.output_text.setText('The current input type is not a dictionary type, so you can not append a dictionary.')

    def clean_text(self):
        self.ui.input_text.setText('')

    def clean_dict(self):
        self.ui.dict_name.setText('')

    def clean_output(self):
        self.ui.output_text.setText('')

    def load_dict(self):
        dict_name = self.ui.dict_name.text()
        if dict_name:
            current_path = os.getcwd()
            if dict_name in os.listdir(current_path):
                self.ui.output_text.setText('')
                self.initial_dict = ChemicalNER(dict_name)
                self.ui.output_text.setText('---Dictionary loading is complete, allowing for the next step of named entity recognition---')
            else:
                self.ui.output_text.setText('')
                self.ui.output_text.setText('---There is no corresponding dictionary, please check the input dictionary name---')
        else:
            self.ui.output_text.setText('')
            self.initial_dict = ChemicalNER()
            self.ui.output_text.setText('---Dictionary loading is complete, allowing for the next step of named entity recognition---')

    def start_ner(self):
        input_text = self.ui.input_text.text()
        input_type = self.ui.input_type.currentText()
        if input_type == 'File':
            self.ui.output_text.setText('')
            get_text = self.initial_dict.ner(input_text, input_type='file')
            get_text = ' | '.join(get_text)
            self.ui.output_text.setText(get_text)
        elif input_type == 'Text':
            self.ui.output_text.setText('')
            get_text = self.initial_dict.ner(input_text, input_type='text')
            get_text = ' | '.join(get_text)
            self.ui.output_text.setText(get_text)
        elif input_type == 'Folder':
            self.ui.output_text.setText('')
            get_text = self.initial_dict.ner(input_text, input_type='folder')
            for i in get_text:
                tmp_output = str(i)
                self.ui.output_text.setText(tmp_output)
        else:
            self.ui.output_text.setText('')
            self.ui.output_text.setText('---The current input type does not support named entity recognition, please reset it.')

    def ner_output(self):
        current_path = os.getcwd()
        save_filepath = current_path + '\\' + 'output'
        input_text = self.ui.input_text.text()
        input_type = self.ui.input_type.currentText()
        if input_type == 'File':
            self.initial_dict.output_file(input_text, input_type='file')
            self.ui.output_text.setText('')
            self.ui.output_text.setText('Recognition is complete and the file is saved at %s' % save_filepath)
        elif input_type == 'Text':
            self.initial_dict.output_file(input_text, input_type='text')
            self.ui.output_text.setText('')
            self.ui.output_text.setText('Recognition is complete and the file is saved at %s' % save_filepath)
        elif input_type == 'Folder':
            self.initial_dict.output_file(input_text, input_type='folder')
            self.ui.output_text.setText('')
            self.ui.output_text.setText('Recognition is complete and the file is saved at %s' % save_filepath)
        else:
            self.ui.output_text.setText('')
            self.ui.output_text.setText('---当The current input type does not support named entity recognition, please reset it.---')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()



# input_text = 'input yuor filepath'
# dict_name = 'input your dict name'
# generate_dict = GenerateDict(input_text, dict_name)
# get_save_path = generate_dict.new_dict()


# dict_name = 'input your dict name'
# input_text = 'input yuor filepath'
# input_type = 'input your file type' # file text or folder
# initial_dict = ChemicalNER(dict_name)
# current_path = os.getcwd()
# save_filepath = current_path + '\\' + 'output'
# if input_type == 'File':
#     initial_dict.output_file(input_text, input_type='file')
# elif input_type == 'Text':
#     initial_dict.output_file(input_text, input_type='text')
# elif input_type == 'Folder':
#     initial_dict.output_file(input_text, input_type='folder')
