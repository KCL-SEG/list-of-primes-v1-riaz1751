"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    count = 0
    subject = 2

    while count < number_of_primes:
        flag = False
        for i in range(2, subject):
            if (subject % i) == 0:
                subject += 1
                flag = True
                break

        if flag == False:
            list.append(subject)
            subject += 1
            count += 1

    return list

x = primes(20)
print(x)
