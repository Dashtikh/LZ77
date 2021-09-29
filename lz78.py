# module for lz78 decoder and encoder
# decoder function
def decoder78(code):
    code = code.replace("<", "")
    code = code.replace(">", "")
    code = code.replace(",", "")
    decode = ""
    counter = 0
    decode = [""]
    decodestring = ""
    start = 0

    while counter < len(code):
        if code[counter] == "0":
            decode.append(code[counter + 1])
            counter = counter + 2
        else:
            decode.append(decode[int(code[counter])] + code[counter + 1])
            counter = counter + 2
    for letter in decode:
        decodestring = decodestring + letter
    return decodestring
