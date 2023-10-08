

def supress_exception(exception = KeyError, result = False):
    def dummy_return(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if result is not None:
                    return result
                else:
                    raise e

        return inner
    return dummy_return


users = {'Medhavi': 'Medhavi@123', 'ABC': 'xyz' }


@supress_exception(KeyError, result=False)
def authenticate(user, password):
    print(f'Authenticating {user}')
    return users.get(user) == password

result = authenticate('Medha', 'Medhavi@123')
print("Authentication result: ", result) 


        