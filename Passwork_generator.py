import string 
import random

#n = int(input('Enter the length of the password which you want to generate : \n'))

s1 = string.ascii_lowercase
#print(s1)

s2 = string.ascii_uppercase
#print(s2)

s3 = string.digits
#print(s3)

s4 = string.punctuation
#print(s4)

'''
l = list()
l.extend(s1)
l.extend(s2)
l.extend(s3)
l.extend(s4)

#print(l)

print('Your password of',n,'length is...')

#Method 1

random.shuffle(l)
print(''.join(l[0:n]))


#Method 2

print(''.join(random.sample(l,n)))
'''
#If we want the specific size of characters, digits, punctuations

lc = int(input('Enter number of lowercase characters do you want in your password : \n'))
uc = int(input('Enter number of uppercase characters do you want in your password : \n'))
n = int(input('Enter number of digits do you want in your password : \n'))
p = int(input('Enter number of special characters do you want in your password : \n'))


l1 = list(s1)
l2 = list(s2)
l3 = list(s3)
l4 = list(s4)


psw = list()
psw.extend(random.sample(l1,lc))
psw.extend(random.sample(l2,uc))
psw.extend(random.sample(l3,n))
psw.extend(random.sample(l4,p))


print('Your password of',lc+uc+n+p,'length is...')
print(''.join(psw))
