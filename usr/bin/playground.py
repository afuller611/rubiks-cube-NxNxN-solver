#!/usr/bin/env python3

from pprint import pformat, pprint
from rubikscubennnsolver import wing_strs_all, reverse_steps
from rubikscubennnsolver.LookupTable import steps_on_same_face_and_layer
from rubikscubennnsolver.misc import parse_ascii_777
from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_444
from rubikscubennnsolver.RubiksCube555 import (
    RubiksCube555,
    solved_555,
    edges_partner_555,
)
from rubikscubennnsolver.RubiksCube666 import (
    RubiksCube666,
    moves_666,
    solved_666,
    rotate_666,
)
from rubikscubennnsolver.RubiksCube777 import RubiksCube777, solved_777
import itertools
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)20s %(levelname)8s: %(message)s")
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))


'''
cube = RubiksCube555(solved_555, "URFDLB")
cube.cpu_mode = "normal"
cube.lt_init()
cube.lt_phase3_lr_center_stage_eo_inner_orbit.build_ida_graph()
'''


cube = RubiksCube666(solved_666, "URFDLB")
cube.cpu_mode = "normal"
cube.lt_init()
#cube.lt_UD_left_oblique_edges_stage.build_ida_graph()
#cube.lt_UD_right_oblique_edges_stage.build_ida_graph()
#cube.lt_UD_outer_x_centers_stage.build_ida_graph()
cube.lt_UD_oblique_edges_stage.build_ida_graph()

