---
description: "Learn more about: JET_INDEXRANGE.tableid property"
title: JET_INDEXRANGE.tableid property 
TOCTitle: 'tableid property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INDEXRANGE.tableid
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_indexrange.tableid(v=EXCHG.10)
ms:contentKeyID: 55103657
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INDEXRANGE.tableid
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXRANGE.tableid
- Microsoft.Isam.Esent.Interop.JET_INDEXRANGE.set_tableid
- Microsoft.Isam.Esent.Interop.JET_INDEXRANGE.get_tableid
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXRANGE.tableid property

Gets or sets the cursor containing the index range. The cursor should have an index range set with JetSetIndexRange.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property tableid As JET_TABLEID
    Get
    Set
'Usage
Dim instance As JET_INDEXRANGE
Dim value As JET_TABLEID

value = instance.tableid

instance.tableid = value
```

``` csharp
public JET_TABLEID tableid { get; set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](./jet-tableid-structure.md)  

## See also

#### Reference

[JET_INDEXRANGE class](./jet-indexrange-class.md)

[JET_INDEXRANGE members](./jet-indexrange-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
