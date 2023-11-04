from twttr import shorten


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HEllO") == "Hll"
    assert shorten("uEoAi") == ""
    assert shorten("") == ""
    assert shorten("tran cao Nguyen") == "trn c Ngyn"
    assert shorten("hello, world") == "hll, wrld"
    assert shorten("My birthday is 9/1/2003") == "My brthdy s 9/1/2003"
