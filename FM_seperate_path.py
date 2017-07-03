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
            
        def set_proj(self,input): # project
            self.projPath = '%s/%s'%(self.variablePath,input)
            self.realTimePath = self.projPath
            self.saList = os.listdir(self.projPath) # [asset , sequence]
            
        def set_sa(self,input): # sequences / asset
            self.saPath = '%s/%s'%(self.projPath,input)
            self.realTimePath = self.saPath
            if input == 'sequences':
                self.seqList = os.listdir(self.saPath) # seq = [Y01,Y02]
            elif input == 'asset':
                self.assList = os.listdir(self.saPath) # asset = [character,props]
                
        #### sequences path ####
                
        def set_seqAss(self,input): # sequences
            self.seqAssPath = '%s/%s'%(self.saPath,input)
            self.realTimePath = self.seqAssPath
            self.shtNameList = os.listdir(self.seqAssPath) # [Y01_0010 , Y01_0010]
            
        def set_shtName(self,input): # shot
            self.shtNamePath = '%s/%s'%(self.seqAssPath,input)
            self.realTimePath = self.shtNamePath
            self.deptList = os.listdir(self.shtNamePath) # [Layout , Animation]
            self.pathN += '%s_'%(input)
            
        def set_dept(self,input): # dept
            self.deptPath = '%s/%s/scenes'%(self.shtNamePath,input)
            self.realTimePath = self.deptPath
            self.filList = os.listdir(self.deptPath) # [Y01_0010_Layout_master.v001.ma , Y01_0010_Layout_master.v002.ma ]
            self.pathN += '%s_'%(input)
            
       
        #### asset path ####    
        '''       
        def set_ass(self,input): # assets
            self.assPath = '%s/%s'%(self.saPath,input)
            self.realTimePath = self.assPath
            self.nameList = os.listdir(self.assPath) # [norman]
        
        def set_name(self,input): # name
            self.namePath = '%s/%s'%(self.assPath,input)
            self.realTimePath = self.namePath
            self.asdeptList = os.listdir(self.namePath) # [Model , Rig]
            
        def set_asdept(self,input): # asset dept
            self.asdeptPath = '%s/%s/scenes'%(self.namePath,input)
            self.realTimePath = self.asdeptPath
            self.asfilList = os.listdir(self.asdeptPath) # [char_norman_Rig.v001.ma]
        '''
         

        
        def enter(self):
            #### list
            self.listRealTimePath =  os.listdir(self.realTimePath)
            print self.listRealTimePath
            #### list
            enter = raw_input()
            enter = str(enter)
            return enter
        
        #def find(self,input):
            #re.findall

            
#t = fileManager()
#t.set_proj(t.enter())
#t.set_sa(t.enter())
#t.set_seqAss(t.enter())
#t.set_shtName(t.enter())
#t.set_dept(t.enter())

