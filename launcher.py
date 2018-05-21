# coding:utf-8

from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from wpanels import loads, trans


from ui.frame import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        self.ob_file = None
        self.wpanel = None
        self.img_file = None
        self.img = None
        self.ob_name = None

        this = self

        self.label_ob_info.setText("使用说明:\n\n\n第一步:拖拽一个.ob文件到当前窗口")

        def a(event):
            print(event)
            if event.mimeData().hasUrls():
                file = str(event.mimeData().urls()[0].toLocalFile())

                print(file)
                if file.endswith(".ob"):
                    this.ob_file = file
                    this.wpanel = loads(file)

                    this.ob_name = file.split("/")[-1].split(".")[0]

                    save_file = "output_bmp/{}.png".format(this.ob_name)
                    this.wpanel.save(save_file)

                    bmp = QtGui.QPixmap(save_file)
                    self.label_ob.setPixmap(bmp)

                    self.label_ob_info.setText("加载表盘成功, bmp文件已经导出到{now_img}目录。\n\n\n第二步:拖拽一张{w}x{h}的图片到本窗口。(你也可以去output_bmp目录下找到{now_img}，修改后拖拽到本窗口"
                                               .format(wpanel=this.wpanel, w=this.wpanel.width, h=this.wpanel.height, now_img=save_file))
                elif file.endswith(".png") or file.endswith(".jpg") or file.endswith(".bmp"):

                    bmp = QtGui.QPixmap(file)
                    self.label_pic.setPixmap(bmp)
                    this.img_file = file
                else:
                    reply = QMessageBox.information(self,  #
                                                    "提示",
                                                    "不支持的文件格式，只支持.ob文件 以及图片.bmp .jpg .png",
                                                    QMessageBox.Yes)

        self.label_ob.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ob.setAcceptDrops(True)


        self.label_ob.dragEnterEvent=a

        self.btn_trans.clicked.connect(self.trans)

        self.checkBox.stateChanged.connect(self.change_color)


    def change_color(self, state):

        if state:
            self.label_pic.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.label_ob.setStyleSheet("background-color: rgb(0, 0, 0);")
        else:
            self.label_pic.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_ob.setStyleSheet("background-color: rgb(255, 255, 255);")


    def trans(self):

        if self.wpanel is None or self.ob_name is None:
            reply = QMessageBox.information(self,  #
                                            "提示",
                                            "请先拖拽添加一个.ob文件到本程序",
                                            QMessageBox.Yes)
            return
        if self.img_file is None:
            reply = QMessageBox.information(self,  #
                                            "提示",
                                            "请先拖拽添加一个图片文件到本程序",
                                            QMessageBox.Yes)
            return


        _, msg = trans("output_ob/{}.ob".format(self.ob_name), self.wpanel, self.img_file)

        if not _:
            reply = QMessageBox.information(self,  #
                                            "提示",
                                            msg,
                                            QMessageBox.Yes)

        else:
            self.label_ob_info.setText(u"转换成功，输出文件路径: {}".format(_))

if __name__ == "__main__":
    import sys
    import os

    if not os.path.exists("./output_bmp"):
        os.mkdir("./output_bmp")
    if not os.path.exists("./output_ob"):
        os.mkdir("./output_ob")

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())