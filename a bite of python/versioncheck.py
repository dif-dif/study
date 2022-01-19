import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn('You need at least a Python 3.0 for this programm, \
        RuntimeWarning')
else:
    print('A normal continuation')