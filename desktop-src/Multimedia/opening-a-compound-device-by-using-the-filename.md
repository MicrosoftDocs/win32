---
title: Opening a Compound Device by Using the Filename
description: Opening a Compound Device by Using the Filename
ms.assetid: 5199bb68-44be-4fad-af5b-8fe89f27caee
keywords:
- mciSendCommand function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Opening a Compound Device by Using the Filename

The following example opens the waveform-audio device by specifying a waveform-audio file named "TIMPANI.WAV" using the [**mciSendCommand**](/windows/win32/Mmsystem/?branch=master) function.


```C++
UINT wDeviceID;
DWORD dwReturn;
MCI_OPEN_PARMS mciOpenParms;
 
// Opens a waveform-audio device by specifying the device and 
// file name.

mciOpenParms.lpstrDeviceType = "waveaudio";
mciOpenParms.lpstrElementName = "timpani.wav";

if (dwReturn = mciSendCommand(NULL, MCI_OPEN,
    MCI_OPEN_TYPE | MCI_OPEN_ELEMENT, (DWORD)(LPVOID) &amp;mciOpenParms))
{
    
    // Error, unable to open device.
    
}

// The device opened successfully; get the device ID.
wDeviceID = mciOpenParms.wDeviceID;
```



 

 




