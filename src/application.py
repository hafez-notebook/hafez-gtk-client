# main.py
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
# ‚?B°E”rKV

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gdk, Gio, Adw
from .window import HafezWindow


class HafezApplication(Adw.Application):

    def __init__(self):
        super().__init__(application_id='ir.hafeznote.Hafez',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action('quit', self.quit, ['<primary>q'])
        self.create_action('about', self.on_about_action)


    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = HafezWindow(application=self)
        win.present()

    def on_about_action(self, widget, _):
        about = Adw.AboutWindow(transient_for=self.props.active_window,
            application_name='Hafez',
            application_icon='ir.hafeznote.Hafez',
            developer_name='Seyed Hosein Mousavi Fard',
            version='0.0.1',
            comments="Hafez notebook Gtk client (A federated note saving app)",
            issue_url="https://github.com/hafez-notebook/hafez-gtk-client/issues",
            copyright="Seyed Hosein Mousavi Fard",
            license_type=Gtk.License.GPL_3_0,
            developers=['Seyed Hosein Mousavi Fard <shmf1385@protonmail.com>'],
            )
        about.present()


    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    """The application's entry point."""
    app = HafezApplication()
    return app.run(sys.argv)

