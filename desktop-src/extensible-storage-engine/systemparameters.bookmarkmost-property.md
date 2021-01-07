---
description: "Learn more about: SystemParameters.BookmarkMost property"
title: SystemParameters.BookmarkMost property 
TOCTitle: 'BookmarkMost property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.SystemParameters.BookmarkMost
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.systemparameters.bookmarkmost(v=EXCHG.10)
ms:contentKeyID: 55104112
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.SystemParameters.BookmarkMost
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SystemParameters.BookmarkMost
- Microsoft.Isam.Esent.Interop.SystemParameters.get_BookmarkMost
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SystemParameters.BookmarkMost property

Gets the maximum size of a bookmark. [JetGetBookmark(JET_SESID, JET_TABLEID, \[\], Int32, Int32)](./api.jetgetbookmark-method.md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared ReadOnly Property BookmarkMost As Integer
    Get
'Usage
Dim value As Integer

value = SystemParameters.BookmarkMost
```

``` csharp
public static int BookmarkMost { get; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[SystemParameters class](./systemparameters-class.md)

[SystemParameters members](./systemparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
