---
title: JET_RECSIZE.cMultiValues property  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'cMultiValues property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.cMultiValues
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.vista.jet_recsize.cmultivalues(v=EXCHG.10)
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

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](hh558039\(v=exchg.10\).md)  
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

Type: [System.Int64](https://docs.microsoft.com/dotnet/api/system.int64?redirectedfrom=MSDN)  

## See also

#### Reference

[JET_RECSIZE structure](hh557010\(v=exchg.10\).md)

[JET_RECSIZE members](hh557127\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Vista namespace](hh558039\(v=exchg.10\).md)

