---
title: Canceling a Network Connection
description: To cancel a connection to a network resource, an application can call the WNetCancelConnection2 function, as shown in the following example.
ms.assetid: a1c80222-4986-4c51-86a5-a1caacb4b2fe
ms.topic: article
ms.date: 05/31/2018
---

# Canceling a Network Connection

To cancel a connection to a network resource, an application can call the [**WNetCancelConnection2**](/windows/win32/api/winnetwk/nf-winnetwk-wnetcancelconnection2a) function, as shown in the following example.

The call to **WNetCancelConnection2** specifies that a network connection should no longer be persistent. The sample calls an application-defined error handler to process errors, and the [**TextOut**](/windows/desktop/api/wingdi/nf-wingdi-textouta) function for printing.


```C++
DWORD dwResult; 
 
// Call the WNetCancelConnection2 function, specifying
//  that the connection should no longer be a persistent one.
//
dwResult = WNetCancelConnection2("z:", 
    CONNECT_UPDATE_PROFILE, // remove connection from profile 
    FALSE);                 // fail if open files or jobs 
 
// Process errors.
//  The device is not a local redirected device.
//
if (dwResult == ERROR_NOT_CONNECTED) 
{ 
    printf("Drive z: not connected.\n"); 
    return dwResult; 
} 
 
// Call an application-defined error handler.
//
else if(dwResult != NO_ERROR) 
{ 
    printf("WNetCancelConnection2 failed.\n"); 
    return dwResult; 
}
//
// Otherwise, report canceling the connection.
//
printf("Connection closed for z: drive.\n"); 
```



The [**WNetCancelConnection**](/windows/win32/api/winnetwk/nf-winnetwk-wnetcancelconnectiona) function is supported for compatibility with earlier versions of Windows for Workgroups. For new applications, use [**WNetCancelConnection2**](/windows/win32/api/winnetwk/nf-winnetwk-wnetcancelconnection2a).

For more information about using an application-defined error handler, see [Retrieving Network Errors](retrieving-network-errors.md).

 

 