[(lambda name, hits: (lambda percentage: print(f"{name[0]}={'0.000' if not sum(percentage) else (lambda num: round(int(num * 1000) * 0.001, 3) if (num * 1000 - int(num * 1000) >= 0.5) else round(num, 3))(sum(percentage) / len(percentage)):.3f}"))([list(['K', '1B', '2B', '3B', 'HR']).index(hit) for hit in hits if hit != 'BB']))(*(map(lambda str : str.split(','), input().split(':')))) for i in [0]*int(input())]