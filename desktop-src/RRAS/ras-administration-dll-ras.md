---
title: RAS administration DLL
description: The DLL exports functions that the RAS server calls whenever a user tries to connect or disconnect.
ms.assetid: 014ab85d-8924-4c7a-89ed-f83e75318ca6
ms.topic: article
ms.date: 05/31/2018
---

# RAS administration DLL

The DLL exports functions that the RAS server calls whenever a user tries to connect or disconnect. You can use the DLL to perform the following administrative functions:

-   Decide whether to allow a user to connect to the server. This can provide a security check in addition to the standard RAS user authentication.
-   Record the time that each user connects to and disconnects from the server. This can be useful for billing or auditing purposes.
-   Assign an IP address to each user. This can be useful for security purposes to map a user's connection to a specific computer.

Implement the following functions when developing a RAS server administration DLL.

-   [**RasAdminAcceptNewConnection**](rasadminacceptnewconnection.md)
-   [**RasAdminConnectionHangupNotification**](rasadminconnectionhangupnotification.md)
-   [**RasAdminGetIpAddressForUser**](rasadmingetipaddressforuser.md)
-   [**RasAdminReleaseIpAddress**](rasadminreleaseipaddress.md)

A RAS administration DLL must implement and export all of the above functions. If any of the functions are not implemented, the remote access service will fail to start.

The [**RasAdminAcceptNewConnection**](rasadminacceptnewconnection.md) and [**RasAdminConnectionHangupNotification**](rasadminconnectionhangupnotification.md) functions enable the DLL to audit user connections to the server. A Windows NT/Windows 2000 RAS server calls the **RasAdminAcceptNewConnection** function whenever a user tries to connect. The function can prevent the user from connecting. You can also use the function to generate an entry in a log for billing or auditing. When the user disconnects, the RAS server calls the **RasAdminConnectionHangupNotification** function, which can log the time at which the user disconnected.

After the RAS server has authenticated a caller, it calls the [**RasAdminGetIpAddressForUser**](rasadmingetipaddressforuser.md) function to get an IP address for the remote client. The DLL can use this function to provide an alternate scheme for mapping an IP address to a dial-in user. If **RasAdminGetIpAddressForUser** is not implemented, a RAS server connects a remote user to an IP address selected from a static pool of IP addresses, or one selected by a Dynamic Host Configuration Protocol (DHCP) server. The **RasAdminGetIpAddressForUser** function allows the DLL to override this default IP address and specify a particular IP address for each user. The **RasAdminGetIpAddressForUser** function can set a flag that causes RAS to call the [**RasAdminReleaseIpAddress**](rasadminreleaseipaddress.md) function when the user disconnects. The DLL can use [**RasAdminReleaseIpAddress**](rasadminreleaseipaddress.md) to update its user-to-IP-address map.

RAS serializes calls into the administration DLL. A call into one of the DLL's functions for a given RAS client will never be preempted by a call to that function for a different RAS client; the initial call is guaranteed to be complete before RAS calls the function for the other client. Furthermore, serialization extends to certain groups of functions. The IP address functions are serialized as a group; a call into either [**RasAdminGetIpAddressForUser**](rasadmingetipaddressforuser.md) or [**RasAdminReleaseIpAddress**](rasadminreleaseipaddress.md) will block calls into both until the initial call is complete. [**RasAdminAcceptNewConnection**](rasadminacceptnewconnection.md) and [**RasAdminConnectionHangupNotification**](rasadminconnectionhangupnotification.md) are also serialized as a group.

RAS executes the functions for assigning IP addresses in one process and executes the functions for connection and disconnection notifications in another process. Consequently, the DLL should not depend on shared data between the two sets of functions.

The RAS server logs an error in the system event log if an error occurs when it tries to load a RAS administration DLL or when calling one of the DLL's functions. This can happen, for example, if the DLL specified the wrong name for an exported function, or if it did not include the function name in the .def file. The entry in the event log indicates the reason for the failure.

**Windows 2000 Server and later:** RAS administration DLLs that implement this function interface no longer work. Instead, use the MprAdmin function interface provided with the more recent versions of Windows. For more information, see the [RAS Administration Reference](remote-access-service-administration-reference.md) in the Routing and RAS documentation.

 

 




