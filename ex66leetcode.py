def plus_one(digits: list):
    last_index = len(digits) - 1
    current_index = last_index
    # situacao 1
    if digits[last_index] < 9:
        digits[last_index] += 1
        return
    if digits[last_index] == 9:
        while current_index > 0:
            if digits[last_index - 1] < 9:
                digits[last_index - 1] += 1
            else:
                pass
            
        

plus_one([9, 1])
