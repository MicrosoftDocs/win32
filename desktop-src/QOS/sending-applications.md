---
title: Sending Applications
description: Information on sending applications.
ms.assetid: '92991864-66b8-4178-b04b-4d2e3f63b232'
---

# Sending Applications

In order for the RSVP SP to invoke RSVP processing and signaling, the following information must be available:

-   Peer address (the receiver's address). This enables RSVP to create its session object.
-   Source address (the sender's local address). This enables RSVP to create its SenderTemplate object.
-   QOS parameters in the form of a **SendingFlowspec** (a member of the [**QOS**](qos.md) structure). This enables RSVP to generate its sender Tspec object.

The means by which the RSVP SP derives information necessary to satisfy those three requirements is outlined in the following table.



| Sender type          | Session information derived from:                                                                                                                         | SenderTemplate derived from:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UDP unicast sender   | Destination address and port specified in the *name* parameter of the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function.                                    | Local port determined by a RSVP SP call to the [**getsockname**](https://msdn.microsoft.com/library/windows/desktop/ms738543) function. For sockets bound explicitly by the application, to a specific address, the RSVP SP calls the getsockname function to get the local address/port.<br/> For sockets bound by the application to INADDR\_ANY, the RSVP SP gets the local address by issuing a routing interface query on the destination address (as obtained from the application's call to the WSAConnect or [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function).<br/> |
| UDP multicast sender | Multicast IP address and port as specified in the *name* parameter of the [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function.                              | Same as above.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| TCP unicast sender   | Peer (destination) address and port as determined by a call to the [**getpeername**](https://msdn.microsoft.com/library/windows/desktop/ms738533) function, following connection establishment. | Local address and local port determined by call to the getsockname function following connection establishment.                                                                                                                                                                                                                                                                                                                                                                                                                                     |



 

Details of each of these sender types are outlined individually in the following reference pages:

-   UDP unicast senders
-   UDP multicast senders
-   TCP unicast senders

## UDP Unicast Senders

The RSVP SP derives information for the initiation of RSVP processing and signaling for UDP unicast senders based on the following table.



| Sender type        | Session information derived from:                                                                                      | SenderTemplate derived from:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UDP unicast sender | Destination address and port specified in the *name* parameter of the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function. | Local port determined by a RSVP SP call to the [**getsockname**](https://msdn.microsoft.com/library/windows/desktop/ms738543) function. For sockets bound explicitly by the application, to a specific address, the RSVP SP calls the [**getsockname**](https://msdn.microsoft.com/library/windows/desktop/ms738543) function to get the local address.<br/> For sockets bound by the application to INADDR\_ANY, the RSVP SP gets the local address by issuing a routing interface query on the destination address (as obtained from the application's call to the WSAConnect or [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function).<br/> |



 

Unicast UDP senders typically call the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function to invoke RSVP processing and signaling. For sockets that have been bound using INADDR\_ANY, the RSVP SP uses the peer address to determine the local address to use SenderTemplate by issuing a routing interface query to the underlying transport service provider. This approach returns the address of the local interface used to reach the specified peer.

Typically, the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function call includes sending QOS parameters (SendingFlowspec). Alternatively, the sending application may use the **WSAIoctl**(SIO\_SET\_QOS) function/opcode call to provide sending QOS parameters to the RSVP SP, either before or after the **WSAConnect** function call.

RSVP processing begins as soon as the RSVP SP knows the peer address (from which it may also determine the local bound address) and the sending QOS parameters.

Application programmers can also choose to use unconnected UDP sockets using **WSAIoctl**(SIO\_SET\_QOS) by specifying a [**QOS\_DESTADDR**](qos-destaddr.md) object in the [ProviderSpecific](the-providerspecific-buffer.md) buffer of the [**QOS**](qos.md) structure. In this scenario, the session information is derived from the **QOS\_DESTADDR** object.

> [!Note]  
> Note for unconnected UDP sockets  An application may choose to use unconnected UDP sockets by specifying a [**QOS\_DESTADDR**](qos-destaddr.md) object in the [ProviderSpecific](the-providerspecific-buffer.md) buffer of the [**QOS**](qos.md) structure. In this case, the session information is derived from the **QOS\_DESTADDR** object.

 

## UDP Multicast Senders

The RSVP SP derives information for the initiation of RSVP signaling for UDP multicast senders based on the following table.



| Sender type          | Session information derived from:                                                                                            | SenderTemplate derived from:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UDP multicast sender | Multicast IP address and port as specified in the *name* parameter of the [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function. | Local port determined by RSVP SP call to the [**getsockname**](https://msdn.microsoft.com/library/windows/desktop/ms738543) function. For sockets bound explicitly by the application, to a specific address, the RSVP SP calls the [**getsockname**](https://msdn.microsoft.com/library/windows/desktop/ms738543) function to get the local address.<br/> For sockets bound by the application to INADDR\_ANY, the RSVP SP gets the local address by issuing a routing interface query on the destination address (as obtained from the application's call to the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) or [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function). <br/> |



 

Multicast UDP senders typically call the [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function to invoke RSVP signaling. The **WSAJoinLeaf** function call provides the destination multicast session address, and may also be used to provide QOS parameters through its LPQOS parameter. If QOS parameters are not provided with the call to **WSAJoinLeaf**, they must be provided separately with a call to the **WSAIoctl**(SIO\_SET\_QOS) function/opcode pair. The RSVP session object included in the corresponding PATH messages is derived from the multicast session address.

For sockets that have been bound using INADDR\_ANY, the RSVP SP uses the multicast session address to determine the local address used in SenderTemplate by issuing a routing interface query to the underlying transport service provider. This approach returns the address of the local interface used to reach the specified peer. RSVP processing begins as soon as the RSVP SP knows the peer address and the sending QOS parameters.

## TCP Unicast Senders

The RSVP SP derives information for the initiation of RSVP processing and signaling for TCP unicast senders based on the following table.



| Sender type        | Session information derived from:                                                                                                                         | SenderTemplate derived from:                                                                                                                 |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| TCP unicast sender | Peer (destination) address and port as determined by a call to the [**getpeername**](https://msdn.microsoft.com/library/windows/desktop/ms738533) function, following connection establishment. | Local address and local port determined by call to the [**getsockname**](https://msdn.microsoft.com/library/windows/desktop/ms738543) function following connection establishment. |



 

Generally, sockets are connected through the interaction of an active and passive peer; the active peer issues a [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function call, and the passive peer issues a [**WSAAccept**](https://msdn.microsoft.com/library/windows/desktop/ms741513) function call. In most circumstances the receiver is the active peer, the sender the passive peer. This page assumes the sender is the passive peer; for cases where the sender is the active peer, refer to TCP unicast receivers.

Upon calling the [**WSAAccept**](https://msdn.microsoft.com/library/windows/desktop/ms741513) function, the TCP unicast sender can gather QOS parameters through the WSAAccept function's callback function, but in order to do so, the application must complete the callback function with status CF\_ACCEPT. The RSVP SP does not use the [ProviderSpecific](the-providerspecific-buffer.md) buffer when calling the **WSAAccept** function's callback function.

Applications may alternatively set QOS parameters on the socket (or any parameters that require use of the [ProviderSpecific](the-providerspecific-buffer.md) buffer) through the use of the **WSAIoctl** (SIO\_SET\_QOS) function/opcode call. However, if the application has previously associated QOS parameters with the socket by calling the **WSAIoctl** (SIO\_SET\_QOS) function/opcode pair, completion of the callback function may modify QOS parameters unless the ServiceType parameters in the corresponding [**FLOWSPEC**](flowspec.md) structures are set to SERVICETYPE\_NOCHANGE.

The application may also set QOS parameters on the listening socket prior to the call to [**WSAAccept**](https://msdn.microsoft.com/library/windows/desktop/ms741513), and these settings are inherited by the accepted socket, but any parameters set in the **WSAAccept** function's callback function take precedence. RSVP processing begins as soon as the RSVP SP knows the peer address, the address to which the socket is locally bound, and the sending QOS parameters.

 

 





