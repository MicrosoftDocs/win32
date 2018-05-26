---
title: Using Visual J++ with Indexing Service APIs
description: Using Visual J++ with Indexing Service APIs
ms.assetid: a3060a49-5442-40e2-a1b1-992334838f92
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Visual J++ with Indexing Service APIs

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

To use the [ActiveX Data Objects (ADO) API](programming-apis.md#-idxs-activex-data-objects-api) with Visual J++, you need to import the appropriate Windows Foundation Classes (WFC) for Java packages. The WFC packages provide the following.

-   Base classes that encapsulate Windows application operations
-   Base classes for the core component model.
-   ADO Java classes that enable data access and data binding.
-   Core Windows native API support classes in WFC.

To import these packages, you include the following statements in your application.


```Java
import com.ms.wfc.*;
import com.ms.wfc.core.*;
import com.ms.wfc.data.*;
import com.ms.com.*;
```



To use the ADO API, you must specify "provider=MSIDXS" when creating an ADO [Recordset](mdidxrecordsetjavasyntax) object.

 

 




