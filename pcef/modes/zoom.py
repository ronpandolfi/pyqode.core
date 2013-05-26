#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PCEF - PySide Code Editing framework
# Copyright 2013, Colin Duquesnoy <colin.duquesnoy@gmail.com>
#
# This software is released under the LGPLv3 license.
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
""" This module contains the editor zoom mode """
import copy
from PySide.QtCore import Qt
from PySide.QtGui import QKeyEvent
from PySide.QtGui import QWheelEvent
from pcef.core import Mode
from pcef import style


class EditorZoomMode(Mode):
    """
    Zoom in/out mode. (the editor font is increased/decreased)
    """
    #: Mode identifier
    IDENTIFIER = "Editor zoom"
    #: Mode description
    DESCRIPTION = "Zoom the editor with ctrl+mouse wheel"

    def __init__(self):
        super(EditorZoomMode, self).__init__(
            self.IDENTIFIER, self.DESCRIPTION)
        self.prev_delta = 0
        self.default_font_size = style.DEFAULT_FONT_SIZE

    def _onStateChanged(self, state):
        if state is True:
            self.editor.codeEdit.mouseWheelActivated.connect(
                self.__onWheelEvent)
            self.editor.codeEdit.keyPressed.connect(self.__onKeyPressed)
        else:
            self.editor.codeEdit.mouseWheelActivated.disconnect(self.__onWheelEvent)
            self.editor.codeEdit.keyPressed.disconnect(self.__onKeyPressed)

    def _onStyleChanged(self):
        pass

    def __onKeyPressed(self, event):
        """
        Resets editor font size to the default font size
        :param event: wheelEvent
        :type event: QKeyEvent
        :return:
        """
        if (event.key() == Qt.Key_0 and
                event.modifiers() & Qt.ControlModifier > 0):
            style = copy.copy(self.currentStyle)
            style.fontSize = self.default_font_size
            event.stop = True
            self.editor.currentStyle = style

    def __onWheelEvent(self, event):
        """
        Increments or decrements editor fonts settings on mouse wheel event
        if ctrl modifier is on.
        :param event: wheel event
        :type event: QWheelEvent
        """
        delta = event.delta()
        if event.modifiers() & Qt.ControlModifier > 0:
            style = copy.copy(self.currentStyle)
            increment = 5
            if delta < self.prev_delta:
                style.fontSize -= increment
            else:
                style.fontSize += increment
            if style.fontSize <= 0:
                style.fontSize = increment
            event.stop = True
            self.editor.currentStyle = style