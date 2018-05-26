---
title: Opening a Simple Device by Using the Device-Type Constant
description: Opening a Simple Device by Using the Device-Type Constant
ms.assetid: 6ed5fd4b-534a-4e03-8130-07f831403a8e
keywords:
- mciSendCommand function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Opening a Simple Device by Using the Device-Type Constant

The following example opens a CD audio device by specifying a device-type constant using the [**mciSendCommand**](/windows/win32/Mmsystem/?branch=master) function.


```C++
UINT wDeviceID;
DWORD dwReturn;
MCI_OPEN_PARMS mciOpenParms;

// Opens a CD audio device by specifying a device-type constant.

mciOpenParms.lpstrDeviceType = (LPCSTR) MCI_DEVTYPE_CD_AUDIO;

if (dwReturn = mciSendCommand(NULL, MCI_OPEN,
    MCI_OPEN_TYPE | MCI_OPEN_TYPE_ID, (DWORD)(LPVOID) &amp;mciOpenParms))
{
    
    // Error, unable to open device.
    
}

// The device opened successfully; get the device ID.
wDeviceID = mciOpenParms.wDeviceID;
```



 

 




