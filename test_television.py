from television import Television
def test_init():
    #Verify Television starts with its default settings
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv = Television()

    #Verify the television turns on
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    #Verify the television turns off
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute():
    tv = Television()

    #Verify muting displays 0 when the television is on
    tv.power()
    tv.volume_up()
    tv.mute()

    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    #Verify the unmuting restores the previous volume
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    #Verify pressing mute while the television is off has no effect
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"

    #Verify the mute setting remains unchanged after powering on
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_channel_up():
    tv = Television()

    # Check the channel doesn't change when off
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # Turn on and increase the channel
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    # Increase to max channel
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    # Check to see channel wraps back to 0
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down():
    tv = Television()

    #Verify the channel doesn't change while the TV is off
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #Verify going below channel 0 wraps to channel 3
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    #Verify the channel decreases normally
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"

    #Verify the channel can decrease back to 0
    tv.channel_down()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_up():
    tv = Television()

    #Verify volume doesn't increase while the TV is off
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #Verify volume increases normally
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    #Verify volume can't go over 2
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    #Verify volume up auto unmutes the television
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    #Verify volume increase unmutes the television
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    tv = Television()

    #Verify volume doesn't decrease while television is off
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #Turn on the TV and increase the volume to 2
    tv.power()
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    #Verify volume decreases normally
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    #Verify volume can't go below 0
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    #Increase volume, then mute television
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    #Verify volume down automatically unmutes the television
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"