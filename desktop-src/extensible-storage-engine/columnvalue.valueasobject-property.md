---
description: "Learn more about: ColumnValue.ValueAsObject property"
title: ColumnValue.ValueAsObject property 
TOCTitle: 'ValueAsObject property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.ColumnValue.ValueAsObject
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.columnvalue.valueasobject(v=EXCHG.10)
ms:contentKeyID: 55101198
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.ColumnValue.ValueAsObject
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.ColumnValue.get_ValueAsObject
- Microsoft.Isam.Esent.Interop.ColumnValue.ValueAsObject
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# ColumnValue.ValueAsObject property

Gets the last set or retrieved value of the column. The value is returned as a generic object.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public MustOverride ReadOnly Property ValueAsObject As Object
    Get
'Usage
Dim instance As ColumnValue
Dim value As Object

value = instance.ValueAsObject
```

``` csharp
public abstract Object ValueAsObject { get; }
```

#### Property value

Type: [System.Object](/dotnet/api/system.object)  

## See also

#### Reference

[ColumnValue class](./columnvalue-class.md)

[ColumnValue members](./columnvalue-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
