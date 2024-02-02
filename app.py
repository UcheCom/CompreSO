import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QLabel, QLineEdit, QFileDialog, QPushButton, QComboBox, QInputDialog
from PyQt5.QtGui import QIcon
from PIL import Image
import os
import PIL
from PyQt5.QtCore import Qt


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image CompreSO'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 600
        self.statusBar().showMessage("Message:")
        self.statusBar().setObjectName("status")
        self.image_width = 0
        self.setFixedSize(self.width, self.height)
        self.setObjectName("main_window")
        stylesheet = ""
        with open("design.qss", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        #.........................main window....................................
        self.single_bubble = QFrame(self)
        self.single_bubble.setObjectName("bubble")
        self.single_bubble.move(50, 100)
        self.single_bubble.mousePressEvent = self.single_bubble_clicked
        
        self.single_bubble_heading = QLabel(self.single_bubble)
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.setText("Compress Image")
        self.single_bubble_heading.move(80, 8)

        self.single_bubble_para = QLabel(self.single_bubble)
        self.single_bubble_para.setObjectName("bubble_para")
        self.single_bubble_para.setText("Click here to compress single Image!")
        self.single_bubble_para.move(25, 32)


        self.sec_bubble =QFrame(self)
        self.sec_bubble.setObjectName("bubble")
        self.sec_bubble.move(50, 275)
        self.sec_bubble.mousePressEvent = self.sec_bubble_clicked

        self.sec_bubble_heading = QLabel(self.sec_bubble)
        self.sec_bubble_heading.setObjectName("bubble_heading")
        self.sec_bubble_heading.setText("Compress Multiple Images")
        self.sec_bubble_heading.move(55, 8)

        self.sec_bubble_para = QLabel(self.sec_bubble)
        self.sec_bubble_para.setText("Want to compress multiple Images at once? Select the folder and get the compressed version of the images in another folder!")
        self.sec_bubble_para.setWordWrap(True);
        self.sec_bubble_para.setObjectName("bubble_para")
        self.sec_bubble_para.move(35, 35)

        #...............Single Bubble Expanded....................
        self.single_bubble_expanded =QFrame(self)
        self.single_bubble_expanded.setObjectName("bubble_expanded")
        self.single_bubble_expanded.move(50, 100)
        self.single_bubble_expanded.setVisible(False)

        
        self.back_arrow_s = QLabel(self.single_bubble_expanded)
        self.back_arrow_s.move(20, 0)
        self.back_arrow_s.setObjectName("back_arrow")
        self.back_arrow_s.setTextFormat(Qt.RichText)
        self.back_arrow_s.setText("&#8592;")
        self.back_arrow_s.mousePressEvent = self.back_arrow_clicked

        self.single_bubble_heading = QLabel(self.single_bubble_expanded)
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.setText("Compress Image")
        self.single_bubble_heading.move(90, 8)

        self.select_image_label = QLabel(self.single_bubble_expanded)
        self.select_image_label.setObjectName("bubble_para")
        self.select_image_label.setText("Choose Image")
        self.select_image_label.move(30, 50)

        self.image_path = QLineEdit(self.single_bubble_expanded)
        self.image_path.setObjectName("path_text")
        self.image_path.move(60, 85)

        self.browse_button = QPushButton(self.single_bubble_expanded)
        self.browse_button.setText("...")
        self.browse_button.setObjectName("browse_button")
        self.browse_button.clicked.connect(self. select_file)
        self.browse_button.move(240,85)

        self.select_image_quality = QLabel(self.single_bubble_expanded)
        self.select_image_quality.setObjectName("bubble_para")
        self.select_image_quality.setText("Choose Quality")
        self.select_image_quality.move(30,130)

        self.quality_path = QLineEdit(self.single_bubble_expanded)
        self.quality_path.setObjectName("quality_path_text")
        self.quality_path.move(60, 160)

        self.quality_combo = QComboBox(self.single_bubble_expanded)
        self.quality_combo.addItem("High")
        self.quality_combo.addItem("Medium")
        self.quality_combo.addItem("Low")
        self.quality_combo.move(170, 160)
        self.quality_combo.currentIndexChanged.connect(self.quality_current_value)
        self.quality_combo.setObjectName("quality_combo")
        self.quality_combo.resize(96, 26)

        self.compress_image = QPushButton(self.single_bubble_expanded)
        self.compress_image.setText("Compress")
        self.compress_image.setObjectName("compress_button")
        self.compress_image.clicked.connect(self.resize_pix)
        self.compress_image.move(100, 260)

        #.................End Single Bubble Expanded.................

        #...................Directory Bubble Expanded...........
        self.sec_bubble_expanded =QFrame(self)
        self.sec_bubble_expanded.setObjectName("bubble_expanded")
        self.sec_bubble_expanded.move(50, 100)
        self.sec_bubble_expanded.setVisible(False)

        self.back_arrow_d = QLabel(self.sec_bubble_expanded)
        self.back_arrow_d.move(10, 5)
        self.back_arrow_d.setObjectName("back_arrow")
        self.back_arrow_d.setTextFormat(Qt.RichText)
        self.back_arrow_d.setText("&#8592;")
        self.back_arrow_d.mousePressEvent = self.back_arrow_clicked

        self.sec_bubble_heading = QLabel(self.sec_bubble_expanded)
        self.sec_bubble_heading.setObjectName("bubble_heading")
        self.sec_bubble_heading.setText("Compress Multiples Images")
        self.sec_bubble_heading.move(70, 8)

        self.select_source_label = QLabel(self.sec_bubble_expanded)
        self.select_source_label.setObjectName("bubble_para")
        self.select_source_label.setText("Choose source directory")
        self.select_source_label.move(30, 50)

        self.source_path = QLineEdit(self.sec_bubble_expanded)
        self.source_path.setObjectName("path_text")
        self.source_path.move(60, 85)

        self.browse_source_button = QPushButton(self.sec_bubble_expanded)
        self.browse_source_button.setText("...")
        self.browse_source_button.setObjectName("browse_button")
        self.browse_source_button.clicked.connect(self.select_folder_source)
        self.browse_source_button.move(240,85)

        self.select_dest_label = QLabel(self.sec_bubble_expanded)
        self.select_dest_label.setObjectName("bubble_para")
        self.select_dest_label.setText("Choose destination directory")
        self.select_dest_label.move(30, 130)

        self.dest_path = QLineEdit(self.sec_bubble_expanded)
        self.dest_path.setObjectName("path_text")
        self.dest_path.move(60, 160)

        self.browse_dest_button = QPushButton(self.sec_bubble_expanded)
        self.browse_dest_button.setText("...")
        self.browse_dest_button.setObjectName("browse_button")
        self.browse_dest_button.clicked.connect(self.select_folder_dest)
        self.browse_dest_button.move(240,160)

        self.select_sec_quality = QLabel(self.sec_bubble_expanded)
        self.select_sec_quality.setObjectName("bubble_para")
        self.select_sec_quality.setText("Choose Quality")
        self.select_sec_quality.move(30,205)

        self.quality_sec_path = QLineEdit(self.sec_bubble_expanded)
        self.quality_sec_path.setObjectName("quality_path_text")
        self.quality_sec_path.move(60, 235)

        self.quality_sec_combo = QComboBox(self.sec_bubble_expanded)
        self.quality_sec_combo.addItem("High")
        self.quality_sec_combo.addItem("Medium")
        self.quality_sec_combo.addItem("Low")
        self.quality_sec_combo.move(170, 235)
        self.quality_sec_combo.currentIndexChanged.connect(self.quality_current_value)
        self.quality_sec_combo.setObjectName("quality_combo")
        self.quality_combo.resize(96, 26)

        self.compress_dir = QPushButton(self.sec_bubble_expanded)
        self.compress_dir.setText("Compress")
        self.compress_dir.setObjectName("compress_button")
        self.compress_dir.clicked.connect(self.resize_folder)
        self.compress_dir.move(100, 290)


        #.................End Dir Bubble.................
 
        #.....................end main window......................

        self.show()

    #.............................Functions............................
    
    def select_file(self):
        
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);; JPEG (*.jpeg)")
        if fileName:
            print(fileName, _)
            self.image_path.setText(fileName)
            img = Image.open(fileName)
            self.image_width = img.width
            self.quality_path.setText(str(self.image_width))

    def select_folder_source(self):
         folder = QFileDialog.getExistingDirectory(self, "select Directory")
         print(folder)
         self.source_path.setText(folder)
         files = os.listdir(folder)
         first_pix = folder + "/" +files[0]
         img = Image.open(first_pix)
         self.image_width = img.width
         self.quality_sec_path.setText(str(self.image_width))
        
    def select_folder_dest(self):
         folder = QFileDialog.getExistingDirectory(self, "select Directory")
         print(folder)   
         self.dest_path.setText(folder)

    def quality_current_value(self):
        if self.quality_combo.currentText() == "High":
            self.quality_path.setText(str(self.image_width))


        if self.quality_combo.currentText() == "Medium":
            self.quality_path.setText(str(int(self.image_width/2)))


        if self.quality_combo.currentText() == "Low":
            self.quality_path.setText(str(int(self.image_width/4)))
    
        if self.quality_sec_combo.currentText() == "High":
            self.quality_sec_path.setText(str(self.image_width))

        if self.quality_sec_combo.currentText() == "Medium":
            self.quality_sec_path.setText(str(int(self.image_width/2)))
 
        if self.quality_sec_combo.currentText() == "Low":
            self.quality_sec_path.setText(str(int(self.image_width/4)))


    def back_arrow_clicked(self, event):
        self.single_bubble.setVisible(True)
        self.sec_bubble.setVisible(True)
        self.single_bubble_expanded.setVisible(False)
        self.sec_bubble_expanded.setVisible(False)    
    
    def single_bubble_clicked(self, event):
        print("single bubble clicked")
        self.single_bubble.setVisible(False)
        self.sec_bubble.setVisible(False)
        self.single_bubble_expanded.setVisible(True)
        self.sec_bubble_expanded.setVisible(False)


    def sec_bubble_clicked(self, event):
        print("sec bubble clicked")
        self.single_bubble.setVisible(False)
        self.sec_bubble.setVisible(False)
        self.single_bubble_expanded.setVisible(False)
        self.sec_bubble_expanded.setVisible(True)

    
    def resize_pix(self):
        old_pix = self.image_path.text()
        print(old_pix)
        print(int(self.quality_path.text()))

        dirs = self.image_path.text().split("/")
        print(dirs)
        new_pix = ""
        new_pix_name, okPressed = QInputDialog.getText(self, "Save Image as","Image name:", QLineEdit.Normal, "")
        if okPressed and new_pix_name != '':
            print(new_pix_name)

            if old_pix[-4:] == "*.jpeg":
                new_pix_name+="*.jpeg"


            if old_pix[-4:] == "*.png":
                new_pix_name+="*.png"

            if old_pix[-4:] == "*.jpg":
                new_pix_name+="*.jpg"
            else:
                new_pix_name+=".jpeg"

        for dir in dirs[:-1]:
            new_pix = new_pix + dir + "/"

        new_pix += new_pix_name
        print(new_pix)

        self.compressionCode(old_pix, new_pix, int(self.quality_path.text()))
        self.statusBar().showMessage("Message: Compressed")

    def resize_folder(self):
        src_dir = self.source_path.text()
        files = os.listdir(src_dir)
        dest_dir = self.dest_path.text()
        i = 0
        for file in files:
            i+=1
            print(file)
            if file[-4:] == '.jpg' or file[-4:] == '.png' or file[-5:] == '.jpeg' or file[-4:] == '.JPG' or file[-4:] == '.PNG' or file[-5:] == '.JPEG':

                old_pix = src_dir+"/"+file
                new_pix = dest_dir+"/"+file

                img = Image.open(old_pix)
                self.image_width = img.width
                self.quality_sec_path.setText(str(self.image_width))

                old_pix = src_dir+"/"+file
                new_pix = dest_dir+"/"+file

                print(old_pix) 
                print(new_pix)

                self.compressionCode(old_pix, new_pix, self.image_width)

                total_images = len(files)
                images_done = i 
                percentage = int(images_done / total_images * 100)

                self.statusBar().showMessage("Message: Compressed "+ str(int(images_done/total_images*100)) + "%")

            else:
                print("ignored" + file)
                continue
        self.statusBar().showMessage("Message: Compressed")

    def compressionCode(self, old_pix, new_pix, my_width):
        try:
            img = Image.open(old_pix)
            
            wpercent = (my_width / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((my_width, hsize), PIL.Image.ANTIALIAS)
            img.save(new_pix)
        except Exception as e:
            self.statusBar().showMessage("Message: "+e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())