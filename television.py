# Topic: TV remote control
# Author: Haoyue Xue
# Date: 8/16/2024
# Details: This is a simple TV remote control
#          that switches the TV on and off, adjusts the volume and channels

class Television:
    """
    A class to represent a Television with basic functionalities such as power on/off,
    mute/unmute, channel control, and volume control.
    """

    # Class constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    # Set up the initial value
    def __init__(self):
        """
        Initialize a Television instance with power off, mute off, volume at the minimum level,
        and channel at the minimum level.
        """
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    # Switching the TV on and off
    def power(self):
        """
        Turn on or off of the television.
        """
        self._status = not self._status

    # TV Mute button
    def mute(self):
        """
        Turn the mute status on or off of the television. If muted, the volume is set to 0, and if unmuted,
        the volume is restored to the previous level.
        """
        if self._status:
            if not self._muted:
                self.buffer_volume = self._volume
                self._volume = 0
            else:
                self._volume = self.buffer_volume
            self._muted = not self._muted

    #  Increments the channel number
    def channel_up(self):
        """
        Increase the channel by 1. If the maximum channel is reached, it wraps around to the minimum channel.
        """
        if self._status:
            if self._channel < self.MAX_CHANNEL:
                self._channel += 1
            else:
                self._channel = self.MIN_CHANNEL

    # Decrements the channel number
    def channel_down(self):
        """
        Decrease the channel by 1. If the minimum channel is reached, it wraps around to the maximum channel.
        """
        if self._status:
            if self._channel > self.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = self.MAX_CHANNEL

    # Increases the volume
    def volume_up(self):
        """
        Increase the volume by 1, up to the maximum volume. If the television is muted, unmute it first.
        """
        if self._status:
            if self._muted:
                self.mute()
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    # Decrease the volume
    def volume_down(self):
        """
        Decrease the volume by 1, down to the minimum volume. If the television is muted, unmute it first.
        """
        if self._status:
            if self._muted:
                self.mute()
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    # Returns the TV's current power, channel, and volume status.
    def __str__(self):
        return f'Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}'




