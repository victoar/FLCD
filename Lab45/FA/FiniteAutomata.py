class Transition:
    def __init__(self, startState, value, endState):
        self.startState = startState
        self.value = value
        self.endState = endState

    def getStartSate(self):
        return self.startState

    def setStartSate(self, startState):
        self.startState = startState

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getEndState(self):
        return self.endState

    def setEndState(self, endState):
        self.endState = endState

    def __str__(self) -> str:
        return str(self.startState) + " " + str(self.value) + " " + str(self.endState)


class FiniteAutomata:
    def __init__(self):
        self.alphabet = []
        self.states = []
        self.transitions = []
        self.initialState = []
        self.endStates = []

    def readFromFile(self):
        with open("fa.in", 'r') as file:
            lineNo = 0
            for line in file:
                if lineNo == 0:
                    self.states = line.split("\n")[0].split(" ")
                    lineNo += 1
                elif lineNo == 1:
                    self.alphabet = line.split("\n")[0].split(" ")
                    lineNo += 1
                elif lineNo == 2:
                    self.initialState = line.split("\n")[0]
                    lineNo += 1
                elif lineNo == 3:
                    self.endStates = line.split("\n")[0]
                    lineNo += 1
                else:
                    transitions_parts = line.split("\n")[0].split(" ")
                    transition = Transition(transitions_parts[0], transitions_parts[1], transitions_parts[2])
                    self.transitions.append(transition)

    def get_next_state(self, curent_state, value):
        for transition in self.transitions:
            if (curent_state == transition.startState) & (transition.value == value):
                return transition.endState
        return None

    def is_accepted(self, variable):
        curent_state = self.initialState
        for character in variable:
            curent_state = self.get_next_state(curent_state, character)
        return curent_state in self.endStates

    def str_alphabet(self):
        to_print = "Alphabet: "
        for elem in self.alphabet:
            to_print += str(elem) + " "
        return to_print

    def str_states(self):
        to_print = "States: "
        for elem in self.states:
            to_print += str(elem) + " "
        return to_print

    def str_initial_state(self):
        to_print = "Initial states: " + str(self.initialState)
        return to_print

    def str_final_states(self):
        to_print = "Final states: "
        for elem in self.endStates:
            to_print += str(elem) + " "
        return to_print

    def str_transition(self):
        to_print = "Transition: "
        for elem in self.transitions:
            to_print += str(elem) + " \n"
        return to_print


def print_menu():
    print("1.Print set of states")
    print("2.Print alphabet")
    print("3.Print transitions")
    print("4.Print initial state")
    print("5.Print final states")
    print("6.Check if string is accepted ")


if __name__ == '__main__':


    while True:
        fa = FiniteAutomata()
        fa.readFromFile()
        print_menu()
        option = input("Choose option: ")
        if option == "1":
            print(fa.str_states())
        elif option == "2":
            print(fa.str_alphabet())
        elif option == "3":
            print(fa.str_transition())
        elif option == "4":
            print(fa.str_initial_state())
        elif option == "5":
            print(fa.str_final_states())
        elif option == "6":
            given_string = input("Give a string: ")
            if fa.is_accepted(given_string):
                print("Accpeted")
            else:
                print("Not accpeted")
        else:
            print("Ciao")
            break
