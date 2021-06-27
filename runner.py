import asyncio
import time
import subprocess
import json
import argparse

with open('schedule.json', 'r') as f:
    data = json.load(f)

parser = argparse.ArgumentParser()
parser. add_argument('-s', dest='schedule', help="Type in the schedule name or id from the JSON file", required=True)
parser. add_argument('-b', dest='browser', help="Type in the browser used", required=True)
args = parser.parse_args()

email = data['credentials']['email']
password = data['credentials']['password']
details = data[args.schedule]

def get_time_diff(future):
    now = time.strftime('%X')
    H1 = int(now[0:2])*60*60
    M1 = int(now[3:5])*60
    S1 = int(now[6:8])
    H2 = int(future[0:2])*60*60
    M2 = int(future[3:5])*60
    S2 = int(future[6:8])
    now_sum = H1+M1+S1
    future_sum = H2+M2+S2
    return future_sum - now_sum

async def join_meet(time_diff, meet, desc):
    await asyncio.sleep(time_diff)
    subprocess.run(f'python automation_scripts/run_{args.browser}.py -e {email} -p {password} -m {meet} -d \"{desc}\"')

async def main():
    task_array = []
    for i in details:
        time_diff = get_time_diff(i['time'])
        if(time_diff>-60):
            task = asyncio.create_task(join_meet(time_diff, i['meet'], i['desc']))
            task_array.append(task)
    for task in task_array:
        await task
if __name__ == '__main__':
    print(f"\nStarted: {time.strftime('%X')}")
    asyncio.run(main())
    print(f"\nEnded: {time.strftime('%X')}")