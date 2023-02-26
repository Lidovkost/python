def list_chr(min_index, max_index, pairs = 10):
    if min_index == max_index:
        return f'{min_index}. - {chr(min_index)}'
    if pairs == 1:
        return f'{min_index}. - {chr(min_index)} \n ' + list_chr(min_index+1, max_index, pairs + 9) # не придумал как от 9 избавиться
    else:
        return f'{min_index}. - {chr(min_index)} ' + list_chr(min_index+1, max_index, pairs-1)
print(list_chr(32, 127))
