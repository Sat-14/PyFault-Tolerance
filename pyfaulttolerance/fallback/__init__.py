from pyfaulttolerance.fallback.api import fallback
from pyfaulttolerance.fallback.events import FallbackListener, register_fallback_listener

__all__ = ("fallback", "FallbackListener", "register_fallback_listener")
