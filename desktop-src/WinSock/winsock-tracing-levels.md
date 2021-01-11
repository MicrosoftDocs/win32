---
description: "Learn more about: Winsock Tracing Levels"
ms.assetid: a92bc4d2-257a-478a-b10d-4fada4323c9b
title: Winsock Tracing Levels
ms.topic: article
ms.date: 05/31/2018
---

# Winsock Tracing Levels

## Levels of Winsock Tracing

There are two levels of logging possible in Winsock tracing:

-   Information
-   Verbose

The information level traces socket create and close events, as well as any errors that occur on the socket.

The verbose level includes the information level events, and adds additional tracing for send and receive events. The verbose logging would be used to catch buffer corruption issues as well as poorly written applications.

Either the information or verbose level can be used with the Winsock Network Event tracing. The Winsock Catalog Change tracing supports only information level.

## Information Event Tracing

The following list details those Winsock network event socket operations that are traced at the information level:

-   Socket creation

    An event is logged on socket creation which can be used to trace the lifetime of a socket. These events also includes sockets created by accepting connections on a listening socket.

-   Bind

    The local IP address is logged to help correlate the Winsock tracing information to an application's socket calls.

-   Connect

    The remote IP address of the connected socket is logged to help correlate the Winsock tracing information to an application's socket calls.

-   Winsock-initiated aborts and cancels

    Anytime Winsock actively aborts or cancels a request, the event is logged.

-   Transport initiated resets

    Anytime the underlying transport indicates a connection has been reset, the event is logged.

-   Send and receive errors

    Whenever a send or receive call to the underlying transport fails, the event is logged.

-   Socket disconnect and close

    An event is logged when a socket handle is closed.

## Verbose Event Tracing

All of the information events are traced at the verbose level. The following list details those additional Winsock network event socket operations that are traced at the verbose level:

-   Send and receive buffers

    Events are logged of user buffer addresses and lengths when send and receive calls are posted to Winsock, as well as upon completion of these calls. This is useful for diagnosing buffer re-use issues as well as inefficient use of buffers.

-   Socket options

    An event is logged when an application changes certain socket option values. Some of the options logged include SO\_SNDBUF, SO\_RCVBUF, SIO\_ENABLE\_CIRCULAR\_QUEUEING, and FIONBIO.

-   WSAPoll and select

    An event is logged of an application's usage of [**WSAPoll**](/windows/win32/api/winsock2/nf-winsock2-wsapoll) and [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) calls which can be used to find performance bottlenecks.

-   Winsock-initiated aborts and cancels

    Anytime Winsock actively aborts or cancels a request, the event is logged.

-   Event mask

    An event is logged of the event mask an application registers for using the [**WSAEventSelect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaeventselect) function.

-   Datagram

    An event is logged whenever a datagram arrives and there is no buffer space in which to copy it.

## Related topics

<dl> <dt>

[Control of Winsock Tracing](control-of-winsock-tracing.md)
</dt> <dt>

[Winsock Tracing](winsock-tracing.md)
</dt> <dt>

[Winsock Catalog Change Tracing Details](winsock-layered-service-provider-tracing-event-details.md)
</dt> <dt>

[Winsock Network Event Tracing Details](winsock-tracing-event-details.md)
</dt> </dl>

 

 
