import os,sched,time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
	i = 0
	f = open('out.txt','w')
	while i < 10 :
		f.write(str(i)) 
		i = i + 1
	sc.enter(5,1,do_something, (sc,))
s.enter(5, 1, do_something, (s,))
s.run()


# timeout = 5.0

# def doWork():
# 	print "hi"
# 	pass
# l = task.LoopingCall(doWork)
# l.start(timeout)
# reactor.run()