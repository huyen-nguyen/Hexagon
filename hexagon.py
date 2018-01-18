# width = input("Enter width: ")
# length = input("Enter length: ")
width = 30
length = 15
upper = " / \\"
side = "|   "
lower = " \\ /"
hexg = [10,10]

def draw_y_axis():
    print "0\t|" + "_" * 170  # FIXXED x-axis
    print "\t"*6 + "  5" + "\t"*5 + "  10" + "\t"*4 + "  15  " + "\t" *4 + "  20" + "\t" * 4 + "  25" + "\t" * 4 + "  30  " + "\t" * 4 + "  35"


def draw_hexagon():  # ---------------------------------------------------------------------------
    print upper * width
    for i in range(length):
        if i % 2:
            print "  " + side * (width + 1) + "\n /" + lower * width  # print the next line with odd i
        else:
            print side * (width + 1) + "\n" + lower * width + " \\"


def draw_hexagon_with_axis():  # ------------------------------------------------------------------
    print ("\t|\t" + upper * width)
    for i in range(length):
        if i % 2:
            print (str(length-i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /" + lower * width)  # print also y-axis
        else:
            print (str(length-i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")  # print y-axis

    # print "0\t|" + "_"*5*width          # SOFT x-axis
    draw_y_axis()


def color_single_hexagon():  # ----------------------COLOR------------------------------------------------------
    for i in range(length):
        if i == 0:
            if i == length - hexg[1]:  # ----- MAIN ------
                print ("\t|\t" + upper * (hexg[0] - 1) + " /*\\" + upper * (width - hexg[0]))
            else:
                print ("\t|\t" + upper * width)

        if i%2:
            if i == length - hexg[1] - 1:    # ----- PREPARE ------
                print (str(length - i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /"
                       + lower * (hexg[0] - 1) + "*\\ /" + lower * (width - hexg[0]))

            elif i == length - hexg[1]:  # ----- MAIN ------
                print (str(length - i) + "\t|\t  " + side * (hexg[0] - 1) + "|***" + side * (width - hexg[0] + 1) + "\n\t|\t /"
                + lower * (hexg[0] - 1) + " \\*/" + lower * (width - hexg[0]))

            else:
                print (str(length - i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /" + lower * width)  # y-axis

        else:
            if i == length - hexg[1] - 1:  # ----- PREPARE ------
                print (str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t"
                   + lower * (hexg[0] - 1) + " \\ /*\\ /" + lower * (width - hexg[0] - 1) + " \\")

            elif i == length - hexg[1]:  # ----- MAIN ------
                print (str(length - i) + "\t|\t" + side * (hexg[0] - 1) + "|***" + side * (width - hexg[0] + 1) + "\n\t|\t"
                       + lower * (hexg[0] - 1) + " \\*/" + lower * (width - hexg[0]) + " \\")
            else:
                print (str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")  # y-axis

    draw_y_axis()

def color_hexagons():
    # ----- READ from file, PUT into list of list  ------
    with open("data.txt") as f:
        lis = []
        for line in f:
            lis.append(list(map(int, line.split(","))))

    sorted_list = sorted(lis, key=lambda x: x[0])  # Sort

    grouped_list = []                                         # ----- GROUP ----
    for k in range(length + 1):
        m = [k]
        for e in sorted_list:
            if k == e[1]:
                m.append(e[0])
        grouped_list.append(m)

    grouped_list = [x for x in grouped_list if len(x) > 1]
    print grouped_list

    screen = []
    full = []
    # ----------------------- COLORING --------------------------
    for i in range(length):
        screen.append("")
        full.append("")
        screen[i] = ""
        full[i] = ""
        prep = 0
        m = 0  # main
        if i % 2:
            print str(length - i) + "\t|\t ",
        elif i != 0:
            print str(length - i) + "\t|\t",

        for hexa in grouped_list:
            if i == length - hexa[0] - 1:  # ----- PREPARE -----
                prep = 1
                if i == 0:
                    screen[i] += "\t|\t" + upper * width
                    screen[i] += "\n" + str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t"
                    screen[i] += lower * hexa[1]
                    for j in range(2, len(hexa)):
                        screen[i] += "*\\ /" + lower * (hexa[j] - hexa[j - 1] - 1)
                    screen[i] += "*\\"
                    if hexa[-1] != width:
                        screen[i] += " /" + lower * (width - hexa[-1] - 1) + " \\"

                elif i % 2:
                    screen[i] += side * (width + 1) + "\n\t|\t /"
                    screen[i] += lower * (hexa[1] - 1) + "*\\ /"
                    for j in range(2, len(hexa)):
                        screen[i] += lower * (hexa[j] - hexa[j - 1] - 1) + "*\\ /"
                    screen[i] += lower * (width - hexa[-1])

                else:
                    screen[i] += side * (width + 1) + "\n\t|\t"
                    screen[i] += lower * hexa[1]
                    for j in range(2, len(hexa)):
                        screen[i] += "*\\ /" + lower * (hexa[j] - hexa[j - 1] - 1)
                    screen[i] += "*\\"
                    if hexa[-1] < width:
                        screen[i] += " /" + lower * (width - hexa[-1] - 1) + " \\"

            if i == length - hexa[0]:  # --------- MAIN ----------
                m = 1
                if i == 0:
                    full[i] += "\t|\t" + upper * (hexa[1] - 1) + " /*\\"
                    for j in range(2, len(hexa)):
                        full[i] += upper * (hexa[j] - hexa[j - 1] - 1) + " /*\\"
                    full[i] += upper * (width - hexa[-1])

                    # -----------
                    full[i] += "\n" + str(length - i) + "\t|\t" + side * (hexa[1] - 1) + "|***"
                    for j in range(2, len(hexa)):
                        full[i] += side * (hexa[j] - hexa[j - 1] - 1) + "|***"
                    full[i] += side * (width - hexa[-1] + 1)

                    # -----------

                    full[i] += "\n\t|\t" + lower * (hexa[1] - 1) + " \\*/"
                    for j in range(2, len(hexa)):
                        full[i] += lower * (hexa[j] - hexa[j - 1] - 1) + " \\*/"
                    full[i] += lower * (width - hexa[-1]) + " \\"

                elif i % 2:
                    # Side
                    full[i] += side * (hexa[1] - 1) + "|***"
                    for j in range(2, len(hexa)):
                        full[i] += side * (hexa[j] - hexa[j - 1] - 1) + "|***"
                    full[i] += side * (width - hexa[-1] + 1)

                    # Lower
                    full[i] += "\n\t|\t /" + lower * (hexa[1] - 1) + " \\*/"
                    for j in range(2, len(hexa)):
                        full[i] += lower * (hexa[j] - hexa[j - 1] - 1) + " \\*/"
                    full[i] += lower * (width - hexa[-1])

                else:
                    full[i] += side * (hexa[1] - 1) + "|***"
                    for j in range(2, len(hexa)):
                        full[i] += side * (hexa[j] - hexa[j - 1] - 1) + "|***"
                    full[i] += side * (width - hexa[-1] + 1)

                    full[i] += "\n\t|\t" + lower * (hexa[1] - 1) + " \\*/"
                    for j in range(2, len(hexa)):
                        full[i] += lower * (hexa[j] - hexa[j - 1] - 1) + " \\*/"
                    full[i] += lower * (width - hexa[-1]) + " \\"

            # ----- PRINT ------
            if hexa == grouped_list[-1]:
                if prep and m:
                    print ''.join(map(max, screen[i], full[i]))

                elif prep and (m == 0):
                    print screen[i]

                elif m and prep == 0:
                    print full[i]

                elif prep == 0 and m == 0:
                    if i == 0:
                        print ("\t|\t" + upper * width + "\n" + str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")

                    elif i % 2:
                        print side * (width + 1) + "\n\t|\t /" + lower * width

                    else:
                        print side * (width + 1) + "\n\t|\t" + lower * width + " \\"
    draw_y_axis()

color_hexagons()
# draw_hexagon()
# draw_hexagon_with_axis()
# color_single_hexagon()

