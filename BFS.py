def bfs(graph, source):

    # אתחול המילונים לצורך שמירת הפרמטרים עבור כל קודקוד
    n = len(graph)
    color = {k: 0 for k in graph}
    dist = {k: -1 for k in graph}
    pi = {k: None for k in graph}

    # חישוב ספציפי עבור קודקוד המקור
    color[source] = 1
    dist[source] = 0

    # הכנסת קודקוד המקור לתור
    q = [source]

    while len(q) > 0:
        # שליפת ראש התור
        top_vertex = q.pop(0)

        # מעבר על הבנים שלו שעוד לא נחשפו ועדכון הפרמטרים שלהם והכנסתם לסוף התור
        for neighbor in graph[top_vertex]:
            if color[neighbor] == 0:
                color[neighbor] = 1
                dist[neighbor] = dist[top_vertex] + 1
                pi[neighbor] = top_vertex
                q.append(neighbor)
        color[top_vertex] = 2

    return color, dist , pi


def distance(graph, source, destination):
    c, d, p = bfs(graph, source)
    return d[destination]


def tree_height(graph, source):
    a, d , z = bfs(graph, source)

    max = 0
    for k in d.keys():
        if d[k] > max:
            max = d[k]
    return max



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
    c, d, p = bfs(g, 6)
    print("color = ", c)
    print("dist = ", d)
    print("pi = ", p)
    ans = distance(g,1,7)
    print(ans)

if __name__ == '__main__':
    main()