#<class '_io.TextIOWrapper'>
def into(filename, mode):
    global rcsy_data
    rcsy_data = open(filename, mode)
def write_rcsy(name, text):
    rcsy_data.write(name + "--" + text + "\n")
    rcsy_data.flush()
