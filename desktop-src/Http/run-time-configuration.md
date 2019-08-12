---
title: Run-Time Configuration
description: The HTTP API enables applications to perform dynamic configuration at run time.
ms.assetid: 5118b48b-b44c-4cf5-9754-ce23c5a0b87e
ms.topic: article
ms.date: 05/31/2018
---

# Run-Time Configuration

The HTTP API enables applications to perform dynamic configuration at run time. Run-time configuration is not persistent, requires only low-level privileges, and affects only your application. Run-time configuration can include any of the following activities:

-   Initializing the HTTP service and creating a server session. An application initializes the HTTP service by calling the [**HttpInitialize**](/windows/desktop/api/Http/nf-http-httpinitialize) function. The server must be initialized before any other server functions can be called. The application then creates a server session by calling the [**HttpCreateServerSession**](/windows/desktop/api/Http/nf-http-httpcreateserversession) function. The server session is a container for properties that apply across all URL groups belonging to that server session. Typically each allication has only one server session. For information on setting server session properties and on their scope, see [**HttpSetServerSessionProperty**](/windows/desktop/api/Http/nf-http-httpsetserversessionproperty).
-   Registering for URLs. After the server session is created, an application can register for URLs by creating one or more URL groups. A URL group is a group of URLs to which the same properties will be applied. An application creates a URL group by calling the [**HttpCreateUrlGroup**](/windows/desktop/api/Http/nf-http-httpcreateurlgroup) function and then adds the desired URLs by calling the [**HttpAddUrlToUrlGroup**](/windows/desktop/api/Http/nf-http-httpaddurltourlgroup) function. After an application has registered for URLs by creating a URL group and has associated the URL group with a request queue (see [Creating and Binding to a Request Queue](creating-and-binding-to-a-request-queue.md)), all requests coming from these URLs are routed to the request queue associated with that application. For more information on settting URL group properties, see [**HttpSetUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpseturlgroupproperty)
-   Enabling features by setting HTTP server properties, such as [authentication](authentication-in-http-version-2-0.md), [logging](server-side-logging-in-http-version-2-0.md), QOS settings, timeouts, enabled state, and binding information. For information on setting properties, see [**HTTP\_SERVER\_PROPERTY**](/windows/desktop/api/Http/ne-http-http_server_property).

 

 




