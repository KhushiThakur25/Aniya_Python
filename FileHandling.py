file = open('data.txt','r')
# data = file.read()
data = file.readline()
print(data)
file.close()

file = open('data1.txt','w')
file.write('Hello python..')
file.close()

file = open('data1.txt','a')
file.write("i'm file handler..")
file.close()

file = open('data1.txt','x')
file.write("hello user")
file.close()