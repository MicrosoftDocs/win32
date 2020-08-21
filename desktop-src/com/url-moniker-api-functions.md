---
title: URL Moniker Functions
description: URL Moniker Functions
ms.assetid: 773743d3-9434-4ec9-b85c-9b971e37682f
ms.topic: article
ms.date: 05/31/2018
---

# URL Moniker Functions

URL moniker functions insulate developers from the complexities of creating, managing, and using URL monikers. These functions are as follows:

-   [**CreateURLMoniker**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775102(v=vs.85))
-   [**IsValidURL**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775112(v=vs.85))
-   [**RegisterMediaTypes**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775118(v=vs.85))
-   [**CreateFormatEnumerator**](/windows/desktop/api/Urlmon/nf-urlmon-createformatenumerator)
-   [**RegisterFormatEnumerator**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775116(v=vs.85))
-   [**RevokeFormatEnumerator**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775121(v=vs.85))
-   [**RegisterMediaTypeClass**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775117(v=vs.85))
-   [**FindMediaTypeClass**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775106(v=vs.85))
-   [**GetClassFileOrMime**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775108(v=vs.85))
-   [**UrlMkSetSessionOption**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775125(v=vs.85))

Your familiarity with these functions can be as follows:

-   Be familiar with [**CreateURLMoniker**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775102(v=vs.85)) and [**IsValidURL**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775112(v=vs.85)) if you will be using URL monikers in stand-alone applications. If you are authoring an ActiveX control, you should use [**IBindHost::CreateMoniker**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775075(v=vs.85)) instead of **CreateURLMoniker**.
-   Be familiar with [**RegisterMediaTypes**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775118(v=vs.85)), [**CreateFormatEnumerator**](/windows/desktop/api/Urlmon/nf-urlmon-createformatenumerator), [**RegisterFormatEnumerator**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775116(v=vs.85)), and [**RevokeFormatEnumerator**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775121(v=vs.85)) if you will be performing any MIME negotiation with URL monikers.
-   Be familiar with [**RegisterMediaTypeClass**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775117(v=vs.85)), [**FindMediaTypeClass**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775106(v=vs.85)), [**GetClassFileOrMime**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775108(v=vs.85)), and [**UrlMkSetSessionOption**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775125(v=vs.85)) only if you have significant experience both with URL monikers and with COM.

## Related topics

<dl> <dt>

[URL Monikers](url-monikers.md)
</dt> </dl>

 

 