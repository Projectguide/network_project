arr = [0,1,2,2,2,3,4]
newl = [4,5]
new1 = [x for y in arr for x in new1 if y not in x]
print(new1)
#tags = [u'man', u'you', u'are', u'awesome']
#>>> entries = [[u'man', u'thats'],[ u'right',u'awesome']]
#>>> [entry for tag in tags for entry in entries if tag in entry]