
def test_sortString():
    assert sortString("aaaabbbbcccc") == "ccccbbbbaaaa"
    assert sortString("rat") == "art"
    assert sortString("leetcode") == "cdelotee"
    assert sortString("ggggggg") == "ggggggg"
    assert sortString("spo") == "ops"
    assert sortString("aabbcc") == "ccbbaa" 
