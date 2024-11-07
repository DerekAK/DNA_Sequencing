def runAlgorithm(t, s):
    matrix_row = [0]*len(s)
    max_number = 0
    max_number_row = 0

    for row in range(len(t)):
        upper_left = 0
        for col in range(len(s)):
            saved_value = matrix_row[col]
            if t[row] == s[col]:
                matrix_row[col] = 1 + upper_left
                if matrix_row[col] > max_number:
                    max_number = matrix_row[col]
                    max_number_row = row
            else: 
                matrix_row[col] = 0
            upper_left = saved_value
    substring_start = max_number_row - max_number + 1

    return len((t[substring_start : max_number_row + 1]))