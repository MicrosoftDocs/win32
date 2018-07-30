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

-   [**CreateURLMoniker**](https://msdn.microsoft.com/library/ms775102(v=VS.85).aspx)
-   [**IsValidURL**](https://msdn.microsoft.com/library/ms775112(v=VS.85).aspx)
-   [**RegisterMediaTypes**](https://msdn.microsoft.com/library/ms775118(v=VS.85).aspx)
-   [**CreateFormatEnumerator**](/windows/desktop/api/Urlmon/nf-urlmon-createformatenumerator)
-   [**RegisterFormatEnumerator**](https://msdn.microsoft.com/library/ms775116(v=VS.85).aspx)
-   [**RevokeFormatEnumerator**](https://msdn.microsoft.com/library/ms775121(v=VS.85).aspx)
-   [**RegisterMediaTypeClass**](https://msdn.microsoft.com/library/ms775117(v=VS.85).aspx)
-   [**FindMediaTypeClass**](https://msdn.microsoft.com/library/ms775106(v=VS.85).aspx)
-   [**GetClassFileOrMime**](https://msdn.microsoft.com/library/ms775108(v=VS.85).aspx)
-   [**UrlMkSetSessionOption**](https://msdn.microsoft.com/library/ms775125(v=VS.85).aspx)

Your familiarity with these functions can be as follows:

-   Be familiar with [**CreateURLMoniker**](https://msdn.microsoft.com/library/ms775102(v=VS.85).aspx) and [**IsValidURL**](https://msdn.microsoft.com/library/ms775112(v=VS.85).aspx) if you will be using URL monikers in stand-alone applications. If you are authoring an ActiveX control, you should use [**IBindHost::CreateMoniker**](https://msdn.microsoft.com/library/ms775075(v=VS.85).aspx) instead of **CreateURLMoniker**.
-   Be familiar with [**RegisterMediaTypes**](https://msdn.microsoft.com/library/ms775118(v=VS.85).aspx), [**CreateFormatEnumerator**](/windows/desktop/api/Urlmon/nf-urlmon-createformatenumerator), [**RegisterFormatEnumerator**](https://msdn.microsoft.com/library/ms775116(v=VS.85).aspx), and [**RevokeFormatEnumerator**](https://msdn.microsoft.com/library/ms775121(v=VS.85).aspx) if you will be performing any MIME negotiation with URL monikers.
-   Be familiar with [**RegisterMediaTypeClass**](https://msdn.microsoft.com/library/ms775117(v=VS.85).aspx), [**FindMediaTypeClass**](https://msdn.microsoft.com/library/ms775106(v=VS.85).aspx), [**GetClassFileOrMime**](https://msdn.microsoft.com/library/ms775108(v=VS.85).aspx), and [**UrlMkSetSessionOption**](https://msdn.microsoft.com/library/ms775125(v=VS.85).aspx) only if you have significant experience both with URL monikers and with COM.

## Related topics

<dl> <dt>

[URL Monikers](url-monikers.md)
</dt> </dl>

 

 




