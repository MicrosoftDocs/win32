---
description: "Learn more about: JET_RETINFO.itagSequence property"
title: JET_RETINFO.itagSequence property 
TOCTitle: 'itagSequence property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_RETINFO.itagSequence
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_retinfo.itagsequence(v=EXCHG.10)
ms:contentKeyID: 55103876
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_RETINFO.itagSequence
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_RETINFO.get_itagSequence
- Microsoft.Isam.Esent.Interop.JET_RETINFO.itagSequence
- Microsoft.Isam.Esent.Interop.JET_RETINFO.set_itagSequence
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_RETINFO.itagSequence property

Gets or sets the sequence number of value in a multi-valued column. The array of values is one-based. The first value is sequence 1, not 0. If the record column has only one value then 1 should be passed as the itagSequence.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property itagSequence As Integer
    Get
    Set
'Usage
Dim instance As JET_RETINFO
Dim value As Integer

value = instance.itagSequence

instance.itagSequence = value
```

``` csharp
public int itagSequence { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[JET_RETINFO class](./jet-retinfo-class.md)

[JET_RETINFO members](./jet-retinfo-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
