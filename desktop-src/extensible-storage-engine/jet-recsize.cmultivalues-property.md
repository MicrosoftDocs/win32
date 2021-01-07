---
description: "Learn more about: JET_RECSIZE.cMultiValues property"
title: JET_RECSIZE.cMultiValues property  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'cMultiValues property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.cMultiValues
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.jet_recsize.cmultivalues(v=EXCHG.10)
ms:contentKeyID: 39510355
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.cMultiValues
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.cMultiValues
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.set_cMultiValues
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.get_cMultiValues
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_RECSIZE.cMultiValues property

Gets the accumulation of the total number of values beyond the first for all columns in the record.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cMultiValues As Long
    Get
    Friend Set
'Usage
Dim instance As JET_RECSIZE
Dim value As Long

value = instance.cMultiValues
```

``` csharp
public long cMultiValues { get; internal set; }
```

#### Property value

Type: [System.Int64](/dotnet/api/system.int64)  

## See also

#### Reference

[JET_RECSIZE structure](./jet-recsize-structure2.md)

[JET_RECSIZE members](./jet-recsize-members.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
