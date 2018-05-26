---
title: Data Source Object Constant
description: Data Source Object Constant
ms.assetid: 5464a358-d422-41dc-adf2-e2c5267c72cd
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Data Source Object Constant

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The CLSID\_INDEX\_SERVER\_DSO constant is the Indexing Service data source object (DSO) class ID (CLSID) used to create an Indexing Service DSO with the [**CoCreateInstance**](_com_cocreateinstance) function.

``` syntax
#define CLSID_INDEX_SERVER_DSO \
    { 0xF9AE8980, 0x7E52, 0x11d0, \
      { 0x89, 0x64, 0x00, 0xC0, 0x4F, 0xD6, 0x11, 0xD7 } }
```

### Remarks

For an example of using the DSO CLSID, see [Accessing OLE DB with the OLE DB Provider for Indexing Service](accessing-ole-db-with-the-ole-db-provider-for-indexing-service.md).

 

 




