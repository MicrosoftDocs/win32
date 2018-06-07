---
title: Versioning
description: The HTTP Server version 2.0 API applies object-scoped versioning to determine the version of the API.
ms.assetid: 2c2d7501-85e0-44ec-aa42-01372b29266e
keywords:
- Versioning in HTTP Server Version 2.0 API
- HTTP Server Version 2.0 API, versioning
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Versioning

The HTTP Server version 2.0 API makes obsolete the version 1.0 request queues and URL associations with the request queue. Object-scoped versioning allows applications to supply application-specific version information. An applications can automatically call the correct version of structures for the operating system on which it is running.

## Request Queues

Starting with HTTP Server version 2.0 API, request queues are created with [**HttpCreateRequestQueue**](httpcreaterequestqueue.md) making obsolete the version 1.0 [**HttpCreateHttpHandle**](httpcreatehttphandle.md) function. URL groups are introduced in version 2.0 with the [**HttpCreateUrlGroup**](httpcreateurlgroup.md) function. URLs are added to the group using [**HttpAddUrlToUrlGroup**](httpaddurltourlgroup.md) which makes obsolete the version 1.0 [**HttpAddUrl**](httpaddurl.md) function. Version 2.0 URL groups must not be used with version 1.0 request queues.

Starting with version 2.0, the following version 1.0 functions are obsolete and cannot be used with version 2.0 request queues:

-   [**HttpCreateHttpHandle**](httpcreatehttphandle.md)
-   [**HttpAddUrl**](httpaddurl.md)
-   [**HttpRemoveUrl**](httpremoveurl.md)

For more information about configuring URL groups, see the [Configuring the URL Group](configuring-the-url-group.md) topic. For more information about version 2.0 request queues, see the [Named Request Queue](named-request-queue.md) topic.

## Object-Scoped Versioning

In version 1.0, the application supplies the HTTP Server API version in the call to [**HttpInitialize**](httpinitialize.md). The version information is accepted only from the first application that called **HttpInitialize** and is applied to all the HTTP Server API applications in the same process. Starting with the version 2.0 API, the global version information supplied in the call to **HttpInitialize** is not used. For version 2.0 applications, the HTTP Server API version is passed in the Version parameter when the request queue or server session is created by [**HttpCreateRequestQueue**](httpcreaterequestqueue.md) or [**HttpCreateServerSession**](httpcreateserversession.md). When the request queue is created with the version 1.0 [**HttpCreateHttpHandle**](httpcreatehttphandle.md), it is automatically marked as version 1.0. Both version 1.0 and version 2.0 applications can run in the same process.

The [**HTTP\_REQUEST**](http-request.md) and [**HTTP\_RESPONSE**](http-response.md) structures are updated to include authentication information in the HTTP Server version 2.0 API. [**HTTP\_REQUEST\_V1**](http-request-v1.md) and [**HTTP\_REQUEST\_V2**](http-request-v2.md) are specific to the version of the API used by the application. However, applications should not use these structures directly in their code; instead they should use **HTTP\_REQUEST** to get the correct version based on the version of the request queue on which the request was received. Also, be aware that size of the **HTTP\_REQUEST** structure is based on the version of the operating system under which the code is compiled.

 

 




