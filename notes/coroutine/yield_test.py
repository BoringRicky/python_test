def consumer():
    r=''
    while True:
        n = yield r
        if not n:
            return
        print('[消费者] Consumer %s ... ' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5 :
        n = n + 1
        print('[生产者] Producing %s ... ' % n)
        r = c.send(n)
        print('[生产者] Consumer return : %s ' % r)
    c.close()

c = consumer()
produce(c)