import sys

class DFA:
    def __init__(self, filename):
        self.state_count = 0
        self.states = set()
        self.initial_state = None
        self.final_state = set()
        self.alphabet = []
        self.transition_lines = {}

        self.load_dfa(filename)

    def load_dfa (self, filename):
        with open (filename, 'r') as file:
            lines = file.read().splitlines()

        if len(lines) < 5:
            print ("Error: DFA not formatted correctly")
            sys.exit(1)
    
        self.num_states = int(lines[0])
        self.states = set(range(self.num_states))

        initial_states = lines[1].split()
        if len(initial_states) != 1:
            print (f"Error: Incorrect number of inital states. Supposed to have 1 you have {initial_states}.")
            sys.exit(1)
        self.initial_state = int(initial_states[0])

        self.final_state = set(map(int, lines[2].split()))
        

        self.alphabet = list(lines[3])


        transition_matrix = lines[4:]
        if len(transition_matrix) != self.num_states:
            print("ERROR: Transition table does not match the number of states")
            sys.exit(1)

        for state, line in enumerate(transition_matrix):
            transition_lines = list(map(int, line.split()))
            if len(transition_lines) != len(self.alphabet):
                print(f"ERROR: Row {state} has incorrect number of transactions")
                sys.exit(1)

            for symbol_index, next_state in enumerate(transition_lines):
                symbol = self.alphabet[symbol_index]
                self.transition_lines[(state, symbol)] = next_state


    def process_string (self, string, file_line_number):
        if string == "":
            return f"[{file_line_number}] No  <empty>"
        current_state = self.initial_state

        for position,symbol in enumerate(string, start = 1):
            if (current_state, symbol) in self.transition_lines:
                current_state = self.transition_lines[(current_state, symbol)]
            else:
                return f"[{file_line_number}] No  {string}"
        return f"[{file_line_number}] Yes {string}" if current_state in self.final_state else f"[{file_line_number}] No  {string}"
        

def main():
    if len(sys.argv) != 3:
        print("Usage: python dfa_evaluator.py <dfa_file> <text_file>")
        return
        
    dfa_file = sys.argv[1]
    text_file = sys.argv[2]

    dfa = DFA(dfa_file)

    with open(text_file, 'r') as file:
        strings = file.read().splitlines()

    for line_number, string in enumerate(strings, start = 1):
        print(dfa.process_string(string, line_number))
if __name__ == "__main__":
    main()


