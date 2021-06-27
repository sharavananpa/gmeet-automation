import subprocess

def main():
    schedule = input('Enter name of the schedule: ')
    browser = input('Enter name of the browser: ')

    subprocess.run(f'python runner.py -s {schedule} -b {browser}')

if __name__ == "__main__":
    print('Scheduling process started!\n')
    main()
    print('\nSchedule complete!')