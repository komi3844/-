import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Чтение дат и максимальных температур из файла.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(row[1])
        low = int(row[3])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    # for index, colimn_header in enumerate(header_row):
    #     print(index, colimn_header)

    # Нанесение данных на диаграмму.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Форматирование диаграммы.
    plt.title('Daily high and lows temperatures - 2014', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()


