---
title: Demand Start on Version 2.0 Request Queues
description: Demand Start on Version 2.0 Request Queues
ms.assetid: 84a744b7-1b0e-4fa7-8015-4840251aa856
ms.topic: article
ms.date: 05/31/2018
---

# Demand Start on Version 2.0 Request Queues

The demand start feature of the HTTP Server version 2.0 API request queues allows controller application to delay worker process instantiation until the first request arrives on the request queue. Thus, the applications can avoid consuming resources until they are required. For more information about the controller application, see the [Named Request Queue](named-request-queue.md) topic.

## Asynchronous Demand Start

The controller application calls [**HttpWaitForDemandStart**](/windows/desktop/api/Http/nf-http-httpwaitfordemandstart) with the handle to the request queue to initiate a demand start notification. For asynchronous completion, the application supplies the overlapped structure in the *pOverlapped* parameter. When **HttpWaitForDemandStart** is called asynchronously, the controller application is notified when the first request arrives on the request queue. After the demand start notification completes, the controller application can register for another demand start notification on the request queue.

The HTTP Server API does not allow more than one simultaneous demand start notification for a request queue. However, when the outstanding demand start notification completes, the application calls [**HttpWaitForDemandStart**](/windows/desktop/api/Http/nf-http-httpwaitfordemandstart) again to start multiple worker processes on the request queue. HTTP does not enforce limitations on the number of demand start notifications or the number of worker processes operating on the request queue. The controller applications can, however, enforce the number of worker processes allowed on a request queue.

The HTTP Server API supports canceling asynchronous [**HttpWaitForDemandStart**](/windows/desktop/api/Http/nf-http-httpwaitfordemandstart) calls. Applications can use [**CancelIoEx**](/windows/desktop/FileIO/cancelioex-func) with the overlapped structure supplied in *pOverlapped*, to cancel an outstanding **HttpWaitForDemandStart** call.

## Synchronous Demand Start

Synchronous demand start is not recommended because the application blocks until a request arrives on the request queue.

 

 
