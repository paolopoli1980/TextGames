import os
import math
import random
import time
import keyboard
class Player:
    def __init__(self,n):
        self.x=0
        self.y=0
        self.mvx=1
        self.mvy=0
        self.path=[]
        self.enemysight=[]
        self.escapesight=[]
        self.keyk=[]
        self.countbox=[[1 for i in range(n)] for j in range(n)]
    
    
    def simple_heromov(self,newchoice,backtrace,level):
        if schema[self.y][self.x]=='k':
            self.keyk.append('k')
        cancelkey=False
        if schema[self.y][self.x]=='K' and len(self.keyk)!=0:
            cancelkey=True
        if schema[self.y][self.x]=='*' or schema[self.y][self.x]=='|' or (schema[self.y][self.x]=='K' and len(self.keyk)==0): #or  newchoice==True:
            
            self.x-=self.mvx
            self.y-=self.mvy
            
            nextmv=random.randint(0,4)

            if nextmv==0:
                self.mvx=1
                self.mvy=0

            if nextmv==1:
                self.mvx=-1
                self.mvy=0

            if nextmv==2:
                self.mvx=0
                self.mvy=1

            if nextmv==3:
                self.mvx=0
                self.mvy=-1
                
        else:
            schema[self.y][self.x]='@'
            schema[yold][xold]='-'
 
        if level==1:
            choosen=False
            if self.mvx!=0 and (schema[self.y+1][self.x]=='-' or schema[self.y-1][self.x]=='-' or schema[self.y+1][self.x]=='E' or schema[self.y-1][self.x]=='E' or schema[self.y+1][self.x]=='k' or schema[self.y-1][self.x]=='k') or ((schema[self.y+1][self.x]=='K' or schema[self.y-1][self.x]=='K') and len(self.keyk)!=0)  and backtrace==False:
                choice=random.randint(0,4)
                if choice==0:
                    self.mvx=0
                    self.mvy=1
                    
                if choice==1:
                    self.mvx=0
                    self.mvy=-1
                if choice<=1:     
                    choosen=True
                   
            if choosen==False:
                if self.mvy!=0 and (schema[self.y][self.x+1]=='-' or schema[self.y][self.x-1]=='-' or schema[self.y][self.x+1]=='E' or schema[self.y][self.x-1]=='E' or schema[self.y][self.x+1]=='k' or schema[self.y][self.x-1]=='k') or ((schema[self.y][self.x-1]=='K' or schema[self.y][self.x+1]=='K') and len(self.keyk)!=0) and backtrace==False:
                    choice=random.randint(0,2)
                    if choice==0:
                        self.mvx=1
                        self.mvy=0
                        
                    if choice==1:
                        self.mvx=-1
                        self.mvy=0

            if cancelkey==True:
                self.keyk.remove('k')

        if level==2:
            memv=10**6
            if self.mvx!=0 and (schema[self.y+1][self.x]=='-' or schema[self.y-1][self.x]=='-'or schema[self.y+1][self.x]=='E' or schema[self.y-1][self.x]=='E' or schema[self.y+1][self.x]=='k' or schema[self.y-1][self.x]=='k' )or ((schema[self.y+1][self.x]=='K' or schema[self.y-1][self.x]=='K') and len(self.keyk)!=0)  and backtrace==False:
                v1=self.countbox[self.y+1][self.x]
                v2=self.countbox[self.y-1][self.x]
               #totv=1/v1+1/v2
                #choice=random.uniform(0,totv)
                if v1<v2:
                    self.mvx=0
                    self.mvy=1
                    memv=v1
                    
                if v1>=v2:
                    self.mvx=0
                    self.mvy=-1
                    memv=v2
               
                
            
            if self.mvy!=0 and (schema[self.y][self.x+1]=='-' or schema[self.y][self.x-1]=='-' or schema[self.y][self.x+1]=='E' or schema[self.y][self.x-1]=='E' or schema[self.y][self.x+1]=='k' or schema[self.y][self.x-1]=='k') or ((schema[self.y][self.x-1]=='K' or schema[self.y][self.x+1]=='K') and len(self.keyk)!=0)  and backtrace==False:
                v1=self.countbox[self.y][self.x+1]
                v2=self.countbox[self.y][self.x-1]
               # totv=1/v1+1/v2

               # choice=random.uniform(0,totv)
                if v1<v2 and v1<memv:
                    self.mvx=1
                    self.mvy=0
                    
                if v1>=v2 and v2<memv:
                    self.mvx=-1
                    self.mvy=0                   

            if cancelkey==True:
                self.keyk.remove('k')

        if level==3:
            memv=10**6
            if self.mvx!=0 and (schema[self.y+1][self.x]=='-' or schema[self.y-1][self.x]=='-'or schema[self.y+1][self.x]=='E' or schema[self.y-1][self.x]=='E' or schema[self.y+1][self.x]=='k' or schema[self.y-1][self.x]=='k' )or ((schema[self.y+1][self.x]=='K' or schema[self.y-1][self.x]=='K' ) and len(self.keyk)!=0)  and backtrace==False:
                v1=self.countbox[self.y+1][self.x]
                v2=self.countbox[self.y-1][self.x]
                v3=self.countbox[self.y][self.x+1]
                v4=self.countbox[self.y][self.x-1]
                if schema[self.y][self.x+1]=='*' or schema[self.y][self.x+1]=='|' or (schema[self.y][self.x+1]=='K' and len(self.keyk)==0):
                    v3=10**6
                if schema[self.y][self.x-1]=='*' or schema[self.y][self.x-1]=='|' or (schema[self.y][self.x-1]=='K' and len(self.keyk)==0):
                    v4=10**6
                    
                
                totv=1/v1+1/v2+1/v3+1/v4
                choice=random.uniform(0,totv)
                if choice<1/v1:
                    self.mvx=0
                    self.mvy=1
                    memv=v1
                    
                if choice>=1/v1 and choice<(1/v1+1/v2):
                    self.mvx=0
                    self.mvy=-1
                    memv=v2
               
                
            if memv==10**6:
                if self.mvy!=0 and (schema[self.y][self.x+1]=='-' or schema[self.y][self.x-1]=='-' or schema[self.y][self.x+1]=='E' or schema[self.y][self.x-1]=='E' or schema[self.y][self.x+1]=='k' or schema[self.y][self.x-1]=='k' ) or ((schema[self.y][self.x-1]=='K' or schema[self.y][self.x+1]=='K') and len(self.keyk)!=0)  and backtrace==False:
                    v1=self.countbox[self.y][self.x+1]
                    v2=self.countbox[self.y][self.x-1]
                    totv=1/v1+1/v2

                    choice=random.uniform(0,totv)
                    if choice<1/v1:
                        self.mvx=1
                        self.mvy=0
                        
                    if choice>=1/v1:
                        self.mvx=-1
                        self.mvy=0                   
            if cancelkey==True:
                self.keyk.remove('k')
           
  

           

        if backtrace==True:
           # print('bakctrue')
            for k,element in enumerate(self.enemysight):
                minimo=10**6
                if math.sqrt((self.x-element[0])**2+(self.y-element[1])**2)<minimo:
                    minimo=math.sqrt((self.x-element[0])**2+(self.y-element[1])**2)
                    memh=k
            cont=0        
            while math.sqrt((self.x+self.mvx-self.enemysight[memh][0])**2+(self.y+self.mvy-self.enemysight[memh][1])**2)<math.sqrt((self.x-self.enemysight[memh][0])**2+(self.y-self.enemysight[memh][1])**2):
                cont+=1
                #print(cont,self.enemysight[memh])
                #time.sleep(0.5)
                
                nextmv=random.randint(0,4)

                if nextmv==0:
                    self.mvx=1
                    self.mvy=0

                if nextmv==1:
                    self.mvx=-1
                    self.mvy=0

                if nextmv==2:
                    self.mvx=0
                    self.mvy=1

                if nextmv==3:
                    self.mvx=0
                    self.mvy=-1
 
                if math.sqrt((self.x+self.mvx-self.enemysight[memh][0])**2+(self.y+self.mvy-self.enemysight[memh][1])**2)<math.sqrt((self.x-self.enemysight[memh][0])**2+(self.y-self.enemysight[memh][1])**2):
                    kdef=0.35
                    dice=random.uniform(0,1)
                    distance=math.sqrt((self.x+self.mvx-self.enemysight[memh][0])**2+(self.y+self.mvy-self.enemysight[memh][1])**2)
                    distance=math.exp(-kdef*distance**2)
                    if dice>distance:
                       # print('break',self.mvx,self.mvy)
                        #time.sleep(0.1)
                        break
                if (cont>100):
                    break
        

            


