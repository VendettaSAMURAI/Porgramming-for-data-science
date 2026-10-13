#!/usr/bin/env python3

import math


def distance(p1, p2):
    # TODO...
    x1 ,y1 =p1
    x2 , y2 =p2
    
    return math.sqrt((x2-x1)**2 +(y2-y1)**2)


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('The distance between the two points:', distance(p1, p2))

############################################################################

if __name__ == "__main__":
    main()