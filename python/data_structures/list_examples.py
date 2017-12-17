#!/usr/bin/env python
def list_print(list_var):
    str=''
    for item in list_var:
        str=str+item+' '
    return str
shoplist =['apple','orange','grapes','banana','onionn','orange']
print 'i have ' + str(len(shoplist)) +' to purchase'
print 'i also have  to buy tomm'
shoplist.append('tomato')
print 'my shop list is now -- ' + list_print(shoplist)
print 'i will arrange my list now' 
shoplist.sort()
print 'my sorted shoplist is -- ' + list_print(shoplist)
print ' the first item i ll buy is', str(shoplist[0])
old=shoplist[0]
del shoplist[0]
print 'new list is -- ' + list_print(shoplist)
shoplist.pop()
print ' new list is -- '+ list_print(shoplist)
shoplist.reverse()
print 'reverse list  -- ' + list_print(shoplist)
shoplist.append('beans')
print 'newly added -- ' + list_print(shoplist)
shoplist.remove('orange')
print 'list after removing -- '+list_print(shoplist)

shoplist.index('orange')
print 'orange place is ' +str(shoplist.index('orange'))
shoplist.insert(3,'berry')
print '7th place is -- ' +list_print(shoplist)
tmp=['rosee','lavender']
shoplist.extend(tmp)
print 'the extended shop list -- '+ list_print(shoplist)
shoplist=shoplist + tmp
print shoplist
shoplist.count('rosee')
print shoplist.count('rosee')
shoplist[3]='newfruit'
print shoplist




