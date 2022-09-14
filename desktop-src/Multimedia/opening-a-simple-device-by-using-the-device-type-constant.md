---
title: Opening a Simple Device by Using the Device-Type Constant
description: Opening a Simple Device by Using the Device-Type Constant
ms.assetid: 6ed5fd4b-534a-4e03-8130-07f831403a8e
keywords:
- mciSendCommand function
ms.topic: article
ms.date: 05/31/2018
---

# Opening a Simple Device by Using the Device-Type Constant

The following example opens a CD audio device by specifying a device-type constant using the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function.


```C++
UINT wDeviceID;
DWORD dwReturn;
MCI_OPEN_PARMS mciOpenParms;

// Opens a CD audio device by specifying a device-type constant.

mciOpenParms.lpstrDeviceType = (LPCSTR) MCI_DEVTYPE_CD_AUDIO;

if (dwReturn = mciSendCommand(NULL, MCI_OPEN,
    MCI_OPEN_TYPE | MCI_OPEN_TYPE_ID, (DWORD)(LPVOID) &mciOpenParms))
{
    
    // Error, unable to open device.
    
}

// The device opened successfully; get the device ID.
wDeviceID = mciOpenParms.wDeviceID;
```



 

 