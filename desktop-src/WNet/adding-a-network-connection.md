---
title: Adding a Network Connection
description: To make a connection to a network resource described by a NETRESOURCE structure, an application can call the WNetAddConnection2, the WNetAddConnection3, or the WNetUseConnection function.
ms.assetid: 0dab9eed-9019-4075-833b-324e5caee257
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Adding a Network Connection

To make a connection to a network resource described by a [**NETRESOURCE**](/windows/win32/Winnetwk/ns-winnetwk-_netresourcea?branch=master) structure, an application can call the [**WNetAddConnection2**](/windows/win32/Winnetwk/nf-winnetwk-wnetaddconnection2a?branch=master), the [**WNetAddConnection3**](/windows/win32/Winnetwk/nf-winnetwk-wnetaddconnection3a?branch=master), or the [**WNetUseConnection**](/windows/win32/Winnetwk/nf-winnetwk-wnetuseconnectiona?branch=master) function. The following example demonstrates use of the **WNetAddConnection2** function.

The code sample calls the **WNetAddConnection2** function, specifying that the system should update the user's profile with the information, creating a "remembered" or persistent connection. The sample calls an application-defined error handler to process errors, and the [**TextOut**](https://msdn.microsoft.com/library/windows/desktop/dd145133) function for printing.


```C++
DWORD dwResult; 
NETRESOURCE nr; 
//
// Call the WNetAddConnection2 function to make the connection,
//   specifying a persistent connection.
//
dwResult = WNetAddConnection2(&amp;nr, // NETRESOURCE from enumeration 
    (LPSTR) NULL,                  // no password 
    (LPSTR) NULL,                  // logged-in user 
    CONNECT_UPDATE_PROFILE);       // update profile with connect information 
 
// Process errors.
//  The local device is already connected to a network resource.
//
if (dwResult == ERROR_ALREADY_ASSIGNED) 
{ 
    printf("Already connected to specified resource.\n"); 
    return dwResult; 
} 
 
//  An entry for the local device already exists in the user profile.
//
else if (dwResult == ERROR_DEVICE_ALREADY_REMEMBERED) 
{ 
    printf("Attempted reassignment of remembered device.\n"); 
    return dwResult; 
} 
else if(dwResult != NO_ERROR) 
{ 
    //
    // Call an application-defined error handler.
    //
    printf("WNetAddConnection2 failed.\n"); 
    return dwResult; 
} 
 
//
// Otherwise, report a successful connection.
//
printf("Connected to the specified resource.\n"); 
```



The [**WNetAddConnection**](/windows/win32/Winnetwk/nf-winnetwk-wnetaddconnection2a?branch=master) function is supported for compatibility with earlier versions of Windows for Workgroups. New applications should call the [**WNetAddConnection2**](/windows/win32/Winnetwk/nf-winnetwk-wnetaddconnection2a?branch=master) function or the [**WNetAddConnection3**](/windows/win32/Winnetwk/nf-winnetwk-wnetaddconnection3a?branch=master) function.

For more information about using an application-defined error handler, see [Retrieving Network Errors](retrieving-network-errors.md).

 

 




