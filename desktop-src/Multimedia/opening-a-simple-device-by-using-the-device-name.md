---
title: Opening a Simple Device by Using the Device Name
description: Opening a Simple Device by Using the Device Name
ms.assetid: 9e116499-2094-40e1-b2bc-3e3b8281a472
keywords:
- mciSendCommand function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Opening a Simple Device by Using the Device Name

The following example opens a CD audio device by specifying the device name using the [**mciSendCommand**](/windows/win32/Mmsystem/?branch=master) function.


```C++
UINT wDeviceID;
DWORD dwReturn;
MCI_OPEN_PARMS mciOpenParms;
 
// Opens a CD audio device by specifying the device name.

mciOpenParms.lpstrDeviceType = "cdaudio";

if (dwReturn = mciSendCommand(NULL, MCI_OPEN, MCI_OPEN_TYPE,
    (DWORD)(LPVOID) &amp;mciOpenParms))
{
    
    // Error, unable to open device.
    
}

// The device opened successfully; get the device ID.
wDeviceID = mciOpenParms.wDeviceID;
```



 

 




