import io
from os import write
import sys
from pathlib import Path
from tqdm import tqdm
from importlib import reload


start_n = 0

file_input = './sample/sample-input-{}.txt'.format
file_output = './sample/sample-output-{}.txt'.format

good_count = 0
bad_count = 0
file_num = len(list(Path('./sample').iterdir()))
for i in tqdm(range(start_n, file_num // 2)):
    i += 1
    sample_input = Path(file_input(i)).read_text()
    sample_output = Path(file_output(i)).read_text()
    i -= 1

    with io.StringIO(sample_input) as stdin, io.StringIO() as stdout:
        sys.stdin, stdin_old = stdin, sys.stdin
        sys.stdout, stdout_old = stdout, sys.stdout

        if 'main' not in locals():
            import main
        else:
            reload(main)

        output = stdout.getvalue()[:-1]

        sys.stdin = stdin_old
        sys.stdout = stdout_old

    if sample_output != output:
        print(i)
        print('-' * 20)
        print(f"sample_input=\n{sample_input}")
        print('-' * 20)
        print(f"sample_output=\n{sample_output}")
        print('-' * 20)
        print(f"output=\n{output}")
        print('=' * 40)

        assert False
        bad_count += 1
    else:
        good_count += 1

print(f"{f'{good_count=:2}':>40}")
print(f"{f'{bad_count=:2}':>40}")
print(f"{f'{good_count + bad_count=:2}':>40}")
print(f"{f'{file_num // 2=:2}':>40}")
print(f"{f'{file_num=:2}':>40}")
