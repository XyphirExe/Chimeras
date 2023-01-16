class Game:

    def __init__(self) -> None:
        self.isRunning = False
        pass

    def run(self):
        self.isRunning = True
        while self.isRunning:
            self.update()
    
    def update(self):
        pass