---
description: "Learn more about: JET_RETRIEVECOLUMN.ibLongValue property"
title: JET_RETRIEVECOLUMN.ibLongValue property 
TOCTitle: 'ibLongValue property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.ibLongValue
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_retrievecolumn.iblongvalue(v=EXCHG.10)
ms:contentKeyID: 55103819
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.ibLongValue
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.set_ibLongValue
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.ibLongValue
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.get_ibLongValue
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_RETRIEVECOLUMN.ibLongValue property

Gets or sets the offset to the first byte to be retrieved from a column of type [LongBinary](./jet-coltyp-enumeration.md) or [LongText](./jet-coltyp-enumeration.md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property ibLongValue As Integer
    Get
    Set
'Usage
Dim instance As JET_RETRIEVECOLUMN
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

[JET_RETRIEVECOLUMN class](./jet-retrievecolumn-class.md)

[JET_RETRIEVECOLUMN members](./jet-retrievecolumn-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
