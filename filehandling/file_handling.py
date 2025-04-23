#1.create-x
#2.read-w
#3.write-r
#4.append-a

# f=open('python/filehandling/sample1.txt','x')
# f.write("sample1 file")
#write
# f=open ('sample.txt','w')
# f.write('hello.\n')#\n new line creation

# f.write('welcome')
#f.write('sample)

#3append
# f=open ('sample.txt','a')
# f.write('\n new data')

#4read
f=open ('sample.txt','r')
print(f.read())
print(f.read(4))
print(f.read())#hell,0,welcome,newdata

f=open('sample.txt','r')
print(f.readline())
print(f.readline(4))
print(f.readline())#>>hello,>>...,>>welc,>>ome,>>---

f=open('sample.txt','r')
print(f.readline())#['hello/n'welcom<\n',newdata]

print(f.tell())#cursor position avidey annu kandpidikan use cheyyunu
f.seek(1)
print(f.read())#cursor position change cheyyan use cheyyunu






