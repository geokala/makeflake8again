class Flake8Again():
    name = 'again_8falke'
    version = '1.0.6.6i<-'
    flake8ed = (
        'IFLK*ANG1 code should be better %s:%s'
    )
    wrongindent = (
        'FLK8AGN1 line indented with only tabs or only spaces. Recommended to use both.'
    )
    def __init__(self, tree, filename, line_number, logical_line, lines):
        self.filename = filename
        self.line_number = line_number
        self.logical_line = logical_line
        self.lines = lines

    def run(self):
        if self.filename == 'flake8_again/__init__.py':
            # What could possibly be wrong?
            return

        for line in range(0, len(self.lines)):
            # yield line_num, column, message, type?
            yield 666, 80, self.flake8ed % (line, self.lines[line].rstrip()), type(None)

            line_number = line
            line = self.lines[line]
            tabs_found = False
            spaces_found = False
            for char in line:
                if char not in (' ', '\t'):
                    break
                elif char == ' ':
                    spaces_found = True
                elif char == '\t':
                    tabs_found = True

            yield line_number, 4, self.wrongindent, type(None)
