---
title: Configuring the Request Queue
description: Configuring the Request Queue
ms.assetid: 'ab03089c-2ef1-457d-a5f5-a4d400f3a7f1'
---

# Configuring the Request Queue

When the request queue is opened or created, the calling application receives a handle to it that can be used to send requests or configure the request queue. Calling [**HttpSetUrlGroupProperty**](httpseturlgroupproperty.md) with **HttpServerBindingProperty** and supplying the request queue handle in the [**HTTP\_BINDING\_INFO**](http-binding-info.md) structure, specified in the *pPropertyInformation* parameter, associates the URL group with the request queue. Request queue properties are set only by the application that creates the request queue. For example, to set the server queue length property, the creator application calls [**HttpSetRequestQueueProperty**](httpsetrequestqueueproperty.md) specifying **HttpServerQueueLengthProperty** in the *Property* parameter.

 

 




