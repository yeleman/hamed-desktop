#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

import logging
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

logger = logging.getLogger(__name__)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    view = QWebEngineView()
    view.setUrl(QUrl("http://ramed-server"))
    view.resize(1024, 750)
    view.show()

    sys.exit(app.exec_())