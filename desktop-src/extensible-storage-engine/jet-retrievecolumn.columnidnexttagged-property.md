---
description: "Learn more about: JET_RETRIEVECOLUMN.columnidNextTagged property"
title: JET_RETRIEVECOLUMN.columnidNextTagged property 
TOCTitle: 'columnidNextTagged property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.columnidNextTagged
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_retrievecolumn.columnidnexttagged(v=EXCHG.10)
ms:contentKeyID: 55103812
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.columnidNextTagged
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.columnidNextTagged
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.get_columnidNextTagged
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.set_columnidNextTagged
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_RETRIEVECOLUMN.columnidNextTagged property

Gets the columnid of the tagged, multi-valued, or sparse column when all tagged columns are retrieved by passing 0 as the columnid.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property columnidNextTagged As JET_COLUMNID
    Get
    Private Set
'Usage
Dim instance As JET_RETRIEVECOLUMN
Dim value As JET_COLUMNID

value = instance.columnidNextTagged
```

``` csharp
public JET_COLUMNID columnidNextTagged { get; private set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](./jet-columnid-structure.md)  

## See also

#### Reference

[JET_RETRIEVECOLUMN class](./jet-retrievecolumn-class.md)

[JET_RETRIEVECOLUMN members](./jet-retrievecolumn-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
