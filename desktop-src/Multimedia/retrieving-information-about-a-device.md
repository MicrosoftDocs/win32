---
title: Retrieving Information About a Device
description: Retrieving Information About a Device
ms.assetid: d038d3fb-43d0-4d9d-836c-205f6d8c98e3
keywords:
- MCI_GETDEVCAPS command
- MCI_STATUS command
- MCI_INFO command
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Retrieving Information About a Device

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Every device responds to the [**capability**](capability.md) ([**MCI\_GETDEVCAPS**](mci-getdevcaps.md)), [**status**](status.md) ([**MCI\_STATUS**](mci-status.md)), and [**info**](info.md) ([**MCI\_INFO**](mci-info.md)) commands. These commands obtain information about the device. For example, the following command returns "true" if a **cdaudio** device can eject the disc:


```C++
mciSendString(
    "capability cdaudio can eject", 
    lpszReturnString, lstrlen(lpszReturnString), NULL);
```



The flags listed for the required and basic commands provide a minimum amount of information about a device. Many devices supplement the required and basic commands with extended flags to provide additional information about the device.

 

 




