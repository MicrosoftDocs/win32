---
title: Versioning (HTTP Server API)
description: The HTTP Server version 2.0 API applies object-scoped versioning to determine the version of the API.
ms.assetid: 2c2d7501-85e0-44ec-aa42-01372b29266e
keywords:
- Versioning in HTTP Server Version 2.0 API
- HTTP Server Version 2.0 API, versioning
ms.topic: article
ms.date: 05/31/2018
---

# Versioning (HTTP Server API)

The HTTP Server version 2.0 API makes obsolete the version 1.0 request queues and URL associations with the request queue. Object-scoped versioning allows applications to supply application-specific version information. An applications can automatically call the correct version of structures for the operating system on which it is running.

## Request Queues

Starting with HTTP Server version 2.0 API, request queues are created with [**HttpCreateRequestQueue**](/windows/desktop/api/Http/nf-http-httpcreaterequestqueue) making obsolete the version 1.0 [**HttpCreateHttpHandle**](/windows/desktop/api/Http/nf-http-httpcreatehttphandle) function. URL groups are introduced in version 2.0 with the [**HttpCreateUrlGroup**](/windows/desktop/api/Http/nf-http-httpcreateurlgroup) function. URLs are added to the group using [**HttpAddUrlToUrlGroup**](/windows/desktop/api/Http/nf-http-httpaddurltourlgroup) which makes obsolete the version 1.0 [**HttpAddUrl**](/windows/desktop/api/Http/nf-http-httpaddurl) function. Version 2.0 URL groups must not be used with version 1.0 request queues.

Starting with version 2.0, the following version 1.0 functions are obsolete and cannot be used with version 2.0 request queues:

-   [**HttpCreateHttpHandle**](/windows/desktop/api/Http/nf-http-httpcreatehttphandle)
-   [**HttpAddUrl**](/windows/desktop/api/Http/nf-http-httpaddurl)
-   [**HttpRemoveUrl**](/windows/desktop/api/Http/nf-http-httpremoveurl)

For more information about configuring URL groups, see the [Configuring the URL Group](configuring-the-url-group.md) topic. For more information about version 2.0 request queues, see the [Named Request Queue](named-request-queue.md) topic.

## Object-Scoped Versioning

In version 1.0, the application supplies the HTTP Server API version in the call to [**HttpInitialize**](/windows/desktop/api/Http/nf-http-httpinitialize). The version information is accepted only from the first application that called **HttpInitialize** and is applied to all the HTTP Server API applications in the same process. Starting with the version 2.0 API, the global version information supplied in the call to **HttpInitialize** is not used. For version 2.0 applications, the HTTP Server API version is passed in the Version parameter when the request queue or server session is created by [**HttpCreateRequestQueue**](/windows/desktop/api/Http/nf-http-httpcreaterequestqueue) or [**HttpCreateServerSession**](/windows/desktop/api/Http/nf-http-httpcreateserversession). When the request queue is created with the version 1.0 [**HttpCreateHttpHandle**](/windows/desktop/api/Http/nf-http-httpcreatehttphandle), it is automatically marked as version 1.0. Both version 1.0 and version 2.0 applications can run in the same process.

The [**HTTP\_REQUEST**](/previous-versions/windows/desktop/legacy/aa364545(v=vs.85)) and [**HTTP\_RESPONSE**](http-response.md) structures are updated to include authentication information in the HTTP Server version 2.0 API. [**HTTP\_REQUEST\_V1**](/windows/desktop/api/Http/ns-http-http_request_v1) and [**HTTP\_REQUEST\_V2**](/windows/desktop/api/Http/ns-http-http_request_v2) are specific to the version of the API used by the application. However, applications should not use these structures directly in their code; instead they should use **HTTP\_REQUEST** to get the correct version based on the version of the request queue on which the request was received. Also, be aware that size of the **HTTP\_REQUEST** structure is based on the version of the operating system under which the code is compiled.

 

 
