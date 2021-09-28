code = input("please insert a coded string: ")
code = code.replace("<", "")
code = code.replace(">", "")
code = code.replace(",", "")
decode = ""
counter = 0
start = 0
end = 0
while counter < len(code):
    if code[counter] == "0":
        decode = decode + code[counter + 2]
        counter = counter + 3
    else:
        start = (-1) * int(code[counter])
        end = start + int(code[counter + 1])
        decode = decode + decode[start:end] + code[counter + 2]
        counter = counter + 3

print(decode)
