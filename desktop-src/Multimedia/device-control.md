---
title: Device Control (Windows Multimedia)
description: Device Control
ms.assetid: b4479803-f1da-4646-909e-c4ef412ebdcd
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Device Control (Windows Multimedia)

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To control an MCI device, you open the device, send the necessary commands to it, and then close the device. The commands can be very similar, even for completely different MCI devices. For example, the following series of MCI commands plays the sixth track of an audio CD by using the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function:


```C++
mciSendString("open cdaudio", lpszReturnString,
    lstrlen(lpszReturnString), NULL);
mciSendString("set cdaudio time format tmsf", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
mciSendString("play cdaudio from 6 to 7", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
mciSendString("close cdaudio", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
```



The next example shows a similar series of MCI commands that plays the first 10,000 samples of a waveform-audio file:


```C++
mciSendString(
    "open c:\mmdata\purplefi.wav type waveaudio alias finch", 
    lpszReturnString, lstrlen(lpszReturnString), NULL);
mciSendString("set finch time format samples", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
mciSendString("play finch from 1 to 10000", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
mciSendString("close finch", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
```



These examples illustrate some interesting facts about MCI commands:

-   The same basic commands ([**open**](open.md), [**set**](set.md), [**play**](play.md), and [**close**](close.md)) are used with CD audio and waveform-audio devices. The same MCI commands are used with all MCI devices.
-   The open command for the waveform-audio device includes a filename specification. The waveform-audio device is a *compound device* (one associated with a data file), while the CD audio device is a *simple device* (one without an associated data file).
-   The set command specifies time formats in each case, but the time-format flag for the CD audio device specifies tracks/minutes/seconds/frames (TMSF) format, while the time format used with the waveform-audio device specifies "samples".
-   The variables used with the "from" and "to" flags are appropriate to the respective time format. For example, for the CD audio device, the variables specify a range of tracks, but for the waveform-audio device, the variables specify a range of samples.

 

 
