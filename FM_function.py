import maya.cmds as cmds
import re # regular Expression
import os #  os.listdir('C:/Users/Administrator/...')
import time
import math
### get user path ###
import getpass
########## Class File Manager ###################
class fileManager(object):
        def __init__(self):
            user = getpass.getuser()
            self.variablePath = 'C:/Users/'+user+'/Documents/yggintern'
            self.defaultPath = self.variablePath
            self.realTimePath = self.defaultPath
            self.listRealTimePath =  os.listdir(self.realTimePath)
            self.projList = os.listdir(self.variablePath) # [JIT,YIT]
            self.pathN = '' ## pathN "Y01_0010_Layout_"
            self.assN = ''
            self.up=1
            
            self.projPath = ''
            self.saList = []
            self.saPath = ''
            self.seqAssList = []
            self.seqAssPath = ''
            self.shtNameList = []
            self.shtNamePath = ''
            self.deptList = []
            self.deptPath = ''
        
        """    
        def enter(self):
            self.listRealTimePath =  os.listdir(self.realTimePath)
            print self.listRealTimePath
            enter = raw_input()
            enter = str(enter)
            print enter
            return enter
        """
                              
        def enterPath(self,*args):
            input = cmds.iconTextScrollList('displayN' ,q=True,selectItem=True)
            input = ''.join(input)
            if input in self.projList:
                count = 2
                for x in self.projList:
                    if input in x:
                        break
                    count+=1
                cmds.optionMenu(['projM'],e=True ,select = count )
                self.set_proj(input)
            if input in self.saList:
                count = 2
                for x in self.saList:
                    if input in x:
                        break
                    count+=1
                cmds.optionMenu(['sa'],e=True ,select = count )
                self.set_sa(input)
            if input in self.seqAssList:
                count = 2
                for x in self.seqAssList:
                    if input in x:
                        break
                    count+=1
                cmds.optionMenu(['seqAss'],e=True ,select = count )
                self.set_seqAss(input)
            if input in self.shtNameList:
                count = 2
                for x in self.shtNameList:
                    if input in x:
                        break
                    count+=1
                cmds.optionMenu(['shotName'],e=True ,select = count )
                self.set_shtName(input)
            if input in self.deptList:
                count = 2
                for x in self.deptList:
                    if input in x:
                        break
                    count+=1
                cmds.optionMenu(['dept'],e=True ,select = count )
                self.set_dept(input)
                
            """
            self.realTimePath = self.realTimePath + "/" + input
            print self.realTimePath
            self.listRealTimePath =  os.listdir(self.realTimePath)
            print self.listRealTimePath
            self.updateCh(input)
            self.set_path()
            """
        
        def repath(self,*args):
            self.realTimePath = os.path.dirname(self.realTimePath)
            
        def save(self,*args):
        #if self.up == 1:
            name = cmds.textField('taskName' , q=True , text=True)
            self.pathN = '%s_%s_'%(self.shtN,self.deptN) # pathN = keep name of path "seq_shot_dept_"
            #name = "master" # name = keep name of file
            #fil = os.listdir(''+self.realTimePath+'') # show list of file (realTimePath)
            v=0
            
            ### check version ##
            for c in self.listRealTimePath:
                if re.search(name,c): # name = name of file
                    b = re.search('[.][v][0-9]+',c)
                    b = str(b.group()) # b = v.xxx
                    ## version
                    a = re.search('[0-9]+',b)
                    a = int(a.group()) # a = x
                    print a
                    if a>v:
                        v=a # v = x (lastest version)
            #####################
            
            #(use self.realTimePath)
            cmds.file(rename = ''+self.realTimePath+'/%s%s.v%03d.ma'%(self.pathN,name,v+1))
            cmds.file(save = True ,type = 'mayaAscii')
            ### save assets ###
            if 'asset' in self.realTimePath:
                self.pathN = '%s_%s_%s_'%(self.assN,self.shtN,self.deptN)
                print self.pathN
                cmds.file(rename = ''+self.realTimePath+'/%s.v%03d.ma'%(self.pathN,v+1))
                cmds.file(save = True ,type = 'mayaAscii')
            self.set_path()
    
        #if self.up == 0 :
            #self.sel = ''.join(self.sel)
            #cmds.file(rename = ''+self.realTimePath+'/'+self.sel+'')
            #cmds.file(save = True ,type = 'mayaAscii')
            
        def open(self,*args):
            self.sel = ''.join(self.sel)
            #(use self.realTimePath)
            cmds.file(''+self.realTimePath+'/'+self.sel+'',open=True)
            
        #def updateOn(self,*args):
            #self.up = 1
        #def updateOff(self,*args):
            #self.up = 0
            
            
            
        ###################
        #                 #
        ##### seperate ####
        #                 #
        ###################
        
        def set_proj(self,input,*args): # project
                self.projPath = '%s/%s'%(self.variablePath,input)
                self.realTimePath = self.projPath
                if self.saList != []:
                    cmds.deleteUI( self.saList , menuItem=True)
                self.saList = os.listdir(self.projPath) # [asset , sequence]
                
                self.set_path()
                cmds.optionMenu(['sa'],e=True ,en=1)
                for x in self.saList:
                    cmds.menuItem(x , l = x , p = 'sa' )
                
                cmds.optionMenu(['sa'],e=True ,select=1)
                cmds.optionMenu(['seqAss'],e=True , en=0)
                cmds.optionMenu(['shotName'],e=True , en=0)
                cmds.optionMenu(['dept'],e=True , en=0)
            
        def set_sa(self,input,*args): # sequences / asset
            self.saPath = '%s/%s'%(self.projPath,input)
            self.realTimePath = self.saPath
            if self.seqAssList != []:
                cmds.deleteUI( self.seqAssList , menuItem=True)
            self.seqAssList = os.listdir(self.saPath)
            
            self.set_path()
            cmds.optionMenu(['seqAss'],e=True ,en=1)
            for x in self.seqAssList:
                cmds.menuItem(x , l = x , p = 'seqAss' )
             
            cmds.optionMenu(['seqAss'],e=True ,select=1)   
            cmds.optionMenu(['shotName'],e=True , en=0)
            cmds.optionMenu(['dept'],e=True , en=0)
        #### sequences path ####
                
        def set_seqAss(self,input,*args): # sequences
            self.seqAssPath = '%s/%s'%(self.saPath,input)
            self.realTimePath = self.seqAssPath
            if self.shtNameList != []:
                cmds.deleteUI( self.shtNameList , menuItem=True)
            self.shtNameList = os.listdir(self.seqAssPath) # [Y01_0010 , Y01_0010]
            if input == 'assets':
                self.assN = input
                
            self.set_path()
            cmds.optionMenu(['shotName'],e=True ,en=1)
            for x in self.shtNameList:
                cmds.menuItem(x , l = x , p = 'shotName' )
            
            cmds.optionMenu(['shotName'],e=True ,select=1)
            cmds.optionMenu(['dept'],e=True , en=0)
            
        def set_shtName(self,input,*args): # shot
            self.shtNamePath = '%s/%s'%(self.seqAssPath,input)
            self.realTimePath = self.shtNamePath
            if self.deptList != []:
                cmds.deleteUI( self.deptList , menuItem=True)
            self.deptList = os.listdir(self.shtNamePath) # [Layout , Animation]
            self.pathN += '%s_'%(input)
            self.shtN = input
            
            self.set_path()
            cmds.optionMenu(['dept'],e=True ,en=1)
            for x in self.deptList:
                cmds.menuItem(x , l = x , p = 'dept' )
            
        def set_dept(self,input,*args): # dept
            self.deptPath = '%s/%s/scenes'%(self.shtNamePath,input)
            self.realTimePath = self.deptPath
            self.filList = os.listdir(self.deptPath) # [Y01_0010_Layout_master.v001.ma , Y01_0010_Layout_master.v002.ma ]
            self.pathN += '%s_'%(input)
            self.deptN = input
            
            self.set_path()
            
        """ 
        def updateCh(self,*args):
            count = 2
            for x in self.projList:
                if input in x:
                    break
                count+=1
            return count
                        

            if input in self.projList:
                self.projPath = self.realTimePath
                self.saList = os.listdir(self.projPath)
            elif input in self.saList:
                self.saPath = self.realTimePath
                self.seqAssList = os.listdir(self.saPath)
            elif input in self.seqAssList:
                self.seqAssPath = self.realTimePath
                self.shtNameList = os.listdir(self.seqAssPath)
                if 'assets' in self.saPath:
                    self.assN = input
                    print self.assN
            elif input in self.shtNameList:
                self.shtNamePath = self.realTimePath
                self.deptList = os.listdir(self.shtNamePath)
                self.shtN = input
            elif input in self.deptList:
                self.deptPath = self.realTimePath
                self.filList = os.listdir(self.deptPath)
                self.deptN = input
        """
        
        def convert_size(self,size_bytes):
           if size_bytes == 0:
               return "0B"
           self.size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
           self.i = int(math.floor(math.log(size_bytes, 1024)))
           self.p = math.pow(1024, self.i)
           self.s = round(size_bytes / self.p, 2)
           return "%s %s" % (self.s, self.size_name[self.i])
            
        def display(self,*args):
            self.listRealTimePath =  os.listdir(self.realTimePath)
            self.fileDate = []
            self.fileSize = []
            for x in self.listRealTimePath:
                self.fileName = x
                self.fileDate.append (time.ctime(os.path.getmtime(('%s/%s')%(self.realTimePath,x))))
                self.Size = os.path.getsize('%s/%s'%(self.realTimePath,x))
                self.fileSize.append  (self.convert_size(self.Size))
        
        def set_default(self,*args):
            self.defaultPath = self.realTimePath
            self.realTimePath = self.defaultPath
        
        def set_path(self,*args):
            self.display()
            self.listRealTimePath =  os.listdir(self.realTimePath)
            cmds.text('path' ,e=True, l = self.realTimePath)
            cmds.iconTextScrollList('displayN',e=True,removeAll=True, append=(self.listRealTimePath))
            cmds.iconTextScrollList('displayD',e=True,removeAll=True, append=(self.fileDate))
            cmds.iconTextScrollList('displayS',e=True,removeAll=True, append=(self.fileSize))
            
        def sel(self,*args):
                self.sel = cmds.iconTextScrollList('displayN',q=True , selectItem=True)
                #if self.up == 0:
                    #self.sel = ''.join(self.sel)
                    #cmds.textField('taskName' , e=True , text = self.sel)

        
'''            
t = fileManager()
t.enterPath(t.enter())
t.set_sa(t.enter())
t.enterPath(t.enter())
t.enterPath(t.enter())
t.enterPath(t.enter())
t.enterPath(t.enter())
t.save(t.enter())
t.display()
'''