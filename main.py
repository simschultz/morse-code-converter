from morse_code import morse_code_src


morse_code_string = ''
my_string = input("Please type a string to convert to morse code: ")
for x in my_string:
    morse_code_string += morse_code_src[x]
    morse_code_string += ' '
print(morse_code_string)