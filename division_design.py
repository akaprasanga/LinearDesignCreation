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
        self.createCanvasBox_2()

        topLayout = QHBoxLayout()

        self.parameterGroupBox.setFixedWidth(350)
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.parameterGroupBox, 1, 0)
        mainLayout.addWidget(self.canvasGroupBox, 1, 1)
        mainLayout.addWidget(self.canvasGroupBox_2, 1, 2)

        self.setLayout(mainLayout)

        self.setWindowTitle("Linear Design Creation")
        self.changeStyle('Fusion')
        self.connect_signals()
        self.design = Design()
        self.init_variables()

    def init_variables(self):
        self.current_img, self.current_img_2 = self.design.create_image()
        self.update_final_img(self.current_img)
        self.update_final_img2()
        self.levelone_list = []
        self.ltwo_list = []
        self.lthree_list = []
        # (107, 114, 143)
        # (220, 178, 137)
        # (202, 131, 39)
        # (193, 154, 141)
        self.l1_color = (0, 0, 0)
        self.l2_color = (255, 137, 51)
        self.l3_color = (107, 114, 143)
        self.l4_color = (51, 130, 255)

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))

    def connect_signals(self):
        self.create_final_imges_btn.clicked.connect(self.create_final_img)
        self.l1_color_btn.clicked.connect(self.open_color_dialog_l1)
        self.l2_color_btn.clicked.connect(self.open_color_dialog_l2)
        self.l3_color_btn.clicked.connect(self.open_color_dialog_l3)
        self.l4_color_btn.clicked.connect(self.open_color_dialog_l4)
        self.save_img_1.clicked.connect(self.saveFileDialog_img1)
        self.save_img_2.clicked.connect(self.saveFileDialog_img2)

    def createParameterGroupBox(self):
        l1_layout = self.level_one_group()
        l2_layout = self.level_two_group()
        l3_layout = self.level_three_group()
        l4_layout = self.level_four_group()

        self.create_final_imges_btn = QPushButton("Create Final Images")
        self.add_line_btn = QPushButton("Save Image")

        self.parameterGroupBox = QGroupBox("Parameters")

        hlayout = QHBoxLayout()

        hlayout.addWidget(self.create_final_imges_btn)

        layout = QVBoxLayout()
        layout.addLayout(hlayout)
        layout.addWidget(l1_layout)
        layout.addWidget(l2_layout)
        layout.addWidget(l3_layout)
        layout.addWidget(l4_layout)


        self.parameterGroupBox.setLayout(layout)

    def level_one_group(self):
        levelone_groupbox = QGroupBox("Level One")
        # self.l1_checkbox = QCheckBox('Enable/Disable')
        self.l1_min = QLineEdit()
        self.l1_min.setText('40')
        self.l1_max = QLineEdit()
        self.l1_max.setText('130')
        self.l1_color_btn = QPushButton('Choose Color')

        levelone_div_label = QLabel("Minim Height:")
        levelone_height_label = QLabel("Maxm Height:")
        random_label = QLabel('Random %')
        thickness_label = QLabel('Thick')
        self.l1_thick = QLineEdit()
        self.l1_thick.setText('2')
        self.l1_random_input = QLineEdit()
        self.l1_random_input.setText('0')

        hlayout = QGridLayout()

        hlayout.addWidget(levelone_div_label, 1, 0)
        hlayout.addWidget(self.l1_min, 1, 1)
        hlayout.addWidget(levelone_height_label, 1, 2)
        hlayout.addWidget(self.l1_max, 1, 3)
        hlayout.addWidget(self.l1_color_btn, 2, 0)
        hlayout.addWidget(random_label, 2, 1)
        hlayout.addWidget(self.l1_random_input, 2, 2)
        hlayout.addWidget(thickness_label, 2, 3)
        hlayout.addWidget(self.l1_thick, 2, 4)
        levelone_groupbox.setLayout(hlayout)
        return levelone_groupbox

    def level_two_group(self):
        leveltwo_groupbox = QGroupBox("Level Two")
        self.l2_checkbox = QCheckBox('Enable/Diable')
        self.l2_checkbox.setChecked(True)
        self.l2_min = QLineEdit()
        self.l2_min.setText('100')
        self.l2_max = QLineEdit()
        self.l2_max.setText('300')
        leveltwo_div_label = QLabel("Mimum W:")
        leveltwo_width_label = QLabel("Maxm W:")
        self.l2_color_btn = QPushButton(' Choose Color ')
        random_label = QLabel('Randomize %')
        self.l2_random_input = QLineEdit()
        self.l2_random_input.setText('0')
        thickness_label = QLabel('Thick')
        self.l2_thick = QLineEdit()
        self.l2_thick.setText('2')
        hlayout = QGridLayout()
        hlayout.addWidget(self.l2_checkbox, 0, 0, 1, 2)
        hlayout.addWidget(leveltwo_div_label, 1, 0)
        hlayout.addWidget(self.l2_min, 1, 1)
        hlayout.addWidget(leveltwo_width_label, 1, 2)
        hlayout.addWidget(self.l2_max, 1, 3)
        hlayout.addWidget(self.l2_color_btn, 2, 0)
        hlayout.addWidget(random_label, 2, 1)
        hlayout.addWidget(self.l2_random_input, 2, 2)
        hlayout.addWidget(thickness_label, 2, 3)
        hlayout.addWidget(self.l2_thick, 2, 4)
        leveltwo_groupbox.setLayout(hlayout)

        return leveltwo_groupbox

    def level_three_group(self):
        levelthree_groupbox = QGroupBox("Level Three")
        self.l3_checkbox = QCheckBox('Enable/Disable')
        self.l3_checkbox.setChecked(True)
        self.l3_min = QLineEdit()
        self.l3_min.setText('16')
        self.l3_max = QLineEdit()
        self.l3_max.setText('60')
        levelthree_div_label = QLabel("Minim H:")
        levelthree_width_label = QLabel("Maxm H:")
        self.l3_color_btn = QPushButton(' Choose color ')
        random_label = QLabel('Randomize %')
        self.l3_random_input = QLineEdit()
        self.l3_random_input.setText('0')
        thickness_label = QLabel('Thick')
        self.l3_thick = QLineEdit()
        self.l3_thick.setText('2')

        hlayout = QGridLayout()
        hlayout.addWidget(self.l3_checkbox, 0, 0, 1, 2)
        hlayout.addWidget(levelthree_div_label, 1, 0)
        hlayout.addWidget(self.l3_min, 1, 1)
        hlayout.addWidget(levelthree_width_label, 1, 2)
        hlayout.addWidget(self.l3_max, 1, 3)
        hlayout.addWidget(self.l3_color_btn, 2, 0)
        hlayout.addWidget(random_label, 2, 1)
        hlayout.addWidget(self.l3_random_input, 2, 2)
        hlayout.addWidget(thickness_label, 2, 3)
        hlayout.addWidget(self.l3_thick, 2, 4)
        levelthree_groupbox.setLayout(hlayout)
        return levelthree_groupbox

    def level_four_group(self):
        levelfour_groupbox = QGroupBox("Level Four")
        self.l4_checkbox = QCheckBox('Enable/Disable')
        self.l4_checkbox.setChecked(True)
        self.l4_min = QLineEdit()
        self.l4_min.setText('100')
        self.l4_max = QLineEdit()
        self.l4_max.setText('300')
        levelfour_div_label = QLabel("Minim W:")
        levelfour_width_label = QLabel("Maxm W:")
        self.l4_color_btn = QPushButton(' Choose color ')
        random_label = QLabel('Random %')
        self.l4_random_input = QLineEdit()
        self.l4_random_input.setText('0')
        thickness_label = QLabel('Thick')
        self.l4_thick = QLineEdit()
        self.l4_thick.setText('2')
        hlayout = QGridLayout()
        hlayout.addWidget(self.l4_checkbox, 0, 0, 1, 2)
        hlayout.addWidget(levelfour_div_label, 1, 0)
        hlayout.addWidget(self.l4_min, 1, 1)
        hlayout.addWidget(levelfour_width_label, 1, 2)
        hlayout.addWidget(self.l4_max, 1, 3)
        hlayout.addWidget(self.l4_color_btn, 2, 0)
        hlayout.addWidget(random_label, 2, 1)
        hlayout.addWidget(self.l4_random_input, 2, 2)
        hlayout.addWidget(thickness_label, 2, 3)
        hlayout.addWidget(self.l4_thick, 2, 4)
        levelfour_groupbox.setLayout(hlayout)
        return levelfour_groupbox

    def createCanvasBox(self):
        self.canvasGroupBox = QGroupBox("Final Image 1")

        self.save_img_1 = QPushButton('Save this Image')
        self.design_img = QLabel(self)

        layout = QVBoxLayout()

        layout.addWidget(self.design_img)
        layout.addWidget(self.save_img_1)
        layout.maximumSize()
        layout.addStretch(1)
        self.canvasGroupBox.setLayout(layout)

    def createCanvasBox_2(self):
        self.canvasGroupBox_2 = QGroupBox("Final Image 2")
        self.save_img_2 = QPushButton('Save this Image')
        self.design_img_2 = QLabel(self)

        layout = QVBoxLayout()

        layout.addWidget(self.design_img_2)
        layout.addWidget(self.save_img_2)
        layout.maximumSize()
        layout.addStretch(1)
        self.canvasGroupBox_2.setLayout(layout)

    def add_level_one(self, img, drawing_list):
        min, max, random_value, thickeness = self.get_parameters_l1()
        # l1_list= [(0, self.current_img.shape[1], 0, self.current_img.shape[0])]
        created_img, l2_list = self.design.divide_vertically(img, min, max, drawing_list, random_value, color_tuple=self.l1_color, thick=thickeness)
        # self.ltwo_list = l2_list
        # self.current_img = created_img
        return created_img, l2_list
        # self.update_final_img(created_img)

    def add_level_two(self, img, drawing_list):
        min, max, random_value, thickeness = self.get_parameters_l2()
        created_img, l3_list = self.design.divide_horizontally(img, min, max, drawing_list, random_value, color_tuple=self.l2_color, thick=thickeness)
        # print(self.lthree_list)
        # self.lthree_list = l3_list
        # self.current_img = created_img
        return created_img, l3_list
        # self.update_final_img(created_img)

    def add_level_three(self, img, drawing_list):
        min, max, random_value, thickness = self.get_parameters_l3()
        created_img, l4_list = self.design.divide_vertically_l3(img, min, max, drawing_list, random_value, color_tuple=self.l3_color, thick=thickness)
        # self.lfour_list = l4_list
        # self.current_img = created_img
        return created_img, l4_list
        # self.update_final_img(created_img)

    def add_level_four(self, img, drawing_list):
        min, max, random_value, thickness = self.get_parameters_l4()
        created_img, level_five_list = self.design.divide_horizontally_l4(img, min, max, drawing_list, random_value, color_tuple=self.l4_color, thick=thickness)
        # self.current_img = created_img
        # self.update_final_img(created_img)
        return created_img, level_five_list

    def on_update_btn_clicked(self):
        img = self.design.create_image()
        self.current_img = img
        self.create_final_img()
        # print(self.current_img.shape)
        self.update_final_img(img)

    def update_final_img(self, img):
        height = self.canvasGroupBox.height()
        final_img = QPixmap(self.numpy_to_pixmap(self.current_img))
        final_img = final_img.scaledToHeight(height-50, mode=Qt.FastTransformation)
        self.design_img.setPixmap(final_img)

    def update_final_img2(self):
        height = self.canvasGroupBox_2.height()
        final_img = QPixmap(self.numpy_to_pixmap(self.current_img_2))
        final_img = final_img.scaledToHeight(height-50, mode=Qt.FastTransformation)
        self.design_img_2.setPixmap(final_img)

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
        # self.update_final_img(created_img)

    def get_parameters_l1(self):
        min = int(self.l1_min.text())
        max = int(self.l1_max.text())
        random_value = int(self.l1_random_input.text())
        thickness = int(self.l1_thick.text())
        return min, max, random_value, thickness

    def get_parameters_l2(self):
        min = int(self.l2_min.text())
        max = int(self.l2_max.text())
        random_value = int(self.l2_random_input.text())
        thickness = int(self.l2_thick.text())
        return min, max, random_value, thickness

    def get_parameters_l3(self):
        min = int(self.l3_min.text())
        max = int(self.l3_max.text())
        random_value = int(self.l3_random_input.text())
        thickness = int(self.l3_thick.text())
        return min, max, random_value, thickness

    def get_parameters_l4(self):
        min = int(self.l4_min.text())
        max = int(self.l4_max.text())
        random_value = int(self.l4_random_input.text())
        thickness = int(self.l4_thick.text())
        return min, max, random_value, thickness

    def hex_to_rgb(self, hex_string):
        h = hex_string.lstrip('#')
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

    def random_status(self):
        if self.randomize_check_box.isChecked():
            v = int(self.randomize_value.text())
        else:
            v = 1
        return v

    def saveFileDialog_img1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "Untitled_1.png",
                                                  "PNG File (*.png);; JPG File (*.jpg)", options=options)
        if fileName:
            from skimage import io
            print(fileName)
            io.imsave(fileName, self.current_img)

    def saveFileDialog_img2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "Untitled_2.png",
                                                  "PNG File (*.png);; JPG File (*.jpg)", options=options)
        if fileName:
            from skimage import io
            print(fileName)
            io.imsave(fileName, self.current_img_2)

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

    def create_final_img(self):
        self.current_img, self.current_img_2 = self.design.create_image()
        if self.l2_checkbox.isChecked() and self.l3_checkbox.isChecked() and self.l4_checkbox.isChecked():
            print('l1 l2 l3 l4')
            l1_list = [(0, self.current_img.shape[1], 0, self.current_img.shape[0])]
            level_1_img, llevel2_list = self.add_level_one(self.current_img, l1_list)
            level_2_img, llevel3_list = self.add_level_two(level_1_img, llevel2_list)
            level_3_img, llevel4_list = self.add_level_three(level_2_img, llevel3_list)
            level_4_img, llevel5_list = self.add_level_four(level_3_img, llevel4_list)


            l1_list_2 = [(0, self.current_img_2.shape[1], 0, self.current_img_2.shape[0])]
            level_1_img_2, llevel2_list_2 = self.add_level_one(self.current_img_2, l1_list_2)
            level_2_img_2, llevel3_list_2 = self.add_level_two(level_1_img_2, llevel2_list_2)
            level_3_img_2, llevel4_list_2 = self.add_level_three(level_2_img_2, llevel3_list_2)
            level_4_img_2, llevel5_list_2 = self.add_level_four(level_3_img_2, llevel4_list_2)

            self.current_img_2 = level_4_img_2
            self.current_img = level_4_img
            self.update_final_img(None)
            self.update_final_img2()
        elif self.l2_checkbox.isChecked() and self.l3_checkbox.isChecked() and (not self.l4_checkbox.isChecked()):
            print('l1 l2 l3 only')
            l1_list = [(0, self.current_img.shape[1], 0, self.current_img.shape[0])]
            level_1_img, llevel2_list = self.add_level_one(self.current_img, l1_list)
            level_2_img, llevel3_list = self.add_level_two(level_1_img, llevel2_list)
            level_3_img, llevel4_list = self.add_level_three(level_2_img, llevel3_list)
            # self.add_level_one(self.current_img_2)
            # self.add_level_two(self.current_img_2)
            # self.add_level_three(self.current_img_2)
            l1_list_2 = [(0, self.current_img_2.shape[1], 0, self.current_img_2.shape[0])]
            level_1_img_2, llevel2_list_2 = self.add_level_one(self.current_img_2, l1_list_2)
            level_2_img_2, llevel3_list_2 = self.add_level_two(level_1_img_2, llevel2_list_2)
            level_3_img_2, llevel4_list_2 = self.add_level_three(level_2_img_2, llevel3_list_2)

            self.current_img = level_3_img
            self.current_img_2 = level_3_img_2
            self.update_final_img(None)
            self.update_final_img2()

        elif self.l2_checkbox.isChecked() and (not self.l3_checkbox.isChecked()):
            print('l1 and l2 only')
            l1_list = [(0, self.current_img.shape[1], 0, self.current_img.shape[0])]
            level_1_img, llevel2_list = self.add_level_one(self.current_img, l1_list)
            level_2_img, llevel3_list = self.add_level_two(level_1_img, llevel2_list)
            # self.add_level_one(self.current_img_2)
            # self.add_level_two(self.current_img_2)
            # self.add_level_three(self.current_img_2)
            l1_list_2 = [(0, self.current_img_2.shape[1], 0, self.current_img_2.shape[0])]
            level_1_img_2, llevel2_list_2 = self.add_level_one(self.current_img_2, l1_list_2)
            level_2_img_2, llevel3_list_2 = self.add_level_two(level_1_img_2, llevel2_list_2)

            self.current_img = level_2_img
            self.current_img_2 = level_2_img_2
            self.update_final_img(None)
            self.update_final_img2()

        elif (not self.l2_checkbox.isChecked()):
            print(' l1 only')
            l1_list = [(0, self.current_img.shape[1], 0, self.current_img.shape[0])]
            level_1_img, llevel2_list = self.add_level_one(self.current_img, l1_list)

            l1_list_2 = [(0, self.current_img_2.shape[1], 0, self.current_img_2.shape[0])]
            level_1_img_2, llevel2_list_2 = self.add_level_one(self.current_img_2, l1_list_2)

            self.current_img = level_1_img
            self.current_img_2 = level_1_img_2
            self.update_final_img(None)
            self.update_final_img2()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    screen = app.primaryScreen()
    h = screen.size().height()
    w = screen.size().width()

    gallery = WidgetGallery()
    # gallery.showMaximized()
    gallery.setFixedSize(screen.size().width()-50, screen.size().height()-100)
    gallery.show()
    sys.exit(app.exec_())
