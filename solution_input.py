first_name = raw_input('Enter your first name: ')
surname = raw_input('Enter your surname: ')
university = raw_input('Enter the university you attended: ')
age = int(raw_input('Enter your age: '))
max_heart_rate = 220 - age

print 'My name is %s %s' % (first_name, surname)
print 'I attended %s' % university
print "I'm currently %d years old" % age
print 'My theoretical maximum heart rate is %d' % max_heart_rate
