from pyfaulttolerance.exceptions import pyfaulttoleranceError


class RateLimitExceeded(pyfaulttoleranceError):
    """
    Occurs when requester have exceeded the rate limit
    """


class EmptyBucket(pyfaulttoleranceError):
    """
    Occurs when requester have exceeded the rate limit
    """
