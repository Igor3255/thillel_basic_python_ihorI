import time

def infinite_loop():
    while True:
        print(time.ctime())
        time.sleep(1)

# запускаем бесконечный цикл
infinite_loop()
