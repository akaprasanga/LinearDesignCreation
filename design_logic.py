import cv2
import numpy as np
from collections import Counter
import random
import time

class DesignLogic():

    def __init__(self):
        pass

    def create_image(self, height=1200, width=900):
        img = np.zeros([height, width, 3], dtype=np.uint8)
        img.fill(255)
        return img, img.copy()

    def create_random_list(self, minimum=5, maximum=20, total= 100):
        sum = 0
        random_list = []
        sum_list = []
        while sum <= total:
            a = random.randint(minimum, maximum)
            b = random.randint(minimum-1, maximum+1)
            c = random.randint(minimum, maximum+2)
            ll = [a, b, c]

            a = ll[random.randint(0,2)]
            sum = sum + a
            random_list.append(a)
            sum_list.append(sum)

        return random_list, sum_list

    def divide_vertically(self, img, minimum_value=5, maximum_value=50, level_list=[], random_value=1, color_tuple=(0, 0, 0), thick=2):

        new_vertical_division_list = []
        for points in level_list:
            x1, x2, y1, y2 = points
            width = x2 - x1
            height = y2 - y1

            plus_minus_tolerance_min = [int(minimum_value+minimum_value*random_value*0.01), int(minimum_value-minimum_value*random_value*0.01)]
            plus_minus_tolerance_max = [int(maximum_value+maximum_value*random_value*0.01), int(maximum_value-maximum_value*random_value*0.01)]

            choose_item = random.randint(0, 1)
            a, draw = self.create_random_list(plus_minus_tolerance_min[choose_item],
                                              plus_minus_tolerance_max[choose_item], height)
            draw = [x + y1 for x in draw]

            last = y1
            for each in draw:
                img = cv2.line(img, (int(x1), int(each)), (int(x2), int(each)), color_tuple, thickness=thick)
                a = (int(x1), int(x2), int(last), int(each))
                new_vertical_division_list.append(a)
                last = each
        return img, new_vertical_division_list

    def divide_horizontally(self, img, minimum_value=5, maximum_value=50, level_list=[], random_value=1, color_tuple=(220, 178, 137), thick=2):

        new_horizontal_division_list = []
        for points in level_list:
            x1, x2, y1, y2 = points
            width = x2 - x1
            height = y2 - y1

            plus_minus_tolerance_min = [int(minimum_value+minimum_value*random_value*0.01), int(minimum_value-minimum_value*random_value*0.01)]
            plus_minus_tolerance_max = [int(maximum_value+maximum_value*random_value*0.01), int(maximum_value-maximum_value*random_value*0.01)]

            choose_item = random.randint(0, 1)
            a, draw = self.create_random_list(plus_minus_tolerance_min[choose_item], plus_minus_tolerance_max[choose_item], width)
            draw = [x + x1 for x in draw]
            last = x1
            for each in draw:
                # if each < x2:
                img = cv2.line(img, (int(each), int(y1)), (int(each), int(y2)), color_tuple, thickness=thick)
                a = (int(last), int(each), int(y1), int(y2))
                last = each
                new_horizontal_division_list.append(a)

        return img, new_horizontal_division_list

    def divide_vertically_l3(self, img, minimum_value=5, maximum_value=50, level_list=[], random_value=1, color_tuple=(202, 131, 39), thick=2):

        new_vertical_division_list = []
        for points in level_list:
            x1, x2, y1, y2 = points
            width = x2 - x1
            height = y2 - y1

            plus_minus_tolerance_min = [int(minimum_value+minimum_value*random_value*0.01), int(minimum_value-minimum_value*random_value*0.01)]
            plus_minus_tolerance_max = [int(maximum_value+maximum_value*random_value*0.01), int(maximum_value-maximum_value*random_value*0.01)]

            choose_item = random.randint(0, 1)
            a, draw = self.create_random_list(plus_minus_tolerance_min[choose_item],
                                              plus_minus_tolerance_max[choose_item], height)
            draw = [x + y1 for x in draw]

            last = y1
            for each in draw:
                if each < y2:
                    img = cv2.line(img, (int(x1), int(each)), (int(x2), int(each)), color_tuple, thickness=thick)
                    a = (int(x1), int(x2), int(last), int(each))
                    new_vertical_division_list.append(a)
                    last = each
                else:
                    each = y2
                    a = (int(x1), int(x2), int(last), int(each))
                    new_vertical_division_list.append(a)
                    last = each
        return img, new_vertical_division_list

    def divide_horizontally_l4(self, img, minimum_value=5, maximum_value=50, level_list=[], random_value=1, color_tuple=(193, 154, 141), thick=2):

        new_horizontal_division_list = []
        for points in level_list:
            x1, x2, y1, y2 = points
            width = x2 - x1
            height = y2 - y1

            plus_minus_tolerance_min = [int(minimum_value+minimum_value*random_value*0.01), int(minimum_value-minimum_value*random_value*0.01)]
            plus_minus_tolerance_max = [int(maximum_value+maximum_value*random_value*0.01), int(maximum_value-maximum_value*random_value*0.01)]
            # random_percent = random.randint(-random_value, random_value)*0.01
            # minimum_value = int(minimum_value + minimum_value*random_percent)
            # maximum_value = int(maximum_value + maximum_value*random_percent)

            choose_item = random.randint(0, 1)
            a, draw = self.create_random_list(plus_minus_tolerance_min[choose_item], plus_minus_tolerance_max[choose_item], width)
            # a, draw = self.create_random_list(minimum_value, maximum_value)
            draw = [x + x1 for x in draw]
            last = x1
            # print('\nRegion ::', points)
            for each in draw:
                # print('Region :', points, 'Line:', (int(each), int(y1)), (int(each), int(y2)))

                if each < x2:
                    # print('Lines',(int(each), int(y1)), (int(each), int(y2)))
                    img = cv2.line(img, (int(each), int(y1)), (int(each), int(y2)), color_tuple, thickness=thick)
                    a = (int(last), int(each), int(y1), int(y2))
                    last = each
                    new_horizontal_division_list.append(a)
                else:
                    each = x2
                    # print('Lines',(int(each), int(y1)), (int(each), int(y2)))
                    # img = cv2.line(img, (int(each), int(y1)), (int(each), int(y2)), color_tuple, 2)
                    a = (int(last), int(each), int(y1), int(y2))
                    last = each
                    new_horizontal_division_list.append(a)
            # last_element = new_horizontal_division_list[-1]
            # new_horizontal_division_list.remove(last_element)
        return img, new_horizontal_division_list


# if __name__ == '__main__':
#     dl = DesignLogic()
#     r_list, sum_list = dl.create_random_list(75, 150, 900)
#     print(r_list, sum_list)



