---
description: "Learn more about: JET_OBJECTLIST.columnidobjtyp property"
title: JET_OBJECTLIST.columnidobjtyp property 
TOCTitle: 'columnidobjtyp property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_OBJECTLIST.columnidobjtyp
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_objectlist.columnidobjtyp(v=EXCHG.10)
ms:contentKeyID: 55103770
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_OBJECTLIST.columnidobjtyp
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_OBJECTLIST.set_columnidobjtyp
- Microsoft.Isam.Esent.Interop.JET_OBJECTLIST.get_columnidobjtyp
- Microsoft.Isam.Esent.Interop.JET_OBJECTLIST.columnidobjtyp
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_OBJECTLIST.columnidobjtyp property

Gets the columnid of the column in the temporary table which stores the type of the table.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property columnidobjtyp As JET_COLUMNID
    Get
    Friend Set
'Usage
Dim instance As JET_OBJECTLIST
Dim value As JET_COLUMNID

value = instance.columnidobjtyp
```

``` csharp
public JET_COLUMNID columnidobjtyp { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](./jet-columnid-structure.md)  

## See also

#### Reference

[JET_OBJECTLIST class](./jet-objectlist-class.md)

[JET_OBJECTLIST members](./jet-objectlist-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
