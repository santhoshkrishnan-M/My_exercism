def classify(number):
   
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisors_sum = 0

    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    if divisors_sum == number:
        return "perfect"
    elif divisors_sum > number:
        return "abundant"
    else:
        return "deficient"