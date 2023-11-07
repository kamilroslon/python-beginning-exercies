import random
class TestClass:
    def __init__(self, some_name, more_name, some_list):
        self.some_name = some_name
        self.more_name = more_name
        self.some_list = some_list
        # self.for_real = False

    def __str__(self):
        return f"Some name: {self.some_name} and more name: {self.more_name}"

    def __repr__(self):
        return f"<Something: {self.some_name}, something else: {self.more_name}>"

    def __len__(self):
        return len(self.some_list)

    # def __bool__(self):
    #     return self.for_real

def generate_list():
    some_list = []
    random_number = random.randint(1, 99)
    for list_element in range(random_number):
        new_element = f"New_element-{list_element}"
        some_list.append(new_element)
    return some_list

if __name__ == '__main__':

    new_list = generate_list()
    some_random_name = TestClass(791728172,12345, new_list)
    some_random_repr = repr(some_random_name)
    print(some_random_repr)
    print(some_random_name)
    print(new_list)
    print(len(some_random_name))
    print(bool(some_random_name))


