"""Fictional dispatch logs, in observation order. One row per report."""

BASE = [
    "traffic medical clearance", "traffic clearance", "outage repair",
    "storm flood cleanup", "medical clearance", "flood cleanup",
]
TRAIN = [
    "traffic medical clearance cleanup", "traffic medical clearance",
    "traffic clearance cleanup", "traffic outage repair clearance",
    "storm outage repair cleanup", "storm flood medical clearance",
    "storm flood cleanup clearance", "storm outage repair clearance",
    "flood medical clearance cleanup", "flood outage repair cleanup",
    "outage repair clearance", "medical traffic clearance",
]
DRILLS = {
    "underpass": "storm flood outage repair",
    "junction": "traffic medical clearance repair",
    "waterfront": "flood medical traffic clearance",
}


def sequences(rows):
    return [row.split() for row in rows]

