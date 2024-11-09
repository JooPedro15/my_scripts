import time


def timer():
    count = 0
    stop = int(input('Enter the seconds to stop.'))
    while True:
        count += 1
        time.sleep(1)
        if count == stop:
            print('ALARM')
            print(count, 'seconds passed.')
            break


def stop_watch():
    input('Press enter to start.')
    start_time = time.time()
    input("Press enter to stop.")
    end_time = time.time()

    seconds = (end_time - start_time)
    minutes = seconds // 60
    seconds = seconds % 60

    print('Time: {}:{}'.format(int(minutes), seconds))