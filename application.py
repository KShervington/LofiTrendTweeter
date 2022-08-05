from flask import Flask
import trendGetter
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

application = Flask(__name__)

@application.route("/")
def index():
    return "Follow @DailyTrend1011!"

def job():
    trendGetter.main()
    print("Success")

scheduler = BackgroundScheduler()
scheduler.add_job(func=job, trigger="interval", days=1)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    application.run(port=5000, debug=True)