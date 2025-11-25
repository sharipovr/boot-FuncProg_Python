def sort_dates(dates):
    dates_sorted = sorted(dates, key=dateTransformed)
    return dates_sorted


def dateTransformed(date):
    d = date.split("-")
    return f"{d[2]}{d[0]}{d[1]}"