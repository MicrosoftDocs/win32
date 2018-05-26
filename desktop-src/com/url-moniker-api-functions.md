---
title: URL Moniker Functions
description: URL Moniker Functions
ms.assetid: 773743d3-9434-4ec9-b85c-9b971e37682f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# URL Moniker Functions

URL moniker functions insulate developers from the complexities of creating, managing, and using URL monikers. These functions are as follows:

-   [**CreateURLMoniker**](_inet_CreateURLMoniker_Function_cpp)
-   [**IsValidURL**](_inet_IsValidURL_Function_cpp)
-   [**RegisterMediaTypes**](_inet_RegisterMediaTypes_Function_cpp)
-   [**CreateFormatEnumerator**](/windows/win32/Urlmon/nf-urlmon-createformatenumerator?branch=master)
-   [**RegisterFormatEnumerator**](_inet_RegisterFormatEnumerator_Function_cpp)
-   [**RevokeFormatEnumerator**](_inet_RevokeFormatEnumerator_Function_cpp)
-   [**RegisterMediaTypeClass**](_inet_RegisterMediaTypeClass_Function_cpp)
-   [**FindMediaTypeClass**](_inet_FindMediaTypeClass_Function_cpp)
-   [**GetClassFileOrMime**](_inet_GetClassFileOrMime_Function_cpp)
-   [**UrlMkSetSessionOption**](_inet_UrlMkSetSessionOption_Function_cpp)

Your familiarity with these functions can be as follows:

-   Be familiar with [**CreateURLMoniker**](_inet_CreateURLMoniker_Function_cpp) and [**IsValidURL**](_inet_IsValidURL_Function_cpp) if you will be using URL monikers in stand-alone applications. If you are authoring an ActiveX control, you should use [**IBindHost::CreateMoniker**](_inet_IBindHost_CreateMoniker_Method) instead of **CreateURLMoniker**.
-   Be familiar with [**RegisterMediaTypes**](_inet_RegisterMediaTypes_Function_cpp), [**CreateFormatEnumerator**](/windows/win32/Urlmon/nf-urlmon-createformatenumerator?branch=master), [**RegisterFormatEnumerator**](_inet_RegisterFormatEnumerator_Function_cpp), and [**RevokeFormatEnumerator**](_inet_RevokeFormatEnumerator_Function_cpp) if you will be performing any MIME negotiation with URL monikers.
-   Be familiar with [**RegisterMediaTypeClass**](_inet_RegisterMediaTypeClass_Function_cpp), [**FindMediaTypeClass**](_inet_FindMediaTypeClass_Function_cpp), [**GetClassFileOrMime**](_inet_GetClassFileOrMime_Function_cpp), and [**UrlMkSetSessionOption**](_inet_UrlMkSetSessionOption_Function_cpp) only if you have significant experience both with URL monikers and with COM.

## Related topics

<dl> <dt>

[URL Monikers](url-monikers.md)
</dt> </dl>

 

 




