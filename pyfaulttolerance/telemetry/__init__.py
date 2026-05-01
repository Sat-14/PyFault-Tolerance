"""
Telemetry instrumentation for pyfaulttolerance components.

This package provides listeners that emit metrics for all pyfaulttolerance fault tolerance
components using various backends.

Available backends:
    - OpenTelemetry: pip install pyfaulttolerance[otel]
    - StatsD: pip install pyfaulttolerance[statsd]
    - Prometheus: pip install pyfaulttolerance[prometheus]

Usage:
    # OpenTelemetry
    from pyfaulttolerance.telemetry.otel import register_listeners
    register_listeners()

    # StatsD
    from pyfaulttolerance.telemetry.statsd import register_listeners
    register_listeners()

    # Prometheus
    from pyfaulttolerance.telemetry.prometheus import register_listeners
    register_listeners()
"""
