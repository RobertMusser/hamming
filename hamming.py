
# encode a message with the proper pairity bits
# TODO currently messages are size 16
def pairty_11_bits(message):
    message = list(message)
    code = list("xxx") + message
    code.insert(4, "x")
    code.insert(8, "x")
    odd_col     = [1, 3, 5, 7, 9, 11, 13, 15]
    right_half  = [2, 3, 6, 7, 10, 11, 14, 15]
    even_rows   = [4, 5, 6, 7, 12, 13, 14, 15]
    bottom_half = [8, 9, 10, 11, 12, 13, 14, 15]
    # set odd col pairity bit
    odd_col_count = 0 # number of 1s in the odd cols
    for i in odd_col:
        odd_col_count += code[i]
    if odd_col_count % 2:
        code[1] = 0
    else:
        code[1] = 1
    # set odd col pairity bit
    right_half_count = 0 # number of 1s in the odd cols
    for i in right_half:
        right_half_count += code[i]
    if right_half_count % 2:
        code[2] = 0
    else:
        code[2] = 1
    # set odd col pairity bit
    even_rows_count = 0 # number of 1s in the odd cols
    for i in even_rows:
        even_rows_count += code[i]
    if even_rows_count % 2:
        code[4] = 0
    else:
        code[4] = 1
    # set bottom half pairity bit
    bottom_half_count = 0 # number of 1s in the odd cols
    for i in bottom_half:
        bottom_half_count += code[i]
    if bottom_half_count % 2:
        code[8] = 0
    else:
        code[8] = 1
    # set total pairity bit
    total_count = 0
    for bit in code:
        if bit != "x":
            total_count += bit

    return code

# decode a message. Return correcred message, unchanged message if no errors, and False 
# if there's more than 1 error
def decode(code):
    return 0

print(pairty_11_bits("00011001101"))

