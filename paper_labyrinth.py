xs,ys = [int(i) for i in input().split()] #xs,ys are the coordinates of the start 
xr,yr = [int(i) for i in input().split()] #xr,yr are the coordinates of the rabbit
width,height = [int(i) for i in input().split()] #width,height of the labyrinth
def h(j):
    '''
    converts hexadecimal to binary
    Args:
        j(string) -> hexadecimal value
    Returns:
        w(list<str>) -> binary form of hexadecimal
    '''
    w = []
    for d in j:
        w.append(bin(int(d,16))[2:].zfill(4))
    print(w)
    return w 
words = []
for i in range(height):
    for j in input().split():
        word = h(j)
        words.append(word)
print(words)
'''
implementation of bfs
'''
def bfs(words,starting_node,goal_node):
    '''
    returns minimum length
    Args:
        graphs(dict) -> adjacency list of graphs 
    Returns:
        length(int) - > minimium length
    '''
    visited = [[False]*width]*height 
    length = [[-1]*width] *height
    queue = []
    if starting_node[0] == xs and starting_node[1] == ys:
        queue.append([(words[starting_node[0]][starting_node[1]],0)]) # node and its length
        i = 0
        j = 0
        while (i< len(words) and j< len(words[0]) and i>= 0 and j>= 0 and len(queue)> 0) :
            current_node = queue.pop(0)[0] 
            
            if j == goal_node[0] and i == goal_node[1]:
                return length[i][j]
            if words[i][j][0] == '0' and not visited[i][j]:
                visited[i][j] = True
                length[i][j] = current_node[1]
                j += 1
                queue.append([(words[i][j],current_node[1] + 1)])
            elif words[i][j][1] == '0'and not visited[i][j]:
                visited[i][j] = True
                length[i][j] = current_node[1]
                i -= 1
                queue.append([(words[i][j],current_node[1] + 1)])
            elif words[i][j][2] == '0' and not visited[i][j]:
                visited[i][j] = True
                length[i][j] = current_node[1]
                j -= 1
                queue.append([(words[i][j],current_node[1] + 1)])
            elif words[i][j][3] == '0' and not visited[i][j]:
                visited[i][j] = True
                length[i][j] = current_node[1]
                i += 1
                queue.append([(words[i][j],current_node[1] + 1)])
    elif starting_node[0] == xr and starting_node[1] == yr:
        queue.append([(words[starting_node[1]][starting_node[0]],0)]) # node and its length
        i = xr
        j = yr
        while (i< len(words) and j< len(words[0]) and i>= 0 and j>= 0 and len(queue)> 0) :
            current_node = queue.pop(0)[0] 
            length[i][j] = current_node[1]
            if j == goal_node[0] and i == goal_node[1]:
                return length[i][j]
            if words[i][j][0] == '0' and not visited[i][j]:
                visited[i][j] = True
                j += 1
                queue.append([(words[i][j],current_node[1] + 1)])
            elif words[i][j][1] == '0'and not visited[i][j]:
                visited[i][j] = True
                i -= 1
                queue.append([(words[i][j],current_node[1] + 1)])
            elif words[i][j][2] == '0' and not visited[i][j]:
                visited[i][j] = True
                j -= 1
                queue.append([(words[i][j],current_node[1] + 1)])
            elif words[i][j][3] == '0' and not visited[i][j]:
                visited[i][j] = True
                i += 1
                queue.append([(words[i][j],current_node[1] + 1)])
    print(length)
    print(visited)
print(bfs(words,[xs,ys],[xr,yr]),bfs(words,[xr,yr],[xs,ys]))