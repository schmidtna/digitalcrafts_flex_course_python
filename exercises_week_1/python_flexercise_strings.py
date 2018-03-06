# caps and uppers ex 1, 2, 3

def string_mods():
    test_string = ("let's do some stuff!")
   

    print(test_string.upper())
    print(test_string.capitalize())
    print(test_string[-1: 0: -1])

# string_mods()

# leet speak conversion

def lt_spk():

    test_str = ("Hello world, in leet speak!")
    test_str = test_str.lower()

    test_str = test_str.replace("a", "4")
    test_str = test_str.replace("e", "3")
    test_str = test_str.replace("g", "6")
    test_str = test_str.replace("i", "1")
    test_str = test_str.replace("o", "0")
    test_str = test_str.replace("s", "5")
    test_str = test_str.replace("t", "7")
    
    
    print(test_str.capitalize())

# lt_spk()

# long vowe swaps
def char_swaps():
    long_vowels = ("A good cheese doesn't need a spoon.")

    long_vowels = long_vowels.replace("aa", "aaaaa")
    long_vowels = long_vowels.replace("ee", "eeeee")
    long_vowels = long_vowels.replace("ii", "iiiii")
    long_vowels = long_vowels.replace("oo", "ooooo")
    long_vowels = long_vowels.replace("uu", "uuuuu")

    print(long_vowels)

# char_swaps()

# caesar cipher

def decode():
   

    code_msg = ("Lbh Zhfg Hayrnea Jung Lbh Unir Yrnearq")
    input_alpha = ("nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
    output_alpha = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    translate_set = str.maketrans(input_alpha, output_alpha)

    print(code_msg.translate(translate_set))
    


decode()
