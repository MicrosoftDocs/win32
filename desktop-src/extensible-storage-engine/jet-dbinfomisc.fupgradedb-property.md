---
description: "Learn more about: JET_DBINFOMISC.fUpgradeDb property"
title: JET_DBINFOMISC.fUpgradeDb property 
TOCTitle: 'fUpgradeDb property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.fUpgradeDb
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.fupgradedb(v=EXCHG.10)
ms:contentKeyID: 39514685
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.fUpgradeDb
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_fUpgradeDb
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_fUpgradeDb
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.fUpgradeDb
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.fUpgradeDb property

Gets a value indicating whether the database is being upgraded. This value is for internal use only.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property fUpgradeDb As Boolean
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As Boolean

value = instance.fUpgradeDb
```

``` csharp
public bool fUpgradeDb { get; internal set; }
```

#### Property value

Type: [System.Boolean](/dotnet/api/system.boolean)  

## See also

#### Reference

[JET_DBINFOMISC class](./jet-dbinfomisc-class.md)

[JET_DBINFOMISC members](./jet-dbinfomisc-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
