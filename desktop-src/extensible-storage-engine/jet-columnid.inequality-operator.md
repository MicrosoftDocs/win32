---
title: JET_COLUMNID.Inequality operator  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Inequality operator '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_COLUMNID.op_Inequality(Microsoft.Isam.Esent.Interop.JET_COLUMNID,Microsoft.Isam.Esent.Interop.JET_COLUMNID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_columnid.op_inequality(v=EXCHG.10)
ms:contentKeyID: 39516136
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_COLUMNID.Inequality
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_COLUMNID.Inequality
- Microsoft.Isam.Esent.Interop.JET_COLUMNID.op_Inequality
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_COLUMNID.Inequality operator

Determines whether two specified instances of JET_COLUMNID are not equal.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Operator <> ( _
    lhs As JET_COLUMNID, _
    rhs As JET_COLUMNID _
) As Boolean
'Usage
Dim lhs As JET_COLUMNID
Dim rhs As JET_COLUMNID
Dim returnValue As Boolean

returnValue = (lhs <> rhs)
```

``` csharp
public static bool operator !=(
    JET_COLUMNID lhs,
    JET_COLUMNID rhs
)
```

#### Parameters

  - lhs  
    Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](hh564510\(v=exchg.10\).md)  
    
    The first instance to compare.

<!-- end list -->

  - rhs  
    Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](hh564510\(v=exchg.10\).md)  
    
    The second instance to compare.

#### Return value

Type: [System.Boolean](https://docs.microsoft.com/dotnet/api/system.boolean?redirectedfrom=MSDN)  
True if the two instances are not equal.  

## See also

#### Reference

[JET_COLUMNID structure](hh564510\(v=exchg.10\).md)

[JET_COLUMNID members](hh558343\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

