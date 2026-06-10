class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []
        operations = {"+", "-", "/", "*"}
        for c in tokens:
            if c in operations:
                right = q.pop()
                left = q.pop()
                if c == "+":
                    q.append(left + right)
                elif c == "-":
                    q.append(left - right)
                elif c == "/":
                    q.append(int(left / right))
                else:
                    q.append(left * right)
            else:
                q.append(int(c))
        return q[-1]
