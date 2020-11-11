---
title: Service Host User State
description: The service host enables an application to associate state data that is scoped at the service-host level.
ms.assetid: e18c6c0c-3205-4f88-9a9b-2515a7cfc462
keywords:
- User Host State Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Service Host User State

The [service host](service-host.md) enables an application to associate state data that is scoped at the service-host level. This state is is specified by a [**WS\_SERVICE\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_service_property) structure that is passed to the [**WsCreateServiceHost**](/windows/desktop/api/WebServices/nf-webservices-wscreateservicehost) function when the application creates a [service host](service-host.md), as illustrated in the following example.

``` syntax
void* quotePtr = (void*) quotes;
WS_SERVICE_PROPERTY serviceProperties[1] = {0};
serviceProperties[0].id = WS_SERVICE_PROPERTY_HOST_USER_STATE;
serviceProperties[0].value = &quotePtr; // assume this is some state that you want to associate with the service host
serviceProperties[0].valueSize = sizeof(quotePtr);
```


The state data is available to all service host callbacks and [service operations](service-operation.md). Callbacks and service operations retrieve the information by calling the [**WsGetOperationContextProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetoperationcontextproperty) function and specifying the context, referenced by the [WS\_OPERATION\_CONTEXT](ws-operation-context.md) structure, and the context property, as one of the values of the [**WS\_OPERATION\_CONTEXT\_PROPERTY\_HOST\_USER\_STATE**](/windows/desktop/api/WebServices/ne-webservices-ws_operation_context_property_id) eunumeration, as illustrated in the following example.

``` syntax
QuoteTable* table = NULL;
HRESULT hr = NOERROR;
if (FAILED (WsGetOperationContextProperty (context, WS_OPERATION_CONTEXT_PROPERTY_HOST_USER_STATE, &table, sizeof(table), NULL, error)))
    return hr;
```

 

 




