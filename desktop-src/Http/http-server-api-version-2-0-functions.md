---
title: HTTP Server API version 2.0 functions
description: The HTTP Server API version 2.0 provides the following functions.
ms.assetid: 12daffca-b403-4f06-8037-206f90e33252
keywords:
- HTTP Server API version 2.0 functions
- Functions HTTP, HTTP Server API version 2.0
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Server API version 2.0 functions

The HTTP Server API version 2.0 provides the following functions.

| Function | Description |
|-|-|
| [**HttpDelegateRequestEx**](/windows/win32/api/http/nf-http-httpdelegaterequestex) | Delegates a request from the source request queue to the target request queue. |
| [**HttpFindUrlGroupId**](/windows/win32/api/http/nf-http-httpfindurlgroupid) | Retrieves a URL group ID for a URL and a request queue. |
| [**HttpIsFeatureSupported**](/windows/win32/api/http/nf-http-httpisfeaturesupported) | Checks whether a particular feature is supported. |

## Server session

| Function | Description |
|-|-|
| [**HttpCloseServerSession**](/windows/desktop/api/Http/nf-http-httpcloseserversession) | |
| [**HttpCreateServerSession**](/windows/desktop/api/Http/nf-http-httpcreateserversession) | |
| [**HttpQueryServerSessionProperty**](/windows/desktop/api/Http/nf-http-httpqueryserversessionproperty) | |
| [**HttpSetServerSessionProperty**](/windows/desktop/api/Http/nf-http-httpsetserversessionproperty) | |

## URL Groups

| Function | Description |
|-|-|
| [**HttpAddUrlToUrlGroup**](/windows/desktop/api/Http/nf-http-httpaddurltourlgroup) | |
| [**HttpCreateUrlGroup**](/windows/desktop/api/Http/nf-http-httpcreateurlgroup) | |
| [**HttpCloseUrlGroup**](/windows/desktop/api/Http/nf-http-httpcloseurlgroup) | |
| [**HttpQueryUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpqueryurlgroupproperty) | |
| [**HttpRemoveUrlFromUrlGroup**](/windows/desktop/api/Http/nf-http-httpremoveurlfromurlgroup) | |
| [**HttpSetUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpseturlgroupproperty) | |

## Request Queue

| Function | Description |
|-|-|
| [**HttpCloseRequestQueue**](/windows/desktop/api/Http/nf-http-httpcloserequestqueue) | |
| [**HttpCreateRequestQueue**](/windows/desktop/api/Http/nf-http-httpcreaterequestqueue) | |
| [**HttpQueryRequestQueueProperty**](/windows/desktop/api/Http/nf-http-httpqueryrequestqueueproperty) | |
| [**HttpSetRequestQueueProperty**](/windows/desktop/api/Http/nf-http-httpsetrequestqueueproperty) | |
| [**HttpShutdownRequestQueue**](/windows/desktop/api/Http/nf-http-httpshutdownrequestqueue) | |
| [**HttpWaitForDemandStart**](/windows/desktop/api/Http/nf-http-httpwaitfordemandstart) | |

## Related topics

[HTTP Server API version 2.0 structures](http-server-api-version-2-0-structures.md)
