class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations = []

        for op in logs:
            # Going to new folder
            if op[-2].isalnum() and op[-1] == '/':
                operations.append(op)
            if op[-3:] == "../":
                if not operations:
                    continue
                else:
                    operations.pop()
        
        return len(operations)