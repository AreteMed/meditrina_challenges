# -*- coding: utf-8 -*-
from datetime import datetime

class PrescriptionScheule(object):
    """
    Your defined schedule for a prescription
    """
    name = ""
    daily = None
    weekly = None
    monthly = None


def get_schedule_suggestions(prescription_schedule, last_dose_date, total_requested=1):
    """
    Given a phase or specified dosing schedule:
        Provide an offset for the next scheduled appointments
    For now we are only looking at schedules that are weekly or monthly
    """
    if not isinstance(prescription_schedule, PrescriptionScheule):
        raise Exception("Invalid schedule object date.")

    if not isinstance(last_dose_date, datetime):
        raise Exception("Invalid dose date.")

    # YOUR CODE

    return ["the future"]
