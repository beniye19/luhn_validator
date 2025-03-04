def luhn_algorithm(number):
    digits = [int(d) for d in str(number)][::-1]
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return sum(digits) % 10 == 0
