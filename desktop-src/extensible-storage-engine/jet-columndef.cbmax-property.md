---
title: JET_COLUMNDEF.cbMax property 
TOCTitle: 'cbMax property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_COLUMNDEF.cbMax
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_columndef.cbmax(v=EXCHG.10)
ms:contentKeyID: 55103491
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_COLUMNDEF.cbMax
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_COLUMNDEF.cbMax
- Microsoft.Isam.Esent.Interop.JET_COLUMNDEF.get_cbMax
- Microsoft.Isam.Esent.Interop.JET_COLUMNDEF.set_cbMax
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_COLUMNDEF.cbMax property

Gets or sets the maximum length of the column. This is only meaningful for columns of type [Text](hh577895\(v=exchg.10\).md), [LongText](hh577895\(v=exchg.10\).md), [Binary](hh577895\(v=exchg.10\).md) and [LongBinary](hh577895\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cbMax As Integer
    Get
    Set
'Usage
Dim instance As JET_COLUMNDEF
Dim value As Integer

value = instance.cbMax

instance.cbMax = value
```

``` csharp
public int cbMax { get; set; }
```

#### Property value

Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  

## See also

#### Reference

[JET_COLUMNDEF class](dn335038\(v=exchg.10\).md)

[JET_COLUMNDEF members](dn335075\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

