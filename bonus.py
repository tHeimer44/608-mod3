import statistics

population = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2, 3, 4, 5, 3, 5, 4, 2, 3, 4, 5, 1, 3, 4, 2, 6, 5, 3, 4, 5, 2, 3, 4, 5, 3, 5, 4, 2, 3, 4, 5, 1, 3, 4, 2, 6, 5, 3, 4, 5, 2, 3, 4, 5, 3, 5, 4, 2, 3, 4, 5, 1, 3, 4, 2, 6, 5, 3, 4, 5, 2, 3, 4, 5, 3, 5, 4, 2, 3, 4, 5, 1, 3, 4, 2, 6, 5, 3, 4, 5, 2, 3, 4, 5, 3, 5, 4, 2, 3, 4, 5]

print('Population variance: ', statistics.pvariance(population))
print('Population standard : ', statistics.pstdev(population))
