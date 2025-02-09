import pandas as pd
import pycountry

special_codes = {
    "EU": ("European Union", "EUR"),
    "XS": ("International Securities", "INT"),
    "XK": ("Kosovo", "XKX"),
    "QS": ("Euroclear France (Internal)", "QS"),
    "QT": ("Switzerland (Internal)", "QT"),
    "XA": ("CUSIP Global Services", "XA"),
    "XB": ("NSD Russia", "XB"),
    "XC": ("WM Datenservice Germany", "XC"),
    "XD": ("SIX Telekurs", "XD"),
    "XF": ("Internal Assignment", "XF"),
    "CNE": ("China", "CHN") 
}

def get_country_info(isin):
    if not isinstance(isin, str) or len(isin) < 2:
        return None, None 

    country_code = isin[:2]

    if country_code in special_codes:
        return special_codes[country_code]

    try:
        country = pycountry.countries.get(alpha_2=country_code)
        if country:
            return country.name, country.alpha_3
    except AttributeError:
        pass

    return None, None
