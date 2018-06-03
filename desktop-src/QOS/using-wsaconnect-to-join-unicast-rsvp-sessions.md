---
title: Using WSAConnect to Join Unicast RSVP Sessions
description: The WSAConnect function is generally used by unicast receivers to join RSVP sessions. The behavior is somewhat different with TCP sessions and UDP unicast sessions.
ms.assetid: f247e925-832a-4ee3-abd6-1ec3cc91827d
keywords:
- Quality of Service QOS , tasks, joining unicast sessions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using WSAConnect to Join Unicast RSVP Sessions

The [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function is generally used by unicast receivers to join RSVP sessions. The behavior is somewhat different with TCP sessions and UDP unicast sessions.

## TCP Sessions

The use of the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function with RSVP-enabled TCP sessions is fairly simple, if somewhat stringent, because parameters match quite well between parameters associated with the **WSAConnect** function and parameters necessary for RSVP to operate. The following table illustrates which conditions of a TCP socket (left column) correspond to RSVP conditions (right column) that enable the TCP socket to join the session.



| TCP Socket is:                                                                                               | RSVP session is joined:                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Not bound, or is bound and not connected (the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function is not issued) | Never.                                                                                                                                                                                                                                                                                          |
| Bound and connected.                                                                                         | If both of the following conditions are true: The port and address specified in any TCP session matches the socket's bound port and address.<br/> SenderTemplate, which is specified in PATH state associated with the session, matches the connected peer's port and address.<br/> |



 

### UDP Unicast Sessions

The use of the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function with RSVP-enabled UDP unicast sessions is less stringent than its use with TCP sessions, largely due to the fact that it is not always possible to determine unique addresses associated with a UDP socket. The following table illustrates which conditions of a UDP unicast socket (left column) correspond to RSVP conditions (right column) that enable the UDP unicast socket to join the session. These mappings do not apply to UDP multicast sessions.



| UDP unicast socket is:                                                                                          | RSVP session is joined:                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Not bound but not connected.                                                                                    | Never.                                                                                                                                                                                                                                                                                          |
| Bound using INADDR\_ANY, but not connected (the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function is not issued). | If the port specified in any UDP session matches the socket's bound port.                                                                                                                                                                                                                       |
| Bound using a specific address and not connected.                                                               | If the port and address specified in any UDP session matches the socket's bound port and address.                                                                                                                                                                                               |
| Bound using INADDR\_ANY, and connected.                                                                         | If both of the following conditions are true: The port specified in any UDP session matches the socket's bound port.<br/> SenderTemplate, which is specified in PATH state associated with the UDP session, matches the connected peer's port and address.<br/>                     |
| Bound using a specific address and connected.                                                                   | If both of the following conditions are true: The port and address specified in any UDP session matches the socket's bound port and address.<br/> SenderTemplate, which is specified in PATH state associated with the session, matches the connected peer's port and address.<br/> |



 

 

 





