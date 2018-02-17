

def horizontal_or_vertical(epsilon, line_section):
    if abs(line_section[0] - line_section[2]) <= epsilon:
        return "vertical"
    else:
        return "horisontal"


def check_into_list(epsilon, selection, element):
    for id_y in selection:
        if abs(element - id_y) <= epsilon:
            return False
    return True


def compute_lines(epsilon, block):
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
        appending = True
        for id_y in selection:
            if abs(element - id_y[0]) <= epsilon:
                appending = False
                break
        if appending:
            selection.append([element])

    selection.sort(key=lambda val: val[0])
    print(selection)

    # заполнение вертикальных линий
    for line in vertical:
        element = (line[0] + line[2])/2
        #для проверки на длинные линии
        upper_bound = 0
        lower_bound = 0
        for id_y in range(len(selection)-1):

            if selection[id_y][0] - epsilon <= line[1] and selection[id_y+1][0] + epsilon >= line[1]:
                if upper_bound:
                    if abs(id_y+1-upper_bound) > 1:
                        for i in range(id_y+1,upper_bound):
                            if check_into_list(epsilon, selection[i], element):
                                selection[i].append(element)
                if check_into_list(epsilon, selection[id_y+1], element):
                    selection[id_y+1].append(element)
                    lower_bound = id_y

            if selection[id_y][0] - epsilon <= line[3] and selection[id_y+1][0] + epsilon >= line[3]:
                if lower_bound:
                    if abs(id_y+1-lower_bound) > 1:
                        for i in range(id_y+1,lower_bound):
                            if check_into_list(epsilon, selection[i], element):
                                selection[i].append(element)
                if check_into_list(epsilon, selection[id_y+1], element):
                    selection[id_y+1].append(element)
                    upper_bound = id_y

    # крайние точки
    min_line = min(min(horizontal, key=lambda val: val[0]),min(horizontal, key=lambda val: val[2]))
    max_line = max(max(horizontal, key=lambda val: val[0]),max(horizontal, key=lambda val: val[2]))
    selection[-1].append(min(min_line[0],min_line[2]))
    selection[-1].append(max(max_line[0],max_line[2]))

    print(selection)
    return [[selection[-1][0],selection[-2][0]],selection[-1][1:]],selection[-2][0]

test_mass = [(531.84, 761.8403999999999, 532.8, 827.8403999999999),
             (489.71999999999997, 761.8403999999999, 490.68, 827.8403999999999),
             (436.68, 761.8403999999999, 437.64,827.8403999999999),
             (346.56, 761.8403999999999, 347.52, 827.8403999999999),
             (292.92, 761.8403999999999, 293.88, 827.8403999999999),
             (235.92, 761.8403999999999,236.88, 827.8403999999999),
             (178.56, 761.8403999999999, 179.51999999999998, 827.8403999999999),
             (129.96, 761.8403999999999, 130.92, 827.8403999999999),
             (36.24,760.8804, 560.88, 761.8403999999999),
             (35.879999999999995, 826.8804, 560.88, 827.8403999999999),
             (49.32, 761.8403999999999, 50.28, 827.8403999999999),
             (531.84,674.3604, 532.8, 721.0404), (531.84, 721.0404, 532.8, 761.8403999999999),
             (489.71999999999997, 674.3604, 490.68, 721.0404),
             (489.71999999999997, 721.0404, 490.68, 761.8403999999999),
             (436.68, 674.3604, 437.64, 721.0404), (436.68, 721.0404,437.64, 761.8403999999999),
             (346.56, 674.3604, 347.52, 721.0404), (346.56, 721.0404, 347.52, 761.8403999999999),
             (292.92, 674.3604, 293.88, 721.0404), (292.92,721.0404, 293.88, 761.8403999999999),
             (235.92, 674.3604, 236.88, 721.0404), (235.92, 721.0404, 236.88, 761.8403999999999),
             (178.56, 674.3604, 179.51999999999998, 721.0404), (178.56, 721.0404, 179.51999999999998, 761.8403999999999),
             (129.96, 674.3604, 130.92, 721.0404), (129.96, 721.0404, 130.92, 761.8403999999999),
             (49.32, 674.3604, 50.28, 721.0404), (49.32, 721.0404, 50.28, 761.8403999999999),
             (531.84, 656.4804, 532.8, 674.3604), (489.71999999999997, 656.4804, 490.68, 674.3604),
             (436.68, 656.4804, 437.64, 674.3604), (346.56, 656.4804, 347.52, 674.3604),
             (292.92, 656.4804, 293.88, 674.3604), (235.92, 656.4804, 236.88, 674.3604),
             (178.56, 656.4804, 179.51999999999998, 674.3604), (49.32, 656.4804, 50.28, 674.3604),
             (33.96, 673.4004, 559.68, 674.3604), (33.96, 656.3604, 558.6, 657.3204),
             (129.96, 656.8403999999999, 130.92, 674.3604), (33.96, 333.5604, 558.9599999999999,334.5204)]
print(compute_lines(1.,test_mass))
