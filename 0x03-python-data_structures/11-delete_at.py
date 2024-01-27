def delete_at(my_list=[], idx=0):
        if not my_list or idx < 0 or idx >= len(my_list):
                    return my_list
                updated_list = [elem for i, elem in (my_list) if i != idx]
                    return updated_list

