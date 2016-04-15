def fb(a):
    for n,i in enumerate(a):
      if i % 15 == 0: a[n] = "Fizz Buzz"
      elif i % 5 == 0: a[n] = "Buzz"
      elif i % 3 == 0: a[n] = "Fizz"
    return a

fizzbuzz = fb([x for x in range(1,101)])
print fizzbuzz
