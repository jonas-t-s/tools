def f(x):
    return 2**x + x
stepsize = 1
x = 0
target = 5
precision = 0.0000000000000001
while abs(f(x) - target) > precision:
    x1 = x + stepsize
    x2 = x - stepsize
    stepsize /= 1.5
    if abs(f(x1) - target) < abs(f(x2) - target):
        x = x1
    else:
        x = x2


print(
    f"x = {x} is close enough to the target value {target}")
print(f"stepsize = {stepsize}")
print(f"abs(f(x) - target) = {abs(f(x) - target)}")
print(
    f"f(x) = {f(x)}")