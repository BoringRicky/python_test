import asyncio

# @asyncio.coroutine
# def hello(p):
#     print("Hello World : " ,p)
#     yield from asyncio.sleep(1)
#     print('Hello again : ',p)

# tasks = [hello(1111),hello(2222)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

hosts = ['www.sina.com.cn','www.sohu.com','www.163.com']

# @asyncio.coroutine
# def wget(host):
#     print('wget %s ... ' % host)
#     connect = asyncio.open_connection(host,80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host,line.decode('utf-8').rstrip()))

#     writer.close()


async def wget(host):
    print('wget %s ... ' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header -> %s ' % (host,line.decode('utf-8').rstrip()))

    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in hosts]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
