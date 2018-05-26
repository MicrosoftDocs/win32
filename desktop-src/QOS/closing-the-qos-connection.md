---
title: Closing the QOS Connection
description: There are a number of ways to close a QOS-enabled connection.
ms.assetid: 824ae8a0-bb97-44fb-8903-7dc4b78293d1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Closing the QOS Connection

There are a number of ways to close a QOS-enabled connection. Generally, any event that closes a socket also ends RSVP SP servicing on the socket. Examples of events that cause the RSVP SP to stop providing QOS functionality on a socket include:

**Note**  RSVP signaling is not supported on Windows XP, Windows Server 2003, or later versions of Windows.

-   Using the [**closesocket**](https://msdn.microsoft.com/library/windows/desktop/ms737582) function to close the socket.
-   Using the [**shutdown**](https://msdn.microsoft.com/library/windows/desktop/ms740481) function to disable sends or receives on a socket. Note, however, that shutting down only the receive capabilities leaves the QOS-enabled send capabilities for the socket intact, and that shutting down only the send capabilities of a socket leaves the QOS-enabled receive capabilities for the socket intact as well.
-   Using the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function with the name parameter set to **NULL**.
-   Using the [**WSAIoctl**](https://msdn.microsoft.com/library/windows/desktop/ms741621) function with the SIO\_SET\_QOS IOCTL opcode, in which the ServiceType member corresponding to SendingFlowspec or ReceivingFlowspec (both of which are of [**FLOWSPEC**](/windows/previous-versions/Qos/ns-qos-_flowspec?branch=master)) is set to SERVICETYPE\_NOTRAFFIC or SERVICETYPE\_BESTEFFORT.
    -   Note that setting SERVICETYPE\_NOTRAFFIC or SERVICETYPE\_BESTEFFORT selectively can disable RSVP SP service for sending and receiving individually. For example, setting the ServiceType member of SendingFlowspec to SERVICETYPE\_NOTRAFFIC or SERVICETYPE\_BESTEFFORT only terminates QOS servicing for sending, and setting the ServiceType member of ReceivingFlowspec to SERVICETYPE\_NOTRAFFIC or SERVICETYPE\_BESTEFFORT only terminates QOS servicing for receiving.

 

 

 




