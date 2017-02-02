class Flake8Again():
    name = 'again_8falke'
    version = '1.0.6.6i<-'
    flake8ed = (
        'IFLK*ANG1 code should be better %s:%s'
    )
    def __init__(self, tree, filename, line_number, logical_line):
        self.filename = filename
        self.line_number = line_number
        self.logical_line = logical_line

    def run(self):
        # yield line_num, column, message, type?
        yield 666, 80, self.flake8ed % (self.line_number, self.logical_line), type(None)
