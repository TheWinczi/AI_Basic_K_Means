
from kmeans import *


def main():
    """ main function in program """
    points = get_random_bulbs(240, 6, 0, 0, 20, 20)
    basic_k_means(6, points)


if __name__ == '__main__':
    main()
