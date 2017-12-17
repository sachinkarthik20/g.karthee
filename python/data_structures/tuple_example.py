
#!usr/bin/env python
crick = ('bat','stumps','ball','ball')
print 'number of items in the showroom is ' + str(len(crick))
new_ground = ('pitch','ground',crick)
print 'number of items in new showroom is ' + str(len(new_ground))
print 'all items in new ground are' + str(new_ground)
print 'last item purchase from warehouse is' + str(new_ground[2])
print 'last item from old zoo is' + str(new_ground[2][2])
print 'number of materials in the store room is ' + str(len(new_ground)-1+len(new_ground[2]))
count=new_ground.count('ball')
print 'the count of ball is: ',count

