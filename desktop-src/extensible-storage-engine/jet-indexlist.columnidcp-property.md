---
description: "Learn more about: JET_INDEXLIST.columnidCp property"
title: JET_INDEXLIST.columnidCp property 
TOCTitle: 'columnidCp property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidCp
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_indexlist.columnidcp(v=EXCHG.10)
ms:contentKeyID: 55103663
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidCp
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.set_columnidCp
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidCp
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.get_columnidCp
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXLIST.columnidCp property

Gets the columnid of the column in the temporary table which stores the code page of the indexed column. The column is of type [Short](./jet-coltyp-enumeration.md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property columnidCp As JET_COLUMNID
    Get
    Friend Set
'Usage
Dim instance As JET_INDEXLIST
Dim value As JET_COLUMNID

value = instance.columnidCp
```

``` csharp
public JET_COLUMNID columnidCp { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](./jet-columnid-structure.md)  

## See also

#### Reference

[JET_INDEXLIST class](./jet-indexlist-class.md)

[JET_INDEXLIST members](./jet-indexlist-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
