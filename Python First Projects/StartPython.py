# -StartPython.py *- coding: utf-8 -*-
"""
Spyder Editor

#%% starts a new cell. Use second green triangle to run just the cell that
your mouse has last clicked in (or Ctrl-Enter on a PC or Command-Return on a
Macintosh or Menu>Run>Run Cell)
"""
#%%
def hello():
    print("Hello, world!")

#%%
def myname():
    print("My name is Nurul")
    
#%%
def ourschool():
    print("Coursera is our school")

#%%  
  
""" This will run forever. In this case Ctrl-C will stop it, but sometimes
that doesn't work. In that case, click away IP Console to stop; click yes to 
kill kernel. Open a new IPConsole on the Console menu to restart """
#%%
def forever():
    while True:
        pass
  
#%% 
    def areaoftriangle(h,b):
        area = .5*h*b
        print("area of the triangle",area,"with","h = ",h,"and b = ", b)
#%%
def celsius_to_fahrenheit(temp):
    newTemp = (temp*9)/5+32
    print(temp,"celsius to fahrenheit is" ,newTemp, end='')
    print(" Ya gitu deh")
#%%
def name():
    fname = input("Enter your first name = ")
    lname = input("Enter your last name = ")
    address = input("Where do you live = ")
    fullname = fname +" "+ lname
    
    print("Your name is ", fullname)
    print("You are from ", address)
#%%
def tabung(d,t):
    volume = 3.14*d*t
    print("Volume tabung : ", volume)
#%%
a={} 
a[1]=1 
a[2]=[2,3,4] 
print(a[2][1])
#%%
 a={1:"A",2:"B",3:"C"} 
 print(a.get(1,4))
#%%
tuple1=(2,4,3) 
tuple3=tuple1*2 
print(tuple3)
#%%
 tupl=("annie","hena",5) 
 print(tupl[2])
 #%%
 tuple1=(5,1,7,6,2) 
 tuple1.pop(2) 
 print(tuple1)
