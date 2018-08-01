---
title: Retrieving the User Name
description: To retrieve the name of the user associated either with a local device connected to a network resource or with the name of a network, an application can call the WNetGetUser function.
ms.assetid: aed410af-d5f0-4389-882b-5b4338b5f900
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving the User Name

To retrieve the name of the user associated either with a local device connected to a network resource or with the name of a network, an application can call the [**WNetGetUser**](https://msdn.microsoft.com/en-us/library/Aa385476(v=VS.85).aspx) function.

The following example uses the device name to retrieve the name of the user. The sample calls an application-defined error handler to process errors, and the [**TextOut**](https://msdn.microsoft.com/library/windows/desktop/dd145133) function for printing.


```C++
CHAR szUserName[80]; 
DWORD dwResult, cchBuff = 80; 
 
// Call the WNetGetUser function.
//
dwResult = WNetGetUser("z:", 
    (LPSTR) szUserName, 
    &cchBuff); 
 
// If the call succeeds, print the user name.
//
if(dwResult == NO_ERROR) 
    printf("User name: %s\n", szUserName); 
 
// Handle the error.
//
else 
{ 
    printf("WNetGetUser failed.\n"); 
}
```



For more information about using an application-defined error handler, see [Retrieving Network Errors](retrieving-network-errors.md).

 

 




