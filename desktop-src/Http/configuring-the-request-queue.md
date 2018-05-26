---
title: Configuring the Request Queue
description: Configuring the Request Queue
ms.assetid: ab03089c-2ef1-457d-a5f5-a4d400f3a7f1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Configuring the Request Queue

When the request queue is opened or created, the calling application receives a handle to it that can be used to send requests or configure the request queue. Calling [**HttpSetUrlGroupProperty**](/windows/win32/Http/nf-http-httpseturlgroupproperty?branch=master) with **HttpServerBindingProperty** and supplying the request queue handle in the [**HTTP\_BINDING\_INFO**](/windows/win32/Http/ns-http-_http_binding_info?branch=master) structure, specified in the *pPropertyInformation* parameter, associates the URL group with the request queue. Request queue properties are set only by the application that creates the request queue. For example, to set the server queue length property, the creator application calls [**HttpSetRequestQueueProperty**](/windows/win32/Http/nf-http-httpsetrequestqueueproperty?branch=master) specifying **HttpServerQueueLengthProperty** in the *Property* parameter.

 

 




