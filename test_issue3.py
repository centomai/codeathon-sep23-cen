def test_validateIPAddress():
    assert validateIPAddress("172.16.254.1") == True
    assert validateIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == True
    assert validateIPAddress("256.256.256.256") == False
    assert validateIPAddress("2001:0db8:85a3::8a2e:0370:7334") == False
    assert validateIPAddress("172.16.254.01") == False