---
description: "Learn more about: JET_DBINFOMISC.dbstate property"
title: JET_DBINFOMISC.dbstate property 
TOCTitle: 'dbstate property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.dbstate
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.dbstate(v=EXCHG.10)
ms:contentKeyID: 39513341
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.dbstate
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_dbstate
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.dbstate
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_dbstate
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.dbstate property

Gets the consistent/inconsistent state of the database.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property dbstate As JET_dbstate
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As JET_dbstate

value = instance.dbstate
```

``` csharp
public JET_dbstate dbstate { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_dbstate](./jet-dbstate-enumeration.md)  

## See also

#### Reference

[JET_DBINFOMISC class](./jet-dbinfomisc-class.md)

[JET_DBINFOMISC members](./jet-dbinfomisc-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
