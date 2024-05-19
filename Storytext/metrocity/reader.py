import os
import sys
import msvcrt
import time

mapfile=open('map.txt','r')
print(mapfile)
matrixconnections=['0']
stringa='*'
lst=[]

class Room:
    def __init__(self,val,stringa,testo):
        
        self.series=stringa
        self.n=val
        self.txt=testo   

def elaborazione(rooms):

    story=open('story.txt','r')
    stringa='*'
    testo=''
    while stringa!='ENDSTORY\n':
        stringa=story.readline()
        testo=''
        series=[]
        try: 
            while stringa[0]=='{':

                val=int(stringa[1:-2])
                while stringa!='BEGINTXT\n':
                    stringa=story.readline()
                    if stringa!='BEGINTXT\n':
                        series.append(stringa[0:-1])
                while stringa!='ENDTXT\n':
                    stringa=story.readline()
                    if stringa!='ENDTXT\n':
                        testo+=stringa
                     
                rooms.append(Room(val,series,testo))
        except:
            pass

    lista=[]                   
    story.close()     
            
 
                            
def fine():
    return 'FINE'       

def block(n,steps,rooms,end):
    lenght=0
    testo=''
    pas=True
    for elem in rooms:     
        
        if elem.n==n:           
            
            for j in elem.series:
                lst=j.split()
                lista=lst[0].split(',')
 
                cont=0
                agree=False
                  
                for k,value in enumerate(steps):
                
                    if int(value)==int(lista[cont]):
                  
                        if cont+1<=len(lista):
                            if cont+1<len(lista):
                                cont+=1
                            else:

                                if len(lista)>lenght: 
                                    testo=elem.txt
                                    lenght=cont                         
    #print(testo)
    memx=''
    for x in testo:
      
      
        if x=='%' and memx=='£':
            pas=False                  
               
             
        memx=x
    
    return pas,testo
def movement(n,steps,rooms,end):
    lenght=0
    testo=''
    
    for elem in rooms:     
        
        if elem.n==n:           
            
            for j in elem.series:
                lst=j.split()
                lista=lst[0].split(',')
 
                cont=0
                agree=False
                  
                for k,value in enumerate(steps):
                
                    if int(value)==int(lista[cont]):
                  
                        if cont+1<=len(lista):
                            if cont+1<len(lista):
                                cont+=1
                            else:

                                if len(lista)>lenght: 
                                    testo=elem.txt
                                    lenght=cont                         
    print(testo)
    memx=''
    for x in testo:
      
      
        if x=='"' and memx=='!':
            if fine()=='FINE':              
                exit()   
             
        memx=x

                    
                
                
   
while stringa!='':
    stringa=mapfile.readline()
    
    matrixconnections.append(stringa[0:-1])


mapfile.close()
names=open('names.txt','r')
stringa='*'
nameslst=['x']
while stringa!='':
    stringa=names.readline()
    
    nameslst.append(stringa[0:-1])

names.close()

os.system('cls') 
n=1
end=False
steps=[n]
length=[0]
rooms=[]
elaborazione(rooms)
movement(n,steps,rooms,end)
while end==False:
    for i in range(len(matrixconnections)):
        numbers=matrixconnections[i].split(' ')
        if i==n:
            for j,el in enumerate(numbers):
                print(int(j+1),el,(nameslst[int(el)]))
            repeat=True
           
            while repeat==True:
                check=True
                choice=''
                char=''
                answer=''
               # while choice=='':
               #     choice=input('Scegli la tua destinazione.')
               # answer=input('Vuoi visitare il luogo? ')
               
                if msvcrt.kbhit():
                    choice = msvcrt.getch()
                   
                
               # print(choice)
                if choice==b'1':
                    char='1'
                if choice==b'2':
                    char='2'
                if choice==b'3':
                    char='3'
                if choice==b'4':
                    char='4'
                if choice==b'5':
                    char='5'
                if choice==b'6':
                    char='6'
                if choice==b'7':
                    char='7'
                if choice==b'8':
                    char='8'
                if choice==b'9':
                    char='9'
                    
                if char!='':
                    answer=input('Vuoi visitare il luogo?')

                #choice=char
                
                #for char in choice:
                   
                if char!='1' and char!='2' and char!='3' and char!='4' and char!='5' and char!='6' and char!='7' and char!='8' and char!='9':
                        
                    check=False
                if check==True:
                    repeat=False
                     
                    
            if (int(choice)<=len(numbers)) and int(choice)>0:
                memn=n
                n=int(numbers[int(choice)-1])
                if block(n,steps,rooms,end)[0]==False:
                    print(block(n,steps,rooms,end)[1])
                    n=memn
                    input()
                  
                
                if answer=='y' and int(choice)<=len(nameslst[int(el)]):                  
                   
                    length=[0]               
                  
                    os.system('cls')
                    movement(n,steps,rooms,end)
                    steps.append(n)
                    print(steps)
                    

            
            
                           
                      
