# 🛡️ PyFault-Tolerance: Bulletproof Python Microservices

Hello! Welcome to **PyFault-Tolerance**. 

If you've ever built microservices, you know that things inevitably go wrong. Networks drop, third-party APIs go down, and databases get overloaded. I built this library to give Python developers a simple, elegant toolkit to handle these failures gracefully.

Think of it as a safety net for your code—protecting your system from crashing entirely just because one small piece failed.

## ✨ What Does It Do?

It provides five essential stability patterns that you can wrap around your code easily:
1. **Circuit Breaker**: Stops sending traffic to a broken service until it recovers.
2. **Retry**: Automatically tries an operation again if it fails momentarily.
3. **Timeout**: Prevents your code from waiting forever on a slow response.
4. **Bulkhead**: Limits how many resources one specific task can consume.
5. **Rate Limiter**: Controls the speed of incoming traffic so you don't get overwhelmed.

## 📊 How They Work Together

Here is a simplified flowchart showing how these patterns protect a request before it reaches an external service:

```mermaid
flowchart LR
    %% Friendly styling
    classDef client fill:#E1BEE7,stroke:#8E24AA,stroke-width:2px,color:#333,rx:10,ry:10
    classDef protection fill:#BBDEFB,stroke:#1976D2,stroke-width:2px,color:#333,rx:5,ry:5
    classDef external fill:#FFCC80,stroke:#F57C00,stroke-width:2px,color:#333,rx:10,ry:10
    classDef error fill:#FFCDD2,stroke:#D32F2F,stroke-width:2px,color:#333,rx:10,ry:10

    Req(["👤 User Request"]):::client --> CB{"Circuit Breaker\n(Is service healthy?)"}:::protection
    
    CB -- Yes --> RL{"Rate Limiter\n(Too fast?)"}:::protection
    CB -- No (Broken) --> FB["Fallback\n(Show default data)"]:::error
    
    RL -- Allowed --> BH{"Bulkhead\n(Too busy?)"}:::protection
    RL -- Denied --> FB
    
    BH -- Space available --> RT{"Retry\n(Try 3 times)"}:::protection
    BH -- Full --> FB
    
    RT -- "Call API" --> Ext["🌐 External Service"]:::external
    Ext -.->|Fails| RT
    
    Ext -->|Success| Success(["✅ Fast Response!"]):::client
    RT -.->|All attempts failed| FB
```

## 🚀 Getting Started

It is fully async-native and built on top of modern Python `asyncio`. I've kept the codebase lightweight and highly readable, so you can easily understand what's happening under the hood.

Just install it and start wrapping your tricky network calls!
