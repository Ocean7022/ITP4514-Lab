import random

numbers = random.sample(range(1, 49), 6)
print(f"[{' '.join(map(str, numbers))}]")