import csv
import streamlit as st
import matplotlib.pyplot as plt


def read_user_input():
    pclass = st.radio('Класс пассажира', ['Любой', 1, 2, 3])
    return pclass


def read_csv_data():
    data = []
    with open('data.csv') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # читаем со второй строки
        for line in csv_reader:
            data.append(line)
    return data


def count_passengers(csv_data, pclass_filter='Любой') -> dict:
    data = {
        'under_30': 0,
        'above_60': 0,
        'total': 0
    }

    for line in csv_data:
        age = line[5]
        if age == '':
            continue  # отбрасываем строки с неизвестным возрастом согласно условию

        pclass = int(line[2])  # применяем фильтр
        if pclass_filter != 'Любой':
            if pclass != pclass_filter:
                continue

        if int(line[1]) == 1:
            age = float(age)
            if age < 30.0:
                data['under_30'] += 1
            elif age > 60.0:
                data['above_60'] += 1
        data['total'] += 1

    return data


def count_survival_rate(data: dict) -> dict:
    return {
        'survival rate under 30': round(data['under_30'] / data['total'] * 100),
        'survival rate above 60': round(data['above_60'] / data['total'] * 100)
    }


def make_page():
    st.title('Лабораторная работа №9')

    st.image('static/titanic.jpg')
    st.header('Данные пассажиров титаника')


def make_figure(data):
    fig = plt.figure(figsize=(10, 5))

    plt.bar(
        ['Доля выживших младше 30 лет', 'Доля выживших старше 60 лет'],
        [data['survival rate under 30'], data['survival rate above 60']],
    )

    plt.xlabel('Возрастная группа')
    plt.ylabel('Доля выживших (%)')
    plt.title('Доля выживших пассажиров по возрастным группам')

    st.pyplot(fig)


def main():
    make_page()
    pclass_filter = read_user_input()
    data = read_csv_data()
    survivors = count_survival_rate(count_passengers(
        data,
        pclass_filter
    ))
    st.table(
        {
            'Возрастная группа': ['До 30 лет', 'Старше 60 лет'],
            'Доля спасшихся (%)': [
                survivors['survival rate under 30'],
                survivors['survival rate above 60']
            ]
         }
    )
    make_figure(survivors)


if __name__ == '__main__':
    main()
