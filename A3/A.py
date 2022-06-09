# Traverse a string.
# Read specifications carefully.
# Run the test by yourself to avoid deductions from failure. If the exam provides a pre-check, you can use that either.

def run_length_encoding(text):
    result = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            if count > 1:  # Characters that are not repeated in sequence remain unchanged"
                result += str(count)  # Any characters repeated in a sentence are represented by that character and its count
            result += text[i]  # You need to make sure that those characters, even just represented once, are displayed (unchanged).
            count = 1
    return result
