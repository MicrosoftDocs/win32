---
title: Extended Query Properties
description: Extended Query Properties
ms.assetid: '2606f410-dac0-49d8-b09d-3e3120aa8b1a'
---

# Extended Query Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following table includes dynamic properties for use with extended queries using the ADO **Recordset** object.



| Property                                                                | Data Type    | Property Group      | Read/Write | Description                                                                                          |
|-------------------------------------------------------------------------|--------------|---------------------|------------|------------------------------------------------------------------------------------------------------|
| Always use content index (DBPROP\_USECONTENTINDEX)                      | DBTYPE\_BOOL | DBPROPFLAGS\_ROWSET | RW         | Default is FALSE. When set to TRUE, indicates that the search will always use Content Index.         |
| Defer scope and security testing (DBPROP\_DEFERNONINDEXEDTRIMMING)      | DBTYPE\_BOOL | DBPROPFLAGS\_ROWSET | RW         | Default is FALSE. When set to TRUE, indicates that the search will defer scope and security testing. |
| Return **PROPVARIANT**s in variant binding (DBPROP\_USEEXTENDEDDBTYPES) | DBTYPE\_BOOL | DBPROPFLAGS\_ROWSET | RW         | Default is FALSE. When set to TRUE, returns **PROPVARIANT** structures in variant binding.           |



 

 

 




