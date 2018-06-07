# coding:utf-8
# python3
# original: u"杨仕航"
# modified: @kevinqqnj
import logging

import numpy as np
from queue import Queue, LifoQueue
import time
import copy


class Record:
    point = None  # 进行猜测的点
    point_index = 0  # 猜测候选列表使用的值的索引
    value = None  # 回溯记录的值


class Sudo:
    def __init__(self, _data):
        # 数据初始化(二维的object数组)
        self.value = np.array([[0] * 9] * 9, dtype=object)  # 数独的值，包括未解决和已解决的
        self.new_points = Queue()  # 先进先出，新解（已解决值）的坐标
        self.record_queue = LifoQueue()  # 先进后出，回溯器
        self.guess_times = 0  # 猜测次数

        # 九宫格的基准列表
        self.base_points = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

        # 整理数据
        self.puzzle = np.array(_data).reshape(9, -1)
        for r in range(0, 9):
            for c in range(0, 9):
                if self.puzzle[r, c]:  # if not Zero
                    # numpy default is int32, convert to int
                    self.value[r, c] = int(self.puzzle[r, c])
                    # 新的确认的值添加到列表中，以便遍历
                    self.new_points.put((r, c))
                    # logger.debug(f'init: answer={self.value[r, c]} at {(r, c)}')
                else:  # if Zero, guess no. is 1-9
                    self.value[r, c] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 剔除数字
    def _cut_num(self, point):
        r, c = point
        val = self.value[r, c]

        # 行
        for i, item in enumerate(self.value[r]):
            if isinstance(item, list):
                if item.count(val):
                    item.remove(val)

                    # 判断移除后，是否剩下一个元素
                    if len(item) == 1:
                        self.new_points.put((r, i))  # 添加坐标到“已解决”列表
                        logger.debug(f'only one in row: answer={self.value[r, i]} at {(r, i)}')
                        self.value[r, i] = item[0]

        # 列
        for i, item in enumerate(self.value[:, c]):
            if isinstance(item, list):
                if item.count(val):
                    item.remove(val)

                    # 判断移除后，是否剩下一个元素
                    if len(item) == 1:
                        self.new_points.put((i, c))
                        logger.debug(f'only one in col: answer={self.value[i, c]} at {(i, c)}')
                        self.value[i, c] = item[0]

        # 所在九宫格(3x3的数组)
        b_r, b_c = map(lambda x: x // 3 * 3, point)  # 九宫格基准点
        for m_r, row in enumerate(self.value[b_r:b_r + 3, b_c:b_c + 3]):
            for m_c, item in enumerate(row):
                if isinstance(item, list):
                    if item.count(val):
                        item.remove(val)

                        # 判断移除后，是否剩下一个元素
                        if len(item) == 1:
                            r = b_r + m_r
                            c = b_c + m_c
                            self.new_points.put((r, c))
                            logger.debug(f'only one in block: answer={self.value[r, c]} at {(r, c)}')
                            self.value[r, c] = item[0]

    # 同一行、列或九宫格中, List里，可能性只有一个的情况
    def _check_one_possbile(self):
        # 同一行只有一个数字的情况
        for r in range(0, 9):
            # 只取出是这一行是List的格子
            values = list(filter(lambda x: isinstance(x, list), self.value[r]))

            for c, item in enumerate(self.value[r]):
                if isinstance(item, list):
                    for value in item:
                        if sum(map(lambda x: x.count(value), values)) == 1:
                            self.value[r, c] = value
                            self.new_points.put((r, c))
                            logger.debug(f'list val is only one in row: answer={self.value[r, c]} at {(r, c)}')
                            return True

        # 同一列只有一个数字的情况
        for c in range(0, 9):
            values = list(filter(lambda x: isinstance(x, list), self.value[:, c]))

            for r, item in enumerate(self.value[:, c]):
                if isinstance(item, list):
                    for value in item:
                        if sum(map(lambda x: x.count(value), values)) == 1:
                            self.value[r, c] = value
                            self.new_points.put((r, c))
                            logger.debug(f'list val is only one in col: answer={self.value[r, c]} at {(r, c)}')
                            return True

        # 九宫格内的单元格只有一个数字的情况
        for r, c in self.base_points:
            # reshape: 3x3 改为1维数组
            values = list(filter(lambda x: isinstance(x, list), self.value[r:r + 3, c:c + 3].reshape(1, -1)[0]))

            for m_r, row in enumerate(self.value[r:r + 3, c:c + 3]):
                for m_c, item in enumerate(row):
                    if isinstance(item, list):
                        for value in item:
                            if sum(map(lambda x: x.count(value), values)) == 1:
                                self.value[r + m_r, c + m_c] = value
                                self.new_points.put((r + m_r, c + m_c))
                                logger.debug(f'list val is only one in block: answer={self.value[r + m_r, c +m_c]} at '
                                             f'{(r + m_r, c +m_c)}')
                                return True

    # 同一个九宫格内数字在同一行或同一列处理(同行列隐性排除)
    def _check_same_num(self):
        for b_r, b_c in self.base_points:
            block = self.value[b_r:b_r + 3, b_c:b_c + 3]

            # 判断数字1~9在该九宫格的分布情况
            _data = block.reshape(1, -1)[0]
            for i in range(1, 10):
                result = map(lambda x: 0 if not isinstance(x[1], list) else x[0] + 1 if x[1].count(i) else 0,
                             enumerate(_data))
                result = list(filter(lambda x: x > 0, result))
                r_count = len(result)

                if r_count in [2, 3]:
                    # 2或3个元素才有可能同一行或同一列
                    rows = list(map(lambda x: (x - 1) // 3, result))
                    cols = list(map(lambda x: (x - 1) % 3, result))

                    if len(set(rows)) == 1:
                        # 同一行，去掉其他行的数字
                        result = list(map(lambda x: b_c + (x - 1) % 3, result))
                        row = b_r + rows[0]

                        for col in range(0, 9):
                            if col not in result:
                                item = self.value[row, col]
                                if isinstance(item, list):
                                    if item.count(i):
                                        item.remove(i)

                                        # 判断移除后，是否剩下一个元素
                                        if len(item) == 1:
                                            self.new_points.put((row, col))
                                            logger.debug(f'block compare row: answer={self.value[row, col]} at {(row, col)}')
                                            self.value[row, col] = item[0]
                                            return True

                    elif len(set(cols)) == 1:
                        # 同一列
                        result = list(map(lambda x: b_r + (x - 1) // 3, result))
                        col = b_c + cols[0]

                        for row in range(0, 9):
                            if row not in result:
                                item = self.value[row, col]
                                if isinstance(item, list):
                                    if item.count(i):
                                        item.remove(i)

                                        # 判断移除后，是否剩下一个元素
                                        if len(item) == 1:
                                            self.new_points.put((row, col))
                                            logger.debug(f'block compare col: answer={self.value[row, col]} at {(row, col)}')
                                            self.value[row, col] = item[0]
                                            return True

    # 排除法解题
    def sudo_exclude(self):
        is_run_same = True
        is_run_one = True

        while is_run_same:
            while is_run_one:
                # 剔除数字
                while not self.new_points.empty():
                    point = self.new_points.get()  # 先进先出
                    self._cut_num(point)

                # 检查List里值为单个数字的情况，如有新answer则加入new_points Queue，立即_cut_num
                is_run_one = self._check_one_possbile()

            # 检查同行或列的情况
            is_run_same = self._check_same_num()
            is_run_one = True

    # 得到有多少个确定的数字
    def get_num_count(self):
        return sum(map(lambda x: 1 if isinstance(x, int) else 0, self.value.reshape(1, -1)[0]))

    # 评分，找到最佳的猜测坐标
    def get_best_point(self):
        best_score = 0
        best_point = (0, 0)

        for r, row in enumerate(self.value):
            for c, item in enumerate(row):
                point_score = self._get_point_score((r, c))
                if best_score < point_score:
                    best_score = point_score
                    best_point = (r, c)
        return best_point

    # 计算某坐标的评分
    def _get_point_score(self, point):
        # 评分标准 (10-候选个数) + 同行确定数字个数 + 同列确定数字个数
        r, c = point
        item = self.value[r, c]

        if isinstance(item, list):
            score = 10 - len(item)
            score += sum(map(lambda x: 1 if isinstance(x, int) else 0, self.value[r]))
            score += sum(map(lambda x: 1 if isinstance(x, int) else 0, self.value[:, c]))
            return score
        else:
            return 0

    # 验证有没错误
    def verify_value(self):
        # 行
        r = 0
        for row in self.value:
            nums = []
            lists = []
            for item in row:
                (lists if isinstance(item, list) else nums).append(item)
            if len(set(nums)) != len(nums):
                # logger.error(f'verify failed. dup in row {r}')
                logger.debug(f'verify failed. dup in row {r}')
                return False  # 数字要不重复
            if len(list(filter(lambda x: len(x) == 0, lists))):
                return False  # 候选列表不能为空集
            r += 1

        # 列
        for c in range(0, 9):
            nums = []
            lists = []
            col = self.value[:, c]

            for item in col:
                (lists if isinstance(item, list) else nums).append(item)
            if len(set(nums)) != len(nums):
                logger.debug(f'verify failed. dup in col {c}')
                return False  # 数字要不重复
            if len(list(filter(lambda x: len(x) == 0, lists))):
                return False  # 候选列表不能为空集

        # 九宫格
        for b_r, b_c in self.base_points:
            nums = []
            lists = []
            block = self.value[b_r:b_r + 3, b_c:b_c + 3].reshape(1, -1)[0]

            for item in block:
                (lists if isinstance(item, list) else nums).append(item)
            if len(set(nums)) != len(nums):
                logger.debug(f'verify failed. dup in block {b_r, b_c}')
                return False  # 数字要不重复
            if len(list(filter(lambda x: len(x) == 0, lists))):
                return False  # 候选列表不能为空集
        return True

    def add_to_queue(self, point, index):
        record = Record()
        record.point = point
        record.point_index = index
        # recorder.value = self.value.copy() #numpy的copy不行
        record.value = copy.deepcopy(self.value)
        self.record_queue.put(record)
        items = self.value[point]
        self.value[point] = items[index]
        self.new_points.put(point)
        return items

    def sudo_solve_iter(self):
        # 排除法解题
        self.sudo_exclude()
        # logger.debug(f'excluded, current result:\n{self.value}')
        if self.verify_value():
            if self.get_num_count() == 81:
                # solve success
                return
            else:
                logger.info(f'current no. of fixed answers: {self.get_num_count()}')
                point = self.get_best_point()
                index = 0
                items = self.add_to_queue(point, index)
                logger.info(f'add to LIFO queue and guessing {items[index]}/{items}: '
                             f'{[x.point for x in self.record_queue.queue]}')
                self.guess_times += 1
                return self.sudo_solve_iter()
        while True:
            if self.record_queue.empty():
                # raise Exception('Sudo is wrong, no answer!')
                logger.error(f'Guessed {self.guess_times} times. Sudo is wrong, no answer!')
                exit()
            # check value ERROR, need to try next index or rollback
            record = self.record_queue.get()
            point = record.point
            index = record.point_index + 1
            items = record.value[point]
            self.value = record.value
            logger.info(f'Recall! Pop previous point, {items} @{point}')
            # 判断索引是否超出范围
            # if not exceed，则再回溯一次
            if index < len(items):
                items = self.add_to_queue(point, index)
                logger.info(f'guessing next index: answer={items[index]}/{items} @{point}')
                self.guess_times += 1
                return self.sudo_solve_iter()


if __name__ == '__main__':
    # 数独题目 http://cn.sudokupuzzle.org/
    # data[0]: 号称最难的数独
    data = [[8, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 3, 6, 0, 0, 0, 0, 0,
             0, 7, 0, 0, 9, 0, 2, 0, 0,
             0, 5, 0, 0, 0, 7, 0, 0, 0,
             0, 0, 0, 0, 4, 5, 7, 0, 0,
             0, 0, 0, 1, 0, 0, 0, 3, 0,
             0, 0, 1, 0, 0, 0, 0, 6, 8,
             0, 0, 8, 5, 0, 0, 0, 1, 0,
             0, 9, 0, 0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 5, 0, 2, 0, 0,
             0, 9, 0, 0, 0, 0, 0, 4, 0,
             0, 0, 0, 0, 1, 0, 0, 0, 0,
             0, 0, 0, 4, 0, 6, 0, 8, 0,
             0, 0, 7, 0, 0, 0, 1, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 8, 0, 9, 4,
             2, 0, 1, 0, 7, 0, 0, 0, 0,
             0, 0, 5, 0, 0, 0, 0, 0, 0]]
    # DEBUG INFO WARNING ERROR CRITICAL
    logging.basicConfig(level=logging.WARN,
                        format='%(asctime)s %(levelname)s %(message)s')
                        # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)-7s %(message)s')
    logger = logging.getLogger(__name__)
    # try:
    t1 = time.time()
    puzzle = data[0]
    sudo = Sudo(puzzle)
    sudo.sudo_solve_iter()

    logger.warning(f'Done! guessed {sudo.guess_times} times, in {time.time() - t1:.3f}sec')
    logger.warning(f'Puzzle:\n{sudo.puzzle}\nAnswer:\n{sudo.value}')

    # except:
    #     logger.error(f'ERROR: {sudo.value}', exc_info=True)
