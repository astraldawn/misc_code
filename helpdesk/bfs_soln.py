import Queue
import numpy
from scipy.spatial import distance # lazy to write a distance function

G = [
"R...",
"....",
".X..",
"...C"
]


G1 = [
"R...",
"....",
"XXXX",
"...C"
]

"""
nway for G
[[  1.   1.   1.   1.]
 [  1.   2.   3.   4.]
 [  1.   0.   3.   7.]
 [  1.   1.   4.  11.]]

nway for G1
[[ 1.  1.  1.  1.]
 [ 1.  2.  3.  4.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]
"""

# helper array for moving to next place
dx = [0,0,1,-1]
dy = [1,-1,0,0]

G = G1 # comment out to see a different case

xlim = 4
ylim = 4

# init everything to 0
vis = numpy.zeros((xlim, ylim)) 
nway = numpy.zeros((xlim, ylim))

(sx, sy) = (0,0) # start pos (R)
(ex, ey) = (3,3) # end pos (C)
nway[sx][sy] = 1 # number of ways to reach start pos

# create queue, put the first pos into queue
q = Queue.Queue()
q.put((sx, sy))

while not q.empty():
    # pull out pos currently at the front of the queue
    cx, cy = q.get()

    # ensure each pos is visited exactly once
    if vis[cx][cy] == 0:

        # set pos to visited
        vis[cx][cy] = 1
        c_dist = distance.euclidean((cx,cy),(ex,ey))

        # when x is encountered, just ignore the square (nway will be 0)
        if G[cx][cy] == 'X':
            continue

        # try to move to all possible positions
        for i in range(0,4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            n_dist = distance.euclidean((nx,ny),(ex,ey))

            # ensure that the new pos is within bounds
            if nx >= 0 and nx < xlim and ny >= 0 and ny < ylim:
                nway[cx][cy] += nway[nx][ny]

                # add the new pos into the queue
                # also think about why it can't be put w/ the bounds checks
                if n_dist < c_dist:
                    q.put((nx,ny))

# look at the array for fun
print nway

if nway[ex][ey] == 0:
    print "error"
else:
    print "Answer ", nway[ex][ey]
