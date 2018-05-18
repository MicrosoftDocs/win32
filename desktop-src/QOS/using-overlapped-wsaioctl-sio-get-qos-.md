---
title: Using Overlapped WSAIoctl(SIO\_GET\_QOS)
description: Applications can register their interest in FD\_QOS events by issuing an overlapped WSAIoctl(SIO\_GET\_QOS) function call.
ms.assetid: 'e90aff2e-a0b4-421e-a63f-ded404579036'
keywords: ["Quality of Service QOS , tasks, using overlapped WSAIoctl"]
---

# Using Overlapped WSAIoctl(SIO\_GET\_QOS)

Applications can register their interest in FD\_QOS events by issuing an overlapped WSAIoctl(SIO\_GET\_QOS) function call. When an application takes this approach, an FD\_QOS event invokes the completion function specified in the CompletionRoutine parameter of the [**WSAIoctl**](https://msdn.microsoft.com/library/windows/desktop/ms741621) function call, and the updated [**QOS**](qos.md) structure is made available in its output buffer. With this approach, the application could be developed to use CompletionRoutine to act on the contents of the output buffer. The WSAIoctl(SIO\_GET\_QOS) function request completes with QOS information that corresponds only to one direction (either the SendingFlowspec or the ReceivingFlowspec is valid, but not both). The [**FLOWSPEC**](flowspec.md) that is invalid has its ServiceType value set to SERVICETYPE\_NOCHANGE.

> [!Note]Sending applications cannot call SIO\_GET\_QOS until a connection has completed. However, a receiving application can call SIO\_GET\_QOS as soon as it is bound. When using overlapped WSAIoctl(SIO\_GET\_QOS) to monitor FD\_QOS events, the RSVP SP also passes an [**RSVP\_STATUS\_INFO**](rsvp-status-info.md) object in the [ProviderSpecific](the-providerspecific-buffer.md) buffer of the updated [**QOS**](qos.md) structure. This enables applications to obtain extended status information about the FD\_QOS event.
>
> If the output buffer associated with the [**WSAIoctl**](https://msdn.microsoft.com/library/windows/desktop/ms741621) function call is not sufficiently sized to contain the full [**QOS**](qos.md) structure and the [**RSVP\_STATUS\_INFO**](rsvp-status-info.md) object that is included in its [ProviderSpecific](the-providerspecific-buffer.md) buffer, the application will get WSA\_ENOBUFS and can reissue the query. The required size is returned as an unsigned integer at the beginning of the output buffer.

 

 

 




