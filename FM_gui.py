import maya.cmds as mc

if cmds.window('saveWindow' , q=True, ex=True):
    cmds.deleteUI('saveWindow' , window=True)
cmds.window('saveWindow' , t='Save / Open File')
cmds.columnLayout('projPath' ,adjustableColumn = True,cal='left')
cmds.rowLayout('pathLayout', numberOfColumns=3, columnWidth3=(80, 75, 150), adjustableColumn=2, columnAlign=(1, 'left'), columnAttach=[(1, 'left', 0), (2, 'left', 0), (3, 'left', 0)] )
cmds.text('path : ')
cmds.textField('path' , text = 'C/:...')
cmds.button(l = 'set as default path' , c = 'default')
cmds.setParent('..')
cmds.separator()
cmds.rowLayout( 'taskLayout',numberOfColumns=3, columnWidth3=(80, 75, 150), adjustableColumn=2, columnAlign=(1, 'left'), columnAttach=[(1, 'left', 0), (2, 'left', 0), (3, 'left', 0)] )
cmds.text('taskName : ')
cmds.textField('taskName' , text = 'master')
cmds.checkBox( label = "auto update version", onCommand = "on_func", offCommand = "off_func",value =1)
cmds.setParent('..')



cmds.columnLayout('menu2' ,adjustableColumn = True)
cmds.rowLayout('sec',adjustableColumn=2 , numberOfColumns=2)

cmds.columnLayout('projPath' ,adjustableColumn = True,cal='left')
cmds.optionMenuGrp( label='project : ' )
cmds.menuItem( label='Red' )
cmds.menuItem( label='Green' )
cmds.separator()
cmds.optionMenuGrp( label='S/A : ' )
cmds.menuItem( label='Red' )
cmds.menuItem( label='Green' )
cmds.separator()
cmds.optionMenuGrp( label='sequences/assets : ' )
cmds.menuItem( label='Red' )
cmds.menuItem( label='Green' )
cmds.separator()
cmds.optionMenuGrp( label='shot/name : ' )
cmds.menuItem( label='Red' )
cmds.menuItem( label='Green' )
cmds.separator()
cmds.optionMenuGrp( label='dept : ' )
cmds.menuItem( label='Red' )
cmds.menuItem( label='Green' )
cmds.setParent('..')

cmds.frameLayout ("Name", label = "Name" )
cmds.iconTextScrollList(allowMultiSelection=True, append=('sphere.png','two','three'))
cmds.setParent('..')


cmds.showWindow('saveWindow')