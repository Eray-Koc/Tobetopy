#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

i = 0
fibonacci = [1 , 1]
while (len(fibonacci) != 20):
    value = fibonacci[i] + fibonacci[i + 1]
    fibonacci.append(value)
    i += 1
for items in fibonacci:
    print(items)


#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
def greatnum(number):
    x = 0
    i = 1
    while(i < number):
        if (number % i == 0):
            x += i
        i += 1
    if (number == x):
        return True
    else:
        return False
  
        
#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

def lcm(number, number2): #EKOK
    number_array = [1,2,3,4,5,6,7]
    x = 1
    i = 2
    while number > 1 or number2 > 1:
        while isprime(i) and (number % i == 0 or number2 % i == 0):
            if number % i == 0 and number2 % i == 0:
                number = number // i
                number2 = number2 // i
            elif number % i == 0:
                number = number // i
            elif number2 % i == 0:
                number2 = number2 // i
            number_array.append(i)
        i += 1
    for i in number_array:
        x *= i
    return x

def gcd(number, number2): #EBOB
    number_array = []
    x = 1
    i = 2
    while number > 1 or number2 > 1:
        while isprime(i) and (number % i == 0 or number2 % i == 0):
            if number % i == 0 and number2 % i == 0:
                number_array.append(i)
                number = number // i
                number2 = number2 // i
            elif number % i == 0:
                number = number // i
            elif number2 % i == 0:
                number2 = number2 // i
        i += 1
    for i in number_array:
        x *= i
    return x





#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.


def isprime(number):
    i = 2
    if number == 2:
        return True
    while i < number:
        if (number % i == 0):
            return False
        i+=1
    return True


#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız.

def prime_list(number):
    number_array = []
    i = 2
    while number >= 2:
        while isprime(i) and number % i == 0:
            number_array.append(i)
            number = number / i
        i+=1
    return number_array

