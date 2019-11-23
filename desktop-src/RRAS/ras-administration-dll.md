---
title: About RAS administration DLLs
description: The RAS Administration DLL exports functions that the RAS server calls whenever a user tries to connect or disconnect.
ms.assetid: c15c6e2d-3bb6-4583-9ac3-19528feb863f
keywords:
- RAS Administration RRAS , RAS administration DLL
ms.topic: article
ms.date: 05/31/2018
---

# About RAS administration DLLs

The RAS Administration DLL exports functions that the RAS server calls whenever a user tries to connect or disconnect. Here are some of the possible uses for a RAS administration DLL:

-   Decide whether to allow a user to connect to the server. The administration DLL can provide a security check in addition to the standard RAS user authentication.
-   Record the time that each user connects to and disconnects from the server. This can be useful for billing or auditing purposes.
-   Assign an IP address to each user. This is useful for security, because this feature is used to map a user's connection to a specific computer.

The location of the RAS Administration DLL is specified in the registry; see [RAS Administration DLL Registry Setup](ras-administration-dll-registry-setup.md).

RAS supports multiple Administration DLLs. The registry supports multiple DLL locations. RAS calls the functions in the DLLs in the order in which the DLLs are listed in the registry; see [RAS Administration DLL Registry Setup](ras-administration-dll-registry-setup.md).

**Windows 2000 Server:** RAS does not support multiple DLLs.

A RAS administration DLL must implement and export all of the following functions:

[**MprAdminAcceptNewLink**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewlink)

[**MprAdminInitializeDll**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmininitializedll)

[**MprAdminLinkHangupNotification**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminlinkhangupnotification)

[**MprAdminTerminateDll**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminterminatedll)

In addition, the RAS administration DLL must implement and export either

[**MprAdminAcceptNewConnection**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection) and

[**MprAdminConnectionHangupNotification**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectionhangupnotification)

or

[**MprAdminAcceptNewConnection2**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection2) and

[**MprAdminConnectionHangupNotification2**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectionhangupnotification2)

If all of the required functions are not implemented, RAS fails to start.

**Windows 2000 Server:** An administration DLL must implement the [**MprAdminGetIpAddressForUser**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingetipaddressforuser) and [**MprAdminReleaseIpAddress**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminreleaseipaddress) functions. If the DLL implements one of these functions it must implement the other as well.

RAS calls the [**MprAdminInitializeDll**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmininitializedll) function when the Routing and Remote Access Service first starts up. The **MprAdminInitializeDll** function provides an opportunity for the administration DLL to do any necessary initialization. Similarly, RAS calls the [**MprAdminTerminateDll**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminterminatedll) service when the Routing and Remote Access Service shuts down. This function allows the administration DLL to perform any necessary cleanup before exiting.

The [**MprAdminAcceptNewConnection**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection) and [**MprAdminConnectionHangupNotification**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectionhangupnotification) functions enable the DLL to audit user connections to the server. A RAS server calls the **MprAdminAcceptNewConnection** function whenever a user tries to connect. This function makes it possible to prevent the user from connecting. The **MprAdminAcceptNewConnection** function could also generate log entries for billing or auditing. When the user disconnects, the RAS server calls the **MprAdminConnectionHangupNotification** function, which can log the time at which the user disconnected.

The [**MprAdminAcceptNewConnection2**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection2) and [**MprAdminConnectionHangupNotification2**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectionhangupnotification2) functions are similar to **MprAdminAcceptNewConnection** and [**MprAdminConnectionHangupNotification**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectionhangupnotification). However, when RAS calls the **MprAdminAcceptNewConnection2** and **MprAdminConnectionHangupNotification2** functions, RAS passes in an additional parameter of type [**RAS\_CONNECTION\_2**](/windows/desktop/api/Mprapi/ns-mprapi-ras_connection_2).

