---
description: Windows Sockets 2 extends the functionality of Windows Sockets 1.1 in a number of areas. The following table summarizes some of the major feature changes.
ms.assetid: 26bfb614-5700-44d3-b4fb-1002d757d15e
title: Winsock Programming Considerations
ms.topic: article
ms.date: 05/31/2018
---

# Winsock Programming Considerations

Windows Sockets 2 extends the functionality of Windows Sockets 1.1 in a number of areas. The following table summarizes some of the major feature changes.



| Features                                                                                                           | Description                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Windows Sockets 2 Architecture](windows-sockets-2-architecture-2.md)                                             | A description of the Windows Sockets 2 architecture.                                                                                                                                                                                                                                           |
| [Socket handles](socket-handles-2.md)                                                                             | A socket handle can optionally be a file handle in Windows Sockets 2. It is possible to use socket handles with standard Windows file I/O functions.                                                                                                                                           |
| [Simultaneous access to multiple transport protocols](simultaneous-access-to-multiple-transport-protocols-2.md)   | Allows an application to use the familiar socket interface to achieve simultaneous access to a number of installed transport protocols.                                                                                                                                                        |
| [Protocol-independent name resolution](protocol-independent-name-resolution-2.md)                                 | Includes a standardized set of functions for querying and working with the myriad name resolution domains that exist today (for example DNS, SAP, and X.500).                                                                                                                                  |
| [Protocol-independent multicast and multipoint](protocol-independent-multicast-and-multipoint-2.md)               | Applications discover what type of multipoint or multicast capabilities a transport provides and use these facilities in a generic manner.                                                                                                                                                     |
| [Overlapped I/O](overlapped-i-o-and-event-objects-2.md)                                                           | Incorporates the overlapped paradigm for socket I/O following the model established in Windows environments.                                                                                                                                                                                   |
| [Scatter/gather I/O](scatter-gather-i-o-2.md)                                                                     | Incorporates scatter/gather capabilities with the overlapped paradigm for socket I/O, following the model established in Windows environments.                                                                                                                                                 |
| [Quality of Service](flow-specification-quality-of-service-2.md) (QoS)                                            | Establishes conventions that applications use to negotiate required service levels for parameters such as bandwidth and latency. Other QoS-related enhancements include mechanisms for network-specific Quality of Service extensions.                                                         |
| [Provider-Specific Extension Mechanism](provider-specific-extension-mechanism-2.md)                               | The [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function enables service providers to offer provider-specific feature extensions.                                                                                                                                                                           |
| [Shared Sockets](shared-sockets-2.md)                                                                             | The [**WSADuplicateSocket**](/windows/desktop/api/Winsock2/nf-winsock2-wsaduplicatesocketa) function is introduced to enable socket sharing across processes.                                                                                                                                                                       |
| [Connection Setup and Teardown](connection-setup-and-teardown-2.md)                                               | An application can obtain caller information such as caller identifier and Quality of Service before deciding whether to accept an incoming connection request. It is also possible (for protocols that support this) to exchange user data between the endpoints at connection teardown time. |
| [Graceful Shutdown, Linger Options, and Socket Closure](graceful-shutdown-linger-options-and-socket-closure-2.md) | An application has several options for shutting down a socket connection (shutdown sequence).                                                                                                                                                                                                  |
| [Protocol-Independent Out-of-Band Data](protocol-independent-out-of-band-data-2.md)                               | The stream socket abstraction includes the notion of out of band (OOB) data.                                                                                                                                                                                                                   |
| [Debug and Trace Facilities](debug-and-trace-facilities-2.md)                                                     | Windows Sockets 2 supports a specially devised version of the Ws2\_32.dll and a separate debug/trace DLL.                                                                                                                                                                                      |
| [Windows Sockets Compatibility Issues](windows-sockets-compatibility-issues-2.md)                                 | Windows Sockets 2 continues to support all of the Windows Sockets 1.1 semantics and function calls except for those dealing with pseudo-blocking.                                                                                                                                              |
| [Handling Winsock Errors](handling-winsock-errors.md)                                                             | How Winsock errors can be retrieved and handled by an application.                                                                                                                                                                                                                             |



 

 

 



