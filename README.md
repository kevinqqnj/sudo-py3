# Sudoku

exclude and recursive method to solve Sudoku
> based on Python秒解最难数独 - 杨仕航的博客 http://yshblog.com/blog/74 .
> fit for python3

### requirements
1. Python3
2. numpy

### run:
`pip3 install numpy`

`python3 sudo-recur.py`
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
DEBUG:__main__:Recall! Pop previous point, [2, 4, 6] @(5, 1)
DEBUG:__main__:guessing next index: answer=4/[2, 4, 6] @(5, 1)
DEBUG:__main__:current no. of fixed answers: 30
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 6]: [(7, 6), (6, 6), (5, 6), (5, 1), (7, 1)]
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [2, 6] @(7, 1)
DEBUG:__main__:guessing next index: answer=6/[2, 6] @(7, 1)
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [2, 6] @(7, 1)
DEBUG:__main__:Recall! Pop previous point, [2, 4, 6] @(5, 1)
DEBUG:__main__:guessing next index: answer=6/[2, 4, 6] @(5, 1)
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [2, 4, 6] @(5, 1)
DEBUG:__main__:Recall! Pop previous point, [6, 8, 9] @(5, 6)
DEBUG:__main__:guessing next index: answer=9/[6, 8, 9] @(5, 6)
DEBUG:__main__:current no. of fixed answers: 28
DEBUG:__main__:add to LIFO queue and guessing 1/[1, 8]: [(7, 6), (6, 6), (5, 6), (1, 6)]
DEBUG:__main__:current no. of fixed answers: 35
DEBUG:__main__:add to LIFO queue and guessing 5/[5, 8]: [(7, 6), (6, 6), (5, 6), (1, 6), (2, 7)]
DEBUG:__main__:verify failed. dup in col 0
DEBUG:__main__:Recall! Pop previous point, [5, 8] @(2, 7)
DEBUG:__main__:guessing next index: answer=8/[5, 8] @(2, 7)
DEBUG:__main__:current no. of fixed answers: 36
DEBUG:__main__:add to LIFO queue and guessing 5/[5, 9]: [(7, 6), (6, 6), (5, 6), (1, 6), (2, 7), (1, 7)]
DEBUG:__main__:current no. of fixed answers: 41
DEBUG:__main__:add to LIFO queue and guessing 4/[4, 7]: [(7, 6), (6, 6), (5, 6), (1, 6), (2, 7), (1, 7), (1, 8)]
DEBUG:__main__:verify failed. dup in row 2
DEBUG:__main__:Recall! Pop previous point, [4, 7] @(1, 8)
DEBUG:__main__:guessing next index: answer=7/[4, 7] @(1, 8)
DEBUG:__main__:current no. of fixed answers: 43
DEBUG:__main__:add to LIFO queue and guessing 3/[3, 4]: [(7, 6), (6, 6), (5, 6), (1, 6), (2, 7), (1, 7), (1, 8), (0, 8)]
DEBUG:__main__:verify failed. dup in row 7
DEBUG:__main__:Recall! Pop previous point, [3, 4] @(0, 8)
DEBUG:__main__:guessing next index: answer=4/[3, 4] @(0, 8)
DEBUG:__main__:current no. of fixed answers: 53
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 8]: [(7, 6), (6, 6), (5, 6), (1, 6), (2, 7), (1, 7), (1, 8), (0, 8), (1, 5)]
DEBUG:__main__:current no. of fixed answers: 55
DEBUG:__main__:add to LIFO queue and guessing 6/[6, 8]: [(7, 6), (6, 6), (5, 6), (1, 6), (2, 7), (1, 7), (1, 8), (0, 8), (1, 5), (5, 5)]
DEBUG:__main__:verify failed. dup in row 6
DEBUG:__main__:Recall! Pop previous point, [6, 8] @(5, 5)
DEBUG:__main__:guessing next index: answer=8/[6, 8] @(5, 5)
DEBUG:__main__:verify failed. dup in row 3
DEBUG:__main__:Recall! Pop previous point, [6, 8] @(5, 5)
DEBUG:__main__:Recall! Pop previous point, [2, 8] @(1, 5)
DEBUG:__main__:guessing next index: answer=8/[2, 8] @(1, 5)
DEBUG:__main__:verify failed. dup in row 5
DEBUG:__main__:Recall! Pop previous point, [2, 8] @(1, 5)
DEBUG:__main__:Recall! Pop previous point, [3, 4] @(0, 8)
DEBUG:__main__:Recall! Pop previous point, [4, 7] @(1, 8)
DEBUG:__main__:Recall! Pop previous point, [5, 9] @(1, 7)
DEBUG:__main__:guessing next index: answer=9/[5, 9] @(1, 7)
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [5, 9] @(1, 7)
DEBUG:__main__:Recall! Pop previous point, [5, 8] @(2, 7)
DEBUG:__main__:Recall! Pop previous point, [1, 8] @(1, 6)
DEBUG:__main__:guessing next index: answer=8/[1, 8] @(1, 6)
DEBUG:__main__:current no. of fixed answers: 29
DEBUG:__main__:add to LIFO queue and guessing 1/[1, 6]: [(7, 6), (6, 6), (5, 6), (1, 6), (3, 6)]
DEBUG:__main__:current no. of fixed answers: 31
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 6, 8]: [(7, 6), (6, 6), (5, 6), (1, 6), (3, 6), (5, 5)]
DEBUG:__main__:current no. of fixed answers: 32
DEBUG:__main__:add to LIFO queue and guessing 4/[4, 6]: [(7, 6), (6, 6), (5, 6), (1, 6), (3, 6), (5, 5), (7, 5)]
DEBUG:__main__:verify failed. dup in row 3
DEBUG:__main__:Recall! Pop previous point, [4, 6] @(7, 5)
DEBUG:__main__:guessing next index: answer=6/[4, 6] @(7, 5)
DEBUG:__main__:verify failed. dup in row 2
DEBUG:__main__:Recall! Pop previous point, [4, 6] @(7, 5)
DEBUG:__main__:Recall! Pop previous point, [2, 6, 8] @(5, 5)
DEBUG:__main__:guessing next index: answer=6/[2, 6, 8] @(5, 5)
DEBUG:__main__:current no. of fixed answers: 32
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 4]: [(7, 6), (6, 6), (5, 6), (1, 6), (3, 6), (5, 5), (7, 5)]
DEBUG:__main__:verify failed. dup in row 3
DEBUG:__main__:Recall! Pop previous point, [2, 4] @(7, 5)
DEBUG:__main__:guessing next index: answer=4/[2, 4] @(7, 5)
DEBUG:__main__:current no. of fixed answers: 33
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 6]: [(7, 6), (6, 6), (5, 6), (1, 6), (3, 6), (5, 5), (7, 5), (7, 1)]
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [2, 6] @(7, 1)
DEBUG:__main__:guessing next index: answer=6/[2, 6] @(7, 1)
DEBUG:__main__:verify failed. dup in row 4
DEBUG:__main__:Recall! Pop previous point, [2, 6] @(7, 1)
DEBUG:__main__:Recall! Pop previous point, [2, 4] @(7, 5)
DEBUG:__main__:Recall! Pop previous point, [2, 6, 8] @(5, 5)
DEBUG:__main__:guessing next index: answer=8/[2, 6, 8] @(5, 5)
DEBUG:__main__:verify failed. dup in row 2
DEBUG:__main__:Recall! Pop previous point, [2, 6, 8] @(5, 5)
DEBUG:__main__:Recall! Pop previous point, [1, 6] @(3, 6)
DEBUG:__main__:guessing next index: answer=6/[1, 6] @(3, 6)
DEBUG:__main__:current no. of fixed answers: 31
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 9]: [(7, 6), (6, 6), (5, 6), (1, 6), (3, 6), (3, 2)]
DEBUG:__main__:current no. of fixed answers: 34
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 6]: [(7, 6), (6, 6), (5, 6), (1, 6), (3, 6), (3, 2), (5, 5)]
DEBUG:__main__:current no. of fixed answers: 36
DEBUG:__main__:add to LIFO queue and guessing 4/[4, 6]: [(7, 6), (6, 6), (5, 6), (1, 6), (3, 6), (3, 2), (5, 5), (7, 5)]
DEBUG:__main__:verify failed. dup in row 1
DEBUG:__main__:Recall! Pop previous point, [4, 6] @(7, 5)
DEBUG:__main__:guessing next index: answer=6/[4, 6] @(7, 5)
DEBUG:__main__:verify failed. dup in col 0
DEBUG:__main__:Recall! Pop previous point, [4, 6] @(7, 5)
DEBUG:__main__:Recall! Pop previous point, [2, 6] @(5, 5)
DEBUG:__main__:guessing next index: answer=6/[2, 6] @(5, 5)
DEBUG:__main__:current no. of fixed answers: 36
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 4]: [(7, 6), (6, 6), (5, 6), (1, 6), (3, 6), (3, 2), (5, 5), (7, 5)]
DEBUG:__main__:verify failed. dup in row 1
DEBUG:__main__:Recall! Pop previous point, [2, 4] @(7, 5)
DEBUG:__main__:guessing next index: answer=4/[2, 4] @(7, 5)
DEBUG:__main__:verify failed. dup in row 1
DEBUG:__main__:Recall! Pop previous point, [2, 4] @(7, 5)
DEBUG:__main__:Recall! Pop previous point, [2, 6] @(5, 5)
DEBUG:__main__:Recall! Pop previous point, [2, 9] @(3, 2)
DEBUG:__main__:guessing next index: answer=9/[2, 9] @(3, 2)
DEBUG:__main__:current no. of fixed answers: 35
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 6]: [(7, 6), (6, 6), (5, 6), (1, 6), (3, 6), (3, 2), (4, 2)]
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [2, 6] @(4, 2)
DEBUG:__main__:guessing next index: answer=6/[2, 6] @(4, 2)
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [2, 6] @(4, 2)
DEBUG:__main__:Recall! Pop previous point, [2, 9] @(3, 2)
DEBUG:__main__:Recall! Pop previous point, [1, 6] @(3, 6)
DEBUG:__main__:Recall! Pop previous point, [1, 8] @(1, 6)
DEBUG:__main__:Recall! Pop previous point, [6, 8, 9] @(5, 6)
DEBUG:__main__:Recall! Pop previous point, [5, 9] @(6, 6)
DEBUG:__main__:guessing next index: answer=9/[5, 9] @(6, 6)
DEBUG:__main__:current no. of fixed answers: 25
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 3]: [(7, 6), (6, 6), (6, 1)]
DEBUG:__main__:current no. of fixed answers: 29
DEBUG:__main__:add to LIFO queue and guessing 4/[4, 6]: [(7, 6), (6, 6), (6, 1), (7, 1)]
DEBUG:__main__:verify failed. dup in row 3
DEBUG:__main__:Recall! Pop previous point, [4, 6] @(7, 1)
DEBUG:__main__:guessing next index: answer=6/[4, 6] @(7, 1)
DEBUG:__main__:verify failed. dup in row 4
DEBUG:__main__:Recall! Pop previous point, [4, 6] @(7, 1)
DEBUG:__main__:Recall! Pop previous point, [2, 3] @(6, 1)
DEBUG:__main__:guessing next index: answer=3/[2, 3] @(6, 1)
DEBUG:__main__:current no. of fixed answers: 26
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 4]: [(7, 6), (6, 6), (6, 1), (6, 5)]
DEBUG:__main__:verify failed. dup in row 1
DEBUG:__main__:Recall! Pop previous point, [2, 4] @(6, 5)
DEBUG:__main__:guessing next index: answer=4/[2, 4] @(6, 5)
DEBUG:__main__:current no. of fixed answers: 27
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 7]: [(7, 6), (6, 6), (6, 1), (6, 5), (6, 3)]
DEBUG:__main__:current no. of fixed answers: 33
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 4]: [(7, 6), (6, 6), (6, 1), (6, 5), (6, 3), (7, 1)]
DEBUG:__main__:current no. of fixed answers: 37
DEBUG:__main__:add to LIFO queue and guessing 1/[1, 4]: [(7, 6), (6, 6), (6, 1), (6, 5), (6, 3), (7, 1), (1, 1)]
DEBUG:__main__:verify failed. dup in row 1
DEBUG:__main__:Recall! Pop previous point, [1, 4] @(1, 1)
DEBUG:__main__:guessing next index: answer=4/[1, 4] @(1, 1)
DEBUG:__main__:current no. of fixed answers: 41
DEBUG:__main__:add to LIFO queue and guessing 1/[1, 8]: [(7, 6), (6, 6), (6, 1), (6, 5), (6, 3), (7, 1), (1, 1), (1, 6)]
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [1, 8] @(1, 6)
DEBUG:__main__:guessing next index: answer=8/[1, 8] @(1, 6)
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [1, 8] @(1, 6)
DEBUG:__main__:Recall! Pop previous point, [1, 4] @(1, 1)
DEBUG:__main__:Recall! Pop previous point, [2, 4] @(7, 1)
DEBUG:__main__:guessing next index: answer=4/[2, 4] @(7, 1)
DEBUG:__main__:current no. of fixed answers: 34
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 7]: [(7, 6), (6, 6), (6, 1), (6, 5), (6, 3), (7, 1), (7, 0)]
DEBUG:__main__:current no. of fixed answers: 37
DEBUG:__main__:add to LIFO queue and guessing 1/[1, 2]: [(7, 6), (6, 6), (6, 1), (6, 5), (6, 3), (7, 1), (7, 0), (1, 1)]
DEBUG:__main__:verify failed. dup in col 6
DEBUG:__main__:Recall! Pop previous point, [1, 2] @(1, 1)
DEBUG:__main__:guessing next index: answer=2/[1, 2] @(1, 1)
DEBUG:__main__:current no. of fixed answers: 42
DEBUG:__main__:add to LIFO queue and guessing 1/[1, 6]: [(7, 6), (6, 6), (6, 1), (6, 5), (6, 3), (7, 1), (7, 0), (1, 1), (0, 1)]
DEBUG:__main__:verify failed. dup in col 3
DEBUG:__main__:Recall! Pop previous point, [1, 6] @(0, 1)
DEBUG:__main__:guessing next index: answer=6/[1, 6] @(0, 1)
DEBUG:__main__:verify failed. dup in row 4
DEBUG:__main__:Recall! Pop previous point, [1, 6] @(0, 1)
DEBUG:__main__:Recall! Pop previous point, [1, 2] @(1, 1)
DEBUG:__main__:Recall! Pop previous point, [2, 7] @(7, 0)
DEBUG:__main__:guessing next index: answer=7/[2, 7] @(7, 0)
DEBUG:__main__:current no. of fixed answers: 37
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 8]: [(7, 6), (6, 6), (6, 1), (6, 5), (6, 3), (7, 1), (7, 0), (5, 1)]
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [2, 8] @(5, 1)
DEBUG:__main__:guessing next index: answer=8/[2, 8] @(5, 1)
DEBUG:__main__:current no. of fixed answers: 40
DEBUG:__main__:add to LIFO queue and guessing 4/[4, 9]: [(7, 6), (6, 6), (6, 1), (6, 5), (6, 3), (7, 1), (7, 0), (5, 1), (5, 0)]
DEBUG:__main__:verify failed. dup in col 3
DEBUG:__main__:Recall! Pop previous point, [4, 9] @(5, 0)
DEBUG:__main__:guessing next index: answer=9/[4, 9] @(5, 0)
DEBUG:__main__:verify failed. dup in col 3
DEBUG:__main__:Recall! Pop previous point, [4, 9] @(5, 0)
DEBUG:__main__:Recall! Pop previous point, [2, 8] @(5, 1)
DEBUG:__main__:Recall! Pop previous point, [2, 7] @(7, 0)
DEBUG:__main__:Recall! Pop previous point, [2, 4] @(7, 1)
DEBUG:__main__:Recall! Pop previous point, [2, 7] @(6, 3)
DEBUG:__main__:guessing next index: answer=7/[2, 7] @(6, 3)
DEBUG:__main__:verify failed. dup in row 1
DEBUG:__main__:Recall! Pop previous point, [2, 7] @(6, 3)
DEBUG:__main__:Recall! Pop previous point, [2, 4] @(6, 5)
DEBUG:__main__:Recall! Pop previous point, [2, 3] @(6, 1)
DEBUG:__main__:Recall! Pop previous point, [5, 9] @(6, 6)
DEBUG:__main__:Recall! Pop previous point, [3, 9] @(7, 6)
DEBUG:__main__:guessing next index: answer=9/[3, 9] @(7, 6)
DEBUG:__main__:current no. of fixed answers: 22
DEBUG:__main__:add to LIFO queue and guessing 3/[3, 5]: [(7, 6), (6, 6)]
DEBUG:__main__:current no. of fixed answers: 24
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 4]: [(7, 6), (6, 6), (6, 1)]
DEBUG:__main__:current no. of fixed answers: 27
DEBUG:__main__:add to LIFO queue and guessing 4/[4, 9]: [(7, 6), (6, 6), (6, 1), (6, 3)]
DEBUG:__main__:current no. of fixed answers: 29
DEBUG:__main__:add to LIFO queue and guessing 3/[3, 8]: [(7, 6), (6, 6), (6, 1), (6, 3), (2, 3)]
DEBUG:__main__:current no. of fixed answers: 32
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 8, 9]: [(7, 6), (6, 6), (6, 1), (6, 3), (2, 3), (3, 3)]
DEBUG:__main__:verify failed. dup in row 1
DEBUG:__main__:Recall! Pop previous point, [2, 8, 9] @(3, 3)
DEBUG:__main__:guessing next index: answer=8/[2, 8, 9] @(3, 3)
DEBUG:__main__:verify failed. dup in row 2
DEBUG:__main__:Recall! Pop previous point, [2, 8, 9] @(3, 3)
DEBUG:__main__:guessing next index: answer=9/[2, 8, 9] @(3, 3)
DEBUG:__main__:current no. of fixed answers: 33
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 8]: [(7, 6), (6, 6), (6, 1), (6, 3), (2, 3), (3, 3), (4, 3)]
DEBUG:__main__:verify failed. dup in row 3
DEBUG:__main__:Recall! Pop previous point, [2, 8] @(4, 3)
DEBUG:__main__:guessing next index: answer=8/[2, 8] @(4, 3)
DEBUG:__main__:verify failed. dup in row 2
DEBUG:__main__:Recall! Pop previous point, [2, 8] @(4, 3)
DEBUG:__main__:Recall! Pop previous point, [2, 8, 9] @(3, 3)
DEBUG:__main__:Recall! Pop previous point, [3, 8] @(2, 3)
DEBUG:__main__:guessing next index: answer=8/[3, 8] @(2, 3)
DEBUG:__main__:current no. of fixed answers: 30
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 3, 9]: [(7, 6), (6, 6), (6, 1), (6, 3), (2, 3), (4, 3)]
DEBUG:__main__:verify failed. dup in row 2
DEBUG:__main__:Recall! Pop previous point, [2, 3, 9] @(4, 3)
DEBUG:__main__:guessing next index: answer=3/[2, 3, 9] @(4, 3)
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [2, 3, 9] @(4, 3)
DEBUG:__main__:guessing next index: answer=9/[2, 3, 9] @(4, 3)
DEBUG:__main__:current no. of fixed answers: 31
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 3]: [(7, 6), (6, 6), (6, 1), (6, 3), (2, 3), (4, 3), (3, 3)]
DEBUG:__main__:verify failed. dup in row 1
DEBUG:__main__:Recall! Pop previous point, [2, 3] @(3, 3)
DEBUG:__main__:guessing next index: answer=3/[2, 3] @(3, 3)
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [2, 3] @(3, 3)
DEBUG:__main__:Recall! Pop previous point, [2, 3, 9] @(4, 3)
DEBUG:__main__:Recall! Pop previous point, [3, 8] @(2, 3)
DEBUG:__main__:Recall! Pop previous point, [4, 9] @(6, 3)
DEBUG:__main__:guessing next index: answer=9/[4, 9] @(6, 3)
DEBUG:__main__:current no. of fixed answers: 31
DEBUG:__main__:add to LIFO queue and guessing 2/[2, 3, 8]: [(7, 6), (6, 6), (6, 1), (6, 3), (4, 3)]
DEBUG:__main__:current no. of fixed answers: 32
DEBUG:__main__:add to LIFO queue and guessing 3/[3, 8]: [(7, 6), (6, 6), (6, 1), (6, 3), (4, 3), (3, 3)]
DEBUG:__main__:current no. of fixed answers: 34
DEBUG:__main__:add to LIFO queue and guessing 5/[5, 6]: [(7, 6), (6, 6), (6, 1), (6, 3), (4, 3), (3, 3), (2, 2)]
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [5, 6] @(2, 2)
DEBUG:__main__:guessing next index: answer=6/[5, 6] @(2, 2)
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [5, 6] @(2, 2)
DEBUG:__main__:Recall! Pop previous point, [3, 8] @(3, 3)
DEBUG:__main__:guessing next index: answer=8/[3, 8] @(3, 3)
DEBUG:__main__:current no. of fixed answers: 40
DEBUG:__main__:add to LIFO queue and guessing 3/[3, 4]: [(7, 6), (6, 6), (6, 1), (6, 3), (4, 3), (3, 3), (7, 1)]
DEBUG:__main__:current no. of fixed answers: 43
DEBUG:__main__:add to LIFO queue and guessing 1/[1, 6]: [(7, 6), (6, 6), (6, 1), (6, 3), (4, 3), (3, 3), (7, 1), (3, 6)]
DEBUG:__main__:verify failed. dup in row 3
DEBUG:__main__:Recall! Pop previous point, [1, 6] @(3, 6)
DEBUG:__main__:guessing next index: answer=6/[1, 6] @(3, 6)
DEBUG:__main__:current no. of fixed answers: 44
DEBUG:__main__:add to LIFO queue and guessing 5/[5, 8]: [(7, 6), (6, 6), (6, 1), (6, 3), (4, 3), (3, 3), (7, 1), (3, 6), (5, 6)]
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [5, 8] @(5, 6)
DEBUG:__main__:guessing next index: answer=8/[5, 8] @(5, 6)
DEBUG:__main__:verify failed. dup in row 0
DEBUG:__main__:Recall! Pop previous point, [5, 8] @(5, 6)
DEBUG:__main__:Recall! Pop previous point, [1, 6] @(3, 6)
DEBUG:__main__:Recall! Pop previous point, [3, 4] @(7, 1)
DEBUG:__main__:guessing next index: answer=4/[3, 4] @(7, 1)
DEBUG:__main__:verify failed. dup in row 3
DEBUG:__main__:Recall! Pop previous point, [3, 4] @(7, 1)
DEBUG:__main__:Recall! Pop previous point, [3, 8] @(3, 3)
DEBUG:__main__:Recall! Pop previous point, [2, 3, 8] @(4, 3)
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
完成，猜测了109次
[[8 1 2 7 5 3 6 4 9]
 [9 4 3 6 8 2 1 7 5]
 [6 7 5 4 9 1 2 8 3]
 [1 5 4 2 3 7 8 9 6]
 [3 6 9 8 4 5 7 2 1]
 [2 8 7 1 6 9 5 3 4]
 [5 2 1 9 7 4 3 6 8]
 [4 3 8 5 2 6 9 1 7]
 [7 9 6 3 1 8 4 5 2]]
耗时：0.559s

Process finished with exit code 0

```



