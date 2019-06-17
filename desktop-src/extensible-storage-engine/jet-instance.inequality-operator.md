---
title: JET_INSTANCE.Inequality operator  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Inequality operator '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_INSTANCE.op_Inequality(Microsoft.Isam.Esent.Interop.JET_INSTANCE,Microsoft.Isam.Esent.Interop.JET_INSTANCE)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_instance.op_inequality(v=EXCHG.10)
ms:contentKeyID: 39512209
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INSTANCE.Inequality
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INSTANCE.Inequality
- Microsoft.Isam.Esent.Interop.JET_INSTANCE.op_Inequality
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INSTANCE.Inequality operator

Determines whether two specified instances of JET_INSTANCE are not equal.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Operator <> ( _
    lhs As JET_INSTANCE, _
    rhs As JET_INSTANCE _
) As Boolean
'Usage
Dim lhs As JET_INSTANCE
Dim rhs As JET_INSTANCE
Dim returnValue As Boolean

returnValue = (lhs <> rhs)
```

``` csharp
public static bool operator !=(
    JET_INSTANCE lhs,
    JET_INSTANCE rhs
)
```

#### Parameters

  - lhs  
    Type: [Microsoft.Isam.Esent.Interop.JET_INSTANCE](hh564593\(v=exchg.10\).md)  
    
    The first instance to compare.

<!-- end list -->

  - rhs  
    Type: [Microsoft.Isam.Esent.Interop.JET_INSTANCE](hh564593\(v=exchg.10\).md)  
    
    The second instance to compare.

#### Return value

Type: [System.Boolean](https://docs.microsoft.com/dotnet/api/system.boolean?redirectedfrom=MSDN)  
True if the two instances are not equal.  

## See also

#### Reference

[JET_INSTANCE structure](hh564593\(v=exchg.10\).md)

[JET_INSTANCE members](hh565454\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

