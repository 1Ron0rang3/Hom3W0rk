import threading

counter = 0

def inc():
    global counter
    for i in range(100_000):
        counter+=1

def dec():
    global counter
    for i in range(100_000):
        counter-=1

t1 = threading.Thread(target=inc)
t2 = threading.Thread(target=dec)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)
