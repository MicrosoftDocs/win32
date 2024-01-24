---
title: Service Proxy and Sessions
description: The service proxy has special behaviors for session and non-session-based channel bindings.
ms.assetid: 6dc9de95-b97c-4acc-9d45-d5e6ebb6bd77
keywords:
- Service Proxy and Sessions Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Service Proxy and Sessions

The [service proxy](service-proxy.md) has special behaviors for session and non-session-based channel bindings. The service proxy provides session based semantics if the underlying channel binding is session based. In this case a single channel is used to service calls. However, if the channel binding is not session based, the service proxy creates a separate channel for each call. Note, though, that non-session-based channels are pooled and maybe reused. In reusing a channel, the service proxy keeps the channel open if the underlying channel has not faulted or the call on a channel has resulted in the service proxy's faulting the channel. Note that. except in the event of a fault, once a channel is opened it is kept open as long as the service proxy is open and is closed only when the service proxy is closed.


If the channel binding is session based and if the underlying channel faults, the service proxy state machine will transition into the [**WS\_SERVICE\_PROXY\_STATE\_FAULTED**](/windows/desktop/api/WebServices/ne-webservices-ws_service_proxy_state) state. In the case of non-session based channel binding, a fault in the underlying channel does not cause the proxy to transition into **WS\_SERVICE\_PROXY\_STATE\_FAULTED** state.

For more information on the service proxy and its relation to state, see the [Service Proxy](service-proxy.md) topic. For examples of different channel bindings see the following examples:

-   non-session channel binding, [HttpCalculatorClientExample](httpcalculatorclientexample.md)
-   session-based channel binding, [SessionfullCalculatorClientExample](sessionfullcalculatorclientexample.md)

 

 




