class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        record_sum = 0

        print("operations:", operations)

        for i in range(len(operations)):
            # If the operation is a +:
            if operations[i] == "+":
                record.append(record[-2] + record[-1])
                record_sum += record[-1]
            # If the operation is a D:
            elif operations[i] == "D":
                record.append(2 * record[-1])
                record_sum += record[-1]
            elif operations[i] == "C":
                record_sum -= record.pop()
            # If the operation is an integer:
            else:
                record.append(int(operations[i]))
                record_sum += record[-1]
            
        print("record_sum:", record_sum)

        return record_sum
