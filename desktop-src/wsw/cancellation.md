---
title: Cancellation
description: Most of operations in the WWSAPI can be canceled during execution.
ms.assetid: 'd73d76e1-bd78-40ce-9f92-e282b6b127ce'
keywords:
- Cancelation Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Cancellation

Most of operations in the WWSAPI can be canceled during execution.

Which function you use to cancel an operation depends on the object affected.

| Function                                           | Description                                                                                                            |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**WsAbortChannel**](/windows/desktop/api/WebServices/nf-webservices-wsabortchannel)           | Cancels all pending input and output on a specified channel and sets the channel state to WS\_CHANNEL\_STATE\_FAULTED. |
| [**WsAbortListener**](/windows/desktop/api/WebServices/nf-webservices-wsabortlistener)         | Cancels all pending input and output on a specified listener.                                                          |
| [**WsAbortServiceProxy**](/windows/desktop/api/WebServices/nf-webservices-wsabortserviceproxy) | Cancels all pending input and output on a specified service proxy.                                                     |
| [**WsAbortServiceHost**](/windows/desktop/api/WebServices/nf-webservices-wsabortservicehost)   | Interrupts and discontinues current operations on the service host.                                                    |
| [**WsAbandonCall**](/windows/desktop/api/WebServices/nf-webservices-wsabandoncall)             | Abandons a call, a specified call on a specified service proxy.                                                        |



 

For information on cancellations that affect [server side service operations](server-side-service-operations.md) and service-model callbacks, see [Call Cancellation](call-cancellation.md).


 

 




