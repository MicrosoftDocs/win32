---
description: "Learn more about: JET_RECORDLIST.columnidBookmark property"
title: JET_RECORDLIST.columnidBookmark property 
TOCTitle: 'columnidBookmark property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_RECORDLIST.columnidBookmark
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_recordlist.columnidbookmark(v=EXCHG.10)
ms:contentKeyID: 55103827
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_RECORDLIST.columnidBookmark
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_RECORDLIST.get_columnidBookmark
- Microsoft.Isam.Esent.Interop.JET_RECORDLIST.set_columnidBookmark
- Microsoft.Isam.Esent.Interop.JET_RECORDLIST.columnidBookmark
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_RECORDLIST.columnidBookmark property

Gets the columnid of the column in the temporary table which stores the bookmark of the record. The column is of type JET_coltyp.Text.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property columnidBookmark As JET_COLUMNID
    Get
    Friend Set
'Usage
Dim instance As JET_RECORDLIST
Dim value As JET_COLUMNID

value = instance.columnidBookmark
```

``` csharp
public JET_COLUMNID columnidBookmark { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](./jet-columnid-structure.md)  

## See also

#### Reference

[JET_RECORDLIST class](./jet-recordlist-class.md)

[JET_RECORDLIST members](./jet-recordlist-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
