import sys
from PyQt5 import QtCore, QtGui,uic
 
qtCreatorFile = "design.ui" # Enter file here.
global ImageFile
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def Test(self):
		options = QtGui.QFileDialog.Options()
		options |= QtGui.QFileDialog.DontUseNativeDialog
		ImageFile = QtGui.QFileDialog.getOpenFileName(self,"Select Image To Process", "","All Files (*);;Image Files(*.jpg *.gif)",options=options)	
		exec(open('main.py').read())
		

	def Close(self):
		self.destroy()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())


