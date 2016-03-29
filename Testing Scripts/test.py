import os,sched,time

s = sched.scheduler(time.time, time.sleep)
f = open('out.txt','w',0)

#successful read/write simultaneoulsy if including 0 param above

#march-6: write to ieng6 and read; run temper-poll command with pi

def do_something(sc):
	i = 0
	while i < 10 :
		f.write(str(i)) 
		i = i + 1
	sc.enter(5,1,do_something, (sc,))
s.enter(5, 1, do_something, (s,))
s.run()
