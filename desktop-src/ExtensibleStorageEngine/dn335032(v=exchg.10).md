---
title: JET_COLUMNCREATE.cbMax property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'cbMax property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_COLUMNCREATE.cbMax
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_columncreate.cbmax(v=EXCHG.10)
ms:contentKeyID: 55103390
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_COLUMNCREATE.cbMax
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_COLUMNCREATE.cbMax
- Microsoft.Isam.Esent.Interop.JET_COLUMNCREATE.set_cbMax
- Microsoft.Isam.Esent.Interop.JET_COLUMNCREATE.get_cbMax
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_COLUMNCREATE.cbMax property

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
Dim instance As JET_COLUMNCREATE
Dim value As Integer

value = instance.cbMax

instance.cbMax = value
```

``` csharp
public int cbMax { get; set; }
```

#### Property value

Type: [System.Int32](https://msdn.microsoft.com/en-us/library/td2s409d)  

## See also

#### Reference

[JET_COLUMNCREATE class](dn335028\(v=exchg.10\).md)

[JET_COLUMNCREATE members](dn335070\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

