time = 0
def dfs(graph):
    global time
    # אתחול המילונים לצורך שמירת הפרמטרים עבור כל קודקוד
    n = len(graph)
    color = {k: 0 for k in graph}
    pi = {k: None for k in graph}
    begin = {k: None for k in graph}
    finish = {k: None for k in graph}

    for v in graph:
        if color[v] == 0:
            dfs_visit(graph, v, color, pi, begin, finish)
    return color, pi, begin, finish


def dfs_visit(graph, v, color, pi, begin, finish):
    global time

    color[v] = 1
    time += 1
    begin[v] = time

    for u in graph[v]:
        if color[u] == 0:
            pi[u] = v
            dfs_visit(graph, u, color, pi, begin, finish)

    time += 1
    finish[v] = time
    color[v] = 2


def disconnecded(graph):
    c , p , s , e = dfs(graph)
    ans = 0
    for u in p :
        if u is None:
            ans += 1
    return ans == 1





def main():
    """
    1 --- 2     3 --- 4
    |     |  /  |  /  |
    |     |/    |/    |
    5     6 --- 7 --- 8
    """
    g = dict()
    g[1] = [2, 5]
    g[2] = [1, 6]
    g[3] = [4, 6, 7]
    g[4] = [3, 7, 8]
    g[5] = [1]
    g[6] = [2, 3, 7]
    g[7] = [3, 4, 7, 8]
    g[8] = [4, 7]
    c, p, b, f = dfs(g)
    print("color = ", c)
    print("pi = ", p)
    print("begin = ", b)
    print("finish = ", f)
    print(disconnecded(g))


if __name__ == '__main__':
    main()