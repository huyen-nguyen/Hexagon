width = 30
length = 15
upper = " / \\"
side = "|   "
lower = " \\ /"
hexg = [10,10]


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
        if i%2:
            print str(length - i) + "\t|\t ",
        else:
            print str(length - i) + "\t|\t",

        for hexa in grouped_list:
            if i == length - hexa[0] - 1:                                    # ----- PREPARE -----
                if i == 0:
                    print upper * width + "prep 0"
                    b = "\t|\t" + side * (width + 1) + "\n\t|\t"
                    b += lower * hexa[1] + "*\\ /"
                    for j in range(2, len(hexa)):
                        b += lower * (hexa[j] - hexa[j - 1] - 1) + "*\\ /"
                    b += lower * (width - hexa[-1] - 1) + " \\"
                    print b + "prep 2aa"

                elif i % 2:
                    a = side * (width + 1) + "\n\t|\t /"
                    a += lower * (hexa[1] - 1) + "*\\ /"
                    for j in range(2, len(hexa)):
                        a += lower * (hexa[j] - hexa[j - 1] - 1) + "*\\ /"
                    a += lower * (width - hexa[-1])
                    print a + "prep 1"

                else:
                    b = side * (width + 1) + "\n\t|\t"
                    b += lower * hexa[1] + "*\\ /"
                    for j in range(2, len(hexa)):
                        b += lower * (hexa[j] - hexa[j - 1] - 1) + "*\\ /"
                    b += lower * (width - hexa[-1] - 1) + " \\"
                    print b + "prep 2"

            # --- end prepare ---

            elif i == length - hexa[0]:                                          # -------- MAIN ----------
                if i == 0:
                    c = upper * (hexa[1] - 1) + " /*\\"
                    for j in range(2,len(hexa)):
                        c += upper * (hexa[j] - hexa[j-1] - 1) + " /*\\"
                    c += upper * (width - hexa[-1])

                    print c + "main 3"

                    s = "\t|\t" + side * (hexa[1] - 1) + "|***"
                    for j in range(2, len(hexa)):
                        s += side * (hexa[j] - hexa[j - 1] - 1) + "|***"
                    s += side * (width - hexa[-1] + 1)
                    print s + "main 4"

                    g = "\t|\t" + lower * (hexa[1] - 1) + " \\*/"
                    for j in range(2, len(hexa)):
                        g += lower * (hexa[j] - hexa[j - 1] - 1) + " \\*/"
                    g += lower * (width - hexa[-1]) + " \\"
                    print g + "main 5"

                elif i % 2:
                    # Side
                    d = side * (hexa[1] - 1) + "|***"
                    for j in range(2,len(hexa)):
                        d += side * (hexa[j] - hexa[j-1] - 1) + "|***"
                    d += side * (width - hexa[-1] + 1)
                    print d + "main 6"

                    # Lower
                    t = "\t|\t /" + lower * (hexa[1] - 1) + " \\*/"
                    for j in range(2, len(hexa)):
                        t += lower * (hexa[j] - hexa[j - 1] - 1) + " \\*/"
                    t += lower * (width - hexa[-1])

                    print t + "main 7"

                else:
                    s = side * (hexa[1] - 1) + "|***"
                    for j in range(2,len(hexa)):
                        s += side * (hexa[j] - hexa[j-1] - 1) + "|***"
                    s += side * (width - hexa[-1] + 1)
                    print s + "main 8"

                    g = "\t|\t" + lower * (hexa[1] - 1) + " \\*/"
                    for j in range(2, len(hexa)):
                        g += lower * (hexa[j] - hexa[j-1] - 1) + " \\*/"
                    g += lower * (width - hexa[-1]) + " \\"
                    print g + "main 9"

            # ----- NORMAL ------
            elif hexa == grouped_list[-1] and i != length - hexa[0] and i != length - hexa[0] - 1:
                if i == 0:
                    print ("\t|\t" + upper * width) + "10"

                if i%2:
                    print side * (width + 1) + "\n\t|\t /" + lower * width + "20"

                else:
                    print side * (width + 1) + "\n\t|\t" + lower * width + " \\" + "30"

    print "0\t|" + "_" * 170  # FIXXED x-axis
    print "\t" * 6 + "  5" + "\t" * 5 + "   10" + "\t" * 5 + "  15  " + "\t" * 4 + "  20" + "\t" * 5 + "25" + "\t" * 5 + "  30  " + "\t" * 4 + "  35"

color_hexagons()