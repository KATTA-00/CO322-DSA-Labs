t = int(input())

oprations = ["*", "/", "+", "-"]

def opration(a, b, op):
    if op == "+":
        return a+b
    if op == "-":
        return a-b
    if op == "*":
        return a*b
    if op == "/":
        return a//b

for _ in range(t):
    arr = list(map(str, input().strip().split(' ')))

    l = len(arr)

    stack = []

    for i in range(l):
        val = arr.pop(0)

        if val not in oprations:
            stack.append(val)
        else:
            a = int(stack.pop())
            b = int(stack.pop())

            stack.append(opration(b, a, val))

    print(stack[0])
    
