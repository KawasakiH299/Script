ss="c22a563acc2a587afbfaaaa6d67bc6e628872b00bd7e998873881f7c6fdc62fc"
u=8617090000000
def x(v, x0,x1):
    xx=[]
    import hashlib
    for j in range(x0,x1):
        d=v+j
        a=hashlib.sha256(str(d).encode()).hexdigest()
        xx.append(str(d)+':::'+a + '\n')
    b=str(x1) + '.txt'
    f=open(b,'wt')
    f.writelines(xx)
    f.close()


from queue import Queue
q_X0=Queue()
q_X1=Queue()
for i in range(10) :
    q_X0.put(i*1000000)
    q_X1.put(i*1000000+999999)

print(q_X0.get(1))
import threading
# for i in range(q_X0.qsize()):
#    t=threading.Thread(target=x(u,q_X0.get(i),q_X1.get(i)))
#    t.start()