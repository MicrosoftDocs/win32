---
description: Some of the socket IOCTL opcodes for Windows Sockets 2 are summarized in the following table.
ms.assetid: fb6447b4-28f5-4ab7-bbdc-5a57ed38a994
title: Summary of Socket Ioctl Opcodes
ms.topic: article
ms.date: 05/31/2018
---

# Summary of Socket Ioctl Opcodes

Some of the socket IOCTL opcodes for Windows Sockets 2 are summarized in the following table. More detailed information is in the Winsock reference on [**Winsock IOCTLs**](winsock-ioctls.md) and the [**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85)) function. There are other new protocol-specific IOCTL opcodes that can be found in the protocol-specific annex.

A complete list of [**Winsock IOCTLs**](winsock-ioctls.md) are available in the Winsock reference.



| Opcode                                                      | Input type                               | Output type                                 | Meaning                                                                                                                                                                                                            |
|-------------------------------------------------------------|------------------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FIONBIO                                                     | Unsigned long                            | \<Not used\>                            | Enables or disables nonblocking mode on the socket.                                                                                                                                                                |
| FIONREAD                                                    | \<Not used\>                         | Unsigned long                               | Determines the amount of data that can be read atomically from the socket.                                                                                                                                         |
| SIOCATMARK                                                  | \<Not used\>                         | BOOL                                        | Determines whether or not all OOB data has been read.                                                                                                                                                              |
| SIO\_ASSOCIATE\_HANDLE                                      | Companion API dependent                  | \<Not used\>                            | Associates the socket with the specified handle of a companion interface.                                                                                                                                          |
| SIO\_ENABLE\_CIRCULAR\_QUEUEING                             | \<Not used>                         | \<Not used>                            | Enables circular queuing.                                                                                                                                                                                          |
| SIO\_FIND\_ROUTE                                            | [**sockaddr**](sockaddr-2.md) structure | \<Not used>                            | Requests the route to the specified address to be discovered.                                                                                                                                                      |
| SIO\_FLUSH                                                  | \<Not used>                         | \<Not used>                            | Discards current contents of the sending queue.                                                                                                                                                                    |
| SIO\_GET\_BROADCAST\_ADDRESS                                | \<Not used>                         | [**sockaddr**](sockaddr-2.md) structure    | Retrieves the protocol-specific broadcast address to be used in [**WSPSendTo**](/previous-versions/windows/desktop/legacy/ms742291(v=vs.85)).                                                                                                                  |
| SIO\_GET\_QOS                                               | \<Not used>                         | [**QOS**](/windows/win32/api/winsock2/ns-winsock2-qos)                          | Retrieves current flow specifications for the socket.                                                                                                                                                              |
| SIO\_GET\_GROUP\_QOS                                        | \<Not used>                         | [**QOS**](/windows/win32/api/winsock2/ns-winsock2-qos)                          | Reserved.                                                                                                                                                                                                          |
| SIO\_MULTIPOINT\_LOOPBACK                                   | BOOL                                     | \<Not used>                            | Controls whether data sent in a multipoint session will also be received by the same socket on the local host.                                                                                                     |
| SIO\_MULTICAST\_SCOPE                                       | int                                      | \<Not used>                            | Specifies the scope over which multicast transmissions will occur.                                                                                                                                                 |
| SIO\_SET\_QOS                                               | [**QOS**](/windows/win32/api/winsock2/ns-winsock2-qos)                       | \<Not used>                            | Establishes new flow specifications for the socket.                                                                                                                                                                |
| SIO\_SET\_GROUP\_QOS                                        | [**QOS**](/windows/win32/api/winsock2/ns-winsock2-qos)                       | \<Not used>                            | Reserved.                                                                                                                                                                                                          |
| SIO\_TRANSLATE\_HANDLE                                      | int                                      | Companion-API dependent                     | Obtains a corresponding handle for socket *s* that is valid in the context of a companion interface.                                                                                                               |
| SIO\_ROUTING\_INTERFACE\_QUERY                              | [**sockaddr**](sockaddr-2.md)           | [**sockaddr**](sockaddr-2.md)              | Obtains the address of the local interface that should be used to send to the specified address.                                                                                                                   |
| SIO\_ROUTING\_INTERFACE\_CHANGE                             | [**sockaddr**](sockaddr-2.md)           | \<Not used>                            | Requests notification of changes in information reported through SIO\_ROUTING\_INTERFACE\_QUERY for the specified address.                                                                                         |
| [**SIO_ADDRESS_LIST_QUERY**](/windows/win32/winsock/sio-address-list-query) | \<Not used>                         | [**SOCKET\_ADDRESS**](/windows/desktop/api/Ws2def/ns-ws2def-socket_address) | Obtains a list of local transport addresses of the socket's protocol family to which the application can bind. The list of addresses varies based on address family and some addresses are excluded from the list. |
| SIO\_ADDRESS\_LIST\_CHANGE                                  | \<Not used>                         | \<Not used>                            | Requests notification of changes in information reported through SIO\_ADDRESS\_LIST\_QUERY                                                                                                                         |
| SIO\_QUERY\_PNP\_TARGET\_HANDLE                             | \<Not used>                         | SOCKET                                      | Obtains socket descriptor of the next provider in the chain on which current socket depends in regards to PnP.                                                                                                     |

## Related topics

<dl> <dt>

[**Winsock IOCTLs**](winsock-ioctls.md)
</dt> <dt>

[**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85))
</dt> </dl>
