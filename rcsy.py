#<class '_io.TextIOWrapper'>
def into(filename, mode):
    global rcsy_data
    rcsy_data = open(filename, mode)
def endl():
    rcsy_data.write("\n")
    rcsy_data.flush()
def write_rcsy(name, text):
    rcsy_data.write(name + "--" + text + "\n")
    rcsy_data.flush()
def write_and(front, back):
    rcsy_data.write(front + "++" + back + "\n")
    rcsy_data.flush()
def write_or(front, back):
    rcsy_data.write(front + "//" + back + "\n")
    rcsy_data.flush()
def write_not(front, back):
    rcsy_data.write(front + "!!" + back + "\n")
    rcsy_data.flush()
def write_list_and(name, list):
    last = list[-1]
    rcsy_data.write(name + ":")
    for i in list:
        if(i == last):
            rcsy_data.write(i + "&" + "a" + "\n")
        else:
            rcsy_data.write(i + "++")
def write_list_or(name, list):
    last = list[-1]
    rcsy_data.write(name + ":")
    for i in list:
        if(i == last):
            rcsy_data.write(i + "&" + "o" + "\n")
        else:
            rcsy_data.write(i + "//")
def write_list_not(name, list):
    last = list[-1]
    rcsy_data.write(name + ":")
    for i in list:
        if(i == last):
            rcsy_data.write(i + "&" + "n" + "\n")
        else:
            rcsy_data.write(i + "!!")
