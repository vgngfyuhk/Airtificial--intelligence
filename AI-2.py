def solve(q=[], r=0):
    if r == 8: return q
    for c in range(8):
        if all(c != qc and r - i != abs(c - qc) for i, qc in enumerate(q)):
            res = solve(q + [c], r + 1)
            if res: return res

q = solve()
for r in range(8):
    print('.' * q[r] + 'Q' + '.' * (7 - q[r]))
