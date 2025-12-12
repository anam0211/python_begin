
""" begin
a=100
b=200
c=300
d='an'
e=100-50j
f=3.31324234234
 #print(a,b,c, sep='? ', end='/')
#day la chu thich """


"""
day la chu 
thich tren nhieu dong
"""

"""" in ra kieu du lieu, lam tron 
#print(type(d)) in  ra kieu du lieu cua bien
print(e)
print('%.2f' %f) #lam tron 2 chu so
g= nguyen hoai 
an
print(g) """


""" ep kieu:
s='12345' 
i=int(s)
print(i)
k=21424324221
st=str(k)
print(st) """


"""
 gan bien va swap
a,b,c=100,200,'ankuro'
print(a,b,c)

e=200
f=300
e,f=f,e
print(e,f)
 """


""" 
toan tu toan hoc
+ - * /
// chia nguyen
% chia du 
** luy thua
"""

""" toan tu logic
and toan tu va (20==20) and (1==1) true
or toan tu hoac or(10<20) or (20==50) true
not toan tu phu dinh not(20==20) false
"""


"""is so sanh hai doi tuong co nam trong cung o nho khong
a is b 
a is not b
"""

""" tim kiem tu trong xau
s='NGUYEN HOAI AN'
print('AN' in s)
print('PHUONG'not in s)
"""


""" nhap du lieu 
s=input('Nhap ten cua ban :')
print('in ra ten cua ban :', s)
a=input()
print(type(a)) #luon la kieu du lieu str

b=int(input('Nhap 1 so nguyen: ')) #ep kieu sang so int
print(type(b))
print(b)
"""

"""
s=input('Nhap 3 so : ')
a=s.split()  #a=[100,200,300]
x,y,z=map(int,a)
j,q,k=a
print(x+y+z) #cong cac so
print(j+q+k) #cong xau """

"""
x,y,z=map(int,input('Nhap 3 so').split())
print(x+y+z)
"""
#------------------------------------------------------
""" hamm
from math import *

print(sqrt(4)) #tra ve so thuc
isqrt #tra ve so nguyen
pow
ceil #lam tron len 2.2->3
floor #lam tron xuong 2.7-> 2
factorial #giai thua
gcd(a,b) #ucln
comb(n,k) #to hop chap k cua n

abs min max sum #ham co san
"""


"""
import math
print(help(math))
"""

#-------------------------------------------------
""" cau lenh if
a=8
if a>=10 and a%2==0:
    print('true')
elif a<10 and a%2==0:
    print('haft')
else: print('false')
"""
#--------------------------------------------
""" chuyen so ve ma ascii va ngươc lai
ord('A')   # 65
chr(65)    # 'A'
"""

#-----------------------------------------------
""" vong lap for va while
a=range(1,10,1)
for i in a:
    print(i,end=' ')


for i in range(51):
    print(i, end=' ') #in ra tu 0 den 50

for i in range(10,0,-1):
    print(i,end=' ') #giam tu 10 ve 1

print('\n')
n=10
s=0
for i in range(1,n+1):
    s+=i
print(s)

for i in range(1,7):
    print(i) #in ra so tu 1 den 7
    i+=100

for i in range(1,21):
    print(i, end=' ')
    if i%7==0:
        break
    print('cau lenh ben duoi break')

for i in range(1,10,3):
    print(i, end=' ')
"""


"""
a,b=10,20
while a<=b:
    print(a)
    a+=1



while True:
    n=int(input('Nhap n: '))
    if n>0: break

n=1234
dem=0
while n!=0:
    dem+=1
    n//=10
print(dem)    

n=1234
m=0
while n!=0:
    m=m*10+n%10
    n//=10
print(m)    

n=1234
print(len(str(n)))
"""

#----------------------------------------------
""" ham
def tong(a,b):
    res=a+b
    return res
print(tong(10,20))

def xinchao(name1,name2,name3):
    print('xin chao', name1,name2, name3)
xinchao('AN', 'Phương', 'My')

def change(n): #tam thoi
    n*=2

def infor(name,job='Xe om'):
    print(name,job)

def tonghieu(a,b):
    tong=a+b
    hieu=a-b
    return tong,hieu
#code de chay chuong trinh
if __name__ == '__main__':
    #code
    x,y= map(int, input().split())
    print(tong(x,y))
    a=100
    change(a) #chinh thuc
    print(a) #a khong thay doi gia tri
    xinchao('X','Y','Z') #posittional argument
    xinchao(name3='Teo', name2='Ty', name1='Nam')
    infor('28tech','Developer') #in ra 28tech Developer
    infor('Teo') #Default argument in ra teo Xe om
    t,h=tonghieu(10,20)
    print(t,h)
    print(tonghieu(10,20))
"""

