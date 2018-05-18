---
title: Cancellation
description: Most of operations in the WWSAPI can be canceled during execution.
ms.assetid: 'dc371921-869f-4775-98d3-80a1006358ba'
keywords: ["Cancelation Web Services for Windows", "WWSAPI", "WWS"]
---

# Cancellation

Most of operations in the WWSAPI can be canceled during execution.

Which function you use to cancel an operation depends on the object affected.

| Function                                           | Description                                                                                                            |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**WsAbortChannel**](wsabortchannel.md)           | Cancels all pending input and output on a specified channel and sets the channel state to WS\_CHANNEL\_STATE\_FAULTED. |
| [**WsAbortListener**](wsabortlistener.md)         | Cancels all pending input and output on a specified listener.                                                          |
| [**WsAbortServiceProxy**](wsabortserviceproxy.md) | Cancels all pending input and output on a specified service proxy.                                                     |
| [**WsAbortServiceHost**](wsabortservicehost.md)   | Interrupts and discontinues current operations on the service host.                                                    |
| [**WsAbandonCall**](wsabandoncall.md)             | Abandons a call, a specified call on a specified service proxy.                                                        |



 

For information on cancellations that affect [server side service operations](server-side-service-operations.md) and service-model callbacks, see [Call Cancellation](call-cancellation.md).

## 

 

 




