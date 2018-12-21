#q2test.py
"""test function for question 2 of the ADS assignment, 2018-19"""
from wcrr51_q2_working import count_ephemeral
import time


def q2test():
    """tests for the function count_ephemeral"""
    """
    correct = True
    time0 = time.time()
    result = count_ephemeral(1, 10, 2)
    time1 = time.time()
    if result != 2:
        correct = False
        print("test failed for n1=1, n2=10, k=2; correct result is 2, result obtained was", result)
    else:
        print("test passed for for n1=1, n2=10, k=2 in", time1 - time0, "seconds.")

    time0 = time.time()
    result = count_ephemeral(1000, 10000, 3)
    time1 = time.time()
    if result != 91:
        correct = False
        print("test failed for n1=1000, n2=10000, k=3; correct result is 91, result obtained was", result)
    else:
        print("test passed for for n1=1000, n2=10000, k=3 in", time1 - time0, "seconds.")

    time0 = time.time()
    result = count_ephemeral(123456, 654321, 4)
    time1 = time.time()
    if result != 376:
        correct = False
        print("test failed for n1=123456, n2=654321, k=4; correct result is 376, result obtained was", result)
    else:
        print("test passed for for n1=123456, n2=654321, k=4 in", time1 - time0, "seconds.")
    if correct:
        print("all tests passed")
    """

    time0 = time.time()
    result = count_ephemeral(1, 10000000, 3)
    time1 = time.time()
    print(result, time1 - time0)


if __name__ == '__main__':
    q2test()
