---
title: Configuring the URL Group
description: .
ms.assetid: be222076-51ff-4907-924f-cc7b0d4fe767
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Configuring the URL Group

The URL group ID is created with the [**HttpCreateUrlGroup**](/windows/win32/Http/nf-http-httpcreateurlgroup?branch=master) function and used in the call to [**HttpSetUrlGroupProperty**](/windows/win32/Http/nf-http-httpseturlgroupproperty?branch=master). The *pPropertyInformation* parameter points to the configuration structure for the property type that is set. The **PropertyInformationLength** parameter specifies the size, in bytes, of the configuration structure. For example, when setting the **HttpServerTimeoutsProperty** the *pPropertyInformation* parameter must point to a buffer that cannot be smaller than the [**HTTP\_TIMEOUT\_LIMIT\_INFO**](/windows/win32/Http/ns-http-_http_timeout_limit_info?branch=master) structure. The URL group configurations are queried by calling [**HttpQueryUrlGroupProperty**](/windows/win32/Http/nf-http-httpqueryurlgroupproperty?branch=master).

After the URL Group is created, URLs are added to the group with [**HttpAddUrlToUrlGroup**](/windows/win32/Http/nf-http-httpaddurltourlgroup?branch=master). The URL group must be associated with a version 2.0 request queue to receive requests. To associate the URL group with a request queue, the application calls [**HttpSetUrlGroupProperty**](/windows/win32/Http/nf-http-httpseturlgroupproperty?branch=master) and specifies **HttpServerBindingProperty** in the *Property* parameter. If this property is not set, matching requests for the URL group are not delivered to a request queue and the HTTP Server API generates a 503 response. The application can only add URLs that have been previously reserved with the service to a URL group when running with low privilege. For more information, see the [Namespace Reservations, Registrations, and Routing](namespace-reservations-registrations-and-routing.md) topic.

 

 




