def bruteforce(text, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text.upper()
    key = -1
    new_text = ""
    for i in text:
        if i in alphabet:
            new_text +=i
    while abs(key)!= len(alphabet):
        result_crypt = ""
        for t in new_text:
            i = alphabet.index(t)
            new_i = i + key
            while new_i < 0:
                new_i = len(alphabet)+new_i
            result_crypt += alphabet[new_i]
        print(result_crypt)
        key -= 1
    return
