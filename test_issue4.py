def test_sortArray():
    assert sortArray([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert sortArray([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sortArray([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sortArray([1]) == [1]
    assert sortArray([]) == []