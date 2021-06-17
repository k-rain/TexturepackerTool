# coding=utf-8
import os
import sys
import json
# import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class TexturePackerTool(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 101)
        Dialog.setMinimumSize(QtCore.QSize(463, 101))
        Dialog.setMaximumSize(QtCore.QSize(463, 101))
        Dialog.setWhatsThis("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.textEdit1 = QtWidgets.QTextEdit(Dialog)
        self.textEdit1.setGeometry(QtCore.QRect(80, 10, 331, 21))
        self.textEdit1.setObjectName("textEdit1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.textEdit2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit2.setGeometry(QtCore.QRect(80, 40, 331, 21))
        self.textEdit2.setObjectName("textEdit2")
        self.btnStart = QtWidgets.QPushButton(Dialog)
        self.btnStart.setGeometry(QtCore.QRect(380, 70, 71, 23))
        self.btnStart.setObjectName("btnStart")
        self.btnSelect1 = QtWidgets.QPushButton(Dialog)
        self.btnSelect1.setGeometry(QtCore.QRect(420, 10, 31, 23))
        self.btnSelect1.setObjectName("btnSelect1")
        self.btnSelect2 = QtWidgets.QPushButton(Dialog)
        self.btnSelect2.setGeometry(QtCore.QRect(420, 40, 31, 23))
        self.btnSelect2.setObjectName("btnSelect2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 68, 281, 28))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        Dialog.setToolTip(_translate("Dialog", "用于打单个文件夹的合图"))
        self.label.setText(_translate("Dialog", "合图源:"))
        self.textEdit1.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "输出目录:"))
        self.textEdit2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnStart.setText(_translate("Dialog", "开始合图"))
        self.btnSelect1.setText(_translate("Dialog", "选择"))
        self.btnSelect2.setText(_translate("Dialog", "选择"))
        self.label_3.setText(_translate(
            "Dialog", "使用说明：选择或键入路径后点击开始合图"))
        self.initUi(Dialog)

    def initUi(self, Dialog):
        Dialog.setWindowTitle("打合图工具")
        Dialog.resize(463, 100)
        Dialog.setFixedSize(463, 100)

        self.btnSelect1.clicked.connect(
            lambda: self.onSelect1Click(self.btnSelect1))
        self.btnSelect2.clicked.connect(
            lambda: self.onSelect2Click(self.btnSelect2))
        self.btnStart.clicked.connect(lambda: self.onStartClick(self.btnStart))

        inputPath = "G:/DGZ-A/arts/ui/GY_???"
        outputPath = "G:/DGZ-A/client/branches/develop/assets/resources/dgz_plist/"
        curPath = os.path.abspath('.')
        config = os.path.join(curPath, "config.json")
        if os.path.isfile(config):
            f = open(config, "r")
            dic = json.load(f)
            inputPath = dic["inputPath"]
            outputPath = dic["outputPath"]
            f.close()
        self.textEdit1.setPlainText(inputPath)
        self.textEdit2.setPlainText(outputPath)

    def isNonePath(self, pathStr):
        return (not pathStr or pathStr == "." or pathStr == "")

    def onSelect1Click(self, button):
        oldDir = self.textEdit1.toPlainText()
        if self.isNonePath(oldDir):
            oldDir = "./"
        path = QtWidgets.QFileDialog.getExistingDirectory(
            None, "选择合图源文件夹", oldDir)
        if self.isNonePath(path):
            path = oldDir
        self.textEdit1.setPlainText(str(path))

    def onSelect2Click(self, button):
        oldDir = self.textEdit2.toPlainText()
        if self.isNonePath(oldDir):
            oldDir = "./"
        path = QtWidgets.QFileDialog.getExistingDirectory(
            None, "选择输出文件夹", oldDir)
        if self.isNonePath(path):
            path = oldDir
        self.textEdit2.setPlainText(str(path))

    def pack_textures(self, inputPath, outputPath, opt, scale, maxSize, sheetSuffix, textureFormat, sizeConstraints, sheetName):
        packCommand = "TexturePacker" + \
            " --format cocos2d" \
            " --maxrects-heuristics best" \
            " --enable-rotation" \
            " --shape-padding 2" \
            " --border-padding 2" \
            " --trim-mode None" \
            " --basic-sort-by Name" \
            " --basic-order Ascending" \
            " --texture-format {textureFormat}" \
            " --data {outputSheetNamePath}{sheetName}.plist" \
            " --sheet {outputSheetNamePath}{sheetName}.{sheetSuffix}" \
            " --max-size {maxSize}" \
            " --opt {opt}" \
            " --size-constraints {sizeConstraints}" \
            " {inputPath}"

        packCommand = packCommand.format(
            textureFormat=textureFormat,
            outputSheetNamePath=os.path.join(outputPath, ""),
            sheetName=sheetName,
            sheetSuffix=sheetSuffix,
            maxSize=maxSize,
            opt=opt,
            sizeConstraints=sizeConstraints,
            inputPath=inputPath)
        os.system(packCommand)
        QMessageBox.information(MainWindow, "提示", "执行完成, 请检查输出目录",)

    # def clearDir(self, root):
    #     if not os.path.isdir(root):
    #         return
    #     dirList = os.listdir(root)
    #     for dir in dirList:
    #         filePath = os.path.join(root, dir)
    #         if os.path.isfile(filePath):
    #             os.remove(filePath)
    #         elif os.path.isdir(filePath):
    #             shutil.rmtree(filePath)

    def dicHasPic(self, dir):
        def isImg(fullName):
            strs = fullName.split(".")
            type = strs[len(strs)-1]
            type = type.lower()
            if type == 'jpg':
                return True
            elif type == 'png':
                return True
            elif type == 'jpeg':
                return True
            elif type == 'bmp':
                return True
            else:
                return False
        for x in os.listdir(dir):
            if isImg(x):
                return True
        return False

    def onStartClick(self, button):
        inDir = self.textEdit1.toPlainText()
        outDir = self.textEdit2.toPlainText()
        if not os.path.isdir(inDir):
            QMessageBox.information(MainWindow, "错误", "输入路径不存在")
            return
        if not self.dicHasPic(inDir):
            QMessageBox.information(MainWindow, "错误", "输入路径下不存在图片")
            return
        if not os.path.isdir(outDir):
            QMessageBox.information(MainWindow, "错误", "输出路径不存在")
            return

        dirList = inDir.split("/")
        lasDir = dirList[len(dirList)-1]

        self.pack_textures(inDir, outDir, 'RGBA8888', 1,
                           2048, 'png', "png", "POT", lasDir)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TexturePackerTool()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    input("输入任意按键继续...")
