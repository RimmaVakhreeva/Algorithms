from itask import ITask


class StringLengthTask(ITask):
    def run(self, data):
        return str(len(data))
