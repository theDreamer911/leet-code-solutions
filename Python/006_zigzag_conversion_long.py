class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        row_map = {row: "" for row in range(1, numRows+1)}
        # print(row_map)

        row = 1
        up = True

        for letter in s:
            row_map[row] += letter
            if (row == 1) or ((row < numRows) and up):
                row += 1
                up = True
                # print(up, row, letter)
            else:
                row -= 1
                up = False
                # print(up, row, letter)

        converted = ""

        # print(s) # PAYPALISHIRING
        # print(s)  # G
        print(row_map)  # {1: 'PAHN', 2: 'APLSIIG', 3: 'YIR'}

        for row in range(1, numRows+1):
            converted += row_map[row]

        return converted

    print(convert("", s="PAYPALISHIRING", numRows=3))
    # print(convert("", s="PAYPALISHIRING", numRows=4))
    # print(convert("", s="ABCDEFGH", numRows=3))
    # print(convert("", s="ABCDE FGH", numRows=3))
