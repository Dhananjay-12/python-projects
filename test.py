# def callme(first_name # this is string 1
#            ,last_name # this is string 2
#            ) :
#     print(f"Hey {first_name} {last_name}, you called me")
    

# callme("David","Singh")    
# print('''this 
#       is a multiline string 
#       ''')

# a = (1,2,3)
# print(type(a))

# min_length = 2

# while True:
#     user_name = input('Please enter your name : ')
#     if  len(user_name) > min_length \
#             and \
#                 user_name.isprintable() \
#                         and user_name.isalpha():
#         break
# print("Hello {0}".format(user_name))    

# a= [1,2,3]
# b= [5,6,7]

# my_tuple = (a,b)
# print(my_tuple)

# a.append(4)
# b.append(8)

# print(my_tuple)
    
    
# a = 500
# b = 100 -500

# print(id(a))
# print(id(b))
# def encode(digit,digit_map):
#     if(max(digit) >= len(digit_map)):
#         return ValueError('digit_map is not long enough to encode the digits')
#     # encoding= ''
#     # for d in digit :
#     #     encoding += digit_map[d]
#     # return encoding 
#     return ''.join([digit_map[d] for d in digit])
# print(encode([15,15],'0123456789ABCDEF'))   

# from fractions import Fraction
 
# ans = Fraction(1,2) * Fraction(2,3)

# print(int(ans))

#FIZZBUZZ
# num = int(input('Enter the number: '))

# if(num % 3 == 0 and num % 5 == 0) :
#     print('FizzBuzz')
# elif num % 3 == 0 :
#     print('Fizz') 
# elif num % 5 == 0 :
#     print('Buzz')      


# from random import choice

# wordlist = [ 'ordinary','tire','nasty','panicky','view','noiseless', 
# 'bang', 
# 'calm', 
# 'pack', 
# 'lettuce', 
# 'piquant', 
# 'wobble']

# def check_user_guess(random_word : str, user_guess_letter: str) :
#      if random_word.__contains__(user_guess_letter):
#          return True
#      else : 
#          return False

# random_word = choice(wordlist)
# print(random_word)

# user_guess_letter  = input('Give a random alphabet here : ').lower()

# result = check_user_guess(random_word,user_guess_letter)

# if result :
#     print('Hooray! You guessed the correct letter')
# else: 
#     print('Nope! try again')    


