---
description: "Learn more about: JET_INDEXLIST.columnidindexname property"
title: JET_INDEXLIST.columnidindexname property 
TOCTitle: 'columnidindexname property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidindexname
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_indexlist.columnidindexname(v=EXCHG.10)
ms:contentKeyID: 55103619
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidindexname
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.get_columnidindexname
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidindexname
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.set_columnidindexname
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXLIST.columnidindexname property

Gets the columnid of the column in the temporary table which stores the name of the index. The column is of type [Text](./jet-coltyp-enumeration.md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property columnidindexname As JET_COLUMNID
    Get
    Friend Set
'Usage
Dim instance As JET_INDEXLIST
Dim value As JET_COLUMNID

value = instance.columnidindexname
```

``` csharp
public JET_COLUMNID columnidindexname { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](./jet-columnid-structure.md)  

## See also

#### Reference

[JET_INDEXLIST class](./jet-indexlist-class.md)

[JET_INDEXLIST members](./jet-indexlist-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
