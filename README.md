# DFA Evaluator

A Python program that loads a Deterministic Finite Automaton (DFA) from a file and evaluates input strings to determine whether they are accepted or rejected.

This project demonstrates concepts from automata theory, file parsing, and command-line program design.

---

## Features
- Loads a DFA definition from a text file
- Validates DFA formatting and transitions
- Processes multiple input strings from a file
- Outputs acceptance results for each string
- Object-oriented Python design

---

## DFA File Format

The DFA file must follow this format:

<number_of_states>  
<initial_state>  
<final_states (space-separated)>  
<alphabet>  
<transition_row_for_state_0>  
<transition_row_for_state_1>  
...

### Example DFA File
```text
3
0
2
ab
1 0
2 0
2 2
```

- States are numbered from 0 to n-1
- Alphabet symbols are listed on one line (no spaces)
- Each transition row corresponds to one state
- Transition rows list next states for each alphabet symbol

---

## Input Strings File

The input file contains one string per line:

```text
ab
aab
abb
baba
```
An empty line represents the empty string.

---

## How to Run

From the project directory, run:

```bash
python dfa_evaluator.py <dfa_file> <input_file>
```

### Example:
```bash
python dfa_evaluator.py example_dfa.txt input_strings.txt
```

---

## Output Format

Example output:

```text
[1] Yes ab
[2] No aab
[3] Yes abb
[4] No baba
```

- "Yes" means the string is accepted
- "No" means the string is rejected
- Line numbers correspond to input file lines

---

## Error Handling

The program checks for:
- Correct number of states
- Exactly one initial state
- Valid transition table size
- Transitions matching the alphabet size
- Proper DFA formatting

If an error is found, the program exits with an explanatory message.

---

## Educational Value

This project demonstrates:
- Deterministic Finite Automata evaluation
- Command-line argument handling
- File parsing and validation
- Object-oriented programming in Python

Suitable for coursework in Automata Theory or Formal Languages.

---

## Author

Kimberly Birmingham

---

## License

Educational use only.
