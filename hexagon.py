# width = input("Enter width: ")
# length = input("Enter length: ")
width = 10
length = 9
upper = " / \\"
side = "|   "
lower = " \\ /"
lis = [2,3]


def draw_hexagon():  # ---------------------------------------------------------------------------
    for i in range(length):
        if i == 0:
            print upper * width + "\n" + side * (width + 1) + "\n" + lower * width + " \\"  # print 1st line of hexagons
        elif i % 2:
            print "  " + side * (width + 1) + "\n /" + lower * width  # print the next line
        else:
            print side * (width + 1) + "\n" + lower * width + " \\"


def draw_hexagon_with_axis():  # ------------------------------------------------------------------
    for i in range(length):
        if i == 0:
            print ("\t|\t" + upper * width + "\n" + str(length-i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")
        elif i % 2:
            print (str(length-i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /" + lower * width)  # print also y-axis
        else:
            print (str(length-i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")  # print y-axis

    # print "0\t|" + "_"*5*width          # SOFT x-axis
    print "0\t|" + "_" * 170  # FIXXED x-axis
    print "\t" * 6 + "  5" + "\t" * 5 + " 10" + "\t" * 5 + "  15  " + "\t" * 4 + "  20"


def color_hexagon():  # ----------------------COLOR------------------------------------------------------
    for i in range(length):
        if i == length - lis[1] - 1:    # ----- PREPARE ------
            if i == 0:
                print ("\t|\t" + upper * width + "\n" + str(length-i) + "\t|\t" + side * (width + 1) + "\n\t|\t"
                       + lower * (lis[0] - 1) + " \\ /*\\ /" + lower * (width - lis[0] - 1) + " \\")
            elif i % 2:
                print (str(length-i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /"
                       + lower * (lis[0] - 1) + "*\\ /" + lower * (width - lis[0]))
            else:
                print (str(length-i) + "\t|\t" + side * (width + 1) + "\n\t|\t"
                       + lower * (lis[0] - 1) + " \\ /*\\ /" + lower * (width - lis[0] - 1) + " \\")

        elif i == length - lis[1]:  # ----- MAIN ------
            if i == 0:
                print ("\t|\t" + upper * (lis[0] - 1) + " /*\\" + upper * (width - lis[0]) + "\n" + str(length - i) + "\t|\t"
                    + side * (lis[0] - 1) + "|***" + side * (width - lis[0] + 1) + "\n\t|\t"
                    + lower * (lis[0] - 1) + " \\*/" + lower * (width - lis[0]) + " \\")

            elif i % 2:
                print (str(length - i) + "\t|\t  " + side * (lis[0] - 1) + "|***" + side * (width - lis[0] + 1) + "\n\t|\t /"
                       + lower * (lis[0] - 1) + " \\*/" + lower * (width - lis[0]))

            else:
                print (str(length - i) + "\t|\t" + side * (lis[0] - 1) + "|***" + side * (width - lis[0] + 1) + "\n\t|\t"
                       + lower * (lis[0] - 1) + " \\*/" + lower * (width - lis[0]) + " \\")

        else:    # ----- NORMAL ------
            if i == 0:
                print ("\t|\t" + upper * width + "\n" + str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")
            elif i % 2:
                print (str(length - i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /" + lower * width)  # y-axis
            else:
                print (str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")  # y-axis

    print "0\t|" + "_" * 170  # FIXXED x-axis
    print "\t" * 6 + "  5" + "\t" * 5 + " 10" + "\t" * 5 + "  15  " + "\t" * 4 + "  20" + "\t" * 5 + "25" + "\t" * 5 + "  30  " + "\t" * 4 + "  35"


# def color():
#     with open("test.txt") as f:
#         for line in f:
#             lis[0], lis[1] = line.split(",")
#             lis[0] = int(lis[0])
#             lis[1] = int(lis[1])
#             color_hexagon()


# draw_hexagon()
# draw_hexagon_with_axis()
color_hexagon()
# color()
