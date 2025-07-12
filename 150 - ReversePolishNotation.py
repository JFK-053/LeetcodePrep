import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}
        result = int(tokens[0])
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operators:
                result = operators[tokens[i]](stack.pop(-2), stack.pop(-1))
                if tokens[i] == "/":
                    result = int(result)
                stack.append(result)
            else:
                stack.append(int(tokens[i]))


        return result