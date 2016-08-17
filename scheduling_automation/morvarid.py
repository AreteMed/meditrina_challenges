# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime, timedelta


class PrescriptionScheule(object):
    """
    Your defined schedule for a prescription
    """
    name = ""
    daily = None
    weekly = None
    monthly = None


def get_schedule_suggestions(prescription_schedule, last_dose_date, black_out_dates=[], total_requested=1):
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

    daily = prescription_schedule.daily
    weekly = prescription_schedule.weekly
    monthly = prescription_schedule.monthly

    phase_map = {daily: 1, weekly: 7, monthly: 30}

    def offset():
        for phase in phase_map:
            if phase:
                return (phase_map.get(phase) / phase) * 24

    next_dates = []
    next_dose = last_dose_date + timedelta(hours=offset())

    while len(next_dates) < total_requested:
        # I assume black_out_dates contains a list of datetime objects
        if next_dose.date() in black_out_dates or next_dose.weekday() == 6:
            next_dose = next_dose + timedelta(days=1)

        next_dates.append(next_dose.replace(hour=last_dose_date.hour, minute=last_dose_date.minute))
        next_dose = next_dose + timedelta(hours=offset())

    return next_dates
