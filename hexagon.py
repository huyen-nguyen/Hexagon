# width = input("Enter width: ")
# length = input("Enter length: ")
width = 30
length = 15
upper = " / \\"
side = "|   "
lower = " \\ /"


def draw_y_axis():
    print "0\t|" + "_" * 170  # FIXXED x-axis
    print "\t"*6 + "  5" + "\t"*5 + "  10" + "\t"*4 + "  15  " + "\t" *4 + "  20" + "\t" * 4 + "  25" + "\t" * 4 + "  30  " + "\t" * 4 + "  35"


def draw_hexagon():  # ---------------------------  DRAW SIMPLE GRID  -----------------------------------
    print upper * width
    for i in range(length):
        if i % 2:
            print "  " + side * (width + 1) + "\n /" + lower * width  # print the next line with odd i
        else:
            print side * (width + 1) + "\n" + lower * width + " \\"


def draw_hexagon_with_axes():  # --------------------DRAW GRID WITH AXES-----------------------------------
    print ("\t|\t" + upper * width)
    for i in range(length):
        if i % 2:
            print (str(length-i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /" + lower * width)  # print also y-axis
        else:
            print (str(length-i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")  # print y-axis
    # print "0\t|" + "_"*5*width          # SOFT x-axis
    draw_y_axis()


def color_hexagons():     # ----------------------COLOR----------------------------------------------

    # ---- Read from file, put into list of list  ---
    with open("data.txt") as f:
        lis = []
        for line in f:
            lis.append(list(map(int, line.split(","))))

    sorted_list = sorted(lis, key=lambda x: x[0])  # Sort

    non_dup = []                # --- Remove duplicates ---
    for value in sorted_list:
        if value not in non_dup:
            non_dup.append(value)

    grouped_list = []           # ----- Group ----
    for k in range(length + 1):
        m = [k]
        for e in non_dup:
            if k == e[1]:
                m.append(e[0])
        grouped_list.append(m)

    grouped_list = [x for x in grouped_list if len(x) > 1]
    print grouped_list

    # ----- Sub functions ------
    def prep_even():
        screen[i] += side * (width + 1) + "\n\t|\t"
        screen[i] += lower * hexa[1]
        for j in range(2, len(hexa)):
            screen[i] += "*\\ /" + lower * (hexa[j] - hexa[j - 1] - 1)
        screen[i] += "*\\"
        if hexa[-1] < width:
            screen[i] += " /" + lower * (width - hexa[-1] - 1) + " \\"

    def main_side():
        full[i] += side * (hexa[1] - 1) + "|***"
        for j in range(2, len(hexa)):
            full[i] += side * (hexa[j] - hexa[j - 1] - 1) + "|***"
        full[i] += side * (width - hexa[-1] + 1)

    def main_lower():
        full[i] += lower * (hexa[1] - 1) + " \\*/"
        for j in range(2, len(hexa)):
            full[i] += lower * (hexa[j] - hexa[j - 1] - 1) + " \\*/"
        full[i] += lower * (width - hexa[-1])

    screen = []
    full = []
    # ----------------------- COLORING -------------------------
    for i in range(length):
        screen.append("")
        full.append("")
        screen[i] = ""
        full[i] = ""
        prep = 0
        m = 0  # main

    # ------ y-axis --------
        if i % 2:
            print str(length - i) + "\t|\t ",
        elif i != 0:
            print str(length - i) + "\t|\t",
            
    # ----------------------- SELECT ---------------------------
        for hexa in grouped_list:
            if i == length - hexa[0] - 1:  # ----- PREPARE -----
                prep = 1
                if i == 0:
                    screen[i] += "\t|\t" + upper * width + "\n" + str(length - i) + "\t|\t"
                    prep_even()

                elif i % 2:
                    screen[i] += side * (width + 1) + "\n\t|\t /"
                    screen[i] += lower * (hexa[1] - 1) + "*\\ /"
                    for j in range(2, len(hexa)):
                        screen[i] += lower * (hexa[j] - hexa[j - 1] - 1) + "*\\ /"
                    screen[i] += lower * (width - hexa[-1])
                else:
                    prep_even()

            if i == length - hexa[0]:  # --------- MAIN ----------
                m = 1
                if i == 0:
                    full[i] += "\t|\t" + upper * (hexa[1] - 1) + " /*\\"
                    for j in range(2, len(hexa)):
                        full[i] += upper * (hexa[j] - hexa[j - 1] - 1) + " /*\\"
                    full[i] += upper * (width - hexa[-1])

                    full[i] += "\n" + str(length - i) + "\t|\t"
                    main_side()
                    full[i] += "\n\t|\t"
                    main_lower()

                elif i % 2:
                    main_side()
                    full[i] += "\n\t|\t /"
                    main_lower()

                else:
                    main_side()
                    full[i] += "\n\t|\t"
                    main_lower()
                    full[i] += " \\"

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
# draw_hexagon_with_axes()

