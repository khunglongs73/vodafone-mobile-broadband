# -*- coding: utf-8 -*-
# Copyright (C) 2006-2009  Vodafone España, S.A.
# Author:  Pablo Martí
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from os.path import join

import gtk
#from gtkmvc import View
from gui.contrib.gtkmvc import View

from gui.consts import APP_SLUG_NAME, GLADE_DIR
from gui.constx import GUI_VIEW_DISABLED, GUI_VIEW_IDLE, GUI_VIEW_BUSY
from gui.translate import _


class DiagnosticsView(View):
    """View for the main diagnostics window"""

    GLADE_FILE = join(GLADE_DIR, "diagnostics.glade")

    def __init__(self, ctrl):
        View.__init__(self, ctrl, self.GLADE_FILE, 'diagnostics_window',
                        register=False, domain=APP_SLUG_NAME)
        self.setup_view()
        ctrl.register_view(self)

    def setup_view(self):
        self.get_top_widget().set_position(gtk.WIN_POS_CENTER_ON_PARENT)

        self['ussd_entry'].set_text('')
        self.set_ussd_reply('')
        self['ussd_textview'].set_editable(False)

    def get_ussd_request(self):
        return self['ussd_entry'].get_text()

    def set_ussd_reply(self, ussd_reply):
        _buffer = self['ussd_textview'].get_buffer()
        _buffer.set_text(ussd_reply)
        self['ussd_textview'].set_buffer(_buffer)

    def set_ussd_state(self, state):
        if state is GUI_VIEW_DISABLED:
            self['send_ussd_button'].set_sensitive(False)
            self['ussd_entry'].set_sensitive(False)
        elif state is GUI_VIEW_IDLE:
            self['send_ussd_button'].set_sensitive(True)
            self['ussd_entry'].set_sensitive(True)
        elif state is GUI_VIEW_BUSY:
            self['send_ussd_button'].set_sensitive(False)
            self['ussd_entry'].set_sensitive(False)
            self.set_ussd_reply('')

    def set_card_manufacturer_info(self, manufacturer):
        self['card_manufacturer_label'].set_text(
            manufacturer if manufacturer is not None else _('Unknown'))

    def set_card_model_info(self, model):
        self['card_model_label'].set_text(
            model if model is not None else _('Unknown'))

    def set_card_firmware_info(self, firmware):
        self['card_firmware_label'].set_text(
            firmware if firmware is not None else _('Unknown'))

    def set_msisdn_info(self, msisdn):
        if msisdn is None:
            msisdn = _('Unknown')
        self['msisdn_name_label'].set_text(msisdn)

    def set_imsi_info(self, imsi):
        if imsi is None:
            imsi = _('Unknown')
        self['imsi_number_label'].set_text(imsi)

    def set_network_info(self, network):
        if network is None:
            network = _('Unknown')
        self['network_name_label'].set_text(network)

    def set_country_info(self, country):
        if country is None:
            country = _('Unknown')
        self['country_name_label'].set_text(country)

    def set_imei_info(self, imei):
        if imei is None:
            imei = _('Unknown')
        self['imei_number_label'].set_text(imei)

    def set_appVersion_info(self, appVersion):
        self['vmb_version'].set_text(appVersion)

    def set_coreVersion_info(self, coreVersion):
        self['core_version'].set_text(coreVersion)
