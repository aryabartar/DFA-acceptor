def split_transitions(transition):
    found = False
    array = []
    for element in transition:
        if element == "{":
            found = True
        elif found:
            found = False
            if element == "}":
                array.append("")
            else :
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


def read_strings(string_file_name):
    dfa_strings = open(string_file_name, "r").read().split("\n")
    return dfa_strings


def check_state_is_final(state, dfa_dict):
    is_final = False
    for element in dfa_dict['F']:
        if state == element:
            is_final = True
    return is_final


def print_results(result_array):
    print("RESULTS : ")
    counter = 1
    for element in result_array:
        print(str(counter) + " => " + str(element))
        counter += 1


def main_func(machine_file_name, string_file_name):
    dfa_dict = get_dfa_elements(open(machine_file_name, "r").read().split("\n"))
    print(dfa_dict)
    result_array = []
    for string in read_strings(string_file_name):
        present_state = dfa_dict["I"][0]
        for element in string:
            transition_index = dfa_dict['E'].index(element)
            present_state = dfa_dict['T'][present_state][transition_index]
        result_array.append(check_state_is_final(present_state, dfa_dict))
    print_results(result_array)


FILES_NAME = (("FIRST_DFA.txt", "Strings_for_first_DFA.txt"),
              ("Second_DFA.txt", "Strings_for_second_DFA.txt"),
              ("Third_DFA.txt", "Strings_for_third_DFA.txt"),
              ("Fourth_DFA.txt", "Strings_for_fourth_DFA.txt"),
              ("Fifth_DFA.txt", "Strings_for_fifth_DFA.txt"))

for item in FILES_NAME:
    main_func(item[0], item[1])
