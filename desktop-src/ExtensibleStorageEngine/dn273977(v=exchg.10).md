---
title: DoubleColumnValue.Size property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Size property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.DoubleColumnValue.Size
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.doublecolumnvalue.size(v=EXCHG.10)
ms:contentKeyID: 55101196
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.DoubleColumnValue.Size
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.DoubleColumnValue.get_Size
- Microsoft.Isam.Esent.Interop.DoubleColumnValue.Size
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# DoubleColumnValue.Size property

Gets the size of the value in the column. This returns 0 for variable sized columns (i.e. binary and string).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Protected Overrides ReadOnly Property Size As Integer
    Get
'Usage
Dim value As Integer

value = Me.Size
```

``` csharp
protected override int Size { get; }
```

#### Property value

Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  

## See also

#### Reference

[DoubleColumnValue class](dn273972\(v=exchg.10\).md)

[DoubleColumnValue members](dn334200\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

