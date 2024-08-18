calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return tuple([len(str(string)), str(string).upper(), str(string).lower()])

def is_contains(string, list_to_search):
    flag = False
    count_calls()
    for element in list_to_search:
        if str(element).upper() == str(string).upper():
            flag = True
            return flag
    if flag != True:
        flag = False
        return flag

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
