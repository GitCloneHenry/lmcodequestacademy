[(lambda name, hits: (lambda percentage: print(f"{name[0]}={0 if not percentage else (int(sum(percentage) / len(percentage) * 1000 + 0.5) / 1000):.3f}"))([list(['K', '1B', '2B', '3B', 'HR']).index(hit) for hit in hits if not hit in ['BB', '']]))(*(str.split(',') for str in input().split(':'))) for i in [0]*int(input())]