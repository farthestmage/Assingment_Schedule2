from datetime import datetime

def calculate_tat(added_on: str, sent_time: datetime) -> float:
    """
    Returns TAT in minutes
    """
    added_on_dt = datetime.strptime(added_on, "%Y-%m-%d %H:%M:%S")
    tat_minutes = (sent_time - added_on_dt).total_seconds() / 60
    return round(tat_minutes, 2)
