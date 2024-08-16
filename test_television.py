import pytest
from television import Television

class TestTelevision:
    def test_init(self):
        self.tv = Television()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tv = Television()
        self.tv.power()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
        self.tv.power()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        self.tv = Television()
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

        self.tv.mute()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"

        self.tv.power()
        self.tv.mute()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 1"

        self.tv.mute()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 1"

    def test_channel_up(self):
        self.tv = Television()
        self.tv.channel_up()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

        self.tv.power()
        self.tv.channel_up()
        assert str(self.tv) == "Power = True, Channel = 1, Volume = 0"

        self.tv._channel = Television.MAX_CHANNEL
        self.tv.channel_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        self.tv = Television()
        self.tv.channel_down()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

        self.tv.power()
        self.tv.channel_down()
        assert str(self.tv) == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        self.tv = Television()
        self.tv.volume_up()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

        self.tv.power()
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"

        self.tv.mute()
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"

        self.tv._volume = Television.MAX_VOLUME
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        self.tv = Television()
        self.tv.volume_down()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

        self.tv.power()
        self.tv._volume = Television.MAX_VOLUME
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"

        self.tv.mute()
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

        self.tv._volume = Television.MIN_VOLUME
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
