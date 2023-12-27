import math
import random
import numpy as np

wordkey=''

x=0
y=0
z=0
def achievements(xgalaxycenterdist, ygalaxycenterdist, zgalaxycenterdist,ho,maxdiam,mindiam,xi1,yi1,zi1,xi2,yi2,zi2):
    print('Try to complete the following achievements!')
    passyes=True
    try:
        centergalaxy=input('1) Insert the coordinate of the center of the galaxy (format x,y,z).')
        #galaxyradius=input('2) Insert the radius of the galaxy.(It lays in the middle of the galaxy, and the stellar density is (1/e) of the center stellar density')
        r1=input('2) Insert the center (integer coordinates) of the biggest empty island')
        r2=input('3) Insert the center (integer coordinates) of the smallest empty island')
        cx,cy,cz=centergalaxy.split(',')
        r1x,r1y,r1z = r1.split(',')
        r2x,r2y,r2z = r2.split(',')
        
        print(-xgalaxycenterdist,-ygalaxycenterdist,-zgalaxycenterdist)
        #print(ho)
        print(maxdiam,mindiam)
    except:
        passyes=False
 
    #print(int(cx),int(cy),int(cz))
    #print(passyes)
    try:
        print('ci sono',passyes)
        if (int(cx)!=-xgalaxycenterdist or int(cy)!=-ygalaxycenterdist or int(cz)!=-zgalaxycenterdist):
            passyes=False
            
 
        #if int(galaxyradius)!=int(ho):
            #passyes=False
            
#        if int(r1)!=int(maxdiam):
#            passyes=False
#        if int(r2)!=int(mindiam):
#            passyes=False
        if (int(xi1)!=int(r1x) or int(yi1)!=int(r1y) or int(zi1)!=int(r1z)):
            passyes=False

        if (int(xi2)!=int(r2x) or int(yi2)!=int(r2y) or int(zi2)!=int(r2z)):
            passyes=False

    except:
        passyes=False
        
    return passyes        
        
    


def rotation_function(alfa,beta,gamma,v):

    Ralfa=np.array([[1,0,0],[0,np.cos(alfa),-np.sin(alfa)],[0,np.sin(alfa),np.cos(alfa)]])
    Rbeta=np.array([[np.cos(beta),0,np.sin(beta)],[0,1,0],[-np.sin(beta),0,np.cos(beta)]])
    Rgamma=np.array([[np.cos(gamma),-np.sin(gamma),0],[np.sin(gamma),np.cos(gamma),0],[0,0,1]])
    Rtot=Rgamma.dot(v)
    Rtot=Rbeta.dot(Rtot)
    Rtot=Ralfa.dot(Rtot)
    return Rtot    

def tensor_calculation(alfa,beta,gamma):
    v=np.array([0,0,1])
    uzx,uzy,uzz=rotation_function(alfa,beta,gamma,v)
    v=np.array([0,1,0])
    uyx,uyy,uyz=rotation_function(alfa,beta,gamma,v)
    v=np.array([1,0,0])                     
    uxx,uxy,uxz=rotation_function(alfa,beta,gamma,v)
   # print('***********')
   # print(uxx,uxy,uxz)
   # print(uyx,uyy,uyz)
   # print(uzx,uzy,uzz)
  
    
   # print(uxx*uyx+uxy*uyy+uxz*uyz)
   # print(uyx*uzx+uyy*uzy+uyz*uzz)
   # print(uxx*uzx+uxy*uzy+uxz*uzz)
   
   # print(uxx**2+uxy**2+uxz**2)
   # print(uyx**2+uyy**2+uyz**2)
   # print(uzx**2+uzy**2+uzz**2)

   # print('*************')
    return np.array([[uxx,uxy,uxz],[uyx,uyy,uyz],[uzx,uzy,uzz]])

def parameters_calculation(rotatedbase,vec):
    solution=np.linalg.solve(rotatedbase.transpose(),vec)
    return solution
    
def empty_island(x,y,z,x0,y0,z0,a,b,c,galaxyx,galaxyy,galaxyz):
    if (x-galaxyx-x0)**2/a**2+(y-galaxyy-y0)**2/b**2+(z-galaxyz-z0)**2/c**2<=1:
        into=True
        
    else:
        into=False
    return into

    

