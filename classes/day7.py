class Animal():
    noise = 'grunt'
    size = 'Large'

    def get_size(self):
        return self.size


class Dog(Animal):
    name = 'a'
    color = 'brown'

    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color

    def set_color(self, this_color):
        self.color = this_color
    
    def get_noise(self):
        return self.noise
obj = Dog()
print(obj.get_name() + ' is ' + obj.get_color())
print(obj.set_color('blue'))
print(obj.get_name() + ' is ' + obj.get_color())
print(obj.get_name() + ' make this noise : ' + obj.get_noise())
print(obj.get_name() + ' is ' + obj.get_size())