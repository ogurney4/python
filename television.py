class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize the television with its default settings"""
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """Turns the television on and off"""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mutes or unmutes the television when it is on"""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increases the channel and returns to the min after the max"""
        if self.__status == True and self.__channel < self.MAX_CHANNEL:
            self.__channel += 1
        elif self.__status == True and self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decreases the channel and returns to the max after the min"""
        if self.__status == True and self.__channel > self.MIN_CHANNEL:
            self.__channel -= 1
        elif self.__status == True and self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """Unmute the television and can increase the volume up to the max"""
        if self.__status:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Unmute the television and can decrease the volume down to the min"""
        if self.__status:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the television's power, channel and volume settings"""
        volume = self.MIN_VOLUME if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"