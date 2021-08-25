from pathlib import Path

from string_length_task import StringLengthTask
from tester import Tester

if __name__ == '__main__':
    path = Path('A01_lucky_tickets/0.String')
    task = StringLengthTask()
    tester = Tester(task, path)
    tester.run_tests()
