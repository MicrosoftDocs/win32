---
Description: DBCONTENTSCOPE
ms.assetid: 22621088-3361-4128-810e-e6c4cefbbd81
title: DBCONTENTSCOPE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DBCONTENTSCOPE

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBCONTENTSCOPE** structure is used to pass a scope argument in a command tree.

``` syntax
typedef struct tagDBCONTENTSCOPE {
  DWORD      dwFlags;           // flags from <xref rid="indexsrv.dbprop_ci_scope_flags">DBPROP_CI_SCOPE_FLAGS</xref>
  LPOLESTR * rgpwszTagName;     // reserved for future use.
  LPOLESTR   pwszElementValue;  // <xref rid="indexsrv.dbprop_ci_include_scopes">DBPROP_CI_INCLUDE_SCOPES</xref> property for the path
} DBCONTENTSCOPE;
```

 

 



