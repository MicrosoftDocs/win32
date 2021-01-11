---
title: Client-side Service Operations
ms.assetid: 9d6e2441-91de-4108-b1c4-282fbca5fe7c
description: "Learn more about: Client-side Service Operations"
keywords:
- Client Side Service Operations Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Client-side Service Operations

The following is the layout of a client-side service operation:

-   [WS\_SERVICE\_PROXY](ws-service-proxy.md)\* serviceProxy: The [service proxy](service-proxy.md) for the call.
-   [WS\_HEAP](ws-heap.md)\* heap: A required heap used for body serialization and deserialization of the [WS\_MESSAGE](ws-message.md).
-   Service Operations Parameters: Parameters pertaining to the service operation.
-   [**Call Properties and their count**](/windows/desktop/api/WebServices/ns-webservices-ws_call_property): An array of call properties.
-   [**Call**](/windows/desktop/api/WebServices/ns-webservices-ws_call_property) property count: The count of call properties.
-   [**WS\_ASYNC\_CONTEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_async_context) asyncContext: Async context for executing the call asynchronously.
-   [WS\_ERROR](ws-error.md) error: Rich error object.


### Signature for Client-side Service Operations

``` syntax
typedef HRESULT(CALLBACK *ICalculator_Add)(WS_SERVICE_PROXY* serviceProxy, 
                                           WS_HEAP* heap, 
                                           ULONG a, ULONG b, ULONG* result, 
                                           const WS_CALL_PROPERTY* callProperties, 
                                           const ULONG callPropertyCount, 
                                           const WS_ASYNC_CONTEXT* asyncContext, 
                                           WS_ERROR* error);
```

### Memory Considerations for Client-side Service Operations

The call to the service operation takes a [WS\_HEAP](ws-heap.md)\* as parameter. This is a required parameter used for serialization/deserialization of message bodies to parameters.

The application must call [**WsResetHeap**](/windows/desktop/api/WebServices/nf-webservices-wsresetheap) whether the call succeeded or not. If the call succeeded and it has outgoing parameters, the application should call **WsResetHeap** immediately after it is finished with the outgoing parameters.

The application should allocate memory for in and out parameters with [**WsAlloc**](/windows/desktop/api/WebServices/nf-webservices-wsalloc). The service proxy may need to reallocate them so provided pointers will be overwritten. An attempt to free such memory will cause the application to crash.

### Client-side Service Operation and WS\_HEAP

``` syntax
HRESULT hr = IProcessOrder_ProcessOrder(serviceProxy, heap, orderNumber, &orderReceipt, NULL, 0, NULL, error);
if(FAILED(hr))
    goto error;
hr = ProcessReceipt(orderReceipt);
WsResetHeap(heap);
if(FAILED(hr))
    goto error;
hr = IProcessOrder_CompleteOrder(serviceProxy, heap, orderNumber, &orderMemo, NULL, 0, NULL, error);
if(FAILED(hr))
    goto error;
hr = ProcessMemo(orderMemo);
WsResetHeap(heap);
if(FAILED(hr))
    goto error;
```

### Error parameter

The application should always pass in the error parameter to:

-   Get rich error information if a failure occurs during the service operation call.
-   Get the fault object if the service returned back a fault. The fault is contained in the error object. In this case, the **HRESULT** value returned from the service operation is **WS\_E\_ENDPOINT\_FAULT\_RECEIVED** (see [Windows Web Services Return Values](windows-web-services-return-values.md)).

### Call Properties for Client-side Service Operations

Call properties allow an application to specify custom settings for a given call. Currently, only one call property is available with the service model, [**WS\_CALL\_PROPERTY\_CALL\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_call_property_id).

``` syntax
WS_CALL_PROPERTY callProperties[1] = {0};
callProperties[0].id = WS_CALL_PROPERTY_CALL_ID;
callProperties[0].value = 5;

HRESULT hr = IProcessOrder_ProcessOrder(serviceProxy, heap, orderNumber, &orderReceipt,  callProperties, WsCountOf(callProperties), NULL, error);
if(FAILED(hr))
    goto error;
//:
//:
hr = IProcessOrder_CompleteOrder(serviceProxy, heap, orderNumber, &orderReceipt, callProperties, WsCountOf(callProperties), NULL, error);
if(FAILED(hr))
    goto error;

//:
//:
//:
// On a separate thread 
// In this case both the calls belong to call group 5, and will abandon as a result of the call to WsAbandonCall. 
hr = WsAbandonCall(serviceProxy, 5, error);
```

### Abandoning a Call

It is often desirable to abandon the results of a call in order to relinquish the control back to the application, such that the actual call completion is handled by the infrastructure. Service proxy provides this facility through [**WsAbandonCall**](/windows/desktop/api/WebServices/nf-webservices-wsabandoncall).

Note that the control to the caller may not be given back immediately, the only guarantee that the service proxy runtime gives is that it would not wait for any I/O bound operation to complete before it gives control back to the caller.

Calls on a client side service operation can be abandoned by means of a call to [**WsAbandonCall**](/windows/desktop/api/WebServices/nf-webservices-wsabandoncall). It takes a service proxy and a call id. A call Id is given as part of a call properties on a service operation.

If the call Id is 0, then the service proxy will abandon all pending calls at that instance.

### Call Timeouts

By default a service proxy has a 30 second timeout for every call. The timeout on a call can be changed by [**WS\_PROXY\_PROPERTY\_CALL\_TIMEOUT**](/windows/desktop/api/WebServices/ne-webservices-ws_proxy_property_id) service proxy property when creating a service proxy through [**WsCreateServiceProxy**](/windows/desktop/api/WebServices/nf-webservices-wscreateserviceproxy).

After a timeout is reached, the call is abandoned.

### Return Values

All success **HRESULT** values must be treated as success, and all failure values must be treated as failures. The following are some of the **HRESULT** values that an application can expect:

-   **WS\_S\_ASYNC**: Call will be completed asynchronously.
-   NOERROR: Call completed successfully.
-   **WS\_E\_OPERATION\_ABANDONED**: The call has been abandoned. The error object contains the reason for abandon.
-   **WS\_E\_INVALID\_OPERATION**: The service proxy is not in an appropriate state to make a call, check the service proxy state to figure out the state of the service proxy.

For a complete list of return values, see [Windows Web Services Return Values](windows-web-services-return-values.md).

### Code Examples

For code examples, see the following:

-   [CallAbandonExample](callabandonexample.md)
-   [**WsAbandonCall**](/windows/desktop/api/WebServices/nf-webservices-wsabandoncall)

 

 




