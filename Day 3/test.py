import sys
sys.path.append('./Day 3')

from funcs import *
from test_cases import *
from utils import _timing_wrapper

test = _timing_wrapper(negate)
test(test_case_1)
test(test_case_2)
test(test_case_3)
test(test_case_4)
# Test cases 5 to 9 may take longer to execute
test(test_case_5)
test(test_case_6)
test(test_case_7)
test(test_case_8)
test(test_case_9)
test = _timing_wrapper(looping)
test(test_case_1)
test(test_case_2)
test(test_case_3)
test(test_case_4)
# Test cases 5 to 9 may take longer to execute
test(test_case_5)
test(test_case_6)
test(test_case_7)
test(test_case_8)
test(test_case_9)
