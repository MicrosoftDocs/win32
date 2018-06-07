---
Description: Some of the socket IOCTL opcodes for Windows Sockets 2 are summarized in the following table.
ms.assetid: fb6447b4-28f5-4ab7-bbdc-5a57ed38a994
title: Summary of Socket Ioctl Opcodes
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Summary of Socket Ioctl Opcodes

Some of the socket IOCTL opcodes for Windows Sockets 2 are summarized in the following table. More detailed information is in the Winsock reference on [**Winsock IOCTLs**](winsock-ioctls.md) and the [**WSPIoctl**](/windows/desktop/api/Ws2spi/) function. There are other new protocol-specific IOCTL opcodes that can be found in the protocol-specific annex.

A complete list of [**Winsock IOCTLs**](winsock-ioctls.md) are available in the Winsock reference.



| Opcode                                                      | Input type                               | Output type                                 | Meaning                                                                                                                                                                                                            |
|-------------------------------------------------------------|------------------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FIONBIO                                                     | Unsigned long                            | &lt;Not used&gt;                            | Enables or disables nonblocking mode on the socket.                                                                                                                                                                |
| FIONREAD                                                    | &lt;Not used&gt;                         | Unsigned long                               | Determines the amount of data that can be read atomically from the socket.                                                                                                                                         |
| SIOCATMARK                                                  | &lt;Not used&gt;                         | BOOL                                        | Determines whether or not all OOB data has been read.                                                                                                                                                              |
| SIO\_ASSOCIATE\_HANDLE                                      | Companion API dependent                  | &lt;Not used&gt;                            | Associates the socket with the specified handle of a companion interface.                                                                                                                                          |
| SIO\_ENABLE\_CIRCULAR\_QUEUEING                             | &lt;Not used&gt;                         | &lt;Not used&gt;                            | Enables circular queuing.                                                                                                                                                                                          |
| SIO\_FIND\_ROUTE                                            | [**sockaddr**](sockaddr-2.md) structure | &lt;Not used&gt;                            | Requests the route to the specified address to be discovered.                                                                                                                                                      |
| SIO\_FLUSH                                                  | &lt;Not used&gt;                         | &lt;Not used&gt;                            | Discards current contents of the sending queue.                                                                                                                                                                    |
| SIO\_GET\_BROADCAST\_ADDRESS                                | &lt;Not used&gt;                         | [**sockaddr**](sockaddr-2.md) structure    | Retrieves the protocol-specific broadcast address to be used in [**WSPSendTo**](/windows/desktop/api/Ws2spi/).                                                                                                                  |
| SIO\_GET\_QOS                                               | &lt;Not used&gt;                         | [**QOS**](https://msdn.microsoft.com/859faa13-bd66-46ee-8452-6ff5d53d66c9)                          | Retrieves current flow specifications for the socket.                                                                                                                                                              |
| SIO\_GET\_GROUP\_QOS                                        | &lt;Not used&gt;                         | [**QOS**](https://msdn.microsoft.com/859faa13-bd66-46ee-8452-6ff5d53d66c9)                          | Reserved.                                                                                                                                                                                                          |
| SIO\_MULTIPOINT\_LOOPBACK                                   | BOOL                                     | &lt;Not used&gt;                            | Controls whether data sent in a multipoint session will also be received by the same socket on the local host.                                                                                                     |
| SIO\_MULTICAST\_SCOPE                                       | int                                      | &lt;Not used&gt;                            | Specifies the scope over which multicast transmissions will occur.                                                                                                                                                 |
| SIO\_SET\_QOS                                               | [**QOS**](https://msdn.microsoft.com/859faa13-bd66-46ee-8452-6ff5d53d66c9)                       | &lt;Not used&gt;                            | Establishes new flow specifications for the socket.                                                                                                                                                                |
| SIO\_SET\_GROUP\_QOS                                        | [**QOS**](https://msdn.microsoft.com/859faa13-bd66-46ee-8452-6ff5d53d66c9)                       | &lt;Not used&gt;                            | Reserved.                                                                                                                                                                                                          |
| SIO\_TRANSLATE\_HANDLE                                      | int                                      | Companion-API dependent                     | Obtains a corresponding handle for socket *s* that is valid in the context of a companion interface.                                                                                                               |
| SIO\_ROUTING\_INTERFACE\_QUERY                              | [**sockaddr**](sockaddr-2.md)           | [**sockaddr**](sockaddr-2.md)              | Obtains the address of the local interface that should be used to send to the specified address.                                                                                                                   |
| SIO\_ROUTING\_INTERFACE\_CHANGE                             | [**sockaddr**](sockaddr-2.md)           | &lt;Not used&gt;                            | Requests notification of changes in information reported through SIO\_ROUTING\_INTERFACE\_QUERY for the specified address.                                                                                         |
| [**SIO\_ADDRESS\_LIST\_QUERY**](/windows/desktop/api/Ws2def/) | &lt;Not used&gt;                         | [**SOCKET\_ADDRESS**](/windows/desktop/api/Ws2def/ns-ws2def-_socket_address) | Obtains a list of local transport addresses of the socket's protocol family to which the application can bind. The list of addresses varies based on address family and some addresses are excluded from the list. |
| SIO\_ADDRESS\_LIST\_CHANGE                                  | &lt;Not used&gt;                         | &lt;Not used&gt;                            | Requests notification of changes in information reported through SIO\_ADDRESS\_LIST\_QUERY                                                                                                                         |
| SIO\_QUERY\_PNP\_TARGET\_HANDLE                             | &lt;Not used&gt;                         | SOCKET                                      | Obtains socket descriptor of the next provider in the chain on which current socket depends in regards to PnP.                                                                                                     |



 

## Related topics

<dl> <dt>

[**Winsock IOCTLs**](winsock-ioctls.md)
</dt> <dt>

[**WSPIoctl**](/windows/desktop/api/Ws2spi/)
</dt> </dl>

 

 



