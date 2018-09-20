---
title: JET_RECSIZE.cbLongValueDataCompressed property  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'cbLongValueDataCompressed property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.cbLongValueDataCompressed
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.vista.jet_recsize.cblongvaluedatacompressed(v=EXCHG.10)
ms:contentKeyID: 39515830
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.cbLongValueDataCompressed
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.get_cbLongValueDataCompressed
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.cbLongValueDataCompressed
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.set_cbLongValueDataCompressed
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_RECSIZE.cbLongValueDataCompressed property

Gets the compressed size of user data in the long-value tree. This is the same as [cbLongValueData](hh557913\(v=exchg.10\).md) if no separated long values are compressed.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](hh558039\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cbLongValueDataCompressed As Long
    Get
    Friend Set
'Usage
Dim instance As JET_RECSIZE
Dim value As Long

value = instance.cbLongValueDataCompressed
```

``` csharp
public long cbLongValueDataCompressed { get; internal set; }
```

#### Property value

Type: [System.Int64](http://msdn2.microsoft.com/en-us/library/6yy583ek)  

## See also

#### Reference

[JET\_RECSIZE structure](hh557010\(v=exchg.10\).md)

[JET\_RECSIZE members](hh557127\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Vista namespace](hh558039\(v=exchg.10\).md)

