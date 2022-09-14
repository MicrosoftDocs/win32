---
description: "Learn more about: JET_DBINFOMISC.bkinfoFullPrev property"
title: JET_DBINFOMISC.bkinfoFullPrev property 
TOCTitle: 'bkinfoFullPrev property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.bkinfoFullPrev
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.bkinfofullprev(v=EXCHG.10)
ms:contentKeyID: 39510503
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.bkinfoFullPrev
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.bkinfoFullPrev
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_bkinfoFullPrev
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_bkinfoFullPrev
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.bkinfoFullPrev property

Gets information about the last successful full backup.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property bkinfoFullPrev As JET_BKINFO
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As JET_BKINFO

value = instance.bkinfoFullPrev
```

``` csharp
public JET_BKINFO bkinfoFullPrev { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_BKINFO](./jet-bkinfo-structure2.md)  

## See also

#### Reference

[JET_DBINFOMISC class](./jet-dbinfomisc-class.md)

[JET_DBINFOMISC members](./jet-dbinfomisc-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