def density_calculation(no,zthin,zthick,h0,x,y,z,alfa,beta,gamma,galaxyx,galaxyy,galaxyz,xi1,yi1,zi1,xi2,yi2,zi2,a1,b1,c1,a2,b2,c2):
   # print (xgalaxycenterdist, ygalaxycenterdist, zgalaxycenterdist)
    #print (matrix)
    matresults=parameters_calculation(matrix,np.array([x,y,z]))
    #print (matresults)
    zp=math.sqrt((matresults[0]*matrix[2][0])**2+(matresults[1]*matrix[2][1])**2+(matresults[2]*matrix[2][2])**2)
   # print('zp:='+str(zp))
    r=math.sqrt((x**2+y**2+z**2)-zp**2)
    
    n=no*(math.exp(-abs(zp)/zthin)+0.083*math.exp(-abs(zp)/zthick))*math.exp(-abs(r)/h0)
    #sec=2/(math.exp(abs(zp)/zthin))
    
    #print('values',x,y,z,xi1,yi1,zi1)
    if empty_island(x,y,z,xi1,yi1,zi1,a1,b1,c1,galaxyx,galaxyy,galaxyz)==True:
        n=0
    if empty_island(x,y,z,xi2,yi2,zi2,a2,b2,c2,galaxyx,galaxyy,galaxyz)==True:
        n=0

    # insert the empty island functions!
    return n


def linear_motion(x,y,z,memnmaxcords,memnmincords,alfa,beta,gamma,galaxyx,galaxyy,galaxyz,xi1,yi1,zi1,xi2,yi2,zi2,a1,b1,c1,a2,b2,c2):
    
    coordinates[0],coordinates[1],coordinates[2]=float(coordinates[0]),float(coordinates[1]),float(coordinates[2])
    
    

    distance=math.sqrt((coordinates[0])**2+(coordinates[1])**2+(coordinates[2])**2)
    dx,dy,dz=(coordinates[0])/int(distance),(coordinates[1])/int(distance),(coordinates[2])/int(distance)
    sx,sy,sz=0,0,0
    
    while abs(sx)<abs(coordinates[0]) or abs(sy)<abs(coordinates[1]) or abs(sz)<abs(coordinates[2]):
        sx+=dx
        sy+=dy
        sz+=dz

        x+=float(dx)
        y+=float(dy)
        z+=float(dz)
        if abs(sx)>abs(coordinates[0]) or abs(sy)>abs(coordinates[1]) or abs(sz)>abs(coordinates[2]):
            x-=float(dx)
            y-=float(dy)
            z-=float(dz)
             
        
        n=density_calculation(n0,zthin,zthick,h0,round(x),round(y),round(z),alfa,beta,gamma,galaxyx,galaxyy,galaxyz,xi1,yi1,zi1,xi2,yi2,zi2,a1,b1,c1,a2,b2,c2)
        
        
        if n>=memnmax[0]:
            memnmax[0]=n
            memnmaxcords=[round(x)-galaxyx,round(y)-galaxyy,round(z)-galaxyz]
            
        if n<=memnmin[0]:
            memnmin[0]=n
            memnmincords=[round(x)-galaxyx,round(y)-galaxyy,round(z)-galaxyz]
        print ('x:=' +str(round(x)-galaxyx)[:7]+'      y:='+str(round(y)-galaxyy)[:7]+'      z:='+str(round(z)-galaxyz)[:7]+'     SND:='+str(n))
    
    print('*********************************************************')    
    print ('mindensity:=' +str(memnmin[0])+ 'coordinate:= ' +str(memnmincords))
    print ('maxdensity:=' +str(memnmax[0])+ 'coordinate:= ' +str(memnmaxcords))
    
    return x,y,z,memnmaxcords,memnmincords


memnmax=[-10**9]
memnmaxcords=[0,0,0]
memnmin=[+10**9]
memnmincords=[0,0,0]


request=input('Do you want to load a game?:=')

