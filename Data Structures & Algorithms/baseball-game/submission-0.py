class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        finalscore = 0

        for i in range(len(operations)):
            if operations[i] == '+':
                first = record.pop()
                second = record[-1]
                record.append(first)
                record.append(first+second)
            elif operations[i] == 'D':
                first = record[-1]
                record.append(first * 2)
            elif operations[i] == 'C':
                record.pop()
            else:
                record.append(int(operations[i]))

        return sum(record)