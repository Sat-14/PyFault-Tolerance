from typing import TYPE_CHECKING, Any

from pyfaulttolerance.events import ListenerFactoryT, ListenerRegistry
from pyfaulttolerance.fallback.typing import ResultT

if TYPE_CHECKING:
    from pyfaulttolerance.fallback.manager import FallbackManager

_FALLBACK_LISTENERS: ListenerRegistry["FallbackManager", "FallbackListener"] = ListenerRegistry()


class FallbackListener:
    async def on_fallback(self, fallback: "FallbackManager", result: ResultT, *args: Any, **kwargs: Any) -> None: ...


def register_fallback_listener(listener: FallbackListener | ListenerFactoryT) -> None:
    """
    Register a listener that will listen to all fallback components in the system
    """
    global _FALLBACK_LISTENERS

    _FALLBACK_LISTENERS.register(listener)
