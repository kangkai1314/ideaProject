#--*-- coding:utf-8 --*--
import redis
import datetime


r=redis.Redis(host='127.0.0.1',port=6379,db=0)
r.set('hello','kangkai')
print r.get('hello')
r.set('test1',[1,2,3,4,5])
print r.get('test1')
r.set('test2',{'name':(1,2,3)})
print r.get('test2')
if r.exists('test2'):
    print 'this is exists'

l,s=r.time()
print l,s
timeStamp = l
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print otherStyleTime
print type(l)
print type(s)

