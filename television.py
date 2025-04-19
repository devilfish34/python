class Television:
    """
    A class to simulate the basic functionality of a television.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Method to initialize the television with default settings.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__prev_volume: int = Television.MIN_VOLUME

    def power(self) -> None:
        """
        Method to toggle the power status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to toggle the mute status of the television.
        When muting, sets volume to 0 and stores previous volume.
        When unmuting, restores volume to previous level.
        """
        if self.__status:
            if not self.__muted:
                self.__prev_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
                self.__muted = True
            else:
                self.__volume = self.__prev_volume
                self.__muted = False

    def channel_up(self) -> None:
        """
        Method to increase the channel by 1, wrapping to MIN_CHANNEL if above MAX_CHANNEL.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the channel by 1, wrapping to MAX_CHANNEL if below MIN_CHANNEL.
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the volume by 1 if below MAX_VOLUME. Unmute if muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.__prev_volume = self.__volume

    def volume_down(self) -> None:
        """
        Method to decrease the volume by 1 if above MIN_VOLUME. Unmute if muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.__prev_volume = self.__volume

    def __str__(self) -> str:
        """
        Method to return the string representation of the television's current state.
        :return: Power = {status}, Channel = {Channel #}, Volume = {Volume lvl}
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
