from pip._internal.cli.cmdoptions import src

from rsc import processing


def test_filter_by_state(test_initial_list):
    assert src.processing.filter_by_state(src.processing.initial_list, state=test_initial_list)


def test_filter_by_state_1():
    assert src.processing.filter_by_state(src.processing.initial_list) == [
        {'id': 414288829, 'state': 'EXECUTED', 'data':
            '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'data':
            '2018*06*30T02:08:58.425572'}]


def test_filter_by_state_sort():
    assert [
               {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 615064591, 'state': 'CANCELED', 'date':
                   '2018-10-14T08:21:33.419441'},
               {'id': 594226727, 'state': 'CANCELED', 'date':
                   '2018-09-12T21:27:25.241689'},
               {'id': 939719570, 'state': 'EXECUTED', 'date':
                   '2018-06-30T02:08:58.425572'}
           ] == processing.sort_by_date(processing.initial_list)
