from PyQt4.QtCore import *
from PyQt4.QtGui import *

nameField = None
myDialog = None

def formOpen( dialog, layerid, featureid ):
  global myDialog
  myDialog = dialog
  global nameField
  nameField = dialog.findChild( QLineEdit, "name" )
  nameField.setText("Inserting a placename is mandatory")
  buttonBox = dialog.findChild(QDialogButtonBox, "buttonBox" )
  buttonBox.accepted.disconnect(dialog.accept)
  buttonBox.accepted.connect(validate)

def validate():
  if nameField.text() == "Inserting a placename is mandatory" or nameField.text().isEmpty():
    QMessageBox.critical( None, "Error", "Inserting a placename is mandatory")
  else:
    myDialog.accept()
    
