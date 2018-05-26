---
title: Enumerating Installed Capture Drivers
description: Enumerating Installed Capture Drivers
ms.assetid: 3a70bf5b-1e0a-48d3-aa6b-be66692f0400
keywords:
- capGetDriverDescription function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Installed Capture Drivers

The following example uses the [**capGetDriverDescription**](/windows/win32/Vfw/nf-vfw-capgetdriverdescriptiona?branch=master) function to obtain the names and versions of the installed capture drivers.


```C++
char szDeviceName[80];
char szDeviceVersion[80];

for (wIndex = 0; wIndex < 10; wIndex++) 
{
    if (capGetDriverDescription(
            wIndex, 
            szDeviceName, 
            sizeof (szDeviceName), 
            szDeviceVersion, 
            sizeof (szDeviceVersion)
        )) 
    {
        // Append name to list of installed capture drivers
        // and then let the user select a driver to use.
    }
} 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




