#first = input("first: ")

#second = input("second: ")
#sum = float(first) + float(second)
#print("sum: " + str(sum))


#course = 'python for beginners'
#print(course.replace('for', '4'))
#print('python' in course)

#x = 10 
#x# = x+3
#x+=3

#x = (10 + 3) * 2
#print(x)

# X = ("wife")
# Y= ("me")
# print("wife")
# print("me")

# x= "python is awesome"
# print(x)

# x = "Python"
# Y = "is"
# Z = " awesome"

# print(x,Y,Z)

# x = 55
# y= 85
# print(x + y)

# x = 5
# y = "johns"
# print(x,y)

# X = " Awesome"

# def myfunc():
#     print("python is " + X)

# myfunc()

#x  = "awesome"

# def myfunc():
#     x = "fantastic"
#     print("python is + x")
# myfunc()

# print("python is" + x)

# def myfunc():
#     global x
#     x = "fantastic"

# myfunc()

# print("python is " + x)

# x = 1 
# y= 19981306
# z= 59897465

# print(type(x))
# print(type(y))
# print(type(z))

# x = float (1.10)
# y= float(1.0)
# z= float (-35.29)

# print(type(x))
# print(type(y))
# print(type(z))

# x = int(1)
# y = int(2.8)
# z = int("3")

# print(x)
# print(y)
# print(z)

# x = 5 
# if x < 10:
#     print ('smaller')
# if x > 20: 
#     print ('bigger')

# print('false')

# n = 5 
# while n > 0:
#     print(n)
#     n = n - 1
# print('blastoff!')

#x= 1000

#if x < 2:
    #print('small')
#elif x < 10:
    #print('medium')
#else : 
    #print('large')
#print('all done')

#x = 60
#if x < 2 :
    #print('below 2')
#elif x < 20:
    #print('below 20')
#elif x < 10 :
    #print('below 10')
#else :
    #print('something else')

# temp = "5 degrees"
# cel = 0
# try:
#     fahr = float(temp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
# except:
#     print(cel)

# x = 25836
# if x < 500 :
#     print('below 500')
# elif x < 900 :
#     print('below 900')
# elif x < 2600 :
#     print('below 2600')
# else:
#     print('something else!')

# this piece of code isn't executing the code put its only remember.
# def print_lyrics():
#     print("i'm a lumberjack, and i', okay")
#     print('I cant feel my face when im with you!!')


# x = 5
# print('hello')
# #def is to restore a function
# #invoke/call is to reuse
# def print_lyrics():
#     print("i'm a lumber jack, and i'm okay.")
#     print('I sleep all night and a I work all day.')
# #these print statements never ran. why? because we defined but did not invoke/call them.
# print('Yo') 
# print_lyrics()
# x = x + 2
# print(x)

# def greet (lang):
#     if lang == 'es':
#         print('hola')
#     elif lang == 'fr':
#         print('bonjour')
#     else:
#         print('Hello')

# def greet(lang):
#     if lang == 'es':
#         return 'hola'
#     elif lang == 'fr':
#         return 'bonjour'
#     else:
#         return 'hello'

# print(greet('en'), 'Daniel')
# print(greet('es'),'skylar')
# print(greet('fr'),'both of us')

# n= 5 
# while n > 0:
#     print(n)
#     n=n - 1
# print ('blastoff!')
# print(n)

# while True:
#     line = input('hello')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')


# while True:
#     line = input('hello')
#     if line == '#':
#         continue
#     if line == 'done' :
#         break
#     print(line)
# print('Done! ')


# n = 0
# while True:
#     if n == 3:
#         break
#     print(n)
#     n = n + 1

# for i in [2,1,5]:
#     print(i)

# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break
#     print("loop:", itervar, smallest)
# print("smallest:", smallest)

# largest_so_far = -1 
# print('Before', largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num > largest_so_far :
#         largest_so_far = the_num
#     print(largest_so_far, the_num)
# print('after', largest_so_far)

# zork = 0
# print('before', zork)
# for thing in (9, 41, 12, 3, 74, 15):
#     zork = zork + thing
#     #if i add one to zork it will count the amount of times it will run.
#     #if i add thing to zork it will add the total of the numbers.
#     print(zork, thing)
# print('after', zork)

# count= 0 
# sum= 0 
# print('before', count, sum)
# for value in [9, 41, 12, 3, 74, 15]:
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# print('after', count, sum, sum / count)

# print('before')
# for value in [9, 41, 12, 3, 74, 15]:
#     if value > 20:
#         print('Large number', value)
# print('after')

# found = False
# print('before', found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3 :
#         found = True
#     print(found, value)
# print('after', found)

# smallest_so_far = -1
# print('before', smallest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num < smallest_so_far :
#         smallest_so_far = the_num
#     print(smallest_so_far, the_num)
# print('after', smallest_so_far)

# smallest = None
# print('before')
# for value in [9, 41, 12, 3, 74, 15]:
#     if smallest is None:
#         smallest = value 
#     elif value < smallest :
#         smallest = value
#     print(smallest, value)
# print('after', smallest)

# str1= "hello"
# str2= 'there'
# bob = str1 + str2
# print(bob)

# fruit = 'banana'
# letter = fruit[1]
# print(letter)


# fruit= 'banana'
# for letter in fruit :
#     print(letter)

# s = 'monty python'
# print(s[:2])
# print(s[0:4])
# print(s[8:])
# print(s[:])

# xfile= open('notes.py')
# for cheese in xfile: 
#     print(cheese)

# fhand = open('notes.py')
# count=0
# for line in fhand:
#     count = count + 1
# print('line count:', count)

# fhand = open('notes.py')
# for line in fhand:
#     if line.startswitch('from'):
#         print(line)

# friends= ('joseph', 'glenn', 'sally')
# for friend in friends :
#     print('Happy New Year:', friend)
# print('Done!')
# for i in range(len(friends)):
#     friend = friends[i]
#     print('Happy New Year:', friend)

# stuff = list()
# stuff.append('book')
# stuff.append(99)
# print(stuff)

# abc = 'with three words'
# stuff= abc.split()
# print(stuff)
# print(len(stuff))
# print(stuff[0])

# counts =dict()
# name = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in name :
#     if name not in counts:
#         counts[name] = 1
#     else :
#         counts[name] = counts[name] + 1
# print(counts)

# counts = dict()
# print('eneter a line of text:')
# line = input("")

# words= line.split()

# print('counting...')
# for word in words:
#     counts[word] = counts.get(word,0) + 1
# print('counts', counts)

# x,y = (4, 'fred')
# print(y)

# a,b = (99, 98)
# print(a)

# d = ('a':10, 'b':1, 'c':22)
# d.item()
# sorted(d.items())

# d = {'a':10, 'b':1, 'c':22}
# t = sorted(d.items())
# for k, v in sorted(d.items()):
#     print(k,v)

# c = {'a':10, 'b':1, 'c':22}
# tmp= list()
# for k, v in c.items():
#     tmp.append((k,v))
# # print(tmp)
# tmp = sorted(tmp,reverse=True)
# print(tmp)