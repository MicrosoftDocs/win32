---
description: "Learn more about: JET_DBINFOMISC.bkinfoDiffPrev property"
title: JET_DBINFOMISC.bkinfoDiffPrev property 
TOCTitle: 'bkinfoDiffPrev property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.bkinfoDiffPrev
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.bkinfodiffprev(v=EXCHG.10)
ms:contentKeyID: 39513441
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.bkinfoDiffPrev
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.bkinfoDiffPrev
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_bkinfoDiffPrev
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_bkinfoDiffPrev
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.bkinfoDiffPrev property

Gets information about the last successful differential backup. Reset when [bkinfoFullPrev](./jet-dbinfomisc.bkinfofullprev-property.md) is set.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property bkinfoDiffPrev As JET_BKINFO
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As JET_BKINFO

value = instance.bkinfoDiffPrev
```

``` csharp
public JET_BKINFO bkinfoDiffPrev { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_BKINFO](./jet-bkinfo-structure2.md)  

## See also

#### Reference

[JET_DBINFOMISC class](./jet-dbinfomisc-class.md)

[JET_DBINFOMISC members](./jet-dbinfomisc-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
