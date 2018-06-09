---
title: URL Moniker Functions
description: URL Moniker Functions
ms.assetid: 773743d3-9434-4ec9-b85c-9b971e37682f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# URL Moniker Functions

URL moniker functions insulate developers from the complexities of creating, managing, and using URL monikers. These functions are as follows:

-   [**CreateURLMoniker**](https://www.bing.com/search?q=**CreateURLMoniker**)
-   [**IsValidURL**](https://www.bing.com/search?q=**IsValidURL**)
-   [**RegisterMediaTypes**](https://www.bing.com/search?q=**RegisterMediaTypes**)
-   [**CreateFormatEnumerator**](/windows/desktop/api/Urlmon/nf-urlmon-createformatenumerator)
-   [**RegisterFormatEnumerator**](https://www.bing.com/search?q=**RegisterFormatEnumerator**)
-   [**RevokeFormatEnumerator**](https://www.bing.com/search?q=**RevokeFormatEnumerator**)
-   [**RegisterMediaTypeClass**](https://www.bing.com/search?q=**RegisterMediaTypeClass**)
-   [**FindMediaTypeClass**](https://www.bing.com/search?q=**FindMediaTypeClass**)
-   [**GetClassFileOrMime**](https://www.bing.com/search?q=**GetClassFileOrMime**)
-   [**UrlMkSetSessionOption**](https://www.bing.com/search?q=**UrlMkSetSessionOption**)

Your familiarity with these functions can be as follows:

-   Be familiar with [**CreateURLMoniker**](https://www.bing.com/search?q=**CreateURLMoniker**) and [**IsValidURL**](https://www.bing.com/search?q=**IsValidURL**) if you will be using URL monikers in stand-alone applications. If you are authoring an ActiveX control, you should use [**IBindHost::CreateMoniker**](45e7247f-c611-4a6a-a630-3c20c3581a7d) instead of **CreateURLMoniker**.
-   Be familiar with [**RegisterMediaTypes**](https://www.bing.com/search?q=**RegisterMediaTypes**), [**CreateFormatEnumerator**](/windows/desktop/api/Urlmon/nf-urlmon-createformatenumerator), [**RegisterFormatEnumerator**](https://www.bing.com/search?q=**RegisterFormatEnumerator**), and [**RevokeFormatEnumerator**](https://www.bing.com/search?q=**RevokeFormatEnumerator**) if you will be performing any MIME negotiation with URL monikers.
-   Be familiar with [**RegisterMediaTypeClass**](https://www.bing.com/search?q=**RegisterMediaTypeClass**), [**FindMediaTypeClass**](https://www.bing.com/search?q=**FindMediaTypeClass**), [**GetClassFileOrMime**](https://www.bing.com/search?q=**GetClassFileOrMime**), and [**UrlMkSetSessionOption**](https://www.bing.com/search?q=**UrlMkSetSessionOption**) only if you have significant experience both with URL monikers and with COM.

## Related topics

<dl> <dt>

[URL Monikers](url-monikers.md)
</dt> </dl>

 

 




