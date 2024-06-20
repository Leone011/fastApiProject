from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

# 创建调度器实例
scheduler = BlockingScheduler()


# 定义任务函数
def my_task():
    print(f"Task executed at {datetime.datetime.now()}")


# 添加任务：每隔 10 秒运行一次
scheduler.add_job(my_task, 'interval', seconds=10)

# 启动调度器
try:
    print("Scheduler started.")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass
