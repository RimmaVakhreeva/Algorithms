from pathlib import Path


class Tester:
    def __init__(self, task, path):
        self.task = task
        self.path = path

    def run_test(self, in_file, out_file):
        try:
            data = in_file.read_text()
            data = data.rstrip()
            expect = out_file.read_text()
            expect = expect.rstrip()
            actual = self.task.run(data)
            return actual == expect
        except:
            return False

    def run_tests(self):
        nr = 0
        while True:
            in_file = Path(self.path / f'test.{nr}.in')
            out_file = Path(self.path / f'test.{nr}.out')
            if not in_file.exists() and not out_file.exists():
                break
            result = self.run_test(in_file, out_file)
            print(f'Test #{nr} - ' + str(result))
            nr += 1
