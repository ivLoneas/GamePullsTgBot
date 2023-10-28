class Poll:
    def __init__(self, question: str, options: str, allow_multiple_choice: bool, is_anonymous: bool):
        self.question = question
        self.options = options
        self.allow_multiple_choice = allow_multiple_choice
        self.is_anonymous = is_anonymous
