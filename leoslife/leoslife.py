#leoslife.py

# John Conways Game of Life.
plan='''displays: the text of the game of life for a set number of X x Y for a set of R turns. 
            
[-][-][-][-][-]
[-][-][-][-][-]
[-][-][-][-][-]
[-][-][-][-][-]
[-][-][-][-][-]

Get X,Y,T, Initial Values, Boundry conditions

Create a data space X x Y
Assign initial value
print initial value and the text' initial value'

do while turns<T:
    check data space according to boundry conditions
    create new data space according to rules and old data space.
    replace dataspace
    print data space.

print end. '''

#import modules needed to run

import random


# define functions to be used

#function to get an integer between lower and upper bound
def getnum(prompt,lower=3,upper=10000):
    while True:
        n=input(prompt+" Enter an integer between %s and %s. : " %(lower,upper))
        if n.isdigit():
            n=int(n)
            if lower<=n<=upper:
                return n

def printset(x):
    for i in x:
        print(i)


def basesurrounding(space,i,j):
    if i==0:
        if j==0:
            s=[space[i][j+1],space[i+1][j],space[i+1][j+1]]
        elif j==(y-1):
            s=[space[i][j-1],space[i+1][j-1],space[i+1][j]]
        else:
            s=[space[i][j-1],space[i][j+1],space[i+1][j-1],space[i+1][j],space[i+1][j+1]]
    elif i==(x-1):
        if j==0:
            s=[space[i-1][j],space[i-1][j+1],space[i][j+1]]
        elif j==(y-1):
            s=[space[i-1][j-1],space[i-1][j],space[i][j-1]]
        else:
            s=[space[i-1][j-1],space[i-1][j],space[i-1][j+1],space[i][j-1],space[i][j+1]]
    else:
        if j==0:
            s=[space[i-1][j],space[i-1][j+1],space[i][j+1],space[i+1][j],space[i+1][j+1]]
        elif j==(y-1):
            s=[space[i-1][j-1],space[i-1][j],space[i][j-1],space[i+1][j-1],space[i+1][j]]
        else:
            s=[space[i-1][j-1],space[i-1][j],space[i-1][j+1],space[i][j-1],space[i][j+1],space[i+1][j-1],space[i+1][j],space[i+1][j+1]]
    return(s)

def findsurrounding(space,i,j,boundry,x):
    if boundry=='d':
        surrounding=0
        for i in x:
            surrounding+=i
        return(surrounding)
    if boundry=='l':
        surrounding=8-len(x)
        for i in x:
            surrounding+=i
        return(surrounding)
    else:
        try:
            return(space[i-1][j-1]+space[i-1][j]+space[i-1][j+1]+space[i][j-1]+space[i][j+1]+space[i+1][j-1]+space[i+1][j]+space[i+1][j+1])
        except IndexError:
            try:#if x goes over. 
                return(space[i-1][j-1]+space[i-1][j]+space[i-1][j+1]+space[i][j-1]+space[i][j+1]+space[0][j-1]+space[0][j]+space[0][j+1])
            except IndexError:
                try:#if y goes over
                    return(space[i-1][j-1]+space[i-1][j]+space[i-1][0]+space[i][j-1]+space[i][0]+space[i+1][j-1]+space[i+1][j]+space[i+1][0])
                except IndexError:#both go over
                    return(space[i-1][j-1]+space[i-1][j]+space[i-1][0]+space[i][j-1]+space[i][0]+space[0][j-1]+space[0][j]+space[0][0])
   
def determinelife(surronding,space,i,j):
    if surronding==3:
        return(1)
    elif (surronding<2 or surronding>3):
        return(0)
    else:
        if space[i][j]==1:
            return(1)
        else:
            return(0)
  
#get x,y,t initial value, boundry condition

x=getnum('How many rows?')
y=getnum('How many columns?')
t=getnum('How many turns?')

#get boundry conditions
boundry=0
while boundry not in ("b","d","l"):   
    boundry=input("Press 'b' for bound dimenions, 'd' for dead boundry, or 'l' for live boundry. : ")

#get initial set up of space
initial=0
while initial not in ('r','c','g','e'):
    initial=input("Press 'r' for random intitial set up, 'c' for a checker board pattern, 'g' for a single glider, or 'e' for a pattern that repeats infinitely. : ")

    if initial=='g':
        if x<5:
            x=5
        if y<5:
            y=5
    if initial=='e':
        if x<6:
            x=6
        if y<6:
            y=6
#create space

space = []
for i in range(x):
    space.append([])
    for j in range(y):
        space[i].append(0)
    

#set intital distribution

if initial=='r':
    for i in range(x):
        for j in range(y):
            space[i][j]=random.randint(0,1)
elif initial=='c':
    for i in range(x):
        for j in range(y):
            if (i+j)%2==0:
                space[i][j]=1
            else:
                space[i][j]=0
elif initial=='g':
    space[1][2]=1
    space[2][3]=1
    space[3][1]=1
    space[3][2]=1
    space[3][3]=1
elif initial=='e':
    space[2][2]=1
    space[2][3]=1
    space[2][4]=1
    space[3][1]=1
    space[3][2]=1
    space[3][3]=1


#show initial conditions of board on turn 0
print("---------Turn 0---------\n")
printset(space)

for turn in range(t):
    #Create new empty space
    new=[]
    for i in range(x):
        new.append([])
        for j in range(y):
            new[i].append(0)
    #rewrite each space
    for i in range(x):
        for j in range(y):
            surrounding=findsurrounding(space,i,j,boundry,basesurrounding(space,i,j))
            mortality=determinelife(surrounding,space,i,j)
            new[i][j]=mortality
    space=new[:]
    print('-------Turn %s--------' %(str(turn+1)))
    printset(space)
#printset(space)
print("This is the end                                                                                   ")