"""
#----------------------------------------------------------------------

a=[1,2,3,4,5]
b=[1,2.3,'An','Chi']
s='NguyenAn'
a=list(s) #in ra N g u...
b=list(range(20))
print(a)
print(b)
print(len(a)) #do dai mang
print(a[5])
for i in range(0,len(a)):
    print(a[i],end=' ')
a.append(10) #them phan tu vao cuoi
a.insert(2,10) #them phan tu vao vi tri bat ki
a.pop(2) #xoa phan tu vi tri so 2
a.pop() #xoa phan tu o cuoi
a.remove(10) #xoa gia tri dau tien neu k co thang nao se bao loi
a.clear() #xoa moi phan tu
a+=b #noi 2 mang
a.count(10) #dem so lan xuat hien
a.index(10) #tra ve chi so
a.reverse() #lat nguoc
a.sort() #O(Nlog(N))
print(max(a))
print(min(a))
print(sum(a))
b=sorted(a)#sap xep sang mang b moi
if 10 in a: #tim kiem 10 trong a O(N) 
a=[1,2,3]
b=a*2 #b= 123123
for x in a:
    print(x)
### change
a=[1,2,3,4]
b=a #a=b va id giong nhau thay doi a cung thay doi b
b=a.copy() #a va b khac nhau
b=a[:] #giong ham copy
### cat mang
#a[start,stop,step]
a=[10,20,30,40,50,60]
b=a[2 : 5 : 1] #30 40 50
b=a[ : 5] # tu 0 den 4
b=a[1 :] # tu 1 den cuoi
b=a[::-1] #lat nguoc mang a
a[2:5]=[1,2,3] #thay chi so 2 den 5 thanh 1 2 3
a[2:5]=[] #xoa
a[: 0]= [1,2,3] #chen vao dau
a[len(a) :]#chen vao cuoi

### lambda thay mang
func=lambda x,y,z : x+y+z
print(func(100,200,300))
print((lambda x,y,z : x+y+z)(100,200,300))
#thay doi ham
a=[1,2,3,4,5]
b=list(map(lambda x : x**2,a))
print(b) #1,4,9,16,25
#loc filter
a=[1,2,-3,-4,5]
b=list(filter(lambda x: x>0,a))
print(b) #1,2,5
b=list(filter(lambda x: x%2==0,a)) #tra ve true
# thay doi gia tri trong mang
def sum_digit(n):
    tong=0
    while n!=0:
        tong+=n%10
        n//=10
    return tong
a=[1,2,3,4,5]
b=[]
b=[x+3 for x in a]
print(b) #4 5 6 7 8


b=[sum_digit(x) for x in a]
print b

# loc cac gia tri trong list
def nt(n):
    for i in range(2, sqrt(n)+1):
        if n%i==0: return False
    return n>1

a=[1,-233,30,-4,99,-192,-13,123]
b=[x for x in a if x>=0]
print(b)

b=[x for x in a if(nt(x))]

# nhap mang

n=int(input())
a=list(map(int,input().split()))
"""
# map(gia tri, gia tri ap dung ham vi du mang a)
#lambda x: x+2 thay doi x
#-------------------------------------------------------------------
#cnt=[0] *100000001#mang danh dau
#chi khi gan bien hay mang moi dung global
#vi du mang a= mang b, bien a= bien b


#print(f" * {p}^{cnt}", end="")

###################################################
#sort
"""
a= [-3,2,-1,-4,5,-6,8]
a.sort() #co tinh chat stable
a.sort(reverse=True) # lat nguoc
a.sort(key = abs, reverse=True) #key co the truyen ham vao
a.sort(key= lambda x:abs(x))
b = [[1,2], [3,2], [5,2], [4,1], [3,6]]
b.sort(key= lambda x:x[0])
b.sort(key= lambda x:(x[0],x[1])) # sort neu x[0]=nhau thi xet toi x[1]
print(b)
"""


#cmp_to_key
"""
from functools import cmp_to_key
#-1 1 0  
#neu a va b da dung thu tu ma ban muon thi tra ve -1, nguoc lai tra ve 1
def cmp(a,b):
    if a<b: #giam dan dung
        return -1
    return 1
    #return a-b tang dan

a=[10,2,3,1,4,5,6,3,0]
a.sort(key= cmp_to_key(cmp))
print(a)
#sort O(NlogN)
 """

