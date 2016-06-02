# -*- coding: utf-8 -*-

import time
from openerp import api, models

import logging

_logger = logging.getLogger(__name__)

class ReportPaymentVoucher(models.AbstractModel):

    _name = 'report.account_ultrasteel.report_paymentvoucher'