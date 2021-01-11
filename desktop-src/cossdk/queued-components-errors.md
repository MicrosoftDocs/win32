---
description: Queued Components Errors
ms.assetid: 29a1bf52-7252-4f8a-bdb7-61b152fb907e
title: Queued Components Errors
ms.topic: article
ms.date: 05/31/2018
---

# Queued Components Errors

When a call to a queued component fails, either because it could not be transmitted to the server (a client-side failure) or because it failed to execute when it arrived (a server-side failure), the corresponding [Message Queuing](/previous-versions/windows/desktop/legacy/ms711472(v=vs.85)) message is called a *poison message*.

The COM+ queued components service handles poison messages by using a series of retry queues. After several retries, the message is moved to a final resting queue. Messages stay in the resting queue until they are moved manually by using the queued components message mover utility. For more information about using the message mover, see [Handling Errors](handling-errors-in-queued-components.md).

Detailed descriptions of the sequence of events that occurs for various sorts of errors can be found in the topics described in the following table.



| Topic                                                                             | Description                                                                                                             |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [Server-Side Errors](server-side-errors.md)<br/>                           | Describes in detail the response of the COM+ queued components service to a server-side failure.<br/>             |
| [Client-Side Errors](client-side-errors.md)<br/>                           | Describes in detail the response of the COM+ queued components service to a client-side failure.<br/>             |
| [Persistent Client-Side Failures](persistent-client-side-failures.md)<br/> | Describes in the detail the response of the COM+ queued components service to repeated client-side failures.<br/> |



 

 

 




