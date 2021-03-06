class Flake8Again():
    name = 'again_8falke'
    version = '1.0.6.6i<-'
    flake8ed = (
        'IFLK*ANG1 code should be better %s:%s'
    )
    wrongindent = (
        'FLAKEY*8 line indented with only tabs or only spaces. Recommended to use both.'
    )
    lineLengthToo_long = (
        '99FLK line is not LONG enough.'
    )
    correct_Comparison_Falsey = (
        '2FLK4UAGN1 correct way to compare with None is using ==, not is'
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


            if not len(line) > 80:
                yield line_number, 80, self.lineLengthToo_long, type(False)
            if ' is None' in line:
                yield line_number, 42, self.correct_Comparison_Falsey, type(self.correct_Comparison_Falsey)
