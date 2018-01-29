import HUI3 as h

print("Score for:", 1, 5, 2, 3, 1, 4, 5, 4)
print(h.get_score(1, 5, 2, 3, 1, 4, 5, 4)) #-0.12849682506752003

print("Score for:", 1, 1, 1, 1, 1, 1, 1, 1)
print(h.get_score(1, 1, 1, 1, 1, 1, 1, 1)) #1.0

print("Score for:", 2, 2, 3, 1, 2, 3, 4, 4)
print(h.get_score(2, 2, 3, 1, 2, 3, 4, 4)) #0.21525760701219243

print("Score for:", 6, 6, 5, 6, 6, 5, 6, 5)
print(h.get_score(6, 6, 5, 6, 6, 5, 6, 5)) #-0.35902730636441177



