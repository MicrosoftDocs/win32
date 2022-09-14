---
title: Opening a Compound Device by Using the Filename
description: Opening a Compound Device by Using the Filename
ms.assetid: 5199bb68-44be-4fad-af5b-8fe89f27caee
keywords:
- mciSendCommand function
ms.topic: article
ms.date: 05/31/2018
---

# Opening a Compound Device by Using the Filename

The following example opens the waveform-audio device by specifying a waveform-audio file named "TIMPANI.WAV" using the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function.


```C++
UINT wDeviceID;
DWORD dwReturn;
MCI_OPEN_PARMS mciOpenParms;
 
// Opens a waveform-audio device by specifying the device and 
// file name.

mciOpenParms.lpstrDeviceType = "waveaudio";
mciOpenParms.lpstrElementName = "timpani.wav";

if (dwReturn = mciSendCommand(NULL, MCI_OPEN,
    MCI_OPEN_TYPE | MCI_OPEN_ELEMENT, (DWORD)(LPVOID) &mciOpenParms))
{
    
    // Error, unable to open device.
    
}

// The device opened successfully; get the device ID.
wDeviceID = mciOpenParms.wDeviceID;
```



 

 