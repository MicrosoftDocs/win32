---
description: "Learn more about: ColumnValue.Size property"
title: ColumnValue.Size property 
TOCTitle: 'Size property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.ColumnValue.Size
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.columnvalue.size(v=EXCHG.10)
ms:contentKeyID: 55101207
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.ColumnValue.Size
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.ColumnValue.get_Size
- Microsoft.Isam.Esent.Interop.ColumnValue.Size
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# ColumnValue.Size property

Gets the size of the value in the column. This returns 0 for variable sized columns (i.e. binary and string).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Protected MustOverride ReadOnly Property Size As Integer
    Get
'Usage
Dim value As Integer

value = Me.Size
```

``` csharp
protected abstract int Size { get; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[ColumnValue class](./columnvalue-class.md)

[ColumnValue members](./columnvalue-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
