---
title: Retrieving the Connection Name
description: To retrieve the name of the network resource associated with a local device, an application can call the WNetGetConnection function, as shown in the following sample.
ms.assetid: 7c02cf9a-cca3-47d8-8a4b-f2245f1db92a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving the Connection Name

To retrieve the name of the network resource associated with a local device, an application can call the [**WNetGetConnection**](https://msdn.microsoft.com/en-us/library/Aa385453(v=VS.85).aspx) function, as shown in the following sample.

The following sample calls an application-defined error handler to process errors, and the [**TextOut**](https://msdn.microsoft.com/library/windows/desktop/dd145133) function for printing.


```C++
TCHAR szDeviceName[80]; 
DWORD dwResult, cchBuff = sizeof(szDeviceName); 
 
// Call the WNetGetConnection function.
//
dwResult = WNetGetConnection(_T("z:"), 
    szDeviceName, 
    &amp;cchBuff); 
 
switch (dwResult) 
{ 
    //
    // Print the connection name or process errors.
    //
    case NO_ERROR: 
        printf("Connection name: %s\n", szDeviceName); 
        break; 
    //
    // The device is not a redirected device.
    //
    case ERROR_NOT_CONNECTED: 
        printf("Device z: not connected.\n"); 
        break;
    //
    // The device is not currently connected, but it is a persistent connection.
    //
    case ERROR_CONNECTION_UNAVAIL: 
        printf("Connection unavailable.\n"); 
        break;
    //
    // Handle the error.
    //
    default: 
        printf("WNetGetConnection failed.\n"); 
}
```



For more information about using an application-defined error handler, see [Retrieving Network Errors](retrieving-network-errors.md).

 

 




