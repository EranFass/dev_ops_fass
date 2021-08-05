"""
We have an existing dictionary that maps US states to their capitals.
1. Print the state capital of Idaho
2. Print all states.
3. Print all capitals.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?
Implement the function def get_state(capital): below so it returns the state.
GOTCHAS: What happens if two states have the same capital name ?
==> YG added ==> Will return the last one from the dictionary,
how do you handle that?
==> YG added ==> code dev if several keys count... ==> OK DONE ;-)
git check
"""

import sys
import pytest

STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    # 'Indiana' : 'Indianapolis',
    'Indiana' : 'Boise',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
    # 'Ababaaa' : 'YoavGUEZ'
}


def capital_of_Idaho():
    print('Capital of Idaho = ' + STATES_CAPITALS['Idaho'])

def all_states():
    print('All States:')
    state_check_ordered = []
    for key in STATES_CAPITALS.keys():
        print(key)

def all_states_check():
    print('All States: Checking if sorted alphabetically:...\n')
    state_check_ordered = []
    for key in STATES_CAPITALS.keys():
        state_check_ordered.append(key)
        # print(list(state_check_ordered) == sorted(state_check_ordered))
    if list(state_check_ordered) == sorted(state_check_ordered):
        print("OK GOOD !!! STATES are sorted alphabetically")
    else:
        print("ATTENTION !!! STATES are not sorted alphabetically!!!")
    # print(state_check_ordered)
    return


def all_capitals():
    print('All Capitals:')
    for value in STATES_CAPITALS.values():
        print(value)

def states_capitals_string():
    print('States and Capitals in a string:')
    str = ''
    for key,value in STATES_CAPITALS.items():
        str += (key + ' -> ' +  value + ' , ')
    print(str[:len(str) - 3])

lambda_expr = {v: k for k, v in STATES_CAPITALS.items()}

def get_state(capital):
    return lambda_expr[capital]

def get_state_yg(capital,value):
    for k, v in STATES_CAPITALS.items():
        if v == value:
            yield k
    # return lambda_expr[capital]


# Here, I test my code.
capital_of_Idaho()
print('\n\n\n')
all_states()
print('\n\n\n')
all_capitals()
print('\n\n\n')
states_capitals_string()
print('\n')
all_states_check()
print('\n\n\n')
print('The state of Madison Capital city = ' + get_state('Madison'))
# ==> YG Added:
print('\n\n\n')
capi = input("What is your Capital city? I will guess your state...")
keys = list(get_state_yg(STATES_CAPITALS, capi))
if len(keys) > 1:
    print("you have more that one answer...\nThe possibilities are:\n\t\t\t\t\t", keys)
else:
    print(f'The state of {capi} Capital city = ' + get_state(capi))

def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']

def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']

def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')

def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        raise KeyError



"""
def main():
    return pytest.main(_file_)
if _name_ == '_main_':
    sys.exit(main())
"""