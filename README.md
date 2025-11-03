# ShopFlow: A SOLID & Clean Architecture Example in Python

A real-world example demonstrating **SOLID principles** and **Clean Architecture** in Python — built specifically for the book  
**["SOLID Principles in Python: A Hands-On Guide for All Developers"]**
by **Fernando Antunes de Magalhães**.

---

## What is ShopFlow?

**ShopFlow** is a minimal yet realistic order-processing system designed to illustrate how core software design principles translate into clean, maintainable, and testable code. Unlike toy examples, ShopFlow models a cohesive slice of a real e-commerce backend—including order creation, inventory checks, payment processing, and SMS notifications—while strictly adhering to:

- **SOLID** design principles  
- **Clean Architecture** layering (Entities, Use Cases, Interfaces, Frameworks & Drivers)  
- Explicit dependency inversion and interface segregation  
- Testability and separation of concerns  

This project serves as a companion to the book, showing both **correct implementations** and **common violations**—with clear explanations of why design choices matter in practice.

---

## About the Book

*"SOLID Principles in Python: A Hands-On Guide for All Developers"* is a practical guide for developers at any level who want to write robust, scalable, and maintainable Python applications. Through realistic examples like ShopFlow, the book bridges theory and practice—helping you recognize anti-patterns, refactor legacy code, and build systems that evolve gracefully.

---

## Project Structure (Clean Architecture)

```
shopflow/
├── domain/              # Enterprise business rules (pure Python)
├── application/         # Use cases and application services
├── infrastructure/      # External concerns (DB, SMS, Payments, etc.)
├── interfaces/          # API adapters, CLI, or web entry points
└── main.py              # Composition root (dependency wiring)
```