---
description: "Learn more about: JET_BKINFO.Equality operator"
title: JET_BKINFO.Equality operator 
TOCTitle: 'Equality operator '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_BKINFO.op_Equality(Microsoft.Isam.Esent.Interop.JET_BKINFO,Microsoft.Isam.Esent.Interop.JET_BKINFO)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_bkinfo.op_equality(v=EXCHG.10)
ms:contentKeyID: 39510688
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_BKINFO.Equality
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_BKINFO.op_Equality
- Microsoft.Isam.Esent.Interop.JET_BKINFO.Equality
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_BKINFO.Equality operator

Determines whether two specified instances of JET_BKINFO are equal.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Operator = ( _
    lhs As JET_BKINFO, _
    rhs As JET_BKINFO _
) As Boolean
'Usage
Dim lhs As JET_BKINFO
Dim rhs As JET_BKINFO
Dim returnValue As Boolean

returnValue = (lhs = rhs)
```

``` csharp
public static bool operator ==(
    JET_BKINFO lhs,
    JET_BKINFO rhs
)
```

#### Parameters

  - lhs  
    Type: [Microsoft.Isam.Esent.Interop.JET_BKINFO](./jet-bkinfo-structure2.md)  
    
    The first instance to compare.

<!-- end list -->

  - rhs  
    Type: [Microsoft.Isam.Esent.Interop.JET_BKINFO](./jet-bkinfo-structure2.md)  
    
    The second instance to compare.

#### Return value

Type: [System.Boolean](/dotnet/api/system.boolean)  
True if the two instances are equal.  

## See also

#### Reference

[JET_BKINFO structure](./jet-bkinfo-structure2.md)

[JET_BKINFO members](./jet-bkinfo-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
