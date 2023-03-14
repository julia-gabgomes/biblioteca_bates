from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import send_follow_emails, block_users


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_follow_emails, "cron", day_of_week="mon-fri", hour=8)
    scheduler.add_job(block_users, "interval", seconds=7)
    # "cron", day_of_week="tue-sat", hour=1
    scheduler.start()
