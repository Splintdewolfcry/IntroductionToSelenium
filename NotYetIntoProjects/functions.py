def write_output(filename, returned_text):
    with open(filename, 'a+') as f:
        f.writelines(returned_text)