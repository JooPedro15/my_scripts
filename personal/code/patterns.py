"""
Printing patterns
"""
counter = 10
for i in range(0, 21):
    if counter > 0:
        print(list(range(0, counter+1)))
        counter -= 1
    elif counter == 0:
        print(list(range(0, counter+1)))
        counter -= 1
    elif counter < 0:
        print(list(range(0, (-counter)+1)))
        counter -= 1