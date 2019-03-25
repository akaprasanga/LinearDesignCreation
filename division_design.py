from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import QDateTime, Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from design_logic import DesignLogic as Design

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        self.createParameterGroupBox()
        self.createCanvasBox()

        topLayout = QHBoxLayout()

        self.parameterGroupBox.setFixedWidth(350)
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.parameterGroupBox, 1, 0)
        mainLayout.addWidget(self.canvasGroupBox, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("Linear Design Creation")
        self.changeStyle('Fusion')
        self.connect_signals()
        self.design = Design()
        self.init_variables()

    def init_variables(self):
        self.current_img = self.design.create_image()
        self.update_final_img(self.current_img)
        self.levelone_list = []
        self.ltwo_list = []
        self.lthree_list = []
        self.l1_color = (193, 154, 141)
        self.l2_color = (220, 178, 137)
        self.l3_color = (107,114,143)
        self.l4_color= (202,131,39)

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))

    def connect_signals(self):
        self.update_button.clicked.connect(self.on_update_btn_clicked)
        self.add_line_btn.clicked.connect(self.saveFileDialog)
        self.l1_push_btn.clicked.connect(self.add_level_one)
        self.l2_push_btn.clicked.connect(self.add_level_two)
        self.l3_push_btn.clicked.connect(self.add_level_three)
        self.l4_push_btn.clicked.connect(self.add_level_four)
        self.l1_color_btn.clicked.connect(self.open_color_dialog_l1)
        self.l2_color_btn.clicked.connect(self.open_color_dialog_l2)
        self.l3_color_btn.clicked.connect(self.open_color_dialog_l3)
        self.l4_color_btn.clicked.connect(self.open_color_dialog_l4)

    def createParameterGroupBox(self):
        l1_layout = self.level_one_group()
        l2_layout = self.level_two_group()
        l3_layout = self.level_three_group()
        l4_layout = self.level_four_group()

        self.update_button = QPushButton("Create Blank Image")
        self.add_line_btn = QPushButton("Save Image")

        self.parameterGroupBox = QGroupBox("Parameters")
        self.randomize_check_box = QCheckBox("Randomize Input Values")
        self.randomize_check_box.setChecked(True)
        self.randomize_value = QLineEdit()
        self.randomize_value.setText('30')

        random_label = QLabel("Percent:")

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.randomize_check_box)
        hlayout.addWidget(random_label)
        hlayout.addWidget(self.randomize_value)

        layout = QVBoxLayout()

        layout.addLayout(hlayout)
        layout.addWidget(l1_layout)
        layout.addWidget(l2_layout)
        layout.addWidget(l3_layout)
        layout.addWidget(l4_layout)

        layout.addWidget(self.update_button)
        layout.addWidget(self.add_line_btn)

        self.parameterGroupBox.setLayout(layout)

    def level_one_group(self):
        levelone_groupbox = QGroupBox("Level One")
        # self.l1_checkbox = QCheckBox('Enable/Disable')
        self.l1_min = QLineEdit()
        self.l1_min.setText('100')
        self.l1_max = QLineEdit()
        self.l1_max.setText('200')
        self.l1_push_btn = QPushButton(' Create Level 1 ')
        self.l1_color_btn = QPushButton('Choose Color')

        levelone_div_label = QLabel("Minim Height:")
        levelone_height_label = QLabel("Maxm Height:")
        random_label = QLabel('Randomize %')
        self.l1_random_input = QLineEdit()
        self.l1_random_input.setText('30')

        hlayout = QGridLayout()
        # vertical_layout = QGridLayout()
        # hlayout.addWidget(self.l1_checkbox, 0, 0)
        hlayout.addWidget(levelone_div_label, 1, 0)
        hlayout.addWidget(self.l1_min, 1, 1)
        hlayout.addWidget(levelone_height_label, 1, 2)
        hlayout.addWidget(self.l1_max, 1, 3)
        hlayout.addWidget(self.l1_color_btn, 2, 0)
        hlayout.addWidget(random_label, 2, 1)
        hlayout.addWidget(self.l1_random_input, 2, 2)
        hlayout.addWidget(self.l1_push_btn, 3, 1)
        # hlayout.addWidget(vertical_layout)
        levelone_groupbox.setLayout(hlayout)
        return levelone_groupbox

    def level_two_group(self):
        leveltwo_groupbox = QGroupBox("Level Two")
        self.l2_min = QLineEdit()
        self.l2_min.setText('150')
        self.l2_max = QLineEdit()
        self.l2_max.setText('200')
        self.l2_push_btn = QPushButton(' Create Level 2 ')
        leveltwo_div_label = QLabel("Mimum W:")
        leveltwo_width_label = QLabel("Maxm W:")
        self.l2_color_btn = QPushButton(' Choose Color ')
        random_label = QLabel('Randomize %')
        self.l2_random_input = QLineEdit()
        self.l2_random_input.setText('30')
        hlayout = QGridLayout()
        hlayout.addWidget(leveltwo_div_label, 0, 0)
        hlayout.addWidget(self.l2_min, 0, 1)
        hlayout.addWidget(leveltwo_width_label, 0, 2)
        hlayout.addWidget(self.l2_max, 0, 3)
        hlayout.addWidget(self.l2_color_btn, 1, 0)
        hlayout.addWidget(random_label, 1, 1)
        hlayout.addWidget(self.l2_random_input, 1, 2)
        hlayout.addWidget(self.l2_push_btn, 2, 1)
        leveltwo_groupbox.setLayout(hlayout)

        return leveltwo_groupbox

    def level_three_group(self):
        levelthree_groupbox = QGroupBox("Level Three")
        self.l3_min = QLineEdit()
        self.l3_min.setText('40')
        self.l3_max = QLineEdit()
        self.l3_max.setText('80')
        self.l3_push_btn = QPushButton('Create Level 3')
        levelthree_div_label = QLabel("Minim H:")
        levelthree_width_label = QLabel("Maxm H:")
        self.l3_color_btn = QPushButton(' Choose color ')
        random_label = QLabel('Randomize %')
        self.l3_random_input = QLineEdit()
        self.l3_random_input.setText('30')

        hlayout = QGridLayout()
        hlayout.addWidget(levelthree_div_label, 0, 0)
        hlayout.addWidget(self.l3_min, 0, 1)
        hlayout.addWidget(levelthree_width_label, 0, 2)
        hlayout.addWidget(self.l3_max, 0, 3)
        hlayout.addWidget(self.l3_color_btn, 1, 0)
        hlayout.addWidget(random_label, 1, 1)
        hlayout.addWidget(self.l3_random_input, 1, 2)
        hlayout.addWidget(self.l3_push_btn, 2, 1)
        levelthree_groupbox.setLayout(hlayout)
        return levelthree_groupbox

    def level_four_group(self):
        levelfour_groupbox = QGroupBox("Level Four")
        self.l4_min = QLineEdit()
        self.l4_min.setText('40')
        self.l4_max = QLineEdit()
        self.l4_max.setText('60')
        self.l4_push_btn = QPushButton('Create Level 4')
        levelfour_div_label = QLabel("Minim H:")
        levelfour_width_label = QLabel("Maxm H:")
        self.l4_color_btn = QPushButton(' Choose color ')
        random_label = QLabel('Randomize %')
        self.l4_random_input = QLineEdit()
        self.l4_random_input.setText('30')
        hlayout = QGridLayout()
        hlayout.addWidget(levelfour_div_label, 0, 0)
        hlayout.addWidget(self.l4_min, 0, 1)
        hlayout.addWidget(levelfour_width_label, 0, 2)
        hlayout.addWidget(self.l4_max, 0, 3)
        hlayout.addWidget(self.l4_color_btn, 1, 0)
        hlayout.addWidget(random_label, 1, 1)
        hlayout.addWidget(self.l4_random_input, 1, 2)
        hlayout.addWidget(self.l4_push_btn, 2, 1)
        levelfour_groupbox.setLayout(hlayout)
        return levelfour_groupbox

    def createCanvasBox(self):
        self.canvasGroupBox = QGroupBox("Image To Process")

        self.design_img = QLabel(self)

        layout = QVBoxLayout()

        layout.addWidget(self.design_img)
        layout.maximumSize()
        layout.addStretch(1)
        self.canvasGroupBox.setLayout(layout)

    def add_level_one(self):
        min, max, random_value = self.get_parameters_l1()
        l1_list= [(0, self.current_img.shape[1], 0, self.current_img.shape[0])]
        created_img, self.ltwo_list = self.design.divide_vertically(self.current_img, min, max, l1_list, random_value, color_tuple=self.l1_color)
        # print(self.ltwo_list)
        self.current_img = created_img
        self.update_final_img(created_img)

    def add_level_two(self):
        min, max, random_value = self.get_parameters_l2()
        created_img, self.lthree_list = self.design.divide_horizontally(self.current_img, min, max, self.ltwo_list, random_value, color_tuple=self.l2_color)
        # print(self.lthree_list)
        self.current_img = created_img
        self.update_final_img(created_img)

    def add_level_three(self):
        min, max, random_value = self.get_parameters_l3()
        created_img, self.lfour_list = self.design.divide_vertically_l3(self.current_img, min, max, self.lthree_list, random_value, color_tuple=self.l3_color)
        self.current_img = created_img
        self.update_final_img(created_img)

    def add_level_four(self):
        min, max, random_value = self.get_parameters_l4()
        created_img, level_five_list = self.design.divide_horizontally_l4(self.current_img, min, max, self.lfour_list, random_value, color_tuple=self.l4_color)
        self.current_img = created_img
        self.update_final_img(created_img)

    def on_update_btn_clicked(self):
        img = self.design.create_image()
        self.current_img = img
        # print(self.current_img.shape)
        self.update_final_img(img)

    def update_final_img(self, img):
        height = self.canvasGroupBox.height()
        final_img = QPixmap(self.numpy_to_pixmap(self.current_img))
        final_img = final_img.scaledToHeight(height-50, mode=Qt.FastTransformation)
        self.design_img.setPixmap(final_img)

    def numpy_to_pixmap(self, img):
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        return qImg

    def add_lines(self):
        number_of_lines, minimum_height = self.get_parameters()
        empty= []
        created_img, self.ltwo_list = self.design.divide_vertically(self.current_img, number_of_lines, minimum_height, empty)
        self.current_img = created_img
        self.update_final_img(created_img)

    def get_parameters_l1(self):
        min = int(self.l1_min.text())
        max = int(self.l1_max.text())
        random_value = int(self.l1_random_input.text())
        return min, max, random_value

    def get_parameters_l2(self):
        min = int(self.l2_min.text())
        max = int(self.l2_max.text())
        random_value = int(self.l2_random_input.text())
        return min, max, random_value

    def get_parameters_l3(self):
        min = int(self.l3_min.text())
        max = int(self.l3_max.text())
        random_value = int(self.l3_random_input.text())
        return min, max, random_value

    def get_parameters_l4(self):
        min = int(self.l4_min.text())
        max = int(self.l4_max.text())
        random_value = int(self.l4_random_input.text())
        return min, max, random_value

    def hex_to_rgb(self, hex_string):
        h = hex_string.lstrip('#')
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

    def random_status(self):
        if self.randomize_check_box.isChecked():
            v = int(self.randomize_value.text())
        else:
            v = 1
        return v

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "Untitled.png",
                                                  "PNG File (*.png);; JPG File (*.jpg)", options=options)
        if fileName:
            from skimage import io
            print(fileName)
            io.imsave(fileName, self.current_img)


    def open_color_dialog_l1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            c = self.hex_to_rgb(color.name())
            self.l1_color = c
            self.l1_min.setStyleSheet("QLineEdit { background-color: rgb"+str(c)+"; color: white }")
            self.l1_max.setStyleSheet("QLineEdit { background-color: rgb"+str(c)+"; color: white }")

    def open_color_dialog_l2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            c = self.hex_to_rgb(color.name())
            self.l2_color = c
            self.l2_min.setStyleSheet("QLineEdit { background-color: rgb"+str(c)+"; color: white }")
            self.l2_max.setStyleSheet("QLineEdit { background-color: rgb"+str(c)+"; color: white }")

    def open_color_dialog_l3(self):
        color = QColorDialog.getColor()
        if color.isValid():
            c = self.hex_to_rgb(color.name())
            self.l3_color = c
            self.l3_min.setStyleSheet("QLineEdit { background-color: rgb"+str(c)+"; color: white }")
            self.l3_max.setStyleSheet("QLineEdit { background-color: rgb"+str(c)+"; color: white }")

    def open_color_dialog_l4(self):
        color = QColorDialog.getColor()
        if color.isValid():
            c = self.hex_to_rgb(color.name())
            self.l4_color = c
            self.l4_min.setStyleSheet("QLineEdit { background-color: rgb"+str(c)+"; color: white }")
            self.l4_max.setStyleSheet("QLineEdit { background-color: rgb"+str(c)+"; color: white }")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.showMaximized()
    gallery.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint)
    gallery.show()
    sys.exit(app.exec_())
