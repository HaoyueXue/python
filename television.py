class Television:

    # Class constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    # Set up the initial value
    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    # Switching the TV on and off
    def power(self):
       self._status = not self._status

    # TV Mute button
    def mute(self):
        if self._status:
            if not self._muted:
                self.buffer_volume = self._volume
                self._volume = 0
            else:
                self._volume = self.buffer_volume
            self._muted = not self._muted

    #  Increments the channel number
    def channel_up(self):
        if self._status:
            if self._channel < self.MAX_CHANNEL:
                self._channel += 1
            else:
                self._channel = self.MIN_CHANNEL

    # Decrements the channel number
    def channel_down(self):
        if self._status:
            if self._channel > self.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = self.MAX_CHANNEL

    # Increases the volume
    def volume_up(self):
        if self._status:
            if self._muted:
                self.mute()
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    # Decrease the volume
    def volume_down(self):
        if self._status:
            if self._muted:
                self.mute()
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    # Returns the TV's current power, channel, and volume status.
    def __str__(self):
            return f'Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}'




