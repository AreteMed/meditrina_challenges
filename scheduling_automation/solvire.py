# -*- coding: utf-8 -*-
"""
Scheduling suggestions
"""
from __future__ import division
from datetime import datetime, timedelta
from collections import OrderedDict

import logging
import sys

logger = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setLevel(logging.DEBUG)
logger.addHandler(out_hdlr)
logger.setLevel(logging.DEBUG)

class PrescriptionScheule(object):
    """
    A prescription class
    """

    CALENDAR_BLOCKS = OrderedDict({
        'hourly': 60,
        'daily': 24,
        'weekly': 7,
        'monthly': 4,
    })

    """
    Your defined schedule for a prescription
    """
    def __init__(self):
        self.name = ""
        self.hourly = None
        self.daily = None
        self.weekly = None
        self.monthly = None

    @staticmethod
    def to_mintues(block):
        minutes = 1
        # stupid order
        for key in ['hourly', 'daily', 'weekly', 'monthly']:
            if key == block:
                return minutes
            value = PrescriptionScheule.CALENDAR_BLOCKS[key]
            logger.info("min " + str(minutes) + " value " + str(value))
            minutes = minutes * value


def get_schedule_suggestions(
        prescription_schedule,
        last_dose_date,
        total_requested=1,
        black_out_dates=[]
    ):
    """
    Given a phase or specified dosing schedule:
        Provide an offset for the next scheduled appointments
    For now we are only looking at schedules that are weekly or monthly
    this function returns a list of datetime.date objects
    """
    if not isinstance(prescription_schedule, PrescriptionScheule):
        raise Exception("Invalid schedule object date.")

    if not isinstance(last_dose_date, datetime):
        raise Exception("Invalid dose date.")

    next_dates = []
    running_offset = 0
    # running_multiple = 1
    for block, multiple in PrescriptionScheule.CALENDAR_BLOCKS.items():
        # starting at smallest... we are in minutes and multiplying
        offset = getattr(prescription_schedule, block)
        if offset is None: continue
        logger.debug(
            "Offset " + str(offset) +
            "rounded " + str(round(multiple / offset)) +
            " open " + str(multiple / offset)
        )
        minutes = PrescriptionScheule.to_mintues(block)
        running_offset += round(multiple / offset) * minutes

    # once we have the offsets then iterate N times
    if running_offset == 0:
        raise Exception("Offset is not set on any field")

    next_dose = last_dose_date
    for _ in range(1, total_requested):
        # for each iteration add one more offset
        next_dose = next_dose + timedelta(minutes=running_offset)
        # if this is a blackout date increment one day
        if next_dose in black_out_dates or next_dose.weekday() == 6:
            next_dose = next_dose + timedelta(days=1)

        next_dates.append(next_dose)

    return next_dates



scrip = PrescriptionScheule()
scrip.weekly = 3

for date in get_schedule_suggestions(scrip, datetime.now(), 15):
    logger.info(date)
