from pathlib import Path
import pandas as pd

class ReportGenerator:
    """
    SRP-Compliant:
    - This class ONLY generates an HTML report.
    - It does NOT load data or manage events/subscriptions.
    """

    def __init__(self, members, events, subscriptions):
        self.members = members
        self.events = events
        self.subscriptions = subscriptions

    def generate_html(self, output_file="association_report.html"):
        # Convert Members to DataFrame
        members_df = pd.DataFrame([{
            "Full Name": m.full_name,
            "Role": m.__class__.__name__,
            "Email": m.email,
            "Phone": m.phone,
            "Address": m.address,
            "Join Date": m.join_date,
            "Skills": ", ".join(m.skills) if m.skills else "—",
            "Interests": ", ".join(m.interests) if m.interests else "—"
        } for m in self.members])

        # Convert Events to DataFrame
        events_df = pd.DataFrame([{
            "Event Name": e.name,
            "Type": e.__class__.__name__,
            "Description": e.description,
            "Date": e.date,
            "Organizer": e.organizer.full_name,
            "Participants": ", ".join([p.full_name for p in e.participants])
        } for e in self.events])

        # Convert Subscriptions to DataFrame
        def get_member_or_donor(sub):
            """Extract member name or donor name from subscription/donation."""
            if hasattr(sub, "member") and sub.member:
                return sub.member.full_name
            return getattr(sub, "donor_name", "N/A")
        
        subs_df = pd.DataFrame([{
            "Member/Donor": get_member_or_donor(s),
            "Type": s.__class__.__name__,
            "Amount": s.amount,
            "Status": getattr(s, "status", "N/A")  # Donation doesn't have status
        } for s in self.subscriptions])

        # Dark themed HTML styling
        html = [
            '<!doctype html>',
            '<html><head><meta charset="utf-8"><title>Association Report</title>',
            '<style>',
            'body{padding:24px;background:#0b1220;color:#e2e8f0;font-family:Arial, sans-serif;}',
            'h1{color:#f8fafc;} h2{margin-top:24px;color:#93c5fd;}',
            'table{width:100%;border-collapse:collapse;margin-bottom:20px;background:#111827;}',
            'th,td{border-bottom:1px solid #1f2937;padding:10px 12px;text-align:left;}',
            'th{background:#0b1220;color:#93c5fd;text-transform:uppercase;font-size:13px;}',
            'tbody tr:nth-child(even){background:#0c1627;} tbody tr:hover{background:#12233a;}',
            '</style></head><body>',
            '<h1>Sports Association Report</h1>',
            '<h2>Members</h2>', members_df.to_html(index=False, escape=False),
            '<h2>Events</h2>', events_df.to_html(index=False, escape=False),
            '<h2>Subscriptions & Donations</h2>', subs_df.to_html(index=False, escape=False),
            '</body></html>'
        ]

        Path(output_file).write_text("\n".join(html), encoding="utf-8")
        print(f"✅ HTML report generated: {output_file}")
