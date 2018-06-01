---
Description: Locale
ms.assetid: a7bf3d15-4532-4719-b50d-a35ff10c3482
title: Locale
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Locale

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **Locale** entry specifies the LCID used for the language represented by the language subkey.

### Summary



|        |                                                                                           |
|--------|-------------------------------------------------------------------------------------------|
| Type:  | **REG\_DWORD**                                                                            |
| Range: | Any LCID made from a language identifier using the [**MAKELCID**](https://www.bing.com/search?q=**MAKELCID**) macro. |



 

### Remarks

The Indexing Service ISAPI implementation variable [CiLocale](https://www.bing.com/search?q=CiLocale) selects a language subkey to use with a specific query.

## Related topics

<dl> <dt>

[Language-Specific Registry Entries](language-specific-registry-entries.md)
</dt> <dt>

[MAKELCID](https://www.bing.com/search?q=MAKELCID)
</dt> </dl>

 

 



