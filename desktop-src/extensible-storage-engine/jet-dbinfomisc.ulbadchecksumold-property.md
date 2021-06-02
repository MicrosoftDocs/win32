---
description: "Learn more about: JET_DBINFOMISC.ulBadChecksumOld property"
title: JET_DBINFOMISC.ulBadChecksumOld property 
TOCTitle: 'ulBadChecksumOld property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.ulBadChecksumOld
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.ulbadchecksumold(v=EXCHG.10)
ms:contentKeyID: 39513159
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.ulBadChecksumOld
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_ulBadChecksumOld
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_ulBadChecksumOld
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.ulBadChecksumOld
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.ulBadChecksumOld property

Gets the number of times a non-correctable checksum error was found before the last repair.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property ulBadChecksumOld As Integer
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As Integer

value = instance.ulBadChecksumOld
```

``` csharp
public int ulBadChecksumOld { get; internal set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[JET_DBINFOMISC class](./jet-dbinfomisc-class.md)

[JET_DBINFOMISC members](./jet-dbinfomisc-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
