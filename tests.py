#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;
from datetime import date
today = date.today()

currentYear = int(today.year)
year = 2021
month = 12
day = 30

def test_code():
    assert main.ageOneHundred(20) == currentYear + 80, "ageOneHundred(20) == year + 80 failed"
    assert main.ageOneHundred(59) == currentYear + 41 , "product3Plus1(59) == year + 41 failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
