---
title: Default Behavior of Drivers
description: Default Behavior of Drivers
ms.assetid: ed6905eb-67ad-421d-be00-4a5585dff7fb
ms.topic: article
ms.date: 05/31/2018
---

# Default Behavior of Drivers

In many situations, the MCI command specifications define the default values and behavior for drivers of a particular device type. Since multimedia devices can have a wide range of features (and limitations), there can be undefined areas of behavior. Also, drivers might handle exceptions differently, based on the capabilities of the device.

For example, consider the following commands sent to a waveform-audio driver using the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function:


```C++
mciSendString("open sound.wav alias sound", lpszReturnString,
    lstrlen(lpszReturnString), NULL);
mciSendString("play sound notify", lpszReturnString,
    lstrlen(lpszReturnString), NULL);
mciSendString("record sound from 0 notify", lpszReturnString,
    lstrlen(lpszReturnString), NULL);
```



The [**record**](record.md) command returns a "Parameter out of range" value and stops the playback started by the previous [**play**](play.md) command. One might expect the driver to validate the record command before stopping playback, but the driver stops the playback first.

 

 