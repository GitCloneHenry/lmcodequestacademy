print('\n'.join(['false', 'true'][c - 5 * b > a] for a, b, c in (list(map(int, input().split())) for i in [0]*int(input()))))