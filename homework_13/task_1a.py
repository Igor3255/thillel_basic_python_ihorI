class Godzilla:
    def __init__(self, stomach_capacity):
        self.stomach_capacity = stomach_capacity
        self.stomach_content = 0
    
    def eat(self, human_volume):
        if self.stomach_content + human_volume > 0.9 * self.stomach_capacity:
            print("Я наївся, більше не можу з'їсти")
        else:
            self.stomach_content += human_volume


