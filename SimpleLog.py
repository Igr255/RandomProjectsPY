class Log(object):
    def __init__(self, name):
        self.name = name
        self.file = open(self.name, 'w')

    def logging(self, text):
        self.file.write(text + "\n")
        return self.file

    def __enter__(self):
        self.file.write("Begin\n")
        return self

    def __exit__(self, *exec):
        if exec is not None:
            self.file.write("End")
        return True

    '''def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.file.write("Exception has been held.\n")
        self.file.write("End")
        return True'''


with Log('mylog.txt') as logfile:
    logfile.logging('Test1')
    logfile.logging('Test2')
    a = 1/0
    logfile.logging('Test3')