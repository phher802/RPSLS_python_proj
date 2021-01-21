from player import Player


class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.current_gesture = []

    def choose_gesture(self):
        def display_list():
            print("These are the available gestures: ")
            for gesture in self.gestures:
                print(gesture)

        def user_input():
            chosen_input = int(input("Choose a gesture to play by entering the number next to the gesture"))
            while chosen_input >= 5:
                chosen_input = int(input("Number is invalid.  Please choose a number from 0 to 4"))
            else:
                self.current_gesture.append(chosen_input)

            print(self.name + " chose " + str(self.current_gesture))

        display_list()
        user_input()








