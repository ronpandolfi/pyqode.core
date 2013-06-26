#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PCEF - Python/Qt Code Editing Framework
# Copyright 2013, Colin Duquesnoy <colin.duquesnoy@gmail.com>
#
# This software is released under the LGPLv3 license.
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""
This module contains the definition of a panel mode
"""
import pcef
from pcef.qt import QtGui
from pcef.core.mode import Mode


class Panel(QtGui.QWidget, Mode):
    """
    Base class for editor panels.

    A panel is a mode and a widget.

    Panels are drawn in the QCodeEdit viewport margins.
    """
    def __init__(self):
        """
        :param name: Panel name (used as an identifier)
        :param description: The panel description
        :return:
        """
        pcef.core.mode.Mode.__init__(self)
        QtGui.QWidget.__init__(self)

    def install(self, editor):
        """
        Extends the Mode.install method to set the editor instance
        as the parent widget.

        :param editor: QCodeEdit instance
        """
        Mode.install(self, editor)
        self.setParent(editor)
        self.editor.updateViewportMargins()

    def onStateChanged(self, state):
        """ Shows/Hides the Panel

        :param state: True = enabled, False = disabled
        :type state: bool
        """
        if state is True:
            self.show()
            self.editor.updateViewportMargins()
        else:
            self.hide()
            self.editor.updateViewportMargins()
