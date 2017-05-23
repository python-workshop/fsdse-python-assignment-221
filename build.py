def count_sentence_fit(sentence, rows, cols):
    if sentence is None:
        raise TypeError('sentence cannot be None')
    if rows is None or cols is None:
        raise TypeError('rows and cols cannot be None')
    if rows < 0 or cols < 0:
        raise ValueError('rows and cols cannot be negative')
    if cols == 0 or not sentence:
        return 0
    string = ' '.join(sentence) + ' '
    start = 0
    str_len = len(string)
    for row in range(rows):
        start += cols
        # We don't need extra space for the current row
        if string[start % str_len] == ' ':
            start += 1
        # The current row can't fit, so we'll need to
        # remove characters from the next word
        else:
            while (start > 0 and string[(start - 1) % str_len] != ' '):
                start -= 1
    return start // str_len