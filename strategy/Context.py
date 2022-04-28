class Context:
    def __init__(self, Strategy):
        self._strategy = Strategy

    def execute_strategy(self):
        self._strategy.say_something(self)