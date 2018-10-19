def split_transitions(transition):
    found = False
    array = []
    for element in transition:
        if element == "{" :
            found = True
        elif found:
            found = False
            array.append(element)
    return array

def get_dfa_elements(dfa_array):
    transition_array = []
    for element in dfa_array:
        first_element = element[0]
        if first_element == 'S':
            s_array = element[2:]
            print(s_array)
        elif first_element == 'E':
            e_array = element[2:]
            print(e_array)
        elif first_element == 'I':
            i_array = element[2:]
            print(i_array)
        elif first_element == 'F':
            f_array = element[2:]
            print(f_array)
        elif first_element == "{":
            transition_array.append(split_transitions(element))
    print(transition_array)


dfa_array = open("FIRST_DFA.txt", "r").read().split("\n")

print(dfa_array)
get_dfa_elements(dfa_array)
