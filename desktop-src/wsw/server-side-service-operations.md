---
title: Server Side Service Operations
description: This section describes service side service operations.
ms.assetid: d209cf2f-47f5-4025-8af4-1626c867a66a
keywords:
- Server Side Service Operations Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Server Side Service Operations

This section describes service side service operations.


The following is the layout of a server side service operation

-   const [WS\_OPERATION\_CONTEXT](ws-operation-context.md)\* context: The operation [context](context.md).
-   Service Operations Parameters: Parameters pertaining to the service operation.
-   const [**WS\_ASYNC\_CONTEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_async_context)\* asyncContext: Async context for executing the service operations asynchronously.
-   [WS\_ERROR](ws-error.md)\* error: Rich error object.

``` syntax
HRESULT CALLBACK Add(const WS_OPERATION_CONTEXT* context, 
                     ULONG a, ULONG b, ULONG* result, 
                     const WS_ASYNC_CONTEXT* asyncContext, 
                     WS_ERROR* error)
{
    *result = a +b;
    return NOERROR;
}
```

## Fault And Error Handling

The server side should use faults to deliver error conditions to the client. It can do so by returning a failing HRESULT and embedding the fault in the error object.

If the fault is not set on the error object and a failure HRESULT is returned, the infrastructure will attempt deliver a fault back to client. The level of details disclosed to the client in such a case is controlled by [**WS\_SERVICE\_PROPERTY\_FAULT\_DISCLOSURE**](/windows/desktop/api/WebServices/ne-webservices-ws_service_property_id) service property on the [Service Host](service-host.md).

## Call Completion

A call on a synchronous server side service operation is said to be complete when either it has returned control back to the service host. For an asynchronous service operation a call is considered complete once the callback notification is issued by the service operation implementation.

## Call Lifetime

Special care should be taken when implementing a server side service operation about its lifetime. The lifetime of a call can greatly affect how long the service host takes to shutdown.

If a server side service operation is expected to block because of some IO bound operation, it is recommended that it registers a cancellation callback such that it is notified if when service host is being aborted, or when the underlying connection is closed by the client.

## Server side service operations and memory consideration

If a service operation needs to allocate memory for its outgoing parameters, it should use [WS\_HEAP](ws-heap.md) object available to it through the [WS\_OPERATION\_CONTEXT](ws-operation-context.md).

Example: Service Operation and WS\_HEAP

``` syntax
HRESULT CALLBACK ProcessOrder (const WS_OPERATION_CONTEXT* context, const ULONG orderNumber, OrderReceipt** orderReceipt, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    WS_HEAP* heap;
    HRESULT hr = WsGetOperationContextProperty (context, WS_OPERATION_CONTEXT_PROPERTY_HEAP, &heap, sizeof(heap), NULL, error);
    if (FAILED(hr))
        return hr;
    hr = WsAlloc(heap, sizeof (OrderReceipt), orderReceipt, error);
    if (FAILED(hr))
        return hr;
    hr = FillInReceipt(*orderReceipt);
    if (FAILED(hr))
        return hr;
    return NOERROR;
} 
```

## Return Values

-   WS\_S\_ASYNC: Call will be completed async.
-   WS\_S\_END: Call completed successfully, the server is not expecting any [WS\_MESSAGE](ws-message.md) from the client beyond this call. If another WS\_MESSAGE comes in then the server should abort the channel.
-   NOERROR/All other success HRESULTS: Call completed successfully. Note that it is recommended that the application should not return HRESULT other then NOERROR for successful completion of service operation.
-   Everything with a failure HRESULT: A fault is send back to the client if one is available in WS\_ERROR. Otherwise a generic fault is send back to the client. See fault discussion above.

See, [Call cancellation](call-cancellation.md).

 

 




