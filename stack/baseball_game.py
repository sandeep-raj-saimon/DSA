class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr =[]

        for operation in operations:
            if (operation == '+'):
                a = arr.pop()
                b = arr.pop()
                c = int(a) + int(b)
                arr.append(b)
                arr.append(a)
                arr.append(c)
            elif (operation == 'C'):
                arr.pop()
            elif (operation == 'D'):
                a = int(arr.pop())
                b = a*2
                arr.append(a)
                arr.append(b)
            else:
                arr.append(int(operation))
        return sum(arr)