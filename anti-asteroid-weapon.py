for i in [0]*int(input()):
    print('\n'.join([f"{a} {b}" for a, b in sorted([list(map(int, input().split(' '))) for j in [0]*int(input())], key=lambda point: (point[0]**2 + point[1]**2)**0.5)]))