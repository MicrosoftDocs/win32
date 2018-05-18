---
title: Using WSAJoinLeaf to Join Multicast RSVP Sessions
description: Multicast UDP receivers are expected to create the multicast UDP socket using the WSASocket function, and indicate that they are multicast receivers in the accompanying (WSASocket) flags.
ms.assetid: 'c1d5c71a-595a-4e19-97fa-8d39653f11fb'
keywords: ["Quality of Service QOS , tasks, joining multicast sessions"]
---

# Using WSAJoinLeaf to Join Multicast RSVP Sessions

Multicast UDP receivers are expected to create the multicast UDP socket using the [**WSASocket**](https://msdn.microsoft.com/library/windows/desktop/ms742212) function, and indicate that they are multicast receivers in the accompanying (**WSASocket**) flags. If multicast UDP sockets don't use the **WSASocket** function (and associated multicast flags), the RSVP SP may not be able to determine that the socket is multicast, and therefore may send undesired RESV messages based on unicast matching rules described in the [Using WSAConnect to Join Unicast RSVP Sessions](using-wsaconnect-to-join-unicast-rsvp-sessions.md) section.

The following table illustrates which conditions of a UDP multicast socket (left column) correspond to RSVP conditions (right column) that enable the UDP multicast socket to join the session (note these mappings do not apply to UDP unicast sessions).



| UDP multicast socket is:                                                                                        | RSVP session is joined:                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Not joined to a specific multicast group (the [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function is not issued). | Never.                                                                                                                           |
| Joined to a specific multicast group (using the **WSAJoinLeaf** function).                                      | The multicast address specified in any UDP session matches the multicast address specified in the **WSAJoinLeaf** function call. |



 

Applications are required to use the **WSAJoinLeaf** function call before sending or receiving multicast traffic, and are required to set the *dwFlags* parameter of the **WSAJoinLeaf** function to JL\_SENDER\_ONLY, JL\_RECEIVER\_ONLY or JL\_BOTH, to indicate the direction in which QOS service is requested.

It is important to note that alternate multicast semantics, such as simply calling the [**sendto**](https://msdn.microsoft.com/library/windows/desktop/ms740148) function with a multicast address (for sending) or using IP\_ADD\_MEMBERSHIP (for receiving) do not invoke QOS service, even if the IOCTL is issued.

 

 




