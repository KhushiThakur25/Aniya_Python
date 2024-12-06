file = open('panda.jpg','rb')
data = file.read()
print(data)
file.close()

file = open('panda1.jpg','wb')
file.write(data)
file.close()