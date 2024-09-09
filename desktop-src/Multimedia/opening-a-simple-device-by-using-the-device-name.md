---
title: Opening a Simple Device by Using the Device Name
description: Opening a Simple Device by Using the Device Name
ms.assetid: 9e116499-2094-40e1-b2bc-3e3b8281a472
keywords:
- mciSendCommand function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Opening a Simple Device by Using the Device Name

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following example opens a CD audio device by specifying the device name using the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function.


```C++
UINT wDeviceID;
DWORD dwReturn;
MCI_OPEN_PARMS mciOpenParms;
 
// Opens a CD audio device by specifying the device name.

mciOpenParms.lpstrDeviceType = "cdaudio";

if (dwReturn = mciSendCommand(NULL, MCI_OPEN, MCI_OPEN_TYPE,
    (DWORD)(LPVOID) &mciOpenParms))
{
    
    // Error, unable to open device.
    
}

// The device opened successfully; get the device ID.
wDeviceID = mciOpenParms.wDeviceID;
```



 

 