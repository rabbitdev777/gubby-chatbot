def get_full_time(exp):
    salary = 20000
    if exp >= 3 and exp < 5:
        k = 1.5
    elif exp >= 5 and exp < 7:
        k = 2
    elif exp >= 7:
        k = 3
    else:
        k = 1
    salary *= k
    return salary


def get_part_time(hours):
    per_hour = 800
    salary = hours*per_hour
    return salary


