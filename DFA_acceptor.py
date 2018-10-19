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
    def make_transition_dict(transition_array, s_array):
        temp_dict = {}
        for i in range(0, len(s_array)):
            temp_dict[s_array[i]] = transition_array[i]
        return temp_dict

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
    main_dict['T'] = make_transition_dict(transition_array, s_array)

    return main_dict


def read_strings():
    dfa_strings = open("Strings_for_first_DFA.txt", "r").read().split("\n")
    return dfa_strings


dfa_array = open("FIRST_DFA.txt", "r").read().split("\n")
dfa_dict = get_dfa_elements(dfa_array)
print(dfa_dict)
start_state = dfa_dict["I"][0]
for element in read_strings()[0]:
    pass
