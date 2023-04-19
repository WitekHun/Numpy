import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

if __name__ == "__main__":
    pv = 120000  # cena początkowa
    price_rate = 0.05  # wzrost ceny o 5% rocznie
    years = 5  # okres oszczędzania
    capital_rate = 0.12  # oprocentowanie 12@ oszczędności kapitalizacja miesięczna
    freq = 12  # częstotliwość kapitalizacji oszczędności w roku
    capital_rate /= freq  # miesięczne oprocentowanie oszczędności
    nper = years * freq  # liczba okresów kapitalizacji oszczędności
    periods = np.arange(1, nper + 1, dtype=int)
    price_periods = np.arange(1, years + 1, dtype=int)

    price = -np.around(
        npf.fv(price_rate, price_periods, 0, pv), 2
    )  # cena mieszkania po roku, 2 latach, ... 5 latach
    price = np.insert(
        price, 0, 120000.00
    )  # cena mieszkania na początku oszczędzania, po roku ,... 5 latach
    end_price = price[-1]
    print(f"Cena końcowa po 5 latach {end_price}zł")

    predicted_payment = np.arange(1850, 1900, 0.01)
    print(predicted_payment)

    arr = np.where(
        (
            -np.around(npf.fv(capital_rate, 60, predicted_payment, 0), 0)
            == np.around(end_price, 0)
        ),
        predicted_payment,
        0,
    )
    print(arr)
    index_arr = np.argwhere(arr != 0)
    monthly_payment = np.around(arr.item(index_arr.item(0)), 2)
    print(f"Minimalna miesięczna wpłata {monthly_payment}zł")
    end_value = -np.around(npf.fv(capital_rate, 60, monthly_payment, 0), 2)
    print(f"Oszczędności po 5 latach {end_value}zł")

    capital_value = -np.around(
        npf.fv(
            capital_rate,
            periods,
            monthly_payment,
            0,
        ),
        2,
    )
    end_value = -np.around(npf.fv(capital_rate, 60, monthly_payment, 0), 2)
    print(
        f"Wartość oszczędności po kolejnych miesiącach {capital_value} \n Oszczędności po 5 latach {end_value}zł"
    )

    plt.plot(np.arange(0, 61, 12), price, label="cena")
    plt.plot(periods, capital_value, label="oszczędności")
    plt.legend()
    plt.xlabel("Liczba okresów w miesiącach")
    plt.ylabel("Kwota [zł]")
    plt.show(block=True)
