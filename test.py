# import os,sched,time
# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):
# 	os.system('ls -l >> out.txt')
# 	print (type(sc))
# 	sc.enter(5,1,do_something, (sc,))
# s.enter(5, 1, do_something, (s,))
# s.run()

import twisted

timeout = 5.0

def doWork():
	print "hi"
	pass
l = task.LoopingCall(doWork)
l.start(timeout)
reactor.run()