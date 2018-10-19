def split_transitions(transition):
    found = False
    array = []
    for element in transition:
        if element == "{":
            found = True
        elif found:
            found = False
            array.append(element)
    return array


def split_comma(string):
    is_odd = True
    array = []
    for element in string:
        if is_odd:
            array.append(element)
        is_odd = not is_odd

    return array


def get_dfa_elements(dfa_array):
    main_dict = {}
    transition_array = []
    for element in dfa_array:
        first_element = element[0]
        if first_element == 'S':
            s_array = split_comma(element[2:])
            main_dict['S'] = s_array
        elif first_element == 'E':
            e_array = split_comma(element[2:])
            main_dict['E'] = e_array
        elif first_element == 'I':
            i_array = split_comma(element[2:])
            main_dict['I'] = i_array
        elif first_element == 'F':
            f_array = split_comma(element[2:])
            main_dict['F'] = f_array
        elif first_element == "{":
            transition_array.append(split_transitions(element))
    main_dict['T'] = transition_array
    return main_dict


dfa_array = open("FIRST_DFA.txt", "r").read().split("\n")
print(dfa_array)
print(get_dfa_elements(dfa_array))
