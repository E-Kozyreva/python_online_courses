# Дополните приведенный код, так чтобы получить список, содержащий только непустые кортежи исходного списка tuples, не меняя порядка их следования.

tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = []

for _ in range(len(tuples)):
    if len(tuples[_]) != 0:
        non_empty_tuples.append(tuples[_])

print(non_empty_tuples)
