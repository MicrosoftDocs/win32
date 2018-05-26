---
title: DBID
description: DBID
ms.assetid: 076f4603-8621-4c32-b4d7-cf8507d240a8
keywords:
- DBID
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBID

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBID** structure encapsulates various ways of identifying a database object. It is used by nodes that must represent a column name, such as column\_name, index\_name, table\_name, schema\_name, catalog\_name, and so forth. (For more information on these nodes, see [Catalog of DML Nodes](catalog-of-dml-nodes.md).) This structure is also used to define bindings.

``` syntax
typedef struct tagDBID {
  union {
    GUID   guid;
    GUID * pguid;
  } uGuid;
  DBKIND eKind;
  union {
    LPWSTR pwszName;
    ULONG  ulPropid;
  } uName;
} DBID;
```

### Remarks

The **DBID** structure identifies the requested columns for a query. Each unique column is represented by a unique combination of GUID and number or GUID and name.

 

 




