nh=open("demo.txt","r")
try:
	nh.write("sjfkjllkj")
except Exception, e:
	print 'An error occurred'
nh.close()