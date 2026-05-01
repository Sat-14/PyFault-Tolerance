---
hide:
  - feedback
---

# pyfaulttolerance

<p align="center">
  <a href="https://github.com/roma-glushko/pyfaulttolerance" target="_blank">
    <img loading="lazy" src="https://raw.githubusercontent.com/roma-glushko/pyfaulttolerance/main/img/pyfaulttolerance-logo.png" alt="pyfaulttolerance">
  </a>
</p>
<p align="center">
    <em>🧘‍♂️️ Lightweight fault tolerance primitives for your resilient and modern Python microservices</em>
</p>
<p align="center">
<a href="https://pypi.org/project/pyfaulttolerance" target="_blank">
    <img loading="lazy" src="https://img.shields.io/pypi/v/pyfaulttolerance?color=%2318afba&label=pypi%20package" alt="Package Version">
</a>
<a href="https://pypi.org/project/pyfaulttolerance" target="_blank">
    <img loading="lazy" src="https://img.shields.io/pypi/dm/pyfaulttolerance?color=%2318afba" alt="Downloads">
</a>
<a href="https://pypi.org/project/pyfaulttolerance" target="_blank">
  <img loading="lazy" src="https://img.shields.io/pypi/pyversions/pyfaulttolerance.svg?color=%2318afba" alt="Supported Python Versions">
</a>

<br/>

<a href="https://pyfaulttolerance.readthedocs.io/en/latest/?badge=latest">
    <img loading="lazy" src="https://readthedocs.org/projects/pyfaulttolerance/badge/?version=latest&color=%2318afba" alt='Documentation Status' />
</a>
<a href="https://github.com/roma-glushko/pyfaulttolerance/actions/workflows/tests.yml">
    <img loading="lazy" src="https://github.com/roma-glushko/pyfaulttolerance/actions/workflows/tests.yml/badge.svg?branch=main" alt='Test Status' />
</a>
<a href="https://app.codecov.io/github/roma-glushko/pyfaulttolerance">
    <img loading="lazy" src="https://img.shields.io/codecov/c/gh/roma-glushko/pyfaulttolerance" alt="Coverage" />
</a>
</p>

---

**pyfaulttolerance** (/ˈhʌɪx/) is a set of well-known stability patterns that are commonly needed
when you build [microservice-based](https://en.wikipedia.org/wiki/Microservices) applications.
pyfaulttolerance is meant to be [Hystrix (Java)](https://github.com/Netflix/Hystrix), [resilience4j (Java)](https://github.com/resilience4j/resilience4j) or [Polly (C#)](https://github.com/App-vNext/Polly) but for the Python world.

!!! note

    This project is under active development and testing in production. Your feedback and help are highly appreciated!

## Key Features

- Implements five commonly used resiliency patterns with various configurations based on advice and experience of industry leaders (e.g. AWS, Google, Netflix)
- Idiomatic Pythonic implementation based on [decorators](https://realpython.com/primer-on-python-decorators) and [context managers](https://realpython.com/python-with-statement)
- [AsyncIO](https://docs.python.org/3/library/asyncio.html) Native Implementation
- Built-in [telemetry](./telemetry.md) support for OpenTelemetry, Prometheus, and StatsD
- Lightweight. Readable Codebase. High Test Coverage

!!! warning
    At this stage, pyfaulttolerance prioritizes speed of development over API stability. 
    This is going to change once we implement [main features and use cases](./roadmap.md#m2-pixi).

## Requirements

- Python 3.9+
- AsyncIO-powered applications ([no sync support?](./faq.md))

## Installation

pyfaulttolerance can be installed from [PyPi](https://pypi.org/project/pyfaulttolerance):

=== "pip"

    ``` sh
    pip install pyfaulttolerance
    ```

=== "uv"

    ```sh
    uv add pyfaulttolerance
    ```

## Components

Here is a short overview of pyfaulttolerance's components:

| Component                                              | Problem                                                                                                                                                                            | Solution                                                                                                                                                                      | Implemented? |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [🔁 Retry](./components/retry.md)                      | Failures happen sometimes, but they self-recover after a short time                                                                                                                | Automatically retry operations on temporary failures                                                                                                                          | ✅            |
| 💾 Cache                                               |                                                                                                                                                                                    |                                                                                                                                                                               |              |
| [⚡️ Circuit Breaker](./components/circuit_breakers.md) | When downstream microservices become overloaded, sending even more load only makes things worse                                                                                    | Temporarily stop sending requests to failing microservices when error thresholds are exceeded. Then check if the pause helped them recover                                    | ✅            |
| [⏱ Timeout](./components/timeout.md)                   | Sometimes operations take too long. We can't wait forever, and after a certain point success becomes unlikely                                                                      | Bound waiting to a reasonable amount of time                                                                                                                                  | ✅            |
| [🚰 Bulkhead](./components/bulkhead.md)                | Without limits, some code can consume too many resources, bringing down the whole application (and upstream services) or slowing down other parts                                  | Limit the number of concurrent calls, queue excess calls, and fail calls that exceed capacity                                                                                 | ✅            |
| [🏃‍♂️ Rate Limiter](./components/rate_limiter.md)     | A microservice can be called at any rate, including one that could bring it down if triggered accidentally                                                                         | Limit the rate at which your system can be accessed                                                                                                                           | ✅            |
| [🤝 Fallback](./components/fallback.md)                | Nothing guarantees that your dependencies will work. What do you do when they fail?                                                                                                | Degrade gracefully by providing default values or placeholders when dependencies are down                                                                                     | ✅            |

<p align="right">
    Inspired by <a href="https://github.com/App-vNext/Polly#resilience-policies" target="_blank">Polly's Resiliency Policies</a>
</p>

## Stay Tuned

pyfaulttolerance is a young but rapidly evolving project. 
There are [tons of things we want to support and integrate with](roadmap.md) to make pyfaulttolerance suitable for different frameworks and use cases.

If you don't want to miss our updates, consider the following options:

* give pyfaulttolerance a star and watch in [Github](https://github.com/roma-glushko/pyfaulttolerance) 
* follow Roman Hlushko (the creator of pyfaulttolerance) in [LinkedIn and other social media](https://www.romaglushko.com)

## Thanks

!!! quote

    We are staying on the shoulders of giants (c)

There are some open source projects and other resources that heavily influenced and inspired pyfaulttolerance to emerge.
Without those projects and people behind them, pyfaulttolerance wouldn't have been created. 
So I wanted to pause for a moment to say a huge thanks wholeheartedly :heart: to:

- [App-vNext/Polly](https://github.com/App-vNext/Polly)
- [resilience4j/resilience4j](https://github.com/resilience4j/resilience4j)
- and tons of other projects previously published on the similar topics

## License

This project is licensed under the terms of the [Apache 2.0 license](https://github.com/roma-glushko/pyfaulttolerance/blob/main/LICENSE).
