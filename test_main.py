from main import count_passengers, count_survival_rate

data = [
        ['1', '0', '3', "Braund, Mr. Owen Harris", 'male', '22', '1', '0', 'A/5 21171', '7.25', '', 'S'],
        ['2', '1', '1', "Cumings, Mrs. John Bradley", 'female', '38', '1', '0', 'PC 17599', '71.2833', 'C85', 'C'],
        ['3', '1', '3', "Heikkinen, Miss. Laina", 'female', '26', '0', '0', 'STON/O2. 3101282', '7.925', '', 'S'],
        ['4', '1', '1', "Futrelle, Mrs. Jacques Heath", 'female', '61', '1', '0', '113803,53.1', 'C123', 'S'],
        ['5', '0', '3', "Allen, Mr. William Henry", 'male', '35', '0', '0', '373450', '8.05', '', 'S'],
    ]


def test_count_survived_passengers():
    pclass_filter = 'Любой'
    answer = count_passengers(data, pclass_filter)

    assert answer == {'under_30': 1,
                      'above_60': 1,
                      'total': 5
                      }


def test_calculate_survival_rate():
    pclass_filter = 'Любой'
    suvivours = count_passengers(data, pclass_filter)

    survival_rate = count_survival_rate(suvivours)
    assert survival_rate == {'survival rate above 60': 20, 'survival rate under 30': 20}


def test_count_survived_first_class():
    pclass_filter = 1
    answer = count_passengers(data, pclass_filter)

    assert answer == {'under_30': 0,
                      'above_60': 1,
                      'total': 2
                      }


def test_count_survived_third_class():
    pclass_filter = 3
    answer = count_passengers(data, pclass_filter)

    assert answer == {'under_30': 1,
                      'above_60': 0,
                      'total': 3
                      }


def test_count_survived_empty():
    answer = count_passengers([])

    assert list(answer.values()) == [0, 0, 0]