---
title: Configuring the URL Group
description: Configuring the URL Group
ms.assetid: be222076-51ff-4907-924f-cc7b0d4fe767
ms.topic: article
ms.date: 05/31/2018
---

# Configuring the URL Group

The URL group ID is created with the [**HttpCreateUrlGroup**](/windows/desktop/api/Http/nf-http-httpcreateurlgroup) function and used in the call to [**HttpSetUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpseturlgroupproperty). The *pPropertyInformation* parameter points to the configuration structure for the property type that is set. The **PropertyInformationLength** parameter specifies the size, in bytes, of the configuration structure. For example, when setting the **HttpServerTimeoutsProperty** the *pPropertyInformation* parameter must point to a buffer that cannot be smaller than the [**HTTP\_TIMEOUT\_LIMIT\_INFO**](/windows/desktop/api/Http/ns-http-http_timeout_limit_info) structure. The URL group configurations are queried by calling [**HttpQueryUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpqueryurlgroupproperty).

After the URL Group is created, URLs are added to the group with [**HttpAddUrlToUrlGroup**](/windows/desktop/api/Http/nf-http-httpaddurltourlgroup). The URL group must be associated with a version 2.0 request queue to receive requests. To associate the URL group with a request queue, the application calls [**HttpSetUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpseturlgroupproperty) and specifies **HttpServerBindingProperty** in the *Property* parameter. If this property is not set, matching requests for the URL group are not delivered to a request queue and the HTTP Server API generates a 503 response. The application can only add URLs that have been previously reserved with the service to a URL group when running with low privilege. For more information, see the [Namespace Reservations, Registrations, and Routing](namespace-reservations-registrations-and-routing.md) topic.

 

 