if request=='y':
    filename=input('Insert the name of the file:=')
    with open(filename,"r") as f:
        zthin=int(f.readline())
        zthick=int(f.readline())
        h0=int(f.readline())
        n0=float(f.readline())
        coordinates=f.readline()
        galaxycenter=f.readline()
        smallestisland=f.readline()
        largestisland=f.readline()   
        mincord=f.readline()
        maxcord=f.readline()    
        
    
   
    lcoordinates=coordinates.split(',')
    lgalaxycenter=galaxycenter.split(',')
    lsmallestisland=smallestisland.split(',')
    llargestisland=largestisland.split(',')
    lmincord=mincord.split(',')
    lmaxcord=maxcord.split(',')
    

    x,y,z=float(lcoordinates[0]), float(lcoordinates[1]), float(lcoordinates[2])
    x,y,z=int(x), int(y), int(z)
    xgalaxycenterdist,ygalaxycenterdist,zgalaxycenterdist=int(lgalaxycenter[0]),int(lgalaxycenter[1]),int(lgalaxycenter[2])

    rotgalaxyalfa, rotgalaxybeta, rotgalaxygamma = math.pi/4*0, math.pi/4*1, math.pi/4*0

    matrix=tensor_calculation(rotgalaxyalfa, rotgalaxybeta, rotgalaxygamma)

    xi1,yi1,zi1,xi2,yi2,zi2 = int(lsmallestisland[0]),int(lsmallestisland[1]),int(lsmallestisland[2]),int(llargestisland[0]),int(llargestisland[1]),int(llargestisland[2]) 
    a1,b1,c1,a2,b2,c2 = lsmallestisland[3],lsmallestisland[4],lsmallestisland[5],llargestisland[3],llargestisland[4],llargestisland[5]
    a1,b1,c1,a2,b2,c2= int(a1),int(b1),int(c1),int(a2),int(b2),int(c2)
    memnmin[0]=float(lmincord[0])
    memnmax[0]=float(lmaxcord[0])
    memnmaxcords=[float(lmaxcord[1]),float(lmaxcord[2]),float(lmaxcord[3])]
    memnmincords=[float(lmincord[1]),float(lmincord[2]),float(lmincord[3])]

else:

    zthin=random.randint(50,100)
    zthick=random.randint(500,1000)
    #rgalaxy=5000

    minelicoef,maxelicoef=100,200
    minelipos,maxelipos=-1000,1000
    '''
    xgalaxycenterdist=1000
    ygalaxycenterdist=-1000
    zgalaxycenterdist=-5
    '''



        
    xgalaxycenterdist, ygalaxycenterdist, zgalaxycenterdist = random.randint(-1000,1000), random.randint(-1000,1000), random.randint(-100,100)

    x,y,z=xgalaxycenterdist, ygalaxycenterdist, zgalaxycenterdist

    rotgalaxyalfa, rotgalaxybeta, rotgalaxygamma = math.pi/4*0, math.pi/4*1, math.pi/4*0

    matrix=tensor_calculation(rotgalaxyalfa, rotgalaxybeta, rotgalaxygamma)

    xi1,yi1,zi1,xi2,yi2,zi2 = random.randint(minelipos,maxelipos), random.randint(minelipos,maxelipos), random.randint(minelipos,maxelipos),random.randint(minelipos,maxelipos), random.randint(minelipos,maxelipos), random.randint(minelipos,maxelipos)
    a1,b1,c1,a2,b2,c2 = random.uniform(minelicoef,maxelicoef),random.uniform(minelicoef,maxelicoef),random.uniform(minelicoef,maxelicoef),random.uniform(minelicoef,maxelicoef),random.uniform(minelicoef,maxelicoef),random.uniform(minelicoef,maxelicoef)
    a1,b1,c1,a2,b2,c2= int(a1),int(b1),int(c1),int(a2),int(b2),int(c2)



        

    #print (matrix)
    #print (xi1,yi1,zi1,a1,b1,c1)
    h0=random.randint(2000,4000)
    n0=0.1




#print(xgalaxycenterdist, ygalaxycenterdist, zgalaxycenterdist,h0)    
    
