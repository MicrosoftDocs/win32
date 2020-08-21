---
title: Playing a Device
description: Playing a Device
ms.assetid: 48d83e06-9e6e-498b-ad9b-0b66f235db25
keywords:
- MCI_PLAY command
- MCIAVI playback window
ms.topic: article
ms.date: 05/31/2018
---

# Playing a Device

The [**play**](play.md) ([**MCI\_PLAY**](mci-play.md)) command starts playing a device. Without any flags, this command starts playing from the current position and plays until the command is interrupted or until the end of the media or file is reached. After playback, the current position is at the end of the media. You can also use the [**seek**](seek.md) ([**MCI\_SEEK**](mci-seek.md)) command to change the current position.

Most devices that support the **play** command also support the "from" (MCI\_FROM) and "to" (MCI\_TO) flags. These flags indicate the position at which the device should start and stop playing. For example, the following command plays a CD audio disc from the beginning of the first track using the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function:


```C++
mciSendString("play cdaudio from 0", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
```



Some device types extend this command to exploit the capabilities of a particular device. For example, the [**play**](play.md) command for the **videodisc** device type includes the "fast" (MCI\_VD\_PLAY\_FAST) , "slow" (MCI\_VD\_PLAY\_SLOW), and "scan" (MCI\_VD\_PLAY\_SCAN) flags.

> [!Note]  
> The units assigned to the position value depend on the time format used by the device. Each device has a default time format, but you should specify the time format by using the [**set**](set.md) ([**MCI\_SET**](mci-set.md)) command before issuing any commands that use position values.

 

## Playing an AVI File

Video files in Windows are made up of at least two interleaved data streams: a video (pictorial) stream and an audio stream. You can easily play these audio-video interleaved (AVI) files by using MCI commands. The following sections discuss playing AVI files.

## Setting Up an MCIAVI Playback Window

Your application can specify the following options to define the playback window for playing an AVI file:

-   Use the MCIAVI driver's default pop-up window.
-   Specify a parent window and window style that the MCIAVI driver can use to create the playback window.
-   Specify a playback window for the MCIAVI driver to use for playback.
-   Play the AVI file on a full-screen display.

If your application does not specify any window options, the MCIAVI driver creates a default window for playing the sequence. The driver creates this playback window for the [**open**](open.md) ([**MCI\_OPEN**](mci-open.md)) command, but it does not display the window until your application sends a command to either display the window or play the file. This default playback window is a pop-up window with a sizing border, title bar, a thick frame, a **window** menu, and a Minimize button.

Your application can also specify a parent window handle and a window style when it issues the **open** command. In this case, the MCIAVI driver creates a window based on these specifications instead of the default pop-up window. Your application can specify any window style available for the [CreateWindow](/windows/win32/api/winuser/nf-winuser-createwindowa) function. Styles that require a parent window, such as WS\_CHILD, should include a parent window handle.

Your application can also create its own window and supply the handle to the MCIAVI driver by using the [**window**](window.md) ([**MCI\_WINDOW**](mci-window.md)) command. The MCIAVI driver uses this window instead of creating one of its own.

When the MCIAVI driver creates the playback window or obtains a window handle from your application, it does not display the window until your application either plays the sequence or sends a command to display the window. Your application can use the **window** command to display the window without playing the sequence. For example, the following command displays the window using [**mciSendString**](/previous-versions//dd757161(v=vs.85)):


```C++
mciSendString("window movie state show", lpszReturnString,
    lstrlen(lpszReturnString), NULL);
```



In this example, "movie" is an alias for the digital-video device.

Your application can also play an AVI file full-screen. To play full-screen, modify the [**play**](play.md) ([**MCI\_PLAY**](mci-play.md)) command with the "fullscreen" (MCI\_MCIAVI\_PLAY\_FULLSCREEN) flag. When your application uses this flag, the MCIAVI driver uses a 320- by 240-pixel full-screen format for playing the sequence. For example, the following command plays the opened file full-screen (using "movie" as an alias):


```C++
mciSendString("play movie fullscreen", lpszReturnString,
    lstrlen(lpszReturnString), NULL);
```



## Changing the Playback State for an AVI file

Your application can use the [**seek**](seek.md) ([**MCI\_SEEK**](mci-seek.md)) command to move the current position to the beginning, the end, or an arbitrary position in an AVI file. There are two seek modes for the MCIAVI driver: exact and inexact. Your application can change the seek mode by using the [**set**](set.md) ([**MCI\_SET**](mci-set.md)) command. When you use **set** "seek exactly on", the MCIAVI driver seeks exactly to the frame your application specifies. This might cause a delay if the file is temporally compressed and your application does not specify a key frame. When you use **set** "seek exactly off", the MCIAVI driver seeks to the nearest key frame in a temporally compressed file.

Some MCI commands let your application alter the playback of an AVI file in other ways. For example, an AVI file, by default, plays at its normal speed, but your application can increase or decrease this speed by using the "speed" flag with the **set** command. For AVI files, a speed value of 1000 is typical. Thus, to play a movie at half its typical speed, your application can use the command **set** "movie speed 500"; alternatively, it can use **set** "movie speed 2000" to play the sequence at twice its normal speed.

The [**setaudio**](setaudio.md) ([**MCI\_SETAUDIO**](mci-setaudio.md)) command lets your application control the audio portion of an AVI file. Your application can mute audio during playback or, in the case of multiple audio stream files, select the audio stream that is played.

The MCIAVI driver has a dialog box to control some of its playback options. Some of the options available to the user include selecting window-oriented or full-screen playback, selecting the seek mode, and zooming the image. Your application can have MCIAVI display this dialog box by using the [**configure**](configure.md) ([**MCI\_CONFIGURE**](mci-configure.md)) command.

## Stream Handlers

The data in an AVI file is treated as a series of streams. An AVI file typically contains an audio and video stream, and there might also be a custom stream that contains text or some other custom data. The MCIAVI driver can use different handlers for these data streams. For more information about custom AVI files, see [Custom File and Stream Handlers](custom-file-and-stream-handlers.md).

 

 