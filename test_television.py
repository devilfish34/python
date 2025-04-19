import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_on_and_off():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute_unmute_on():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_mute_unmute_off():
    tv = Television()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_up_off():
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_up_on_wrap():
    tv = Television()
    tv.power()
    for _ in range(5):
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

def test_channel_down_off():
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_down_on_wrap():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_volume_up_off():
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_volume_up_on():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_volume_up_muted():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_up_beyond_max():
    tv = Television()
    tv.power()
    for _ in range(5):
        tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down_off():
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_volume_down_on():
    tv = Television()
    tv.power()
    for _ in range(3):
        tv.volume_up()
    for _ in range(2):
        tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_down_muted():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_down_beyond_min():
    tv = Television()
    tv.power()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
