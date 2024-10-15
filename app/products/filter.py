def filt(data):
    clean_filters = {k: v for k, v in data.items() if v is not None}
    return clean_filters