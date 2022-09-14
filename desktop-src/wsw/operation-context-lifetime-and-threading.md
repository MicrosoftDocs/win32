---
title: Operation Context Lifetime and Threading
description: The lifetime of the operation context, represented by a WS\_OPERATION\_CONTEXT handle, determines the lifetime of the properties it contains.
ms.assetid: 37caf382-2b33-464d-b6c1-e4bd3271a5aa
keywords:
- Operation Context Lifetime and Threading Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Operation Context Lifetime and Threading

The lifetime of the operation context, represented by a [WS\_OPERATION\_CONTEXT](ws-operation-context.md) handle, determines the lifetime of the properties it contains. Therefore, a context should only be used within the lifetime of the [service operation](service-operation.md) or the callback to which its provided. The lifetime of a synchronous call is the execution of function itself. For an asynchronous call the lifetime ends once the asynchronous call is completed. The Service Model gives no guarantees about the context once the call is completed. The behavior of relying on operation context or any of its properties beyond its lifetime is undefined.


See also, the session based calculator example, [SessionfullCalculatorServiceExample](sessionfullcalculatorserviceexample.md).

## Threading Model

The operation context supports free threading, however this is true of the operation context itself and does not apply to any of the properties it contains.

When you register a cancel callback for a service operation through the [**WsRegisterOperationForCancel**](/windows/desktop/api/WebServices/nf-webservices-wsregisteroperationforcancel) function, note that the first registration will succeed; setting the cancel callback multiple times, however, will fail.

 

 




