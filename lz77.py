# module for lz77 decoder and encoder


# encoder function
def encoder77(sentence):

    search_Buffer = ""
    code = ""
    counter = -2

    while len(sentence) > 0:
        if sentence[-1 * len(sentence)] not in search_Buffer:
            search_Buffer = search_Buffer + sentence[0]
            code = code + "00" + sentence[-1 * len(sentence)]
            sentence = sentence[1:]
        else:
            if sentence in search_Buffer:
                code = code + str(-1 * ((search_Buffer[::-1].find(sentence[::-1])) - len(search_Buffer))) + str(
                    len(sentence) - 1)
                search_Buffer = search_Buffer + sentence
                sentence = ""
            elif sentence[-1 * len(sentence):-1] in search_Buffer:
                substr = sentence[:-1]
                startindex = len(search_Buffer) - search_Buffer.rfind(substr)
                length = len(substr)
                added = sentence[-1]
                code = code + str(startindex) + str(length) + added
                search_Buffer = search_Buffer + sentence[:-1]
                sentence = ""
            else:
                while counter > (-1 * len(sentence)):
                    if sentence[-1 * len(sentence):counter] in search_Buffer:
                        substr = sentence[:counter]
                        startindex = len(search_Buffer) - search_Buffer.rfind(substr)
                        length = len(substr)
                        added = sentence[counter]
                        code = code + str(startindex) + str(length) + added
                        search_Buffer = search_Buffer + sentence[:counter + 1]
                        sentence = sentence[counter + 1:]
                        counter = - 2
                        break
                    else:
                        counter = counter - 1

    return code


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
