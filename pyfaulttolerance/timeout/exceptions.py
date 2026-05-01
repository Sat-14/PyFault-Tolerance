from pyfaulttolerance.exceptions import pyfaulttoleranceError


class MaxDurationExceeded(pyfaulttoleranceError):
    """
    Occurs if some task took more time than it was given
    """
