

def do_stuff(num):
    try:
        sum = int(num) + 5
    except ValueError as err:
        return err
    return sum
