### test sys ###
import getpass
import sys
user = getpass.getuser()
path = "C:/Users/"+user+"/Documents/yggSaveGUI"

if not path in sys.path:
    sys.path.append(path)

    
import package.FM_gui as gui

reload(gui)
