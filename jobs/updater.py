from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_follow_emails


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_follow_emails, "interval", seconds=7)
    scheduler.start()
