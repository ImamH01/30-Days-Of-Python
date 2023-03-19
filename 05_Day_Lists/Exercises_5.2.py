ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0], ages[-1])
import statistics

print(statistics.median(ages))


def average(ages):
    return sum(ages) / len(ages)


print(average(ages))
range = max(ages) - min(ages)
print(range)
max_average = max(ages) - average(ages)
min_average = min(ages) - average(ages)
print(abs(max_average), abs(min_average))
