import numpy as np
import matplotlib.pyplot as plt
import csv

K = lambda x: np.exp(-x**2)/np.sqrt(2*np.pi)

def parzen(h,N,data,x,month,year,day):
    """

    :param h: Czułość parzena
    :param N: ilośc danych
    :param data: Dane
    :param x: Zakres danych
    :param month: Miesiąc
    :param year: Rok
    :param day: Dzień
    :return: Funkcja Rysuje skumulowanego parzena na danych dostarczonych
    """
    y = 1/(N * h) * sum(K((x-i)/h) for i in data)
    plt.figure("21-01-2013 -> "+day+'-'+month+'-'+year)
    plt.plot(x, y)
    plt.scatter(data, [0] * len(data), s=0.1)
    plt.xlabel("Price in $")
    plt.ylabel("density")
    plt.show()

def file(path):
    """

    :param path: ścieżka do pliku .CSV
    :return: Zwraca Ceny Bitcoina oraz daty
    """
    btc_data = []
    date = []
    with open(path, newline='') as f:
        reader = csv.reader(f, quoting = csv.QUOTE_NONE)
        for row in reader:
            date.append(row[0])
            btc_data.append(float((float(row[2])+float(row[3]))/2))
    return btc_data, date

btc_data, date = file("Data Bitfinex BTCUSD.csv")

def parzen_data(btc_data,date):
    """

    :param btc_data: Ceny Bitcoina
    :param date: Daty
    :return: Funkcja Tworzy skumulowanego parzena od stycznia 2013 roku do czerwca 2018 roku, kumulując dane co rok.
    """

    N = len(btc_data)
    btc_data = np.array(btc_data)
    h = 0.2
    year, month, day = date[0].split('-')
    for i in range(N):
        nyear, nmonth, nday = date[i].split('-')
        if nyear == '2018':
            h+=10
        if int(nmonth) == 6 and int(nday) == 10:
            x = np.linspace(min(btc_data[0:i]), max(btc_data[0:i]))
            parzen(h,i,btc_data[0:i],x,nmonth,nyear,nday)
            year,month,day = nyear,nmonth,nday
        h+=0.2


def plot_all(data,date):
    """

    :param data: Ceny Bitcoina
    :param date: Daty
    :return: Funkcja rysuje wykres ceny Bitcoina w czasie
    """
    plt.plot(date,data,color = 'g')
    plt.xlabel("Time")
    plt.ylabel("Price in $")
    plt.show()

def main():
    print("Wybierz opcję...")
    print("1.Cena Bitcoina w $ od stycznia 2013 roku do czerwca 2018 roku: ")
    print("2.Analiza cen Bitcoina metodą kumulowanego parzena: ")
    choose = int(input())
    if choose == 1:
        plot_all(btc_data,date)
    elif choose == 2:
        parzen_data(btc_data,date)
    else:
        print("Nieprawidłowa liczba")
        return main()
main()


