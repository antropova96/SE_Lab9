import csv
import streamlit as st
import matplotlib.pyplot as plt


def count_passengers() -> dict:
    data = {
        '1': {
            'under_30': 0,
            'above_60': 0,
            'total': 0
        },
        '2': {
            'under_30': 0,
            'above_60': 0,
            'total': 0
        },
        '3': {
            'under_30': 0,
            'above_60': 0,
            'total': 0
        }
            }

    with open('data.csv') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # читаем со второй строки
        for line in csv_reader:
            if int(line[1]) == 1:
                age = line[5]
                if age == '':
                    continue  # отбрасываем строки с неизвестным возрастом согласно условию
                age = float(age)
                pclass = line[2]
                if age < 30.0:
                    data[pclass]['under_30'] += 1
                elif age > 60.0:
                    data[pclass]['above_60'] += 1
                data[pclass]['total'] += 1

    return data


def survival_rate(data: dict) -> dict:
    answ = {
        'Passenger class': [],
        'Survival rate under 30': [],
        'Survival rate above 60': []
    }
    for key in data:
        answ['Passenger class'].append(key)
        answ['Survival rate under 30'].append(round(data[key]['under_30'] / data[key]['total'] * 100, 2)),
        answ['Survival rate above 60'].append(round(data[key]['above_60'] / data[key]['total'] * 100, 2)),
    return answ


def make_page():
    st.title('Лабораторная работа №9')

    st.image('static/titanic.jpg')
    st.header('Данные пассажиров Титаника')


def read_user_input():
    checkbox = st.selectbox('Класс пассажира', ['Любой', 1, 2, 3])
    return checkbox


def make_figure(data, filter=None):
    fig = plt.figure(figsize=(10, 5))
    if isinstance(filter, int):
        data = {
            key: value[filter-1] for key, value in data.items()
        }
    classes = data['Passenger class']
    survival_rates_under_30 = data['Survival rate under 30']
    survival_rates_above_60 = data['Survival rate above 60']

    plt.bar(classes, survival_rates_under_30, width=0.2, label='Процент выживших младше 30 лет', color='b', align='center')
    plt.bar(classes, survival_rates_above_60, width=0.2, label='Процент выживших старше 60 лет', color='r', align='center')

    plt.xlabel('Класс билета')
    plt.ylabel('Процент выживших (%)')
    plt.title('Процент выживших с учетом класса билета')
    plt.legend()

    st.pyplot(fig)


def main():
    survivors = survival_rate(count_passengers())
    make_page()
    st.table(survivors)
    checkbox = read_user_input()
    make_figure(survivors, filter=checkbox)


if __name__ == '__main__':
    main()
