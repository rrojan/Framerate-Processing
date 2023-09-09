from utils import clear, get_filecount, calculate_eta
import time
import sys


def main():
    MAX_ITERS = 99999999
    i = 0

    start_time = time.time()
    first_frame_created_time = start_time

    for i in range(MAX_ITERS):
        tmp_count = get_filecount('./tmp_frames')
        out_count = get_filecount('./out_frames')

        try:
            completed = '{:.2f}'.format((out_count / tmp_count) * 100)
        except ZeroDivisionError:
            print('No frames in tmp_frames to process')
            sys.exit(0)

        eta = calculate_eta(first_frame_created_time, float(completed))

        clear()
        print(f'Current progress:', completed, '%')
        print(f'Completed frames:', out_count)
        print(f'Time remaining:', eta)

        # Break loop if 100%. If overshoots (some frame issue), then something is wrong
        if completed == '100.00':
            sys.exit(0)
        elif len(completed) >= 6:
            raise Exception('Tmp and out frame counts do not match')

        time.sleep(5)

    raise Exception('Maximum frame count exceeded')


if __name__ == '__main__':
    main()
