import time
yesterday = time.strftime('%Y-%m-%d',time.localtime(time.time()-86400))
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print yesterday
print today