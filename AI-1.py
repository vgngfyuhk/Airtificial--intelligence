import heapq

goal = [[1,2,3],[4,5,6],[7,8,0]]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def h(s):
    return sum(abs((v-1)//3 - i) + abs((v-1)%3 - j)
               for i in range(3) for j in range(3) if (v:=s[i][j]))

def solve(start):
    q = [(h(start), 0, start, [])]
    seen = set()
    while q:
        _, g, s, p = heapq.heappop(q)
        key = tuple(map(tuple, s))
        if key in seen: continue
        seen.add(key)
        if s == goal: return p + [s]
        x, y = next((i,j) for i in range(3) for j in range(3) if s[i][j]==0)
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<3 and 0<=ny<3:
                ns = [r[:] for r in s]
                ns[x][y], ns[nx][ny] = ns[nx][ny], ns[x][y]
                heapq.heappush(q, (g+1+h(ns), g+1, ns, p+[s]))

def show(p): [print('\n'.join(map(str, b))+'\n') for b in p]

start = [[1,2,3],[4,0,6],[7,5,8]]
res = solve(start)
print("Moves:", len(res)-1)
show(res)
