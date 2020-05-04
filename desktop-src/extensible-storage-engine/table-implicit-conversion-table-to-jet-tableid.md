---
title: Table Implicit conversion (Table to JET_TABLEID)
TOCTitle: Implicit conversion (Table to JET_TABLEID)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Table.op_Implicit(Microsoft.Isam.Esent.Interop.Table)~Microsoft.Isam.Esent.Interop.JET_TABLEID
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.table.op_implicit(v=EXCHG.10)
ms:contentKeyID: 55104156
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Table.Implicit
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Table.Implicit
- Microsoft.Isam.Esent.Interop.Table.op_Implicit
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Table Implicit conversion (Table to JET_TABLEID)

Implicit conversion operator from a Table to a JET_TABLEID. This allows a Table to be used with APIs which expect a JET_TABLEID.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Widening Operator CType ( _
    table As Table _
) As JET_TABLEID
'Usage
Dim input As Table
Dim output As JET_TABLEID

output = CType(input, JET_TABLEID)
```

``` csharp
public static implicit operator JET_TABLEID (
    Table table
)
```

#### Parameters

  - table  
    Type: [Microsoft.Isam.Esent.Interop.Table](dn351163\(v=exchg.10\).md)  
    
    The table to convert.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](hh566310\(v=exchg.10\).md)  
The JET_TABLEID of the table.  

## See also

#### Reference

[Table class](dn351163\(v=exchg.10\).md)

[Table members](dn351162\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

