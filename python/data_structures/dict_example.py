#!usr/bin/env python
mob ={'apple':'mac','lenovo':'android','microsoft':'windows'}
print 'apple specific is ' + mob['apple']
del mob['microsoft']
print '\n there are {} mobile phone \n'.format(len(mob))
for name,address in mob.items():
    print 'software {} at {} '. format(name,address)
    mob['vivo'] = 'nokia'
    if 'vivo' in mob:
        print('\nvivo address is '+ mob['vivo'] )

