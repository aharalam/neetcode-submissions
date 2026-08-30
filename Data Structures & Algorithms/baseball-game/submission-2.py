class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        record_sum = 0

        for i in range(len(operations)):
            if operations[i] == "+":
                record.append(record[-1] + record[-2])
                record_sum += record[-1]
            elif operations[i] == "D":
                record.append(2 * record[-1])
                record_sum += 2 * record[-1]
            elif operations[i] == "C":
                record_sum -= record.pop()
            else:
                record.append(int(operations[i]))
                record_sum += record[-1]
        print(record)
        
        return sum(record)
