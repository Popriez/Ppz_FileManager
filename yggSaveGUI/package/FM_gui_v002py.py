### test sys ###
import getpass
import sys
import maya.cmds as cmds
user = getpass.getuser()
path = "C:/Users/"+user+"/Documents/yggSaveGUI"
if not path in sys.path:
    sys.path.append(path)
    
import package.FM_function as function
reload(function)

f = function.fileManager()

f.display()


if cmds.window('saveWindow' , q=True, ex=True):
    cmds.deleteUI('saveWindow' , window=True)
cmds.window('saveWindow' , t='Save / Open File')
cmds.columnLayout('projPath' ,adjustableColumn = True,cal='left')
cmds.rowLayout('pathLayout', numberOfColumns=3, columnWidth3=(80, 75, 150), adjustableColumn=2, columnAlign=(1, 'left'), columnAttach=[(1, 'left', 0), (2, 'left', 0), (3, 'left', 0)] )
cmds.text('path : ')
cmds.text('path' , l = f.realTimePath ,backgroundColor = [0.18,0.18,0.18])
#cmds.button(l = 'set as default path' , c = f.set_default)
cmds.setParent('..')
cmds.separator()
cmds.rowLayout( 'taskLayout',numberOfColumns=2, columnWidth3=(80, 75, 150), adjustableColumn=2, columnAlign=(1, 'left'), columnAttach=[(1, 'left', 0), (2, 'left', 0), (3, 'left', 0)] )
cmds.text('taskName : ')
cmds.textField('taskName' , text = 'master')
#cmds.checkBox( label = "auto update version", onCommand = f.updateOn, offCommand = f.updateOff,value =1)
cmds.setParent('..')



cmds.rowLayout('sec',adjustableColumn=2 , numberOfColumns=2)

cmds.columnLayout('projPath' ,adjustableColumn = True,cal='left')

cmds.optionMenu(['projM'], label='project : ',changeCommand=f.set_proj )
cmds.menuItem( 'noneproj',label='none', p = 'projM' , en=False )
for x in f.listRealTimePath:
    cmds.menuItem(x , l = x , p = 'projM' )
cmds.separator(h=30)

cmds.optionMenu(['sa'], label='S/A : ' ,en=0 ,changeCommand=f.set_sa)
cmds.menuItem( 'nonesa',label='none', p = 'sa', en=False )
cmds.separator(h=30)

cmds.optionMenu(['seqAss'], label='sequences/assets : ' , en=0 , changeCommand=f.set_seqAss)
cmds.menuItem( 'noneseq',label='none', p = 'seqAss', en=False )
cmds.separator(h=30)

cmds.optionMenu(['shotName'], label='shot/name : ', en=0 , changeCommand=f.set_shtName )
cmds.menuItem( 'noneshot',label='none', p = 'shotName' , en=False)
cmds.separator(h=30)

cmds.optionMenu( ['dept'],label='dept : ', en=0 , changeCommand=f.set_dept )
cmds.menuItem( 'nonedept',label='none', p = 'dept', en=False )
cmds.setParent('..')

cmds.columnLayout('menu2' ,adjustableColumn = True,cal='right')
cmds.paneLayout(configuration = 'vertical3')
cmds.frameLayout ("Name", label ="Name",w=200 )
cmds.iconTextScrollList('displayN', append=(f.listRealTimePath),h=200 ,doubleClickCommand=f.enterPath , selectCommand=f.sel)
cmds.setParent('..')
cmds.frameLayout ("Date", label ="Date Modiefied" )
cmds.iconTextScrollList('displayD',allowMultiSelection=True,en=0, append=(f.fileDate),h=200 )
cmds.setParent('..')
cmds.frameLayout ("Size", label ="Size" )
cmds.iconTextScrollList('displayS',allowMultiSelection=True,en=0, append=(f.fileSize),h=200 )
cmds.setParent('..')
cmds.setParent('..')

cmds.rowLayout('trd' , numberOfColumns=2 , columnAlign=(1, 'right'))
cmds.button('open' , l='open' ,width=150 ,c = f.open)
cmds.button('save' , l='save' ,width=150 , c = f.save)


cmds.showWindow('saveWindow')