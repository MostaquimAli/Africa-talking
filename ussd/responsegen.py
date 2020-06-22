def generate_response(text):
    arr = None
    if text.strip():
        arr = text.strip().split('*')
        arr_length = len(arr)
    if not arr:
        response = "CON Welcome to GCWU Credit Union. What is your username?"
    elif arr_length == 1:
        response = "CON What is your password?"
    else:
        if(user_false(arr)):
            response = "END Invalid Username and password"
            return response
        if arr_length == 2:
            response = "CON Please select option? \n1. Borrow Money \n2. See Account Status"
        elif arr_length == 3:
            if arr[2] == '1':
                response = "END Borrow Money is in DEV phase"
            elif arr[2] == '2':
                response = "END Account Status is in DEV phase"
            else:
                response = "END Invalid Option"

    return response

def user_false(arr):
    user = arr[0]
    pwd = arr[1]
    if user == 'agray55' and pwd == 'test':
        return False
    return True
