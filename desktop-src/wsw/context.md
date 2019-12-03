---
title: Context (Windows Web Services)
description: A context is used in Service Model service operations and callbacks to pass relevant state data to the service operation or callback when it is invoked.
ms.assetid: 44283854-96df-4e6b-8464-3df685896f07
keywords:
- Context Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Context (Windows Web Services)

A context is used in Service Model [service operations](service-operation.md) and callbacks to pass relevant state data to the service operation or callback when it is invoked. A context is referenced by a [WS\_OPERATION\_CONTEXT](ws-operation-context.md) structure. The properties of a context can be retrieved with the [**WsGetOperationContextProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetoperationcontextproperty) function, as illustrated in the following code.

``` syntax
WS_MESSAGE* requestMessage = NULL;
HRESULT hr = WsGetOperationContextProperty (
                context, 
                WS_OPERATION_CONTEXT_PROPERTY_INPUT_MESSAGE, 
                &requestMessage, 
                sizeof(requestMessage),
                error);
```

Not all the context properties are available at any given time. See the context property documentation regarding availability of a specific property in a callback or a [service operation](service-operation.md).

For more information on how to maintain operation context lifetime and threading, see the [Operation Context Lifetime and Threading](operation-context-lifetime-and-threading.md) topic.

The following enumeration is part of the context:

-   [**WS\_OPERATION\_CONTEXT\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_operation_context_property_id)

The following function is part of the context:

-   [**WsGetOperationContextProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetoperationcontextproperty)

The following handle is part of the context:

-   [WS\_OPERATION\_CONTEXT](ws-operation-context.md)

 

 




