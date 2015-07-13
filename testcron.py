from datetime import datetime

with open('testcron.txt', 'a+') as f:
    f.write('Cron Job Ran at {0}\n'.format(datetime.now()))