class Wolf:
    def __init__(self,xw,yw):
        self.x=xw
        self.y=yw
        self.mvx=1
        self.mvy=0
        self.path=[]
        self.pathnow=[]

    def simple_wolfmov(self,i,newchoice):
        
        if schema[self.y][self.x]=='*' or schema[self.y][self.x]=='|' or schema[self.y][self.x]=='K' or schema[self.y][self.x]=='k':# or newchoice==True:
            self.x-=self.mvx
            self.y-=self.mvy
            nextmv=random.randint(0,4)

            if nextmv==0:
                self.mvx=1
                self.mvy=0

            if nextmv==1:
                self.mvx=-1
                self.mvy=0

            if nextmv==2:
                self.mvx=0
                self.mvy=1

            if nextmv==3:
                self.mvx=0
                self.mvy=-1
                
        else:
            schema[self.y][self.x]='W'
            schema[yold][xold]='-'
        choosen=False
        if self.mvx!=0 and (schema[self.y+1][self.x]=='-' or schema[self.y-1][self.x]=='-'):# and newchoice==True:
            choice=random.randint(0,3)
            if choice==1:
                self.mvx=0
                self.mvy=1
                
            if choice==2:
                self.mvx=0
                self.mvy=-1
            choosen=True
        if choosen==False:    
            if  self.mvy!=0 and (schema[self.y][self.x+1]=='-' or schema[self.y][self.x-1]=='-'):# and newchoice==True:
                choice=random.randint(0,3)
                if choice==1:
                    self.mvx=1
                    self.mvy=0
                    
                if choice==2:
                    self.mvx=-1
                    self.mvy=-0    

def visual(y,x):
    
    if x==hero.x:
        vision=True
        if hero.y<y:
            yline=hero.y
        else:
            yline=y
        deltay=math.fabs(y-hero.y)
        for i in range(int(deltay)-1):

            yline+=1
            xline=hero.x
            
            xline=int(xline)
            if (schema[yline][xline])!='-' and (schema[yline][xline])!='@' :
                vision=False

    if x!=hero.x:        
        m=float((y-hero.y)/(x-hero.x))

        
        q=y-m*x
        deltax=math.fabs(x-hero.x)
        deltay=math.fabs(y-hero.y)
        
        vision=True
        if hero.x<x:
            xline=hero.x
        else:
            xline=x
        #print(x,y,deltax)
        for i in range(int(deltax)-1):

            xline+=1
            yline=m*xline+q
            yline=int(yline)
           # print(xline,yline)
           # print(schema[yline][xline])
            if (schema[yline][xline])!='-' and (schema[yline][xline])!='@':
                vision=False

        if hero.y<y:
            yline=hero.y
        else:
            yline=y
            
        for i in range(int(deltay)-1):

            yline+=1
            xline=(yline-q)/m
            
            xline=int(xline)
            if (schema[yline][xline])!='-' and (schema[yline][xline])!='@' :
                vision=False
    #vision=True
    if vision==True:
        if schema[y][x]=='-':
            hero.escapesight.append([x,y])
        if schema[y][x]=='W':
            hero.enemysight.append([x,y])
            
    return vision    
    
    
    

