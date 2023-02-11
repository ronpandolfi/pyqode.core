"""
Extends the checker mode example with a global checker panel (that shows all
the error found in the document).
"""
import logging
logging.basicConfig(level=logging.DEBUG)
import sys

from qtpy import QtWidgets
from pyqode.core.api import CodeEdit
from pyqode.core.panels import GlobalCheckerPanel
from pyqode.core.modes import CheckerMode, CheckerMessages

# use server from this directory so that checker.py is in sys.path
import server


def check(request):
    """
    Worker function that performs the analysis. Here this is a dumb checker
    that always return 3 messages:
        - 1 info message on line 1
        - 1 warning message on line 2
        - 1 error message on line 3

    :param request:  request data (dict).
    :return: True, list of messages
    """
    return [
        ('An information message', CheckerMessages.INFO, 0),
        ('A warning message', CheckerMessages.WARNING, 100),
        ('An error message', CheckerMessages.ERROR, 200),
    ]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    editor = CodeEdit()
    editor.backend.start(server.__file__)
    editor.resize(800, 600)
    editor.setCenterOnScroll(False)
    # use a string instead of the function directly (otherwise we
    # get __main__.check instead of checker.check)
    # print(editor.modes.append(CheckerMode(check)))  # does not work if
                                                      # function is in main
                                                      # module
    print(editor.modes.append(CheckerMode('global_checker.check')))
    print(editor.panels.append(GlobalCheckerPanel(),
                               GlobalCheckerPanel.Position.RIGHT))

    # we could also use the pyqode.python.backend like this (uncomment the next
    # two lines if you have pyqode.python)
    # from pyqode.python.backend import run_pep8
    # print(editor.modes.append(CheckerMode(run_pep8)))
    editor.show()
    editor.setPlainText('AAA\n' * 500, '', '')
    app.exec_()
    editor.close()
    del editor
    del app