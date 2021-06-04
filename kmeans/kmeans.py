
from random import uniform
from kmeans.constants.constants import *
from copy import deepcopy
from math import sqrt
import matplotlib.pyplot as plt

from .point.point import Point


def basic_k_means(clusters: int, points: list[Point]):
    iteration = 0
    roots = get_random_points(clusters, 0, 0, 20, 20)
    roots_points = match_points_to_clusters(points, roots)
    show_result(roots_points, roots, "iteracja "+str(iteration))

    while True:
        roots_copy = deepcopy(roots)
        for i, root_points in enumerate(roots_points):
            x, y = calculate_new_cluster_centre(root_points)
            if x is not None or y is not None:
                roots[i].x = x
                roots[i].y = y

        iteration += 1
        roots_points = match_points_to_clusters(points, roots)
        show_result(roots_points, roots, "iteracja "+str(iteration))

        if are_points_lists_equal(roots_copy, roots):
            break


def show_result(clusters_points: list[list[Point]], clusters_coords: list[Point], title: str = ""):
    plt.figure()
    for i, root_points in enumerate(clusters_points):
        xs, ys = map_points_into_lists(root_points)
        plt.scatter(xs, ys, c=[POINTS_COLORS[i] for _ in range(len(xs))])

    xs, ys = map_points_into_lists(clusters_coords)
    plt.scatter(xs, ys, c=[ROOT_COLOR for _ in range(len(xs))], s=ROOT_RADIUS, alpha=ROOT_ALPHA)
    plt.title(title)
    plt.show()


def match_points_to_clusters(points: list[Point], clusters_centre_points: list[Point]):
    clusters = len(clusters_centre_points)
    distances = get_distances(points, clusters_centre_points)

    roots_points = [[] for _ in range(clusters)]
    for i in range(len(points)):
        point_distances = [distances[j][i] for j in range(clusters)]
        root_index = point_distances.index(min(point_distances))
        roots_points[root_index].append(points[i])
    return roots_points


def get_distances(points: list[Point], clusters_centre_points: list[Point]):
    distances = []
    for i in range(len(clusters_centre_points)):
        distance = []
        for point in points:
            distance.append(get_distance(clusters_centre_points[i].x, clusters_centre_points[i].y, point.x, point.y))
        distances.append(distance.copy())
    return distances


def get_distance(x0, y0, x1, y1):
    # return sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    # return abs(x0 - x1) + abs(y0 - y1)
    return max(abs(x0 - x1), abs(y0 - y1))


def calculate_new_cluster_centre(cluster_points: list[Point]):
    xs, ys = map_points_into_lists(cluster_points)
    x = get_mean(xs)
    y = get_mean(ys)
    return x, y


def get_mean(data: list):
    try:
        return sum(data) / len(data)
    except ZeroDivisionError:
        return None


def are_points_lists_equal(l1: list[Point], l2: list[Point]):
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


def map_points_into_lists(points: list[Point]):
    xs = list(map(lambda p: p.x, points))
    ys = list(map(lambda p: p.y, points))
    return xs, ys


def get_random_points(count: int, x: float, y: float, width: float, height: float):
    points = []
    for i in range(count):
        point = Point(uniform(x, x+width), uniform(y, y+height))
        points.append(point)
    return points


def get_random_point(x: float, y: float, width: float, height: float):
    x, y = uniform(x, x+width), uniform(y, y+height)
    return Point(x, y)


def get_random_bulbs(count: int, groups: int, x: float, y: float, width: float, height: float):

    bulbs_centres = []
    x_off = width / (groups/2)
    y_off = height / 2
    radius = min(x_off/4, y_off/4)

    for i in range(groups//2):
        rand_x = uniform(x+i*x_off, x+(i+1)*x_off)
        rand_y = uniform(y, y+y_off)
        bulbs_centres.append(Point(rand_x, rand_y))

    for i in range(groups//2):
        rand_x = uniform(x+i*x_off, x+(i+1)*x_off)
        rand_y = uniform(y+y_off, y+y_off*2)
        bulbs_centres.append(Point(rand_x, rand_y))

    points = []
    for i in range(groups):
        for j in range(count//groups):
            off_x = uniform(-radius, radius)
            off_y = uniform(-radius, radius)
            points.append(Point(bulbs_centres[i].x+off_x, bulbs_centres[i].y+off_y))

    return points
