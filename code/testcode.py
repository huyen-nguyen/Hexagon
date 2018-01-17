# # # # # def test(i,n):
# # # # #     print ~(i-n) - (n-i-1)
# # # # #
# # # # # test(2,3)
# # # # # test(300,457)
# # # # # test(-3,-283)
# # # # # test(56,-23)
# # # # # test(344, 9000)
# # # # #
# # # # # print '1'*3
# # # #
# # # # # print (2>1)*(2<=9)
# # # # # for j in range(n / WIDTH):  # lines
# # # # #     print upper * WIDTH + '\n' + side[:3] * (1 + WIDTH) + ' \n' + lower * WIDTH
# # # # #
# # # # # print upper * (n % WIDTH) + '\n' + side[:4] * (1 + n % WIDTH) + '\n' + lower * (n % WIDTH)
# # # #
# # # # # def draw_axis():
# # # # #     print '|\n'*30 + '|'
# # # # #     print '|' + '_'*30
# # # # #
# # # # #
# # # #
# # # # #
# # # #
# # # #
# # # #
# # # # # draw_axis()
# # # # # print "hi"
# # # # # print "huyen"
# # # # #
# # # # # print''.join([[ 'hoa' , 'la' ][i] for i in range(2)])
# # # #
# # # #
# # # # # LENGTH = 6
# # # # # for i in range(LENGTH):
# # # # #     if i == 0:
# # # # #         print " i==0 "
# # # # #     else:
# # # # #         print ("dong thu 1 khi i = " + str(i) )
# # # # #         print ("dong thu 2 khi i = " + str(i) )
# # # #
# # # #
# # # # class HexagonGrid(object):
# # # #     def __init__(self, width, length):
# # # #         self.width = width
# # # #         self.height = length
# # # #
# # # # length = 20
# # # # for i in range(length):
# # # #     if i == 0:
# # # #         print i
# # # #
# # # #     elif i%2:
# # # #         print i
# # # #     else:
# # # #         print i
# # # #
# # # # width = 30
# # # # length = 15
# # # # upper = " / \\"
# # # # side = "|   "
# # # # lower = " \\ /"
# # # # tup = (3,3)
# # # #
# # # #
# # # # def color_hexagon():  # ----------------------COLOR------------------------------------------------------
# # # #     for i in range(length):
# # # #         if i == 0:
# # # #             if i == length - tup[1] - 1:  # prepare
# # # #                 print ("\t|\t" + upper * width + "\n" + str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t"
# # # #                        + lower * (tup[0] - 1) + " \\ /*\\ /" + lower * (width - tup[0] - 1) + " \\")
# # # #
# # # #             elif i == length - tup[1]:  # main
# # # #                 print ("\t|\t" + upper * (tup[0] - 1) + " /*\\" + upper * (width - tup[0]) + "\n" + str(length - i) + "\t|\t"
# # # #                 + side * (tup[0] - 1) + "|***" + side * (width - tup[0] + 1) + "\n\t|\t"
# # # #                 + lower * (tup[0] - 1) + " \\*/" + lower * (width - tup[0]) + " \\")
# # # #             else:
# # # #                 print ("\t|\t" + upper * width + "\n" + str(length - i) + "\t|\t" + side * (
# # # #                 width + 1) + "\n\t|\t" + lower * width + " \\")
# # # #
# # # #         elif i % 2:
# # # #             if i == length - tup[1] - 1:  # prepare
# # # #                 print (str(length - i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /"
# # # #                        + lower * (tup[0] - 2) + "*\\ /" + lower * (width - tup[0]))
# # # #
# # # #             elif i == length - tup[1]:  # main
# # # #                 print (str(length - i) + "\t|\t  "
# # # #                        + side * (tup[0] - 1) + "|***" + side * (width - tup[0] + 1) + "\n\t|\t /"
# # # #                        + lower * (tup[0] - 1) + " \\*/" + lower * (width - tup[0]))
# # # #             else:
# # # #                 print (str(length - i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /" + lower * width)
# # # #
# # # #         elif i == length - tup[1] - 1:  # prepare
# # # #             print (str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t"
# # # #                    + lower * (tup[0] - 2) + "*\\ /" + lower * (width - tup[0]) + " \\")
# # # #
# # # #         elif i == length - tup[1]:  # main
# # # #             print (str(length - i) + "\t|\t" + side * (tup[0] - 1) + "|***" + side * (width - tup[0] + 1) + "\n\t|\t"
# # # #                 + lower * (tup[0] - 1) + " \\*/" + lower * (width - tup[0]) + " \\")
# # # #
# # # #         else:
# # # #             print (str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")
# width = 30
# length = 15
# upper = " / \\"
# side = "|   "
# lower = " \\ /"
# hexg = [12,1]
# x = ['1','2']
# print ('h')
# # #
# # #
# # # def color_single_hexagon():  # ----------------------COLOR------------------------------------------------------
# # #     for i in range(length):
# # #
# # #         if i == length - hexg[1] - 1:    # ----- PREPARE ------
# # #             if i == 0:
# # #                 print ("\t|\t" + upper * width + "\n" + str(length-i) + "\t|\t" + side * (width + 1) + "\n\t|\t"
# # #                        + lower * (hexg[0] - 1) + " \\ /*\\ /" + lower * (width - hexg[0] - 1) + " \\")
# # #             elif i % 2:
# # #                 print (str(length-i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /"
# # #                        + lower * (hexg[0] - 1) + "*\\ /" + lower * (width - hexg[0]))
# # #             else:
# # #                 print (str(length-i) + "\t|\t" + side * (width + 1) + "\n\t|\t"
# # #                        + lower * (hexg[0] - 1) + " \\ /*\\ /" + lower * (width - hexg[0] - 1) + " \\")
# # #
# # #         elif i == length - hexg[1]:  # ----- MAIN ------
# # #             if i == 0:
# # #                 print ("\t|\t" + upper * (hexg[0] - 1) + " /*\\" + upper * (width - hexg[0]) + "\n" + str(length - i) + "\t|\t"
# # #                     + side * (hexg[0] - 1) + "|***" + side * (width - hexg[0] + 1) + "\n\t|\t"
# # #                     + lower * (hexg[0] - 1) + " \\*/" + lower * (width - hexg[0]) + " \\")
# # #
# # #             elif i % 2:
# # #                 print (str(length - i) + "\t|\t  " + side * (hexg[0] - 1) + "|***" + side * (width - hexg[0] + 1) + "\n\t|\t /"
# # #                        + lower * (hexg[0] - 1) + " \\*/" + lower * (width - hexg[0]))
# # #
# # #             else:
# # #                 print (str(length - i) + "\t|\t" + side * (hexg[0] - 1) + "|***" + side * (width - hexg[0] + 1) + "\n\t|\t"
# # #                        + lower * (hexg[0] - 1) + " \\*/" + lower * (width - hexg[0]) + " \\")
# # #
# # #         else:    # ----- NORMAL ------
# # #             if i == 0:
# # #                 print ("\t|\t" + upper * width + "\n" + str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")
# # #             elif i % 2:
# # #                 print (str(length - i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /" + lower * width)  # y-axis
# # #             else:
# # #                 print (str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")  # y-axis
# # #
# # #     print "0\t|" + "_" * 170  # FIXXED x-axis
# # #     print "\t" * 6 + "  5" + "\t" * 5 + " 10" + "\t" * 5 + "  15  " + "\t" * 4 + "  20" + "\t" * 5 + "25" + "\t" * 5 + "  30  " + "\t" * 4 + "  35"
# # #
# #
# #
# # def color_single_hexagon():  # ----------------------COLOR------------------------------------------------------
# #     for i in range(length):
# #         if i == 0:
# #             if i == length - hexg[1]:  # ----- MAIN ------
# #                 print ("\t|\t" + upper * (hexg[0] - 1) + " /*\\" + upper * (width - hexg[0]))
# #             else:
# #                 print ("\t|\t" + upper * width)
# #
# #         if i%2:
# #             if i == length - hexg[1] - 1:    # ----- PREPARE ------
# #                 print (str(length - i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /"
# #                        + lower * (hexg[0] - 1) + "*\\ /" + lower * (width - hexg[0]))
# #
# #             elif i == length - hexg[1]:  # ----- MAIN ------
# #                 print (str(length - i) + "\t|\t  " + side * (hexg[0] - 1) + "|***" + side * (width - hexg[0] + 1) + "\n\t|\t /"
# #                 + lower * (hexg[0] - 1) + " \\*/" + lower * (width - hexg[0]))
# #
# #             else:
# #                 print (str(length - i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /" + lower * width)  # y-axis
# #
# #         else:
# #             if i == length - hexg[1] - 1:  # ----- PREPARE ------
# #                 print (str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t"
# #                    + lower * (hexg[0] - 1) + " \\ /*\\ /" + lower * (width - hexg[0] - 1) + " \\")
# #
# #             elif i == length - hexg[1]:  # ----- MAIN ------
# #                 print (str(length - i) + "\t|\t" + side * (hexg[0] - 1) + "|***" + side * (width - hexg[0] + 1) + "\n\t|\t"
# #                        + lower * (hexg[0] - 1) + " \\*/" + lower * (width - hexg[0]) + " \\")
# #             else:
# #                 print (str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")  # y-axis
# #
# #     print "0\t|" + "_" * 170  # FIXXED x-axis
# #     print "\t" * 6 + "  5" + "\t" * 5 + "   10" + "\t" * 5 + "  15  " + "\t" * 4 + "  20" + "\t" * 5 + "25" + "\t" * 5 + "  30  " + "\t" * 4 + "  35"
# #
# #
# # def color_ssingle_hexagon():  # ----------------------COLOR------------------------------------------------------
# #     for i in range(length):
# #         if i == length - hexg[1] - 1:    # ----- PREPARE ------
# #             if i == 0:
# #                 print ("\t|\t" + upper * width)
# #             if i % 2:
# #                 print (str(length-i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /"
# #                        + lower * (hexg[0] - 1) + "*\\ /" + lower * (width - hexg[0]))
# #             else:
# #                 print (str(length-i) + "\t|\t" + side * (width + 1) + "\n\t|\t"
# #                        + lower * (hexg[0] - 1) + " \\ /*\\ /" + lower * (width - hexg[0] - 1) + " \\")
# #
# #         elif i == length - hexg[1]:  # ----- MAIN ------
# #             if i == 0:
# #                 print ("\t|\t" + upper * (hexg[0] - 1) + " /*\\" + upper * (width - hexg[0]) + "\n" + str(length - i) + "\t|\t"
# #                     + side * (hexg[0] - 1) + "|***" + side * (width - hexg[0] + 1) + "\n\t|\t"
# #                     + lower * (hexg[0] - 1) + " \\*/" + lower * (width - hexg[0]) + " \\")
# #
# #             elif i % 2:
# #                 print (str(length - i) + "\t|\t  " + side * (hexg[0] - 1) + "|***" + side * (width - hexg[0] + 1) + "\n\t|\t /"
# #                        + lower * (hexg[0] - 1) + " \\*/" + lower * (width - hexg[0]))
# #
# #             else:
# #                 print (str(length - i) + "\t|\t" + side * (hexg[0] - 1) + "|***" + side * (width - hexg[0] + 1) + "\n\t|\t"
# #                        + lower * (hexg[0] - 1) + " \\*/" + lower * (width - hexg[0]) + " \\")
# #
# #         else:    # ----- NORMAL ------
# #             if i == 0:
# #                 print ("\t|\t" + upper * width)
# #             if i % 2:
# #                 print (str(length - i) + "\t|\t  " + side * (width + 1) + "\n\t|\t /" + lower * width)  # y-axis
# #             else:
# #                 print (str(length - i) + "\t|\t" + side * (width + 1) + "\n\t|\t" + lower * width + " \\")  # y-axis
# #
# #     print "0\t|" + "_" * 170  # FIXXED x-axis
# #     print "\t" * 6 + "  5" + "\t" * 5 + "   10" + "\t" * 5 + "  15  " + "\t" * 4 + "  20" + "\t" * 5 + "25" + "\t" * 5 + "  30  " + "\t" * 4 + "  35"
# # color_single_hexagon()
# s = t = ''
# grouped_list = [[1,2],[3,4],[6,7,5],[2,3,2]]
#
#
# for i in range(length):
#     for hexa in grouped_list:
#
#         if i == length - hexa[0] - 1:  # ----- PREPARE -----
#             if i == 0:
#                 print "prep111"
#
#             if i % 2:
#                 print s + "prep333"
#
#             else:
#                 print s + "prep444"
#
#         elif i == length - hexa[0]:  # ---- MAIN ------
#             if i == 0:
#                 print s + "main555"
#
#             if i % 2:
#                 print s + "main999"
#
#             else:
#                 print t + "main===="
#
#         if hexa == grouped_list[-1] and i != length - hexa[0] and i != length - hexa[0] - 1:
#             print "haha"

s = 'hi there'
print s[1]