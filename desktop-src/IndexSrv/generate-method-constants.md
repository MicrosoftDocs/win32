---
Description: Generate Method Constants
ms.assetid: 4e71c840-885d-4274-8011-0a8efbb374b6
title: Generate Method Constants
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Generate Method Constants

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The generate method constants specify the method to use when generating alternate word forms in pattern matching queries.

``` syntax
#define GENERATE_METHOD_EXACT   ( 0 )  // The query string value must match exactly.
#define GENERATE_METHOD_PREFIX  ( 1 )  // The query string value is a prefix for strings in documents.
#define GENERATE_METHOD_INFLECT ( 2 )  // Generate multiple forms of the query string word to match documents.
```

### Remarks

The **dwGenerateMethod** member of the [**DBCONTENT**](dbcontent.md) structure uses these constants.

 

 



