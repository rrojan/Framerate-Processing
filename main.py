import os
import time


def clear():
    # for windows name is 'nt' while it is 'posix' for *nix mac / linux
    clear_cmd = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear_cmd)


def get_filecount(path):
    count = 0
    for _path in os.listdir(path):
        if os.path.isfile(os.path.join(path, _path)):
            count += 1
    return count


def main():
    MAX_ITERS = 99999999
    i = 0

    while i < MAX_ITERS:
        i += 1

        tmp_count = get_filecount('./tmp_frames')
        out_count = get_filecount('./out_frames')
        completed = '{:.2f}'.format((out_count / tmp_count) * 100)
        clear()
        print(f'Current progress:', completed, '%')
        print(f'Completed frames:', out_count)

        # Break loop if 100%. If overshoots (some frame issue) then something is wrong
        if completed == '100.00':
            break
        elif len(completed) >= 6:
            raise Exception('Tmp and out frame counts do not match')

        time.sleep(5)

    raise Exception('Maximum framecount exceeded')


if __name__ == '__main__':
    main()
