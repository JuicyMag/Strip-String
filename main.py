#this program will consume a string and strip out a specified chunk of that string and return that chunk.

#use case - enter a string with a message and url and url takes user to child pornography - want to remove that harmful https link.
# input = "hi I'm not malicious go to https://www.notporn.com"
# return_string = "hi I'm not malicious go to "
keyword = "https"
input_text ="hi I'm not malicious go to https://www.somethingmalicious.com"
def slice_URL_position(input_text, text_to_strip):
    sliced_string = " "
    if text_to_strip in input_text:
        sliced_string = input_text.index(text_to_strip)
    return  sliced_string
# print(input_text[slice_URL_position(input_text, 'https'):])
b = input_text.replace(input_text[slice_URL_position(input_text,'https'):], "<CENSORED CONTENT>")
print(b)