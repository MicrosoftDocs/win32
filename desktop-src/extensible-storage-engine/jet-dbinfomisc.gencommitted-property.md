---
description: "Learn more about: JET_DBINFOMISC.genCommitted property"
title: JET_DBINFOMISC.genCommitted property 
TOCTitle: 'genCommitted property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.genCommitted
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.gencommitted(v=EXCHG.10)
ms:contentKeyID: 39513072
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.genCommitted
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.genCommitted
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_genCommitted
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_genCommitted
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.genCommitted property

Gets the maximum log generation committed to the database. Typically the current log generation.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property genCommitted As Integer
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As Integer

value = instance.genCommitted
```

``` csharp
public int genCommitted { get; internal set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[JET_DBINFOMISC class](./jet-dbinfomisc-class.md)

[JET_DBINFOMISC members](./jet-dbinfomisc-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
