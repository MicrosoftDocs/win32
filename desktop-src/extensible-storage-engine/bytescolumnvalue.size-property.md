---
description: "Learn more about: BytesColumnValue.Size property"
title: BytesColumnValue.Size property 
TOCTitle: 'Size property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.BytesColumnValue.Size
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.bytescolumnvalue.size(v=EXCHG.10)
ms:contentKeyID: 55101188
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.BytesColumnValue.Size
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.BytesColumnValue.get_Size
- Microsoft.Isam.Esent.Interop.BytesColumnValue.Size
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# BytesColumnValue.Size property

Gets the size of the value in the column. This returns 0 for variable sized columns (i.e. binary and string).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
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

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[BytesColumnValue class](./bytescolumnvalue-class.md)

[BytesColumnValue members](./bytescolumnvalue-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
