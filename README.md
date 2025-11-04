📌 README : SOLID Refactor Summary:

This project is a refactored version of the Sports Association Management System (TP1 & TP2), updated to apply the SOLID principles as required in TP3.

✅ SOLID Principles Applied:

1. Single Responsibility Principle (SRP)
-Data classes now store data only (Member, Event, Subscription).
-Logic moved into separate manager classes:
MemberManager, EventManager, SubscriptionManager, and ReportGenerator.
→ Solved the issue of classes having multiple responsibilities.

2. Open/Closed Principle (OCP)
-New event types added without modifying the base class: Trip, Meeting, Competition.
-Subscription extended with: Donation, MonthlySubscription, AnnualSubscription.
→ System can now be extended without changing existing code.

3. Liskov Substitution Principle (LSP)
-display_event_details(event) works for all event subclasses.
-Each event subclass overrides describe() correctly.
→ Subclasses behave like the base Event without breaking code.

4. Interface Segregation Principle (ISP)
-Small interfaces created: Payable, Organizable, Registrable.
→ Classes only implement what they need.

5. Dependency Inversion Principle (DIP)

-High-level code depends on abstractions, not implementations.
-Introduced StorageInterface and UIInterface and injected CSV + CLI at runtime.
→ Easier to switch to JSON/Database/Web UI later.