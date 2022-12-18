class Solution:
    def convert(self, s: str, numRows: int) -> str:
        m, li = [''] * numRows, list(range(numRows)) + \
            list(range(numRows-2, 0, -1))
        for ind, ch in enumerate(s):
            m[li[ind % (numRows*2-2) if not numRows*2-2 == 0 else 0]] += ch
        return "".join(m)
