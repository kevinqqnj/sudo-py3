# Sudoku

exclude and recursive method to solve Sudoku
> based on Python秒解最难数独 - 杨仕航的博客 http://yshblog.com/blog/74 .
> fit for python3

### requirements
1. Python3
2. numpy

### run:
`pip3 install numpy`

```
/home/kevinqq/git/sudo-py3/venv/bin/python /home/kevinqq/git/sudo-py3/sudo-recur.py
DEBUG:__main__:current no. of fixed answers: 21
DEBUG:__main__:add to LIFO queue and guessing 3/[3, 9]: [(7, 6)]
DEBUG:__main__:current no. of fixed answers: 22
DEBUG:__main__:add to LIFO queue and guessing 5/[5, 9]: [(7, 6), (6, 6)]
DEBUG:__main__:current no. of fixed answers: 25
DEBUG:__main__:add to LIFO queue and guessing 6/[6, 8, 9]: [(7, 6), (6, 6), (5, 6)]
DEBUG:__main__:verify failed. dup in col 0
DEBUG:__main__:Recall! Pop previous point, [6, 8, 9] @(5, 6)
DEBUG:__main__:guessing next index: answer=8/[6, 8, 9] @(5, 6)
DEBUG:__main__:current no. of fixed answers: 29
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 4, 6]: [(7, 6), (6, 6), (5, 6), (5, 1)]
DEBUG:__main__:verify failed. dup in col 0
...
DEBUG:__main__:guessing next index: answer=3/[2, 3, 8] @(4, 3)
DEBUG:__main__:current no. of fixed answers: 41
DEBUG:__main__:add to LIFO queue and guessing 1/[1, 4]: [(7, 6), (6, 6), (6, 1), (6, 3), (4, 3), (1, 1)]
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [1, 4] @(1, 1)
DEBUG:__main__:guessing next index: answer=4/[1, 4] @(1, 1)
DEBUG:__main__:current no. of fixed answers: 42
DEBUG:__main__:add to LIFO queue and guessing 1/[1, 6, 8]: [(7, 6), (6, 6), (6, 1), (6, 3), (4, 3), (1, 1), (4, 1)]
DEBUG:__main__:verify failed. dup in row 4
DEBUG:__main__:Recall! Pop previous point, [1, 6, 8] @(4, 1)
DEBUG:__main__:guessing next index: answer=6/[1, 6, 8] @(4, 1)
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [1, 6, 8] @(4, 1)
DEBUG:__main__:guessing next index: answer=8/[1, 6, 8] @(4, 1)
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [1, 6, 8] @(4, 1)
DEBUG:__main__:Recall! Pop previous point, [1, 4] @(1, 1)
DEBUG:__main__:Recall! Pop previous point, [2, 3, 8] @(4, 3)
DEBUG:__main__:guessing next index: answer=8/[2, 3, 8] @(4, 3)
DEBUG:__main__:current no. of fixed answers: 33
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 3]: [(7, 6), (6, 6), (6, 1), (6, 3), (4, 3), (3, 3)]
DEBUG:__main__:current no. of fixed answers: 42
DEBUG:__main__:add to LIFO queue and guessing 3/[3, 4]: [(7, 6), (6, 6), (6, 1), (6, 3), (4, 3), (3, 3), (7, 1)]
DEBUG:__main__:current no. of fixed answers: 45
DEBUG:__main__:add to LIFO queue and guessing 1/[1, 6]: [(7, 6), (6, 6), (6, 1), (6, 3), (4, 3), (3, 3), (7, 1), (4, 1)]
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [1, 6] @(4, 1)
DEBUG:__main__:guessing next index: answer=6/[1, 6] @(4, 1)
INFO:__main__:Done! guessed 109 times, in 0.540sec
INFO:__main__:Puzzle:
[[8 0 0 0 0 0 0 0 0]
 [0 0 3 6 0 0 0 0 0]
 [0 7 0 0 9 0 2 0 0]
 [0 5 0 0 0 7 0 0 0]
 [0 0 0 0 4 5 7 0 0]
 [0 0 0 1 0 0 0 3 0]
 [0 0 1 0 0 0 0 6 8]
 [0 0 8 5 0 0 0 1 0]
 [0 9 0 0 0 0 4 0 0]]
INFO:__main__:Answer:
[[8 1 2 7 5 3 6 4 9]
 [9 4 3 6 8 2 1 7 5]
 [6 7 5 4 9 1 2 8 3]
 [1 5 4 2 3 7 8 9 6]
 [3 6 9 8 4 5 7 2 1]
 [2 8 7 1 6 9 5 3 4]
 [5 2 1 9 7 4 3 6 8]
 [4 3 8 5 2 6 9 1 7]
 [7 9 6 3 1 8 4 5 2]]

```



