---
title: Retrieving Information About a Movie
description: Retrieving Information About a Movie
ms.assetid: '678272e0-67fe-4ec1-88a8-924a773445a7'
keywords: ["mciSendCommand function"]
---

# Retrieving Information About a Movie

The following example sets the time format to frames and obtains the current position if the device is playing using the [**mciSendCommand**](mcisendcommand.md) function.


```C++
MCI_DGV_SET_PARMS mciSet; 
MCI_DGV_STATUS_PARMS mciStatus; 
 
// Put in frame mode. 
mciSet.dwTimeFormat = MCI_FORMAT_FRAMES; 
mciSendCommand(wDeviceID, MCI_SET, 
    MCI_SET_TIME_FORMAT, 
    (DWORD)(LPSTR)&amp;mciSet); 
 
mciStatus.dwItem = MCI_STATUS_MODE; 
mciSendCommand(wDeviceID, MCI_STATUS, 
    MCI_STATUS_ITEM, 
    (DWORD)(LPSTR)&amp;mciStatus); 
 
// If device is playing, get the position. 
if (mciStatus.dwReturn == MCI_MODE_PLAY)
{ 
    mciStatus.dwItem = MCI_STATUS_POSITION; 
    mciSendCommand(wDeviceID, MCI_STATUS, MCI_STATUS_ITEM, 
        (DWORD)(LPSTR)&amp;mciStatus); 
 
    // Update the position from mciStatus.dwReturn. 
} 
```



 

 




