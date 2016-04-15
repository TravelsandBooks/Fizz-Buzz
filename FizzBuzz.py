def fb(a):
    for n,i in enumerate(a):
      if i % 15 == 0: a[n] = "Fizz Buzz"                #this is just neater -- lowest common denominator
      elif i % 5 == 0: a[n] = "Buzz"
      elif i % 3 == 0: a[n] = "Fizz"
    return a
def print_fb(b):
    for i,n in enumerate(b):
        if (i + 1) % 10 == 0: print str(n) + " \n"      #if it's an index divisible by 10, break the line
        else: print str(n) + " ",                       #otherwise just print the value with a space
fizzbuzz = fb([x for x in range(1,101)])                #we're doing it for all numbers from 1 to 100
print_fb(fizzbuzz)
