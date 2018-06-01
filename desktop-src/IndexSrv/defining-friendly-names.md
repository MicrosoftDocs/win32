---
Description: Defining Friendly Names
ms.assetid: bf40a23f-1e47-4adf-a4b7-42aae71d39c2
title: Defining Friendly Names
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Defining Friendly Names

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The friendly names of known properties listed in the property names for a Web catalog are always available, even if they are not explicitly defined in the names section. See [List of Property Names for a Web Catalog](list-of-property-names-for-a-web-catalog.md). For example, a friendly name such as MetaDescription for the HTML meta property can be defined as

``` syntax
MetaDescription(DBTYPE_WSTR|DBTYPE_BYREF) = D1B5D3F0-C0B3-11CF-9A92-00A0C908DBF1 description
```

 

 