def screen_schema(n,whole):
    
    
    for i in range(n):
        if schema[i][0]=='"':
            break
        for j in range(n):

           
            
            if (schema[i][j]!=0 and schema!='"'):
                if schema[i][j]=='@' or visual(i,j)==True or whole==True : 
                    print(schema[i][j],end="")
                    
                    
               
                else:
                    print(" ",end="")
            elif schema[i][j]!='"':
                    print ("\n")
                    break

def read_schema(nfile):
    
    fileschema='sch'+str(nfile)+'/schema.txt'
    with open(fileschema) as f:
        maps=f.read()
    
    contalinee=0
    contacolonne=0
    for elemento in maps:
        if elemento!='\n':
            schema[contalinee][contacolonne]=elemento
            if elemento=='@':
                hero.x=contacolonne
                hero.y=contalinee
                
            if elemento=='W':
                wolves.append(Wolf(contacolonne,contalinee))
                
        else:
            contacolonne=-1
            contalinee+=1
                
        contacolonne+=1


   


                        
                        
level=2
nattempt=100                        
for ntemp in range(nattempt):
    n=100
    schema=[[0 for i in range(n)] for j in range(n)]
    hero=Player(n)
    wolves=[]
    read_schema('5')

    pathnow=[schema[hero.y][hero.x-1],schema[hero.y][hero.x+1],schema[hero.y-1][hero.x],schema[hero.y+1][hero.x]]
    hero.path=[schema[hero.y][hero.x-1],schema[hero.y][hero.x+1],schema[hero.y-1][hero.x],schema[hero.y+1][hero.x]]
    whole=False
    for element in wolves:
        element.pathnow=[schema[element.y][element.x-1],schema[element.y][element.x+1],schema[element.y-1][element.x],schema[element.y+1][element.x]]
    start=True



    
    for i in range(n):
        for j in range(n):
            if schema[j][i]=='*' or schema[j][i]=='|':
                hero.countbox[j][i]=10**6


    while start==True:
        hero.escapesight=[]
        hero.enemysight=[]
        
        os.system('cls')
        screen_schema(n,whole)
        time.sleep(0.05)
       
        
        xold=hero.x
        yold=hero.y
        heroxold=hero.x
        heroyold=hero.y
        hero.x+=hero.mvx
        hero.y+=hero.mvy
       # print('ddddddddddd\n')
       # print(hero.mvx,hero.mvy)
        #time.sleep(0.3)
        backtrace=False 
        if len(hero.enemysight)!=0:
            backtrace=True
           # print('vision')
            #hero.mvx=-hero.mvx
           # hero.mvy=-hero.mvy
            #time.sleep(0.4)

            

           
       
       
        if schema[hero.y][hero.x]=='E':
            print(ntemp+1)
            exit()
        if schema[hero.y][hero.x]=='W':
            start=False
            break
            
        newchoice=False
        
     #   if hero.path!=pathnow:
     #       hero.path[:]=pathnow[:]
     #       newchoice=True
        hero.simple_heromov(newchoice,backtrace,level)

        for i,element in enumerate(wolves):
            xold=element.x
            yold=element.y
            element.x+=element.mvx
            element.y+=element.mvy
            if schema[element.y][element.x]=='@':
                start=False
                break        
            newchoice=False 
     #       if element.path!=element.pathnow:
     #          element.path[:]=element.pathnow[:]
     #           newchoice=True
            element.simple_wolfmov(i,newchoice)
        hero.countbox[hero.y][hero.x]+=1
 
    whole=False
    screen_schema(n,whole)
    print (hero.countbox)
