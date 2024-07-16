from hashlib import sha1
from multiprocessing import Process, Queue
import os 

def rainbow(name, start, end):
	f = open("hash/hash" + str(name) + ".txt", "w")
	for i in range(start, end):
		hash = str(i) + "salt_for_you"
		for j in range(500):
			hash = sha1(hash.encode('utf-8')).hexdigest()
		f.write(str(i) + ":" + hash + "\n")
	f.close()

def process():
	pr1 = Process(target = rainbow, args = (1, 10000000, 20000000))
	pr2 = Process(target = rainbow, args = (2, 20000000, 30000000))
	pr3 = Process(target = rainbow, args = (3, 30000000, 40000000))
	pr4 = Process(target = rainbow, args = (4, 40000000, 50000000))
	pr5 = Process(target = rainbow, args = (5, 50000000, 60000000))
	pr6 = Process(target = rainbow, args = (6, 60000000, 70000000))
	pr7 = Process(target = rainbow, args = (7, 70000000, 80000000))
	pr8 = Process(target = rainbow, args = (8, 80000000, 90000000))
	pr9 = Process(target = rainbow, args = (9, 90000000, 100000000))
	
	pr1.start()
	pr2.start()
	pr3.start()
	pr4.start()
	pr5.start()
	pr6.start()
	pr7.start()
	pr8.start()
	pr9.start()

	pr1.join()
	pr2.join()
	pr3.join()
	pr4.join()
	pr5.join()
	pr6.join()
	pr7.join()
	pr8.join()
	pr9.join()
 
 
if __name__ == "__main__":
    process()
