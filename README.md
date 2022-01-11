# ShlagDeck
A StreamDeck - but without the budget.

![Picture of the ShlagDeck in action](/shlagdeck.JPEG)

I needed a StreamDeck to control my Twitch Stream, but i really didn't want to spend 70$ or even more, so i decided to grab a couple of random knock off Chinese mechanical switches (cherry blue clones), as well as some old keycaps, a perf board, an arduino and make my own !

It would have been ideal to use an arduino pro mini, as it can act as a native USB keyboard, but all i had laying around was a nano. No problem, all the Nano will do is output the key number that was pressed to the USB serial port, then a Python script is used to transform that into a keypress, and BOOM ! ShlagDeck :D

In my version, i've used 5 buttons, they press F13, F14, F15, F16 and F17, which i can use as a hotkey in any application i want (mainly, Streamlabs and Discord, but anything could work).
