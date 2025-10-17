def solution(phone_book):
    hash = {num: True for num in phone_book}
    
    for phone_num in phone_book:
        for i in range(1, len(phone_num)):
            prefix = phone_num[:i]
            if prefix in hash:
                return False
    return True
