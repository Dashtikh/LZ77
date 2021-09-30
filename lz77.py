# module for lz77 decoder and encoder

# decoder function
def decoder77(code):
    code = code.replace("<", "")
    code = code.replace(">", "")
    code = code.replace(",", "")
    decode = ""
    counter = 0

    start = 0

    while counter < len(code):
        if code[counter] == "0":
            decode = decode + code[counter + 2]
            counter = counter + 3
        else:
            for letter in range(0, int(code[counter + 1])):
                start = (-1) * int(code[counter])
                decode = decode + decode[start]
            decode = decode + code[counter + 2]
            counter = counter + 3

    return decode