#--------------------------------------------------------------
#set k sx tang dan
"""
a=[1,2,3,5,4,3,1]
b= set(a)
print (b)
s={1,2,3,4}
s.add(5)
s.add(1)
s.update([2,6,7,1,2,3])
print(s)
s.remove(2) # xoa 1 phan tu
s.discard(1) #xoa 1 phan tu
#s.clear()
for x in s:
    print(x)
if 4 in s: print('Found')
t={4,3,2,5,7,6}
u=s.union(t) #v=s|t hop 2 tap set
u=s&t #giao
u= s-t #lay s khong lay t
u=s^t #khong lay giao s va t
print(s.isdisjoint(t)) # xem co phan tu chung khong
print(t.issubset(s)) #xem t phai la con cua s khong
print(s.issubset(t)) # kiem tra s phai la cha cua t khong
"""
#------------------------------------------------------
#dictionary dem tan suat k sx tang dan
"""
b=dict(a)
infor = {'An':'Deptrai','Chi':'Thui','yeu':'Nhau'}
print(infor.get('Chi))
print(infor.keys())
print(infor.values())
print(infor.items())
for key in infor.keys():
    print(key,infor[key])
for key,value in infor.items():
    print(key,value)
for x in infor:
    print(x,infor[x])
infor['An'] = 'Deptraivcl'# thay doi value
infor.pop('yeu') #phai co cai key r xoa
a=[1,2,4,3,1,2,3,1,5]
d={}
for x in a:
    if(x in d):
        d[x]+=1
    else:
        d[x]=1
for key, value in d.items():
    print(key,value)
f=list(d.items()) #in ra tu be den lon
f.sort(key=lambda x: x[0])
for x,y in f:
    print(x,y)
d1={}
for x in a: #c1
    d1[x]=x**2
d2={x:x**2 for x in a} #c2
"""

#counter collection
"""
from collections import Counter #xuat hien theo thu tu xuat hien
a=[1,2,1,3,1,4,1,0,2,5]
b= list(Counter(a).items())
print(b)
 #set va dict deu lưu dạng tuple
 #----------------------------------------------------------
 #khai bao mang 2 chieu
n,m=map(int,input().split())
a=[[0 for _ in range(n)] for _ in range(m)]
for i in range(n):
    a[i]=list(map(int,input().split()))
    """
#--------------------------------------------------------------------------------
#xau ky tu
"""
s='NguyenAn'
t="""
"""
s=str(100) #type string
t=s[::-1]
print(t) #lat nguoc
s='NguyenAn'
x,y,*z=s
print(x,y,z)#N g [u,y,e,n,A,n]
#khai bao xau s khong the thay doi dc ptu nhu mang
s='Nguyen'
t='An'
st=s+' '+t #Nguyen An
s="Nguyen An Dep Trai vcl"
t=s.replace("vcl","vl") # Nguyen An dep trai vl thay the tat ca tu vcl
s='Nguyen,An,dep,trai'
t=s.split(',') #['Nguyen', 'An', 'dep','trai]
s='Nguyen,,,,An,,,oi,,vl'
s=s.replace(',',' ')
t=s.split() #[Nguyen, An...]
a=['Nguyen', 'An', 'Oi']
print(' '.join(a)) #Nguyen An Oi
s.upper() #chuyen sang in hoa
s.lower() #chuyen sang in thuong
s.capitalize() #chuyen chu hoa chu cai dau
s.swapcase() #chuyen hoa thanh thuong va nguoc lai
s.title() #viet hoa chu cai dau cua tung tu, cac ki tu con lai viet thuong
if "An" in s:
    print('Found')
print(s.find("An")) # tra ve chi so nho nhat xau con tra ve -1 neu khong tim thay
print(ord('A'))
print(chr(65))
"""
#OOP----------------------------------------------------------------------------------------
"""
class Person:
    nationlity='Viet Nam' #thuoc tinh chung
    def __init__(self, name, job):
        self.name=name #public
        self.__job=job #private
    def greet(self):
        print('Xin chao')
    def infor(self):
        print(self.name)
    def get_job(self):
        return self.__job
    def set_name(self,name):
        self.name=name
if __name__ == '__main__':
    p1=Person('Teo','Dev')
    p2=Person('Ty', 'Engineer')
    print(p1.nationlity, p1.name,p1.get_job())
    print(p2.nationlity,p2.name,p2.get_job())
    p1.greet()
    p2.greet()
    p1.infor()
    p2.infor()
    """


"""
from collections import Counter

a=[1,2,1,3,1,4,1,0,2,5]
b= list(Counter(a).items())

b.sort(key=lambda x:(x[1],x[0]))
for x in b:
    print(x[0])
"""

#date-----------------------
"""from datetime import date

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

d = date(y2, m2, d2) - date(y1, m1, d1)
print(abs(d.days))
    
"""


