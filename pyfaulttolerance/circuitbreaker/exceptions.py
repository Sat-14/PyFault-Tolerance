from pyfaulttolerance.exceptions import pyfaulttoleranceError


class BreakerFailing(pyfaulttoleranceError):
    """
    Occurs when you try to execute actions that was identified as failing by the circuit breaker
    """
