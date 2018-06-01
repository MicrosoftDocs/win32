---
title: DBPROP\_USEEXTENDEDDBTYPES
description: DBPROP\_USEEXTENDEDDBTYPES
ms.assetid: 8c62a64d-5cb1-4c96-a727-b72e270b17d4
keywords:
- DBPROP_USEEXTENDEDDBTYPES
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBPROP\_USEEXTENDEDDBTYPES

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The DBPROP\_USEEXTENDEDDBTYPES property controls the data type of columns bound by OLE DB accessors.

### Summary



|                  |                            |
|------------------|----------------------------|
| **Property Set** | DBPROPSET\_QUERYEXT        |
| **Property ID**  | DBPROP\_USEEXTENDEDDBTYPES |
| **Value Type**   | DBTYPE\_BOOL               |
| **Default**      | VARIANT\_FALSE             |



 

### Remarks

If the value is VARIANT\_TRUE, accessor column bindings can be based on [**PROPVARIANT**](https://www.bing.com/search?q=**PROPVARIANT**) structures. By default, only OLE Automation **VARIANT** structures and any directory binding are allowed for accessor column bindings.

Many frequently used properties are stored using types that are not OLE Automation **VARIANT** structures. This causes considerable overhead in the OLE DB accessor used to retrieve the data, since the data must be coerced into a different type.

Clients that can make use of [**PROPVARIANT**](https://www.bing.com/search?q=**PROPVARIANT**) structures should set DBPROP\_USEEXTENDEDDBTYPES to VARIANT\_TRUE and use OLE DB accessors with bindings that use **PROPVARIANT** types.

 

 




