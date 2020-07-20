from itertools import count
from itertools import cycle

# --- COUNT--- #
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

# --- COUNT--- #

# --- CYCLE--- #

x = 0
for el in cycle(["XZ", 123, 89.0]):
    if x >= 5:
        break
    print(el)
    x += 1

# --- CYCLE--- #

# --- COUNT и CYCLE со звездочкой--- #

from itertools import count
from itertools import cycle
from itertools import islice

new_list = [el for el in islice(count(3, 10), 3)]
iter = cycle(new_list)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

# --- COUNT и CYCLE со звездочкой--- #