if a1>b1 and a1>c1:
    diam1=a1

if b1>a1 and b1>c1:
    diam1=b1

if c1>a1 and c1>b1:
    diam1=c1

if a2>b2 and a2>c2:
    diam2=a2

if b2>a2 and b2>c2:
    diam2=b2

if c2>a2 and c2>b2:
    diam2=c2

if diam1>diam2:
    maxdiam=diam1
    mindiam=diam2
else:
    maxdiam=diam2
    mindiam=diam1
        
    
while wordkey!='exit':
    wordkey=input('Insert the command:=')

    if wordkey=='rw':
        data=input('Insert the maxstep for axis:=')
        nsteps=input('Insert number of movements:=')
        
        try:
            nsteps=int(nsteps)
            for i in range(nsteps):
                data=int(data)
                
                coordinates=[random.randint(-data,data),random.randint(-data,data),random.randint(-data,data)]
            
                
                if len(coordinates)==3:
                    x,y,z,memnmaxcords,memnmincords = linear_motion(x,y,z,memnmaxcords,memnmincords,rotgalaxyalfa,rotgalaxybeta,rotgalaxygamma,xgalaxycenterdist,ygalaxycenterdist,zgalaxycenterdist,xi1,yi1,zi1,xi2,yi2,zi2,a1,b1,c1,a2,b2,c2)

        except:
            pass
                 
                
        
    if wordkey=='ml':
        
        data=input('Insert the displacement coordinates:=')
        coordinates=data.split(',')
       
        try:
            if len(coordinates)==3:
                x,y,z,memnmaxcords,memnmincords = linear_motion(x,y,z,memnmaxcords,memnmincords,rotgalaxyalfa,rotgalaxybeta,rotgalaxygamma,xgalaxycenterdist,ygalaxycenterdist,zgalaxycenterdist,xi1,yi1,zi1,xi2,yi2,zi2,a1,b1,c1,a2,b2,c2)

        except:
            pass
 
    if wordkey=='achievements':
            if diam1>=diam2:
                if achievements(xgalaxycenterdist, ygalaxycenterdist, zgalaxycenterdist,h0,maxdiam,mindiam,xi1,yi1,zi1,xi2,yi2,zi2)==True:
                    print('You won!')
                    exit
                else:
                    print ('You didn''t get the solution')
            if diam1<diam2:
                if achievements(xgalaxycenterdist, ygalaxycenterdist, zgalaxycenterdist,h0,maxdiam,mindiam,xi2,yi2,zi2,xi1,yi1,zi1)==True:
                    print('You won!')
                    exit
                else:
                    print ('You didn''t get the solution')
                
print(-xgalaxycenterdist, -ygalaxycenterdist, -zgalaxycenterdist)
print (h0)
print (xi2,yi2,zi2,a2,b2,c2)
print (xi1,yi1,zi1,a1,b1,c1)



request=input('Do you want to save the game?:=')


if request=='y':
    filename=input('Insert the name of the file:=')
    with open(filename,"w") as f:
        f.write(str(zthin)+str('\n'))
        f.write(str(zthick)+str('\n'))
        f.write(str(h0)+str('\n'))
        f.write(str(n0)+str('\n'))
        f.write(str(x)+','+str(y)+','+str(z)+str('\n'))
        f.write(str(xgalaxycenterdist)+','+ str(ygalaxycenterdist)+','+ str(zgalaxycenterdist)+str('\n'))
        f.write(str(xi1)+','+str(yi1)+','+str(zi1)+','+str(a1)+','+str(b1)+','+str(c1)+str('\n'))
        f.write(str(xi2)+','+str(yi2)+','+str(zi2)+','+str(a2)+','+str(b2)+','+str(c2)+str('\n'))
        f.write(str(memnmin[0])+','+str(memnmincords[0])+','+str(memnmincords[1])+','+str(memnmincords[2])+str('\n'))
        f.write(str(memnmax[0])+','+str(memnmaxcords[0])+','+str(memnmaxcords[1])+','+str(memnmaxcords[2])+str('\n'))
        
        
        
    f.close()
    print('ok')
   