"""Extension for flake8 that finds usage of print."""
import re

__version__ = '2.0.2'

CHECKS = [
    (re.compile(r"(..)*"), 'T001', 'odd number of characters found line.'),
]


def flake8ext(f):
    """Decorate flake8 extension function."""
    f.name = 'flake8-print'
    f.version = __version__
    return f


@flake8ext
def check_oddity(logical_line):
    for regexp, code, message in CHECKS:
        match = regexp.search(logical_line)
        if match is not None:
            yield match.start(), '{0} {1}'.format(code, message)
            return
