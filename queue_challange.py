from collections import deque
from queue_learn import Queue

def queue_challenge():
    my_queue = Queue()
    word_list = ["wore", "a", "silly", "hat", "the", "aardvark"]

    #expected_answer = ["the", "aardvark", "wore", "a", "silly", "hat"]


    for word in word_list:

        my_queue.enqueue(word)

    for i in range(4):
        my_queue.dequeue()
    for j in word_list:
            my_queue.enqueue(j)
    my_queue.__setattr__()
    return my_queue


if __name__ == "__main__":

    result = queue_challenge()
    print(result)