# -*- coding: utf-8 -*-
import base64
import json
import qrcode

def one(x):
    if x==0:
        ip=input("Pleae input the context you would like to encode:")
        try:
            st=ip.encode()
            res=base64.b64encode(st)
            print(res.decode())
        except:
            print("wrong input")
    else:
        ip=input("Pleae input the context you would like to decode:")
        try:
            st=ip.encode()
            res=base64.b64decode(st)
            print(res.decode())
        except:
            print("wrong input")
            
def two():   
 try:
    ip=input("Use commas to separate the character strings:")
    arr=ip.split(",")
    arr1=arr[::2]
    arr2=arr[1::2]
    d0={}
    i=0
    while i<len(arr1):
       n=arr1[i]
       d0[n]= arr2[i]
       i=i+1
    js=json.dumps(d0)
    print(js)
    print(type(js))

    d1={}
    j=0
    while j<len(arr2):
      m=arr2[j]
      d1.setdefault(m,[]).append(arr1[j])
      j=j+1
    print(d1)
    print(type(d1))
 except:
    print("wrong input")
    

def three():
    
   ip=input('Please input the name of your file:')
   op=open("{}.txt".format(ip))
   data=op.read()
   img_file = r'qrcode.jpg'

   img = qrcode.make(data)

   img.save(img_file)

   img.show()


num=input("Which function do you want to use? Input 1,2 or 3:")
if num=="1":
    num0=input("Please input 0 to encode, 1 to decode:")
    one(num0)
elif num=="2":
    two()
else:
    three()
    


   


