---
title: Closing All MCI Devices Used by an Application
description: Closing All MCI Devices Used by an Application
ms.assetid: 1d7d3800-b38f-4187-ba57-9849fef4d707
ms.topic: article
ms.date: 05/31/2018
---

# Closing All MCI Devices Used by an Application

The following example closes all of the MCI devices that are opened by an application using the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function.


```C++
UINT wDeviceID;
DWORD dwReturn;
 
// Closes all MCI devices opened by this application.
// Waits until devices are closed before returning.

if(dwReturn = mciSendCommand(MCI_ALL_DEVICE_ID, MCI_CLOSE, MCI_WAIT, 
    NULL))
    
    // Error, unable to close all devices.
    
```



 

 