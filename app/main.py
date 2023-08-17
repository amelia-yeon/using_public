import time

from common import env, exception
from controller.get_data import GetPublicData as ctrl_getpublic
from common.logger import LoggerFactory
from apscheduler.schedulers.background import BackgroundScheduler

LoggerFactory.create_logger()

# sched = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')
# sched.start()


# @sched.scheduled_job('cron', minute='2')
# def time_print():
#     print(f'test: {time.strftime("%H:%M:%S")}')

# 공공 API Bigquery 테이블에 저장 -> 나중에 배치 까지 적용할 것 - 아래 부분 배치 
# @sched.scheduled_job('cron', day_of_week=env.RENOVATION_DAY, hour='00', minute='30')
# @sched.scheduled_job('cron', hour='12', minute='30')

def public_api():
    # data = ctrl_getpublic().property()
    data = '1234'
    print(data)
    return {'data' : data}

public_api()




