---
title: DateTimeColumnValue.Size property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Size property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.DateTimeColumnValue.Size
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.datetimecolumnvalue.size(v=EXCHG.10)
ms:contentKeyID: 55101209
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.DateTimeColumnValue.Size
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.DateTimeColumnValue.get_Size
- Microsoft.Isam.Esent.Interop.DateTimeColumnValue.Size
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# DateTimeColumnValue.Size property

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

Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  

## See also

#### Reference

[DateTimeColumnValue class](dn334238\(v=exchg.10\).md)

[DateTimeColumnValue members](dn334192\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

