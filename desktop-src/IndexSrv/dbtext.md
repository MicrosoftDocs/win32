---
title: DBTEXT
description: DBTEXT
ms.assetid: 24a96f9c-68a0-4e98-b2a4-3be12c56d069
keywords:
- DBTEXT
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBTEXT

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBTEXT** structure is used by the DBOP\_text\_command node. It stores the dialect to use to interpret the string stored in the **pwszText** member. The error locator is filled in by the provider, that is, the first offending token is indicated as the index into the text array, together with its length.

``` syntax
typedef struct tagDBTEXT {
  LPWSTR pwszText;
  ULONG  ulErrorLocator;  // set by validation routines
  ULONG  ulTokenLength;   // length of offending token
  GUID   guidDialect;     // GUID of the language and dialect
} DBTEXT;
```

### Remarks

For additional information about the *guidDialect* parameter, see the description of DBOP\_text\_command in [Special Operators](special-operators.md).

 

 




