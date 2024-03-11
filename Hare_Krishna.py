
import os 

# Directory 
a = "Hare krishna 💗 "
b = 0
location = "/home/ankit/Desktop/"

for x in range(100):
    b+=1
    c = a + str(b)
    print(c)
    path = os.path.join(location, c)
    os.rmdir(path)


