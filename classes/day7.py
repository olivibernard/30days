class Dog():
    name = 'a'
    color = 'brown'

    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color

obj = Dog()
print(obj.get_color())
print(obj.get_name())