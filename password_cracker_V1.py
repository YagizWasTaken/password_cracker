import random


uppercase_letters="QWERTYUIOPASDFGHJKLZXCVBNM"
numbers="1234567890"
lowercase_letters="qwertyuıoplkjhgfdsazxcvbnm"
consonant_letters="qwrtypsdfghjklzxcvbnm"
vowel_letters="euioa"
tries=0

while True:
    tries +=1
    password=random.choice(uppercase_letters)+random.choice(vowel_letters)+random.choice(consonant_letters)+random.choice(vowel_letters)+random.choice(consonant_letters)+str(random.choice(numbers))+str(random.choice(numbers))+str(random.choice(numbers))+str(random.choice(numbers))
    print(password+"             "+str(tries))
    if tries == 100000000:
        exit()

