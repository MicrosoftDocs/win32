---
title: Like Operator Constants
description: Like Operator Constants
ms.assetid: 9eb2cfcb-9ed8-4e5f-9a75-080f6f71a74b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Like Operator Constants

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The Like operator constants are a collection of globally unique identifiers (GUIDs) for the Like operator.

``` syntax
extern const OLEDBDECLSPEC GUID DBGUID_LIKE_SQL = \
    {0xc8b521f6,0x5cf3,0x11ce,
        {0xad,0xe5,0x00,0xaa,0x00,0x44,0x77,0x3d}};
extern const OLEDBDECLSPEC GUID DBGUID_LIKE_DOS = \
    {0xc8b521f7,0x5cf3,0x11ce,
        {0xad,0xe5,0x00,0xaa,0x00,0x44,0x77,0x3d}};
extern const OLEDBDECLSPEC GUID DBGUID_LIKE_OFS = \
    {0xc8b521f8,0x5cf3,0x11ce,
        {0xad,0xe5,0x00,0xaa,0x00,0x44,0x77,0x3d}};
extern const OLEDBDECLSPEC GUID DBGUID_LIKE_MAPI = \
    {0xc8b521f9,0x5cf3,0x11ce,
        {0xad,0xe5,0x00,0xaa,0x00,0x44,0x77,0x3d}};
```

### Remarks

The OLE DB Provider for Indexing Service uses only the DBGUID\_LIKE\_OFS constant, which signifies an Indexing Service Like operator.

 

 




