import maya.cmds as mc
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
            self.projList = os.listdir(self.variablePath) # [JIT,YIT]
            self.pathN = '' ## pathN "Y01_0010_Layout_"
            self.assN = ''
            
        def enter(self):
            self.listRealTimePath =  os.listdir(self.realTimePath)
            print self.listRealTimePath
            enter = raw_input()
            enter = str(enter)
            print enter
            return enter
                              
        def enterPath(self,input,*args):
            self.realTimePath = self.realTimePath + "/" + input
            print self.realTimePath
            self.listRealTimePath =  os.listdir(self.realTimePath)
            print self.listRealTimePath
            self.updateCh(input)
        
        def repath(self,*args):
            self.realTimePath = os.path.dirname(self.realTimePath)
            
        def save(self,name,*args):
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
            mc.file(rename = ''+self.realTimePath+'/%s%s.v%03d.ma'%(self.pathN,name,v+1))
            mc.file(save = True ,type = 'mayaAscii')
            ### save assets ###
            if 'asset' in self.realTimePath:
                self.pathN = '%s_%s_%s_'%(self.assN,self.shtN,self.deptN)
                print self.pathN
                mc.file(rename = ''+self.realTimePath+'/%s.v%03d.ma'%(self.pathN,v+1))
                mc.file(save = True ,type = 'mayaAscii')
        
        def saveover(self,name,*args):
            mc.file(rename = ''+self.realTimePath+'/'+name+'')
            mc.file(save = True ,type = 'mayaAscii')
            
        def open(self,name,*args):
            #(use self.realTimePath)
            mc.file(''+self.realTimePath+'/'+name+'',open=True)
            
            
            
        ###################
        #                 #
        ##### seperate ####
        #                 #
        ###################
        
        def set_proj(self,input,*args): # project
            self.projPath = '%s/%s'%(self.variablePath,input)
            self.realTimePath = self.projPath
            self.saList = os.listdir(self.projPath) # [asset , sequence]
            
        def set_sa(self,input,*args): # sequences / asset
            self.saPath = '%s/%s'%(self.projPath,input)
            self.realTimePath = self.saPath
            self.seqAssList = os.listdir(self.saPath)
        #### sequences path ####
                
        def set_seqAss(self,input,*args): # sequences
            self.seqAssPath = '%s/%s'%(self.saPath,input)
            self.realTimePath = self.seqAssPath
            self.shtNameList = os.listdir(self.seqAssPath) # [Y01_0010 , Y01_0010]
            if input == assets:
                self.assN = input
            
        def set_shtName(self,input,*args): # shot
            self.shtNamePath = '%s/%s'%(self.seqAssPath,input)
            self.realTimePath = self.shtNamePath
            self.deptList = os.listdir(self.shtNamePath) # [Layout , Animation]
            self.pathN += '%s_'%(input)
            self.shtN = input
            
        def set_dept(self,input,*args): # dept
            self.deptPath = '%s/%s/scenes'%(self.shtNamePath,input)
            self.realTimePath = self.deptPath
            self.filList = os.listdir(self.deptPath) # [Y01_0010_Layout_master.v001.ma , Y01_0010_Layout_master.v002.ma ]
            self.pathN += '%s_'%(input)
            self.deptN = input
         
        def updateCh(self,input,*args):
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
            for x in self.listRealTimePath:
                self.fileName = x
                self.fileDate = time.ctime(os.path.getmtime(('%s/%s')%(self.realTimePath,x)))
                self.Size = os.path.getsize('%s/%s'%(self.realTimePath,x))
                self.fileSize = self.convert_size(self.Size)
                print '%s : %s : %s'%(self.fileName,self.fileDate,self.fileSize)
        
        def set_default(self,*args):
            self.defaultPath = self.realTimePath
            self.realTimePath = self.defaultPath
        
            
t = fileManager()
t.enterPath(t.enter())
t.set_sa(t.enter())
t.enterPath(t.enter())
t.enterPath(t.enter())
t.enterPath(t.enter())
t.enterPath(t.enter())
t.save(t.enter())
t.display()