
def generate_next_fibonacci_number(i, j):
    return i + j

a_old = 1
a_current = 1

print(a_old)
print(a_current)

for k in range(10):
    swap = a_current
    a_current = generate_next_fibonacci_number(a_old, a_current)
    a_old = swap
    print(a_current)