class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("SubClasses must implemt this method")