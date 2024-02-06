#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for n in range(list_length):
            try:
                num1 = float(my_list_1[n]) if isinstance(my_list_1[n], (int, float)) else None
                num2 = float(my_list_2[n]) if isinstance(my_list_2[n], (int, float)) else None
                
                if num1 is None or num2 is None:
                    print("wrong type")
                    result.append(0)
                elif num2 == 0:
                    print("division by 0")
                    result.append(0)
                else:
                    result.append(num1 / num2)
            except IndexError:
                print("out of range")
                result.append(0)
    finally:
        return result
