

def horizontal_or_vertical(epsilon, line_section):
    if abs(line_section[0] - line_section[2])<=epsilon:
        return "vertical"
    else:
        return "horisontal"

def check_into_list(epsilon, selection, element):
    appending = True
    for id_y in selection:
        if abs(element - id_y[0]) <= epsilon:
            return False
    return True

def computation_line(epsilon, block):
    # к верхней горизонтальной линии будем крепить те вертикальные, которые ниже
    selection = []
    vertical = []
    horizontal = []

    #раскидываем линии на горизонтальные и вертикальные
    for line in block:
        if horizontal_or_vertical(epsilon, line)=="horisontal":
            horizontal.append(line)
        else:
            vertical.append(line)

    for line in horizontal:
        element = (line[1] + line[3])/2
        if check_into_list(epsilon,selection,element):
            selection.append([element])

    selection.sort(key=lambda val: val[0])

    for line in vertical:
        element = (line[0] + line[2])/2
        for id_y in range(len(selection)-1):

            if selection[id_y] - epsilon <= line[1] and selection[id_y+1] + epsilon >= line[1]:
                if check_into_list(epsilon, selection, element):
                    selection[id_y].append(element)

            if selection[id_y] - epsilon <= line[3] and selection[id_y+1] + epsilon >= line[3]:
                if check_into_list(epsilon, selection, element):
                    selection[id_y].append(element)

    #крайние точки
    selection[0].append(min(min(horizontal, key=lambda val: val[0]),min(horizontal, key=lambda val: val[3])))
    selection[0].append(max(max(horizontal, key=lambda val: val[0]),max(horizontal, key=lambda val: val[3])))

    return selection

