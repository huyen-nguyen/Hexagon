# width = input("Enter width: ")
# length = input("Enter length: ")
width = 30
length = 15
upper = " / \\"
side = "|   "
lower = " \\ /"
hexg = [10,10]


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
    print "0\t|" + "_" * 170  # FIXXED x-axis
    print "\t" * 6 + "  5" + "\t" * 5 + " 10" + "\t" * 5 + "  15  " + "\t" * 4 + "  20"


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

    print "0\t|" + "_" * 170  # FIXXED x-axis
    print "\t" * 6 + "  5" + "\t" * 5 + "   10" + "\t" * 5 + "  15  " + "\t" * 4 + "  20" + "\t" * 5 + "25" + "\t" * 5 + "  30  " + "\t" * 4 + "  35"


def color_hexagons():
    # ----- READ from file, PUT into list of list  ------
    with open("data.txt") as f:
        lis = []
        for line in f:
            lis.append(list(map(int,line.split(","))))

    sorted_list = sorted(lis, key=lambda x: x[0])   # Sort

    # ----- GROUP ----
    grouped_list = []
    for k in range (length+1):
        m = [k]
        for e in sorted_list:
            if k == e[1]:
                m.append(e[0])
        grouped_list.append(m)

    grouped_list = [x for x in grouped_list if len(x)>1]
    print grouped_list

    # ---- COLORING ------
    for i in range(length):
        for hexa in grouped_list:
            if i == 0:              # ----- i = 0 ------
                if i == length - hexa[0]:        # Main
                    print "\t|\t" + upper * (hexa[1] - 1) + " /*\\",
                    for j in range(2, len(hexa)):
                        print upper[1:] + upper * (hexa[j] - hexa[j-1]-2) + " /*\\",
                    print upper[1:] + upper * (width - hexa[-1] - 2)

                else:
                    print ("\t|\t" + upper * width)

            if i%2:

                if i == length - hexa[0] - 1:    # prepare
                    print str(length - i) + "\t|\t  "+ side * (width + 1) + "\n\t|\t /" + lower * (hexa[1] - 1) + "*\\ /",
                    for j in range(2,len(hexa)):
                        print lower[1:] + lower * (hexa[j] - hexa[j-1] -2 ) + "*\\ /",
                    print lower[1:] + lower * (width - hexg[-1] - 2)

                elif i == length - hexa[0]:       # Main
                    # SIDE
                    print str(length - i) + "\t|\t  "+ side * (hexa[1] - 1) + "|***",
                    for j in range(2,len(hexa)):
                        print side * (hexa[j] - hexa[j-1]) + "\***",
                    print side * (width - hexa[1] -1)

                    # LOWER
                    print "\t|\t /"+ lower * (hexa[1] - 1) + " \\*/",
                    for j in range(2,len(hexa)):
                        print lower[1:] + lower * (hexa[j] - hexa[j-1]-2) + " \\*/",
                    print lower[1:] + lower * (width - hexa[-1] - 2)

                else:
                    print (str(length - i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /" + lower * width)

            else:
                if i == length - hexa[0] - 1:       # Prepare
                    print str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * (hexa[1] - 1) + " \\ /*",
                    for j in range(2,len(hexa)):
                        print lower[1:] + lower * (hexa[j] - hexa[j-1] - 2) + "*\\ /",
                    print lower * (width - hexg[-1] - 1) + " \\"

                elif i == length - hexa[0]:
                    # SIDE
                    print str(length - i) + "\t|\t" + side * (hexa[1] - 1) + "|***",
                    for j in range(2, len(hexa)):
                        print side * (hexa[j] - hexa[j - 1]) + "\***",
                    print side * (width - hexa[1] - 1)

                    # LOWER
                    print "\t|\t" + lower * (hexa[1] - 1) + " \\*/",
                    for j in range(2, len(hexa)):
                        print lower[1:] + lower * (hexa[j] - hexa[j - 1] - 2) + " \\*/",
                    print lower[1:] + lower * (width - hexa[-1] - 2) + " \\"

                else:
                    print (str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")


# color_hexagons()
# draw_hexagon()
# draw_hexagon_with_axis()
color_single_hexagon()

