def levels():
    print("0.exit\n1.UP\n2.Down\n3.left\n4.rigth")
    i=int(input("? "))
    return i
x=0
y=0
files=input("give me the name of map .txt level")
f1=open("map.txt","r")
level=f1.read()
f1.close()
l=level.split("\n")
ttrue=True
xback=x
yback=y
while ttrue:
    xback=x
    yback=y
    a=levels()
    if a==0:
        ttrue=False
    elif a==1:
        y=y-1
    elif a==2:
        y=y+1
    elif a==3: 
        x=x-1
    elif a==4:
        x=x+1
    if y<0:
       x=xback
       y=yback
       print("out of board")
    elif x<0:
       x=xback
       y=yback
       print("out of board")
    elif x>len(l[y]):
       x=xback
       y=yback
       print("out of board")
    elif y>len(l):
       x=xback
       y=yback
       print("out of board")
    ll=l[y]
    lll=ll[x]
    print("X:"+str(x)+",Y:"+str(y)+"\nroom:"+lll)
