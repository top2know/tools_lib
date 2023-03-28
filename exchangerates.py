import pandas as pd

data = pd.read_csv('currencies.csv', sep=';')
currencies = {'RUB': 1}

for i, row in data.iterrows():
    currencies[row['Букв. код']] = float(row['Курс']) / row['Единиц']


def is_currently_supported(cur):
    return cur in currencies


def get_rate(base='EUR', target='USD'):
    if not is_currently_supported(base):
        raise Exception(f'Unknown currency {base}')
    if not is_currently_supported(target):
        raise Exception(f'Unknown currency {target}')
    return currencies[base] / currencies[target]

