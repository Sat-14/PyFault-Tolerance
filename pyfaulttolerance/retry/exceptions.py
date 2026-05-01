from pyfaulttolerance.exceptions import pyfaulttoleranceError


class AttemptsExceeded(pyfaulttoleranceError):
    """
    Occurs when all attempts were exceeded with no success
    """
