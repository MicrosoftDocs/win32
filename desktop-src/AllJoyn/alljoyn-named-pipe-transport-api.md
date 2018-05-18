---
title: AllJoyn Named Pipe Transport API
description: This API describes the named pipe transport, which ised instead of TCP/IP in order to implement brokered loopback connectivity to the router node in AllJoyn.
ms.assetid: '7B31CA11-7FA1-41E0-BFED-B75B8D193649'
---

# AllJoyn Named Pipe Transport API

This API describes the named pipe transport, which ised instead of TCP/IP in order to implement brokered loopback connectivity to the router node in AllJoyn. It is the router node's responsibility to implement appropriate policies to restrict an app from talking directly to each other or to arbitrary desktop apps.

This API is public in order to allow code we contribute to the AllJoyn SDK (distributed through the [AllSeen Alliance](http://go.microsoft.com/fwlink/p/?LinkID=526503)) to call this API. It is not expected to be used directly by developers, but is expected to be used by apps that compile using the AllJoyn SDK.

## In this section



| Topic                                                  | Description                                                                                                                                                                                             |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllJoynConnectToBus**](alljoynconnecttobus.md)     | Opens the AllJoyn Router Node Service named pipe, and sets it to **PIPE\_NOWAIT**.                                                                                                                      |
| [**AllJoynCloseBusHandle**](alljoynclosebushandle.md) | Closes the Named Pipe handle.                                                                                                                                                                           |
| [**AllJoynSendToBus**](alljoynsendtobus.md)           | Sends data to the bus via named pipe. The caller of this API is responsible to check if the *bytesTransferred* is less than the requested bytes and call this API again to resend the rest of the data. |
| [**AllJoynReceiveFromBus**](alljoynreceivefrombus.md) | Receives data from the bus via named pipe.                                                                                                                                                              |
| [**AllJoynEventSelect**](alljoyneventselect.md)       | Provides AllJoyn transport functionality similar to the TCP socket [**WSAEventSelect**](https://msdn.microsoft.com/library/windows/desktop/ms741576) functionality.                                                                        |
| [**AllJoynEnumEvents**](alljoynenumevents.md)         | Provides AllJoyn transport functionality similar to the TCP socket [**WSAEnumNetworkEvents**](https://msdn.microsoft.com/library/windows/desktop/ms741572) functionality.                                                            |



 

 

 




