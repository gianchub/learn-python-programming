# This is not a valid Python module - Don't run it.

>>> _ = list
>>> map(lambda *a: a, range(3))  # 1 iterable
<map object at 0x10acf8f98>  # Not useful! Let's use alias
>>> _(map(lambda *a: a, range(3)))  # 1 iterable
[(0,), (1,), (2,)]
>>> _(map(lambda *a: a, range(3), 'abc'))  # 2 iterables
[(0, 'a'), (1, 'b'), (2, 'c')]
>>> _(map(lambda *a: a, range(3), 'abc', range(4, 7)))  # 3
[(0, 'a', 4), (1, 'b', 5), (2, 'c', 6)]
>>> # map stops at the shortest iterator
>>> _(map(lambda *a: a, (), 'abc'))  # empty tuple is shortest
[]
>>> _(map(lambda *a: a, (1, 2), 'abc'))  # (1, 2) shortest
[(1, 'a'), (2, 'b')]
>>> _(map(lambda *a: a, (1, 2, 3, 4), 'abc'))  # 'abc' shortest
[(1, 'a'), (2, 'b'), (3, 'c')]
