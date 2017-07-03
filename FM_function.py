import maya.cmds as mc
import re # regular Expression
import os #  os.listdir('C:/Users/Administrator/...')
### get user path ###
import getpass
########## Class File Manager ###################
class fileManager(object):
        def __init__(self):
            user = getpass.getuser()
            self.variablePath = 'C:/Users/'+user+'/Documents/yggintern'
            self.realTimePath = self.variablePath
            self.projList = os.listdir(self.variablePath) # [JIT,YIT]
            self.pathN = '' ## pathN "Y01_0010_Layout_"
            
        def enter(self):
            self.listRealTimePath =  os.listdir(self.realTimePath)
            print self.listRealTimePath
            self.enter = raw_input()
            self.enter = str(self.enter)
            return self.enter
                              
        def enterPath(self,input):
            self.listRealTimePath =  os.listdir(self.realTimePath)
            print self.listRealTimePath
            self.realTimePath = self.realTimePath + "/" + input
            if re.search("[A-Z][0-9]+[_][0-9]+",self.realTimePath):
                self.pathN += '%s_'%(input)
            print self.realTimePath
            
        def save(self,name,*args):
            pathN = 'Y01_0010_Layout_' # pathN = keep name of path "seq_shot_dept_"
            #name = "master" # name = keep name of file
            fil = os.listdir(''+self.realTimePath+'') # show list of file (realTimePath)
            v=0
            
            ### check version ###
            for c in fil:
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
            
        def open(self,name,*args):
            #(use self.realTimePath)
            mc.file(''+self.realTimePath+'/'+name+'',open=True)
            
#t = fileManager()
#t.enterPath(t.enter())
#t.enterPath(t.enter())
#t.enterPath(t.enter())
#t.enterPath(t.enter())
#t.enterPath(t.enter())
#t.enterPath(t.enter())