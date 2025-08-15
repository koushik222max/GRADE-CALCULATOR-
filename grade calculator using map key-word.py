a=list(map(int,input('Enter the marks seprated by comma:').split(',')))
b=len(a)
total=sum(a)

avg=total/b


print('\nYour total is:',total)
print('\nYour average is:',avg)

if avg==100:
    print('\nYou got \'o\' grade')

elif avg>=85:
    print('\nYou got \'A+\' grade')

elif avg>=75:
    print('\nYou got \'A\' grade')

elif avg>=60:
    print('\nYou got \'B+\' grade')

elif avg>=45:
    print('\nYou got \'B\' grade')

elif avg<45:
    print('\nYou got \'c\' grade')
