from interfaces.storage_interface import StorageInterface
from interfaces.ui_interface import UIInterface
from managers.event_manager import EventManager
from managers.finance_manager import FinanceManager
from models.competition import Competition
from models.monthly_subscription import MonthlySubscription
from models.annual_subscription import AnnualSubscription
from datetime import date
from services.report_generator import ReportGenerator


def run_application(storage: StorageInterface, ui: UIInterface):
    """Main application logic with dependency injection (DIP)."""
    # Load members via storage abstraction
    members = storage.load_members()

    event_manager = EventManager()
    finance_manager = FinanceManager()

    # Create Event (OCP subclasses)
    competition = Competition(
        "Local Championship", "Football competition between local clubs",
        date(2025, 3, 15), organizer=members[0], sport_type="Football"
    )

    # Register participants (using EventManager for SRP compliance)
    event_manager.add_event(competition)
    for m in members:
        event_manager.register_member_for_event(competition, m)

    # Payments
    sub1 = MonthlySubscription(members[0], 2000)
    sub2 = AnnualSubscription(members[1], 10000)

    finance_manager.process(sub1)
    finance_manager.process(sub2)

    # Display results via UI abstraction
    event_details = event_manager.display_event_details(competition)
    transactions = finance_manager.list_transactions()
    ui.show_results(event_details, transactions)

    # Generate report
    report = ReportGenerator(members, [competition], [sub1, sub2])
    report.generate_html()


if __name__ == "__main__":
    # DIP - Dependency Injection: Choose implementations here
    # Storage implementations
    from storage.csv_storage import CSVStorage
    
    # UI implementations - switch between CLI and Web
    from ui.cli_ui import CLIUI
    from ui.web_ui import WebUI
    
    # Choose storage implementation
    storage = CSVStorage("members.csv")
    
    # Choose UI implementation (CLI or Web)
    # Uncomment the one you want to use:
    ui = CLIUI()  # For command-line interface
    # ui = WebUI("web_output.html")  # For web interface
    
    # Run application with injected dependencies
    run_application(storage, ui)