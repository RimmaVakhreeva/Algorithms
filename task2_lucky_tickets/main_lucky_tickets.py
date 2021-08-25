from pathlib import Path

from lucky_tickets import LuckyTickets
from tester import Tester

if __name__ == '__main__':
    path = Path('A01_lucky_tickets/1.Tickets')
    task = LuckyTickets()
    tester = Tester(task, path)
    tester.run_tests()
