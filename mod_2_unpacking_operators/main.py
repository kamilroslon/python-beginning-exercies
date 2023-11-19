
def exercise_1(*args):
    result = ""
    for argument in args:
        result += argument
        result += "-"
    return result

def exercise_2(**kwargs):
    for name, age in kwargs.items():
        print(f"Name: {name}, age: {age}")


def run_example():

    result = exercise_1("something", "is", "illegal")
    print(result)

def run_example_2():

    persons = {
        "Kamil": 35,
        "Asia": 33,
        "Jagoda": 4
    }
    exercise_2(**persons)

def run_example_3():

    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]

    list_all = [*list1, *list2]

    print(list_all)

def run_example_4():

    persons = {
        "Kamil": 35,
        "Asia": 33,
        "Jagoda": 4
    }

    animals = {
        "Rybka": 0.5,
        "Kotek": 1
    }

    all = {**persons, **animals}

    print(all)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    run_example()

    run_example_2()

    run_example_3()

    run_example_4()
