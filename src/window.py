# window.py
#
# Copyright 2022 Haj Mousa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
# �?B�E�rKV

from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(resource_path='/ir/hafeznote/Hafez/ui/window.ui')
class HafezWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'HafezWindow'

    stack = Gtk.Template.Child()
    stack_pages = ['notebooks', 'notes']
    stack_current_page = 'first'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def next_page(self, button):
        if self.stack_current_page == self.stack_pages[-1]:
            return
        self.stack_current_page = self.stack_pages[self.stack_pages.index(self.stack_current_page) - 1]
        self.stack.set_visible_child_name(self.stack_current_page)

    def previous_page(self, button):
        if self.stack_current_page == self.stack_pages[0]:
            return
        self.stack_current_page = self.stack_pages[self.stack_pages.index(self.stack_current_page) - 1]
        self.stack.set_visible_child_name(self.stack_current_page)
