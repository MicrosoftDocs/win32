---
title: Creating and Binding to a Request Queue
description: A request queue is a service queue that holds pending requests for a specific application.
ms.assetid: 93f8b230-af0a-4582-b35b-d65f6841e525
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Binding to a Request Queue

A request queue is a service queue that holds pending requests for a specific application. An application creates the request queue independently of the URL group or server session by calling the [**HttpCreateRequestQueue**](/windows/desktop/api/Http/nf-http-httpcreaterequestqueue) function, and sets the request queue properties by calling the [**HttpSetRequestQueueProperty**](/windows/desktop/api/Http/nf-http-httpsetrequestqueueproperty) function. These properties are the verbosity of 503 responses, the maximum length of the queue, and the activity state.

To cause requests to be routed to its request queue, the application binds the URL group it created as part of [run-time configuration](run-time-configuration.md) to the queue by calling [**HttpSetUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpseturlgroupproperty) with **HttpServerBindingProperty** specified in the *Property* parameter. Incoming requests from the URLs in the group are then routed to the specified request queue.

 

 




