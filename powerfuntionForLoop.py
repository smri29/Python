def raise_to_power (base_num, pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return result
solution=raise_to_power(3,7)
print(solution)
