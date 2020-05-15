# FORMATING
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
x = 'var'
print(f'kek {x}')

price = 49
txt = "The price is {1:.2f} dollars, {0}"

print(txt.format(price, 2))

txt = "The price is {:.2f} dollars, {}"
print(txt.format(price, 2))

b = "Hello, World!"
print(b[2:5])  # cutting the strings

print(b[-5:-2])  # cutting the strings with negative index ???

a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

txt = "The rain in Spain stays mainly in the plain"
x = "plain" in txt
out = "{} is in the string : {}"
print(out.format("plain", x))

print('quot "heh" ')

print('ALL_UPPER'.isupper())  # returns true

print('not_all_UPPER'.isupper())
print(len('str'))  # 3

print("string".index("tr"))  # 3

try:
    print("string".index("zzz"))  # 3
except:
    print("returned error when idex is not found")

print('Roma'.replace('Roma', 'Rita'))


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


## backward each workd
def backward_string_by_word(text: str) -> str:
    if len(text) == 0:
        return text

    words = text.split(' ')
    result_words = [word[::-1] for word in words]

    return ' '.join(result_words)


# These "asserts" are used for self-checking and not for an auto-testing
assert backward_string_by_word('') == ''
assert backward_string_by_word('world') == 'dlrow'
assert backward_string_by_word('hello world') == 'olleh dlrow'
assert backward_string_by_word('hello   world') == 'olleh   dlrow'
assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
print("Coding complete? Click 'Check' to earn cool rewards!")

print('1'<'0')