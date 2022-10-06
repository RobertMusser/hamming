

# encode a message with the proper pairity bits
# TODO currently messages are size 11
def encode(message):
    message = [int(i) for i in list(message)]
    code = list("xxx") + message
    code.insert(4, "x")
    code.insert(8, "x")
    code.insert(16, "x")
    # now code is padded so indices are constant
    odd_col_i    = [9,  17, 3,  11, 19, 5,  13, 21, 7,  15]
    w2_col_i     = [3,  10, 11, 18, 19, 6,  7,  14, 15, 22]
    right_half_i = [5,  6,  7,  12, 13, 14, 15, 20, 21, 22]
    mid_row_i    = [9,  10, 11, 12, 13, 14, 15]
    bottom_row_i = [17, 18, 19, 20, 21, 22]
    # set odd col pairity bit
    odd_col = []
    for i in odd_col_i:
        odd_col.append(code[i])
    code[1] = 1 if odd_col.count(1) % 2 else code[1] = 0



    # TODO here
    # set odd col pairity bit
    right_half_count = 0 # number of 1s in the odd cols
    for i in right_half:
        right_half_count += code[i]
    if right_half_count % 2:
        code[2] = 1
    else:
        code[2] = 0
    # set odd col pairity bit
    even_rows_count = 0 # number of 1s in the odd cols
    for i in even_rows:
        even_rows_count += code[i]
    if even_rows_count % 2:
        code[4] = 1
    else:
        code[4] = 0
    # set bottom half pairity bit
    bottom_half_count = 0 # number of 1s in the odd cols
    for i in bottom_half:
        bottom_half_count += code[i]
    if bottom_half_count % 2:
        code[8] = 1
    else:
        code[8] = 0
    # set total pairity bit
    total_count = 0
    for bit in code:
        if bit != "x":
            total_count += bit
    if total_count % 2:
        code[0] = 1
    else:
        code[0] = 0
    return code

# decode a message. Return correcred message, unchanged message if no errors, and False 
# if there's more than 1 error
# Stolen from: https://www.youtube.com/watch?v=b3NxrZOu_CE&t=0s
def decode(code):
	# xor all every index holding a 1
	loc = my_reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(code) if bit])
	# no error
	if loc == 0:
		message = [code[3]] + code[5:8] + code[9:16]
		return message
	else:
		# fix single error 
		code[loc] = int(not code[loc])
		# now check for multiple errors
		count = 0
		for bit in code:
			count += int(bit)
		if count % 2:
			# 2 or more errors, we got nothing
			return False
		message = [code[3]] + code[5:8] + code[9:16]
		return message

# given list (listy), reduces the list with the 2 arg function (func)
# functools reduce is much more robust, but can't import on the pi...
def my_reduce(func, listy):
    safe_list = listy.copy()
    total = func(safe_list.pop(0), safe_list.pop(0))
    for elem in safe_list:
        total = func(total, elem)
    return total

msg = list("11100110001")
msg = encode(msg)
msg[10] = int(not msg[10])
print(msg)
print(decode(msg))