#strip()--------------------
"""
"  hello \n".strip()        # -> "hello"
"\tA B C\t".strip()         # -> "A B C"
"--abc--".strip("-")        # -> "abc"
"00123".strip("0")          # -> "123"
"abXYba".strip("ab")        #xoa ky tu a hoac b
str(s).lstrip() # bỏ bên trái
str(s).rstrip() # bỏ bên phải.
str(s).endswith(("a","b","c")) #ket thuc boi nhung ky tu nay
u, v = map(int, s.split('>'))
"""

import csv


s = "h3ll0_w0rld!"
pairs = [("3", "e"), ("0", "o"), ("_", " ")]
for old, new in pairs:
    s = s.replace(old, new)
print(s)  # "hello world!"


a = bytearray(10**9)


#mang 2 chieu [[],[]]=======================================================================================
n,m=map(int,input().split())
a=[]
for _ in range(n):
    s=list(input())
    a.append(s)
print(a)



n,m=map(int,input().split())
a=[ [0 for _ in range(m)] for _ in range(n)] #n hang m cot
for i in range(n):
    s=input()
    for j in range(m):
        a[i][j]=s[j]
print(a)

#file csv=======================================================================================================
"""
name,score,ethnicity,region
Nguyen Hong Ngat,26,Kinh,1
Chu Thi Minh,14,Dao,3

f = open("ten_file.txt", "r")   # mở file
data = f.read()                # đọc nội dung
f.close()                      # đóng file

a=[]
with open("thisinh.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)  
    for i, row in enumerate(reader, start=1):
        name = row["name"].strip()
        score = float(row["score"])
        ethnicity = row["ethnicity"].strip()
        region = int(row["region"])

        ts = ThiSinh(i, name, score, ethnicity, region)
        a.append(ts)

"""
#file json==============================================================================================
"""
import json
with open("tet.json","r") as f:
    r=json.load(f)
    for row in r["tet"]:
        print(row["name"])
"""


#self.id=f"TS{id:02d}"   {self.tong:.1f}



#decimal============================================================================================================
#return rs.quantize(Decimal('0.1'), ROUND_HALF_UP) ,  rs=Decimal(0)
#from decimal import ROUND_HALF_UP, Decimal
"""
from datetime import datetime, time, timedelta
from datetime import datetime

# Tạo hai đối tượng datetime
dt1 = datetime(2025, 11, 22, 12, 30, 45)
dt2 = datetime(2025, 11, 25, 14, 45, 30)
# Tính sự chênh lệch giữa hai datetime
delta = dt2 - dt1

# Tạo 2 đối tượng time
time1 = time(10, 30)  # 10:30 AM
time2 = time(12, 30)  # 12:30 PM
# Chuyển đối tượng time thành datetime (với một ngày cụ thể)
datetime1 = datetime.combine(datetime.today(), time1)
datetime2 = datetime.combine(datetime.today(), time2)
# Tính sự chênh lệch giữa hai thời gian
delta = datetime2 - datetime1
from datetime import date

# Tạo hai đối tượng ngày (date)
date1 = date(2025, 11, 22)
date2 = date(2025, 11, 25)
# Tính sự chênh lệch giữa hai ngày
delta = date2 - date1

"""


# đọc nhiều dòng ===============================================================================================
import sys
s = sys.stdin.read()
#re===============================================================================================================
"""
import re
if not re.search(r"[A-Za-z0-9]", part):

parts = re.split(r"[.?!]+", s)// re.sub(r"[])
s = "Hello!!! How are you? I am fine... Thanks!"
["Hello", " How are you", " I am fine", " Thanks", ""]

"""

"""
Kiểu dữ liệu của s	Ví dụ	Độ phức tạp của if w in s
string (chuỗi)	"hello world"	O(n × m)
list (danh sách)	["apple", "banana"]	O(n)
set	{"apple", "banana"}	O(1) trung bình
dict (kiểm tra key)	{'apple': 3}	O(1) trung bình
"""
#if isinstance(v, int):
"""
import ast
line = input().strip()
d = ast.literal_eval(line)
{"a": 2, "b": 3, "c": "hello", "d": 4}
Chuyển str dạng như trên về dict
"""
#if capital[0].lower() in 'aeiou': 


"""
x = 10
a = [1, 2, 3]

def f():
    global x   # đổi được x
    x = 20

    a[0] = 99  # đổi được list
    # a = [7,8,9]  # KHÔNG đổi được list ngoài, vì đây là list local

f()
print(x)   # 20
print(a)   # [99, 2, 3]
"""

"""
csv, json 
import sys

"""
