---
description: "Learn more about: JET_DBINFOMISC.genMinRequired property"
title: JET_DBINFOMISC.genMinRequired property 
TOCTitle: 'genMinRequired property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.genMinRequired
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.genminrequired(v=EXCHG.10)
ms:contentKeyID: 39514817
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.genMinRequired
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_genMinRequired
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_genMinRequired
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.genMinRequired
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.genMinRequired property

Gets the minimum log generation required for replaying the logs. Typically the checkpoint generation.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property genMinRequired As Integer
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As Integer

value = instance.genMinRequired
```

``` csharp
public int genMinRequired { get; internal set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[JET_DBINFOMISC class](./jet-dbinfomisc-class.md)

[JET_DBINFOMISC members](./jet-dbinfomisc-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
