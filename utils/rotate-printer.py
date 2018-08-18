#!/usr/bin/env python3

"""
Used to print the logic that is in rotate_444() and rotate_555() in
https://github.com/dwalton76/rubiks-cube-lookup-tables/blob/master/rotate.c
"""

from copy import copy
from pprint import pformat
from rubikscubennnsolver import RubiksCube
from rubikscubennnsolver.RubiksCube222 import solved_222, moves_222
from rubikscubennnsolver.RubiksCube333 import solved_333, moves_333
from rubikscubennnsolver.RubiksCube444 import solved_444, moves_444
from rubikscubennnsolver.RubiksCube555 import solved_555, moves_555
from rubikscubennnsolver.RubiksCube666 import solved_666, moves_666
from rubikscubennnsolver.RubiksCube777 import solved_777, moves_777
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

build_rotate_xxx_c = True


if build_rotate_xxx_c:
    print("""
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "rotate_xxx.h"

""")

for (size, solved_state) in (
    (2, solved_222),
    (3, solved_333),
    (4, solved_444),
    (5, solved_555),
    (6, solved_666),
    (7, solved_777),
    ):

    cube = RubiksCube(solved_state, 'URFDLB')
    max_square_index = size * size * 6

    # Change each value to be equal to its square position
    for x in range(1, max_square_index+1):
        cube.state[x] = str(x)

    original_state = copy(cube.state)

    if size == 2:
        steps = moves_222

    elif size == 3:
        steps = moves_333

    elif size == 4:
        steps = moves_444

    elif size == 5:
        steps = moves_555

    elif size == 6:
        steps = moves_666

    elif size == 7:
        steps = moves_777

    else:
        raise Exception("Add support for size %s" % size)

    steps = list(steps)
    steps.extend(["x", "x'", "y", "y'", "z", "z'"])

    if build_rotate_xxx_c:
        print("void")
        print("rotate_%d%d%d(char *cube, char *cube_tmp, int array_size, move_type move)" % (size, size, size))
        print("{")
        print("    /* This was contructed using utils/rotate-printer.py */")
        print("    memcpy(cube_tmp, cube, sizeof(char) * array_size);")
        print("")
        first_step = True

        for step in steps:
            cube.rotate(step)
            cube.print_case_statement_C(step, first_step)
            cube.state = copy(original_state)
            first_step = False

        print(r'''
    default:
        printf("ERROR: invalid move %d\n", move);
        exit(1);
    }
}
''')

    else:
        rotate_mapper = {}

        for step in steps:
            step_pretty = step.replace("'", "_prime")
            function_name = "rotate_%d%d%d_%s" % (size, size, size, step_pretty)
            rotate_mapper[step] = function_name

            cube.rotate(step)
            rotate_mapper[step] = cube.print_case_statement_python(function_name, step)
            cube.state = copy(original_state)

        print("swaps_%d%d%d = %s" % (size, size, size, pformat(rotate_mapper, width=10024)))
        print("\ndef rotate_%d%d%d(cube, step):" % (size, size, size))
        print("    return [cube[x] for x in swaps_%d%d%d[step]]" % (size, size, size))
        print("")
