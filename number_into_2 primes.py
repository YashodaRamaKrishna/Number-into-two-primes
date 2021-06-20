# Video for the logic : https://youtu.be/QydSu2w_nT8

## Take the number
number = 100

## creating function with parameter 'number'
def fun(number):
    ## Check if the number is odd
    if number % 2 != 0:
        ## Check if (number-2) a prime or not
        for i in range(3, number - 2):
            if (number - 2) % i == 0:
                return f"No two primes can be split to make {number}"
        else:
            return f"{number-2} + 2 = {number}"

    ## Check if the number is even
    else:
        primes = []
        ## Find all the primes from 3 to (number/2) and store them in primes list. [Primes from group 1]
        for i in range(3, ((number // 2) + 1)):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        ## Complements are the numbers from Group2.
        # These are obtained by subtracting each prime(prime list) from the even number.
        ## Check if the complement is prime. If it is, store in com list.
        ## Here we are directly checking if the complement
        # is prime rather than storing all the complements in a seperate list.
        com = []
        for i in primes:
            for j in range(3, number - i):
                if (number - i) % j == 0:
                    break
            else:
                com.append(i)
        ## Here these conditional statements are to return the list of numbers.
        if len(com) >= 1:
            return [f"{number-i} + {i} = {number}" for i in com]
        else:
            return f"No two primes can be split to make {number}"


print(fun(number))
