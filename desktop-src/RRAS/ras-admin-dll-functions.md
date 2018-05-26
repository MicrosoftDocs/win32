---
title: RAS Administration DLL Functions
description: A RAS administration DLL must implement and export all of the following functions
ms.assetid: bf2bd4d4-6da2-471e-843c-c0f0563d3795
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RAS Administration DLL Functions

A RAS administration DLL must implement and export all of the following functions:

-   [**MprAdminAcceptNewLink**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptnewlink?branch=master)
-   [**MprAdminAcceptReauthentication**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptreauthentication?branch=master) or [**MprAdminAcceptReauthenticationEx**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptreauthenticationex?branch=master)
-   [**MprAdminInitializeDll**](/windows/win32/Mprapi/nf-mprapi-mpradmininitializedll?branch=master) or [**MprAdminInitializeDllEx**](/windows/win32/Mprapi/?branch=master)
-   [**MprAdminLinkHangupNotification**](/windows/win32/Mprapi/nf-mprapi-mpradminlinkhangupnotification?branch=master)
-   [**MprAdminTerminateDll**](/windows/win32/Mprapi/nf-mprapi-mpradminterminatedll?branch=master)

**Windows 2000/NT:** The RAS administration DLL must also implement and export the following pair of functions: [**MprAdminGetIpAddressForUser**](/windows/win32/Mprapi/nf-mprapi-mpradmingetipaddressforuser?branch=master) and [**MprAdminReleaseIpAddress**](/windows/win32/Mprapi/nf-mprapi-mpradminreleaseipaddress?branch=master)

In addition, the RAS administration DLL must implement and export one of the following pairs of functions:

-   [**MprAdminAcceptNewConnection**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptnewconnection?branch=master) and [**MprAdminConnectionHangupNotification**](/windows/win32/Mprapi/nf-mprapi-mpradminconnectionhangupnotification?branch=master)
-   [**MprAdminAcceptNewConnection2**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptnewconnection2?branch=master) and [**MprAdminConnectionHangupNotification2**](/windows/win32/Mprapi/nf-mprapi-mpradminconnectionhangupnotification2?branch=master)
-   [**MprAdminAcceptNewConnection3**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptnewconnection3?branch=master) and [**MprAdminConnectionHangupNotification3**](/windows/win32/Mprapi/nf-mprapi-mpradminconnectionhangupnotification3?branch=master)
-   [**MprAdminAcceptNewConnectionEx**](/windows/win32/Mprapi/nf-mprapi-mpradminacceptnewconnectionex?branch=master) and [**MprAdminConnectionHangupNotificationEx**](https://msdn.microsoft.com/library/windows/desktop/dd408066)

If one of the required functions is not implemented, the remote access service fails to start.

An administration DLL is not required to implement the following pairs of functions:

-   [**MprAdminGetIpAddressForUser**](/windows/win32/Mprapi/nf-mprapi-mpradmingetipaddressforuser?branch=master) and [**MprAdminReleaseIpAddress**](/windows/win32/Mprapi/nf-mprapi-mpradminreleaseipaddress?branch=master)
-   [*MprAdminGetIpv6AddressForUser*](/windows/win32/Mprapi/nf-mprapi-mpradmingetipv6addressforuser?branch=master) and [*MprAdminReleaseIpv6AddressForUser*](/windows/win32/Mprapi/nf-mprapi-mpradminreleaseipv6addressforuser?branch=master)

However, if the DLL implements one function in a pair listed above, it must implement the other function in the pair as well.

For more information on RAS Administration DLLs, see the overview topic, [RAS Administration DLL](ras-administration-dll.md).

 

 




