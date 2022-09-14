---
description: "Learn more about: JET_DBINFOMISC.cbPageSize property"
title: JET_DBINFOMISC.cbPageSize property 
TOCTitle: 'cbPageSize property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.cbPageSize
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.cbpagesize(v=EXCHG.10)
ms:contentKeyID: 39512879
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.cbPageSize
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_cbPageSize
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_cbPageSize
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.cbPageSize
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.cbPageSize property

Gets the database page size. A value of 0 means 4Kb pages.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cbPageSize As Integer
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As Integer

value = instance.cbPageSize
```

``` csharp
public int cbPageSize { get; internal set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[JET_DBINFOMISC class](./jet-dbinfomisc-class.md)

[JET_DBINFOMISC members](./jet-dbinfomisc-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
