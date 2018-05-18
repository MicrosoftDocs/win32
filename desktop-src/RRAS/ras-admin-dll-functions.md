---
title: RAS Administration DLL Functions
description: A RAS administration DLL must implement and export all of the following functions
ms.assetid: 'bf2bd4d4-6da2-471e-843c-c0f0563d3795'
---

# RAS Administration DLL Functions

A RAS administration DLL must implement and export all of the following functions:

-   [**MprAdminAcceptNewLink**](mpradminacceptnewlink.md)
-   [**MprAdminAcceptReauthentication**](mpradminacceptreauthentication.md) or [**MprAdminAcceptReauthenticationEx**](mpradminacceptreauthenticationex.md)
-   [**MprAdminInitializeDll**](mpradmininitializedll.md) or [**MprAdminInitializeDllEx**](mpradmininitializedllex.md)
-   [**MprAdminLinkHangupNotification**](mpradminlinkhangupnotification.md)
-   [**MprAdminTerminateDll**](mpradminterminatedll.md)

**Windows 2000/NT:** The RAS administration DLL must also implement and export the following pair of functions: [**MprAdminGetIpAddressForUser**](mpradmingetipaddressforuser.md) and [**MprAdminReleaseIpAddress**](mpradminreleaseipaddress.md)

In addition, the RAS administration DLL must implement and export one of the following pairs of functions:

-   [**MprAdminAcceptNewConnection**](mpradminacceptnewconnection.md) and [**MprAdminConnectionHangupNotification**](mpradminconnectionhangupnotification.md)
-   [**MprAdminAcceptNewConnection2**](mpradminacceptnewconnection2.md) and [**MprAdminConnectionHangupNotification2**](mpradminconnectionhangupnotification2.md)
-   [**MprAdminAcceptNewConnection3**](mpradminacceptnewconnection3.md) and [**MprAdminConnectionHangupNotification3**](mpradminconnectionhangupnotification3.md)
-   [**MprAdminAcceptNewConnectionEx**](mpradminacceptnewconnectionex.md) and [**MprAdminConnectionHangupNotificationEx**](https://msdn.microsoft.com/library/windows/desktop/dd408066)

If one of the required functions is not implemented, the remote access service fails to start.

An administration DLL is not required to implement the following pairs of functions:

-   [**MprAdminGetIpAddressForUser**](mpradmingetipaddressforuser.md) and [**MprAdminReleaseIpAddress**](mpradminreleaseipaddress.md)
-   [*MprAdminGetIpv6AddressForUser*](mpradmingetipv6addressforuser.md) and [*MprAdminReleaseIpv6AddressForUser*](mpradminreleaseipv6addressforuser.md)

However, if the DLL implements one function in a pair listed above, it must implement the other function in the pair as well.

For more information on RAS Administration DLLs, see the overview topic, [RAS Administration DLL](ras-administration-dll.md).

 

 




