---
Description: QUERY\_STRING Variables
ms.assetid: 4af717b0-56dd-4467-a142-b9a1259f0d01
title: QUERY\_STRING Variables
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# QUERY\_STRING Variables

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following table defines the conventional URL tags in the QUERY\_STRING variable used by the [**SetQueryFromURL**](iixssoquery-setqueryfromurl.md) and [**QueryToURL**](iixssoquery-querytourl.md) methods defined on the IXSSO Query object.



| Tag    | Description                                                                                   |
|--------|-----------------------------------------------------------------------------------------------|
| **ae** | Used by the **AllowEnumeration** property. If set to a nonzero digit, enumeration is allowed. |
| **ct** | Used by the **Catalog** property.                                                             |
| **di** | Used by the **Dialect** property.                                                             |
| **gd** | GroupBy descending. Used by the **GroupBy** property.                                         |
| **gr** | Used by the **GroupBy** property.                                                             |
| **mh** | Used by the **MaxRecords** property.                                                          |
| **qu** | Full text of query. Used by the **Query** property.                                           |
| **so** | Used by the **SortBy** property.                                                              |
| **sd** | Sort descending. Used by the **SortBy** property.                                             |



 

 

 



