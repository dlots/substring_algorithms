ASCII_TABLE_LENGTH = 128
RUSSIAN_TABLE_LENGTH = 36
ALPHABET_LENGTH = ASCII_TABLE_LENGTH + RUSSIAN_TABLE_LENGTH
ASCII_LAST_CODE = 127
RUSSIAN_ALPHABET_FIRST_CODE = 1040


class State:
    def __init__(self, pattern=''):
        self.pattern = pattern
        self.links = [-1 for x in range(ALPHABET_LENGTH)]
        self.is_end = False
        self.fake_link = 0
        self.fake_link_is_end = False

    def __str__(self):
        return self.pattern


def get_symbol_index(symbol):
    index = ord(symbol)
    if index > 127:
        index -= RUSSIAN_ALPHABET_FIRST_CODE - ASCII_LAST_CODE + 1
    return index


class Automata:
    def __init__(self, patterns):
        """

        :param patterns: list of patterns to build an automata from.
        Use a list with one item to pass a single pattern.
        """
        self.__root = State()
        self.__states = [self.__root]
        self.__size = 1
        self.__current_state_index = 0
        self.__report = None
        self.__build_automata(patterns)

    def __get_next_index(self, current_state_index, symbol):
        return self.__states[current_state_index].links[get_symbol_index(symbol)]

    def __insert_pattern(self, pattern):
        current_state_index = 0
        for symbol in pattern:
            next_index = self.__get_next_index(current_state_index, symbol)
            if next_index == -1:
                current_state = self.__states[current_state_index]
                self.__states.append(State(current_state.pattern + symbol))
                current_state.links[get_symbol_index(symbol)] = self.__size
                current_state_index = self.__size
                self.__size += 1
            else:
                current_state_index = next_index
        self.__states[current_state_index].is_end = True

    def __get_pattern_index(self, pattern):
        current_state_index = 0
        for symbol in pattern:
            current_state_index = self.__get_next_index(current_state_index, symbol)
            if current_state_index == -1:
                return -1
        return current_state_index

    def __build_automata(self, patterns):
        for pattern in patterns:
            self.__insert_pattern(pattern)
        for state in self.__states:
            suffix = state.pattern[1:]
            while suffix != '':
                suffix_index = self.__get_pattern_index(suffix)
                if suffix_index == -1:
                    suffix = suffix[1:]
                else:
                    state.fake_link = suffix_index
                    state.fake_link_is_end = self.__states[suffix_index].is_end
                    suffix = ''

    def __report_find(self, symbol_pos):
        pattern = self.__states[self.__current_state_index].pattern
        self.__report[pattern].append(symbol_pos - len(pattern) + 1)

    def __state_transition(self, symbol, symbol_pos):
        next_index = self.__get_next_index(self.__current_state_index, symbol)
        if next_index != -1:
            # If there is a link for a symbol, use it.
            self.__current_state_index = next_index
            if self.__states[self.__current_state_index].is_end:
                self.__report_find(symbol_pos)

            # And check if any prefix is an accepting state.
            saved_current_state = self.__current_state_index
            while self.__states[self.__current_state_index].fake_link_is_end:
                self.__current_state_index = self.__states[self.__current_state_index].fake_link
                self.__report_find(symbol_pos)
            self.__current_state_index = saved_current_state
        else:
            # If there is no link for a symbol, use the fake link and try again.
            self.__current_state_index = self.__states[self.__current_state_index].fake_link
            self.__state_transition(symbol, symbol_pos)

    def process_text(self, text):
        self.__current_state_index = 0
        self.__report = {pattern: [] for pattern in patterns}
        for symbol_pos in range(len(text)):
            self.__state_transition(text[symbol_pos], symbol_pos)
        return self.__report


def aho_corasick(text, patterns):
    automata = Automata(patterns)
    return automata.process_text(text)


if __name__ == "__main__":
    # Simple test for bad case.
    patterns = ['ааб', 'аб', 'а', 'б', 'aab', 'ab', 'a', 'b']
    text = 'баабbaab'
    print(aho_corasick(text, patterns))
