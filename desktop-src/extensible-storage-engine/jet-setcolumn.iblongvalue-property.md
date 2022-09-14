---
description: "Learn more about: JET_SETCOLUMN.ibLongValue property"
title: JET_SETCOLUMN.ibLongValue property 
TOCTitle: 'ibLongValue property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_SETCOLUMN.ibLongValue
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_setcolumn.iblongvalue(v=EXCHG.10)
ms:contentKeyID: 55103931
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_SETCOLUMN.ibLongValue
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_SETCOLUMN.get_ibLongValue
- Microsoft.Isam.Esent.Interop.JET_SETCOLUMN.ibLongValue
- Microsoft.Isam.Esent.Interop.JET_SETCOLUMN.set_ibLongValue
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_SETCOLUMN.ibLongValue property

Gets or sets offset to the first byte to be set in a column of type [LongBinary](./jet-coltyp-enumeration.md) or [LongText](./jet-coltyp-enumeration.md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property ibLongValue As Integer
    Get
    Set
'Usage
Dim instance As JET_SETCOLUMN
Dim value As Integer

value = instance.ibLongValue

instance.ibLongValue = value
```

``` csharp
public int ibLongValue { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[JET_SETCOLUMN class](./jet-setcolumn-class.md)

[JET_SETCOLUMN members](./jet-setcolumn-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
