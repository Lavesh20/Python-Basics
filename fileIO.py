str = "Hello I am Lavesh"

with open("test.txt","w") as f:
    f.write(str)

with open("test.txt","r") as f:
   s= f.read()
   print(s)

with open("test.txt","a") as f:
    f.write(" i am appending this")