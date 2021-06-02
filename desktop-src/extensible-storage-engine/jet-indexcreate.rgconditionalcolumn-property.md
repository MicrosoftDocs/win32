---
description: "Learn more about: JET_INDEXCREATE.rgconditionalcolumn property"
title: JET_INDEXCREATE.rgconditionalcolumn property 
TOCTitle: 'rgconditionalcolumn property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INDEXCREATE.rgconditionalcolumn
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_indexcreate.rgconditionalcolumn(v=EXCHG.10)
ms:contentKeyID: 55103653
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INDEXCREATE.rgconditionalcolumn
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXCREATE.get_rgconditionalcolumn
- Microsoft.Isam.Esent.Interop.JET_INDEXCREATE.set_rgconditionalcolumn
- Microsoft.Isam.Esent.Interop.JET_INDEXCREATE.rgconditionalcolumn
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXCREATE.rgconditionalcolumn property

Gets or sets the optional conditional columns.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property rgconditionalcolumn As JET_CONDITIONALCOLUMN()
    Get
    Set
'Usage
Dim instance As JET_INDEXCREATE
Dim value As JET_CONDITIONALCOLUMN()

value = instance.rgconditionalcolumn

instance.rgconditionalcolumn = value
```

``` csharp
public JET_CONDITIONALCOLUMN[] rgconditionalcolumn { get; set; }
```

#### Property value

Type: \[\]  

## See also

#### Reference

[JET_INDEXCREATE class](./jet-indexcreate-class.md)

[JET_INDEXCREATE members](./jet-indexcreate-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
