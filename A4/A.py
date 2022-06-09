# I/O: read/write file

filename = "abc123.txt"

def write_secret_sentence(text):
    vowels = "aeiouAEIOU"
    secret_text = ""
    for t in text:
        if t in vowels:
            secret_text += "*"
        else:
            secret_text += t
    # I/O
    f = open(filename, "w")
    f.write(secret_text)
    f.close()
