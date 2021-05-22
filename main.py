
from kmeans import *


def main():
    """ main function in program """
    points = get_random_bulbs(200, 4, 0, 0, 20, 20)
    basic_k_means(4, points)


if __name__ == '__main__':
    main()
