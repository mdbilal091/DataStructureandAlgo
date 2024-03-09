# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from stack import Stack


def listing():
    ls = [1, 2, 3, 10, "Arqam", False]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def reverse_string(my_string):
    reversed_string = ""
    stc = Stack()
    #print(range(len(my_string)))

    #for char in range(len(my_string)):
    for char in my_string:
        #print(char)
        #print(my_string[char])
        stc.push(char)
    print(stc)
    while not stc.is_empty():
        reversed_string += stc.pop()
    print(reversed_string)

    return reversed_string

        #print(reversed_string)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_string = "gninrael nIdekiL htiw tol a nrael"
    reverse_string(test_string)



""" print_hi('Mohammed Bilal')
    ls = [1,2,3,10,"Arqam", False]
    print(ls.append(2))

    my_tuple = (1, 2, "Arqam", True)
    print(my_tuple)

    my_dict = {'name':'Arqam Mohammed', 'age':2, 'city':'San Fransisco'}
    print(my_dict['age'])

    from array import array

    my_array = array('i', [1, 2, 3, 4, 5])
    print(my_array)

    queue = []
    queue.append('a')
    queue.append('b')
    queue.append('c')
    print("Initial queue")
    print(queue)
    print("\nElements dequeued from queue")
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
    print("\nQueue after removing elements")
    print(queue)
"""

'''   s = Stack()
    print(s)

    s.push(1)
    s.push("Robert")
    s.push(3.145)

    s.push([1, 2, 3])

    print(s)

    s.pop()
    print(s)

    print(s.peek())

    print(s.size())

    print(s.is_empty())

    s.pop()
    print(s.pop())
    s.pop()

    print(s.is_empty())
 '''
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
