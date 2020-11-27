# import logging
# from time import sleep, ctime
#
#
# """单线程启动"""
# #调用日志
# logging.basicConfig(level=logging.INFO)
#
# #设置2个线程
# def loop0():
#     logging.info("start loop0 at " + ctime())
#     sleep(4)
#     logging.info("end loop0 at " + ctime())
#
# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(6)
#     logging.info("end loop1 at " + ctime())
#
# def main():
#     logging.info("start all at " + ctime())
#     loop0()
#     loop1()
#     #顺序执行loop0,loop1
#     sleep(6)
#     logging.info("end all at " + ctime())
#
# if __name__ == '__main__':
#     main()
#
# """多线程启动，_thread是将线程同时启动"""
# import logging
# from time import sleep, ctime
# import _thread
#
#
# logging.basicConfig(level = logging.INFO)
#
# def loop0():
#     logging.info("start loop0 at " + ctime())
#     sleep(4)
#     logging.info("end loop0 at " + ctime())
#
# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(6)
#     logging.info("end loop1 at " + ctime())
#
# def main():
#     logging.info("start all at " + ctime())
#     _thread.start_new_thread(loop0, ())
#     _thread.start_new_thread(loop1, ())
#     #主main要sleep，不然main主线程运行结束时，会把子进程loop0,loop1关闭
#     sleep(6)
#     logging.info("end all at " + ctime())
#
# if __name__ == '__main__':
#     main()
#
# """多线程启动，threading是基于_thread的功能"""
# import logging
# import threading
# from time import ctime, sleep
#
# logging.basicConfig(level=logging.INFO)
#
# loops = [2, 4]
#
#
# def loop(nloop, nsec):
#     logging.info("start loop " + str(nloop) + " at " + ctime())
#     sleep(nsec)
#     logging.info("end loop " + str(nloop) + " at " + ctime())
#
#
# def main():
#     logging.info("start all at " + ctime())
#     threads = []
#     nloops = range(len(loops))
#     for i in nloops:
#         # 调用loop函数，args参数传给loop
#         t = threading.Thread(target=loop, args=(i, loops[i]))
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         threads[i].join()
#     logging.info("end all at " + ctime())
#
#
# if __name__ == '__main__':
#     main()


"""自定义多线程启动，把threading继承成mythread"""
import logging
import threading
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)

loops = [2, 4]

#新建MyThread类，继承threading.Thread
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at " + ctime())

def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop, (i,loops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())

if __name__ ==  '__main__':
    main()

