---
title: Call cancellation
description: Call cancellation notification cancels the operation of server side service operations and service-model callbacks.
ms.assetid: dc371921-869f-4775-98d3-80a1006358ba
keywords:
- Call cancellation Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Call cancellation

Call cancellation notification cancels the operation of [server side service operations](server-side-service-operations.md) and service-model callbacks. Such cancellation can be for one of two reasons:

-   The service host has stopped operations because of a call to the [**WsAbortServiceHost**](/windows/desktop/api/WebServices/nf-webservices-wsabortservicehost) function.
-   The underlying channel has raised a fault.


To receive a cancellation notification, the service operation or service-model callback must register a [**WS\_OPERATION\_CANCEL\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_operation_cancel_callback) callback by calling the [**WsRegisterOperationForCancel**](/windows/desktop/api/WebServices/nf-webservices-wsregisteroperationforcancel) function.

Optionally, as part of the registering for cancellation notification, the service operation or service-model callback can also register application-specific state data and the [**WS\_OPERATION\_FREE\_STATE\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_operation_free_state_callback) callback.

The state data is made available to the [**WS\_OPERATION\_CANCEL\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_operation_cancel_callback) callback. On call completion, the [**WS\_OPERATION\_FREE\_STATE\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_operation_free_state_callback) callback is called to give the application an opportunity to free the state data.

For a code example, see [BlockingServiceExample](blockingserviceexample.md).

The cancellation callback is called only once for the lifetime of the [server side service operations](server-side-service-operations.md) or callback function.

Call cancellation is available in for all service host callbacks that take [WS\_OPERATION\_CONTEXT](ws-operation-context.md) as a parameter.

The following API elements relate to call cancellation.

| Callback                                                                         | Description                                                                                                                                |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_OPERATION\_CANCEL\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_operation_cancel_callback)          | Invoked by service model to notify a cancellation of an asynchronous service operation as a result of an aborted shutdown of service host. |
| [**WS\_OPERATION\_FREE\_STATE\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_operation_free_state_callback) | Invoked by service model to allow an application to clean up state data that was registered with the cancellation callback.                |



 



| Function                                                             | Description                                                                                       |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**WsRegisterOperationForCancel**](/windows/desktop/api/WebServices/nf-webservices-wsregisteroperationforcancel) | Allows a service operation or service-model callback to register for a cancellation notification. |



 

 

 




