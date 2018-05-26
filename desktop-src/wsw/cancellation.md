---
title: Cancellation
description: Most of operations in the WWSAPI can be canceled during execution.
ms.assetid: dc371921-869f-4775-98d3-80a1006358ba
keywords:
- Cancelation Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Cancellation

Most of operations in the WWSAPI can be canceled during execution.

Which function you use to cancel an operation depends on the object affected.

| Function                                           | Description                                                                                                            |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**WsAbortChannel**](/windows/win32/WebServices/nf-webservices-wsabortchannel?branch=master)           | Cancels all pending input and output on a specified channel and sets the channel state to WS\_CHANNEL\_STATE\_FAULTED. |
| [**WsAbortListener**](/windows/win32/WebServices/nf-webservices-wsabortlistener?branch=master)         | Cancels all pending input and output on a specified listener.                                                          |
| [**WsAbortServiceProxy**](/windows/win32/WebServices/nf-webservices-wsabortserviceproxy?branch=master) | Cancels all pending input and output on a specified service proxy.                                                     |
| [**WsAbortServiceHost**](/windows/win32/WebServices/nf-webservices-wsabortservicehost?branch=master)   | Interrupts and discontinues current operations on the service host.                                                    |
| [**WsAbandonCall**](/windows/win32/WebServices/nf-webservices-wsabandoncall?branch=master)             | Abandons a call, a specified call on a specified service proxy.                                                        |



 

For information on cancellations that affect [server side service operations](server-side-service-operations.md) and service-model callbacks, see [Call Cancellation](call-cancellation.md).

## 

 

 




