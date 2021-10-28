#-*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class EventExtended(models.Model):
    _inherit = 'event.event'

    needs_rrno = fields.Boolean(string='Rijksregisternummer?', required=True, default=False)


class EventTypeExtended(models.Model):
    _inherit = 'event.type'

    abbreviation = fields.Char(string='Afkorting')


class EventRegistrationExtended(models.Model):
    _inherit = 'event.registration'

    rrno = fields.Char(string='Rijksregisternummer')
    attest_no = fields.Char(string='Attestnummer',compute='_compute_attest_no')

    def _get_website_registration_allowed_fields_rrno(self):
        return {'name', 'phone', 'email', 'mobile', 'event_id', 'partner_id', 'event_ticket_id', 'rrno'}

    def _compute_attest_no(self):
        for record in self:
            record.attest_no = str(record.event_id.event_type_id.abbreviation or '') + str(record.event_id.with_context(tz=record.event_id.date_tz).date_begin.strftime('%Y%m%d')) + str(record.id).zfill(4)