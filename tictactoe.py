def display(arr,ch):
  if(ch=='c'):
    one=5
    two=3
  else:
    one=3
    two=5
  for i in range(1,10):
   if(i%3==0):
     if(arr[i]==one):
       print('X')
     elif(arr[i]==two):
       print('O')
     else:
       print('0')
   else:
     if(arr[i]==one):
       print('X',end=" ")
     elif(arr[i]==two):
       print('O',end=" ")
     else:
       print('0',end=" ")
def find(a,b,c,s):
  if(s[a]==2):
    return a
  elif(s[b]==2):
    return b
  elif(s[c]==2):
    return c
def Possi_Win(a):
  if(a[1]*a[2]*a[3]==50):
    return [find(1,2,3,a),1]
  if(a[4]*a[5]*a[6]==50):
    return [find(4,5,6,a),1]
  if(a[7]*a[8]*a[9]==50):
    return [find(7,8,9,a),1]
  if(a[1]*a[4]*a[7]==50):
    return [find(1,4,7,a),1]
  if(a[5]*a[2]*a[8]==50):
    return [find(5,2,8,a),1]
  if(a[9]*a[6]*a[3]==50):
    return [find(3,6,9,a),1]
  if(a[1]*a[5]*a[9]==50):
    return [find(1,5,9,a),1]
  if(a[5]*a[7]*a[3]==50):
    return [find(3,5,7,a),1]
  if(a[1]*a[2]*a[3]==18):
    return [find(1,2,3,a),0]
  if(a[4]*a[5]*a[6]==18):
    return [find(4,5,6,a),0]
  if(a[7]*a[8]*a[9]==18):
    return [find(7,8,9,a),0]
  if(a[1]*a[4]*a[7]==18):
    return [find(1,4,7,a),0]
  if(a[5]*a[2]*a[8]==18):
    return [find(5,2,8,a),0]
  if(a[9]*a[6]*a[3]==18):
    return [find(9,6,3,a),0]
  if(a[1]*a[5]*a[9]==18):
    return [find(1,5,9,a),0]
  if(a[5]*a[7]*a[3]==18):
    return [find(5,7,3,a),0]
  for i in range(1,10):
    if(a[i]==2):
      return [i,0]
def Poss_Win(a):
  if(a[1]*a[2]*a[3]==18):
    return [find(1,2,3,a),0]
  if(a[4]*a[5]*a[6]==18):
    return [find(4,5,6,a),0]
  if(a[7]*a[8]*a[9]==18):
    return [find(7,8,9,a),0]
  if(a[1]*a[4]*a[7]==18):
    return [find(1,4,7,a),0]
  if(a[5]*a[2]*a[8]==18):
    return [find(5,2,8,a),0]
  if(a[9]*a[6]*a[3]==18):
    return [find(9,6,3,a),0]
  if(a[1]*a[5]*a[9]==18):
    return [find(1,5,9,a),0]
  if(a[5]*a[7]*a[3]==18):
    return [find(5,7,3,a),0]
  if(a[1]*a[2]*a[3]==50):
    return [find(1,2,3,a),1]
  if(a[4]*a[5]*a[6]==50):
    return [find(4,5,6,a),1]
  if(a[7]*a[8]*a[9]==50):
    return [find(7,8,9,a),1]
  if(a[1]*a[4]*a[7]==50):
    return [find(1,4,7,a),1]
  if(a[5]*a[2]*a[8]==50):
    return [find(5,2,8,a),1]
  if(a[9]*a[6]*a[3]==50):
    return [find(3,6,9,a),1]
  if(a[1]*a[5]*a[9]==50):
    return [find(1,5,9,a),1]
  if(a[5]*a[7]*a[3]==50):
    return [find(3,5,7,a),1]
  for i in range(1,10,2):
    if(a[i]==2):
      return [i,0]
def check(x,n,a):
  while(x>=10 or x<=0):
   print("Enter a valid position")
   x=int(input("Enter the %d player position"%(n)))
  if(a[x]==2):
     a[x]=3
  else:
    while(a[x]!=2):
      x=int(input("Enter the %d player position"%(n)))
      if(a[x]!=2):
        print("Position already taken, enter another position")
    a[x]=3
  return a
arr=[2]*10
flag=True
res=[0,0]
count=1
print("Enter which player should make first move--->computer or human ")
ch=input("Type c for computer and h for human")
ch=ch.lower()
if(ch=='h'):
  while(count<10):
    if(flag==True):
      x=int(input("Enter the 1st player position"))
      arr=check(x,1,arr)
      flag=False
      count+=1
    else:
      print("Computer move")
      if(count==2):
        if(arr[5]==2):
          arr[5]=5
        elif(arr[1]==2):
          arr[1]=5
      elif(count==4):
        res=Poss_Win(arr)
        arr[res[0]]=5
      else:
        res=Possi_Win(arr)
        arr[res[0]]=5
        if(res[1]==1):
          print("Computer  won: Depremssiom !")
          display(arr,ch)
          break
      flag=True
      count+=1
    display(arr,ch)
  if(count==10):
    print('Its a tie')
else:
  while(count<10):
    if(flag==True):
      print("Computer move")
      if(count==1):
        arr[5]=5
      elif(count==3):
        if(arr[1]==2):
          arr[1]=5
        else:
          arr[3]=5
      else:
        res=Possi_Win(arr)
        arr[res[0]]=5
        if(res[1]==1):
          print("Computer  won: Depremssiom !")
          display(arr,ch)
          break
      flag=False
      count+=1
    else:
       x=int(input("Enter the 1st player position"))
       arr=check(x,1,arr)
       flag=True
       count+=1
    display(arr,ch)
  if(count==10):
    print("It's a Tie")