RAS supports multiple Administration DLLs. The remote-access user is allowed to connect only if the implementation of the [**MprAdminAcceptNewConnection**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection) or [**MprAdminAcceptNewConnection2**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection2) function in each of the DLLs accepts the connection. In other words, every DLL must accept the connection in order for the user to be allowed to connect.

It is possible for a single RAS connection to use multiple links when connecting to a RAS server. The [**MprAdminAcceptNewLink**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewlink) and [**MprAdminLinkHangupNotification**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminlinkhangupnotification) functions make it possible for the Administration DLL to manage individual links in a connection. RAS calls **MprAdminAcceptNewLink** whenever a new link is established for a connection. Because all connections involve at least one link, RAS always calls **MprAdminAcceptNewLink** once immediately after [**MprAdminAcceptNewConnection**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection) or [**MprAdminAcceptNewConnection2**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection2) returns, provided that [**MprAdminAcceptNewConnection**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection) or [**MprAdminAcceptNewConnection2**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection2) accepted the connection. RAS calls **MprAdminLinkHangupNotification** whenever a link for a connection is shutdown.

Because RAS supports multiple Administration DLLs, the remote-access user is allowed to connect only if the implementation of the [**MprAdminAcceptNewLink**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewlink) function in each of the DLLs accepts the connection. In other words, every DLL must accept the link in order for the link to be established.

After the RAS server has authenticated a user, it calls the [**MprAdminGetIpAddressForUser**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingetipaddressforuser) function to get an IP address for the remote client. This function provides an alternate scheme for mapping an IP address to a dial-in user. If **MprAdminGetIpAddressForUser** is not implemented, a RAS server associates the remote user with an IP address that is selected from a static pool of IP addresses, or one selected by a Dynamic Host Configuration Protocol (DHCP) server. The **MprAdminGetIpAddressForUser** function allows the DLL to override this default IP address and specify a particular IP address for each user. The **MprAdminGetIpAddressForUser** function can set a flag that causes RAS to call the [**MprAdminReleaseIpAddress**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminreleaseipaddress) function when the user disconnects. The DLL can then use **MprAdminReleaseIpAddress** to update its user-to-IP-address mapping.

RAS supports multiple Administration DLLs, but it calls the [**MprAdminGetIpAddressForUser**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingetipaddressforuser) and [**MprAdminReleaseIpAddress**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminreleaseipaddress) functions only in the first DLL that implements and export them. RAS ignores implementations of these functions in the other DLLs. RAS checks the DLLs for these functions in the order in which they are listed in the [registry](ras-administration-dll-registry-setup.md).

RAS serializes calls into the administration DLL. A call into one of the DLL's functions for a given RAS client does not preempt a call to that function for a different RAS client; RAS does not call the function for the other client until the initial call is complete. Furthermore, serialization extends to certain groups of functions. The IP address functions are serialized as a group; a call into either [**MprAdminGetIpAddressForUser**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingetipaddressforuser) or [**MprAdminReleaseIpAddress**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminreleaseipaddress) blocks calls into both functions until the initial call has returned. [**MprAdminAcceptNewConnection**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminacceptnewconnection) and [**MprAdminConnectionHangupNotification**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminconnectionhangupnotification) are also serialized as a group.

RAS executes the functions that assign IP addresses in one process; the functions for connection and disconnection notifications are executed in another process. Consequently, the DLL does not depend on shared data between these two sets of functions.

Do not call any of the [RAS Administration Functions](ras-administration-functions.md) or [RAS User Administration Functions](ras-user-administration-functions.md) from inside a callout function. Calls to these functions will not return when made from within a callout function.

The RAS server logs an error in the system event log if an error occurs when it tries to load a RAS administration DLL or when calling one of the DLL's functions. This can happen, for example, if the DLL specified the wrong name for an exported function, or if it did not include the function name in the DEF file. The entry in the event log indicates the reason for the failure.

**Windows 2000/NT:** Multiple administration DLLs are not supported.

 

 




