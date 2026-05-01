from pyfaulttolerance.exceptions import pyfaulttoleranceError


class BulkheadFull(pyfaulttoleranceError):
    """
    Occurs when execution requests has exceeded allowed amount
    """
