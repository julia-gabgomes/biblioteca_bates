from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_follow_emails


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_follow_emails, "cron", day_of_week="mon-fri", hour=8)
    scheduler.start()
