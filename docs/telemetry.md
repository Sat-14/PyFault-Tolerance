# Telemetry

pyfaulttolerance provides built-in telemetry support to help you monitor your fault tolerance components in production.
All components emit events that can be captured by listeners and forwarded to your observability stack.

Telemetry is built on top of pyfaulttolerance's [event system](./events.md). For details on creating custom listeners or understanding how events flow, see the Events documentation.

## Supported Backends

| Backend | Installation | Description |
|---------|--------------|-------------|
| [OpenTelemetry](#opentelemetry) | `pip install pyfaulttolerance[otel]` | Industry-standard observability framework |
| [Prometheus](#prometheus) | `pip install pyfaulttolerance[prometheus]` | Popular metrics and alerting toolkit |
| [StatsD](#statsd) | `pip install pyfaulttolerance[statsd]` | Simple daemon for aggregating statistics |

## OpenTelemetry

[OpenTelemetry](https://opentelemetry.io/) is the industry-standard observability framework for cloud-native software.

### Installation

```sh
pip install pyfaulttolerance[otel]
```

### Quick Start

Register listeners for all components with a single call:

```python
from pyfaulttolerance.telemetry.otel import register_listeners

# Uses the global meter provider
register_listeners()
```

Or with a custom meter:

```python
from opentelemetry import metrics
from pyfaulttolerance.telemetry.otel import register_listeners

meter = metrics.get_meter("my-service")
register_listeners(meter=meter)
```

### Individual Listeners

You can also register listeners for specific components:

```python
from pyfaulttolerance.telemetry.otel import RetryListener
from pyfaulttolerance.retry import retry

listener = RetryListener()

@retry(attempts=3, listeners=[listener])
async def my_function():
    ...
```

### Metrics Reference

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `pyfaulttolerance.retry.attempts` | Counter | `component`, `exception` | Number of retry attempts |
| `pyfaulttolerance.retry.exhausted` | Counter | `component` | Retry attempts exhausted |
| `pyfaulttolerance.retry.success` | Counter | `component` | Successful operations |
| `pyfaulttolerance.circuitbreaker.state_transitions` | Counter | `component`, `from_state`, `to_state` | State transitions |
| `pyfaulttolerance.circuitbreaker.success` | Counter | `component`, `state` | Successful operations |
| `pyfaulttolerance.timeout.exceeded` | Counter | `component` | Timeout exceeded |
| `pyfaulttolerance.bulkhead.rejected` | Counter | `component` | Rejected due to capacity |
| `pyfaulttolerance.fallback.triggered` | Counter | `component`, `reason` | Fallback triggered |

## Prometheus

[Prometheus](https://prometheus.io/) is an open-source monitoring and alerting toolkit.

### Installation

```sh
pip install pyfaulttolerance[prometheus]
```

### Quick Start

Register listeners for all components:

```python
from pyfaulttolerance.telemetry.prometheus import register_listeners

# Uses the default global registry
register_listeners()
```

Or with a custom registry:

```python
from prometheus_client import CollectorRegistry
from pyfaulttolerance.telemetry.prometheus import register_listeners

registry = CollectorRegistry()
register_listeners(registry=registry)
```

### Individual Listeners

```python
from pyfaulttolerance.telemetry.prometheus import CircuitBreakerListener
from pyfaulttolerance.circuitbreaker import consecutive_breaker

listener = CircuitBreakerListener()

breaker = consecutive_breaker(
    failure_threshold=5,
    recovery_time_secs=30,
    listeners=[listener],
)
```

### Metrics Reference

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
| `pyfaulttolerance_retry_attempts_total` | Counter | `component`, `exception` | Number of retry attempts |
| `pyfaulttolerance_retry_exhausted_total` | Counter | `component` | Retry attempts exhausted |
| `pyfaulttolerance_retry_success_total` | Counter | `component` | Successful operations |
| `pyfaulttolerance_circuitbreaker_state_transitions_total` | Counter | `component`, `from_state`, `to_state` | State transitions |
| `pyfaulttolerance_circuitbreaker_success_total` | Counter | `component`, `state` | Successful operations |
| `pyfaulttolerance_timeout_exceeded_total` | Counter | `component` | Timeout exceeded |
| `pyfaulttolerance_bulkhead_rejected_total` | Counter | `component` | Rejected due to capacity |
| `pyfaulttolerance_fallback_triggered_total` | Counter | `component`, `reason` | Fallback triggered |

## StatsD

[StatsD](https://github.com/statsd/statsd) is a simple daemon for aggregating statistics.

### Installation

```sh
pip install pyfaulttolerance[statsd]
```

### Quick Start

Register listeners for all components:

```python
from pyfaulttolerance.telemetry.statsd import register_listeners

# Uses default client (localhost:8125, prefix='pyfaulttolerance')
register_listeners()
```

Or with a custom client:

```python
import statsd
from pyfaulttolerance.telemetry.statsd import register_listeners

client = statsd.StatsClient('statsd.example.com', 8125, prefix='myapp')
register_listeners(client=client)
```

### Individual Listeners

```python
import statsd
from pyfaulttolerance.telemetry.statsd import TimeoutListener
from pyfaulttolerance.timeout import timeout

client = statsd.StatsClient(prefix='myapp')
listener = TimeoutListener(client=client)

@timeout(timeout_secs=5, listeners=[listener])
async def slow_operation():
    ...
```

### Metrics Reference

All metrics are prefixed with the client prefix (default: `pyfaulttolerance`).

| Metric | Type | Description |
|--------|------|-------------|
| `retry.<name>.attempts` | Counter | Retry attempt made |
| `retry.<name>.attempts.<exception>` | Counter | Retry attempt by exception type |
| `retry.<name>.exhausted` | Counter | Retry attempts exhausted |
| `retry.<name>.success` | Counter | Successful operation |
| `circuitbreaker.<name>.state.working` | Counter | Transitioned to working state |
| `circuitbreaker.<name>.state.recovering` | Counter | Transitioned to recovering state |
| `circuitbreaker.<name>.state.failing` | Counter | Transitioned to failing state |
| `circuitbreaker.<name>.success` | Counter | Successful operation |
| `timeout.<name>.exceeded` | Counter | Timeout exceeded |
| `bulkhead.<name>.rejected` | Counter | Rejected due to capacity |
| `fallback.<name>.triggered` | Counter | Fallback triggered |
| `fallback.<name>.triggered.<reason>` | Counter | Fallback by reason (exception/predicate) |

## Custom Listeners

For creating custom listeners, see the [Events documentation](./events.md#listener-interfaces).
