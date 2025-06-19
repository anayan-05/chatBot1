class ChatMemory:
    def __init__(self, max_turns=3):
        self.max_turns = max_turns
        self.history = []

    def add_turn(self, user_input):
        self.history.append(user_input)
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_context(self):
        return " ".join(self.history)
