import os

# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

from anki.hooks import wrap
from aqt.clayout import CardLayout


from . import css
from . import html


highlighters = {'html': html.HtmlHighlighter,
                'css': css.CssHighlighter}


def showMore(obj):
    showInfo('Type: {}\nstr(): {}'.format(type(obj), str(obj)))


def attach_highlighter(self):
    mw.my_widgets = []
    editors = {'html': [self.tform.front, self.tform.back],
               'css':  [self.tform.css]}

    # TODO: test this on other platforms besides Linux
    monospace = QFont('Monospace')
    monospace.setStyleHint(QFont.TypeWriter)
    mw.my_widgets.append(monospace)

    for language, text_edits in editors.items():
        for text_edit in text_edits:
            text_edit.setFont(monospace)
            highlighter = highlighters[language]
            highlighter_widget = highlighter(text_edit.document())
            mw.my_widgets.append(highlighter_widget)


CardLayout.readCard = wrap(CardLayout.readCard, attach_highlighter)
