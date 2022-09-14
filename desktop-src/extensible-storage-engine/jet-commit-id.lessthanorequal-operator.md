---
description: "Learn more about: JET_COMMIT_ID.LessThanOrEqual operator"
title: JET_COMMIT_ID.LessThanOrEqual operator  (Microsoft.Isam.Esent.Interop.Windows8)
TOCTitle: 'LessThanOrEqual operator '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.op_LessThanOrEqual(Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID,Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.windows8.jet_commit_id.op_lessthanorequal(v=EXCHG.10)
ms:contentKeyID: 55104413
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.LessThanOrEqual
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.LessThanOrEqual
- Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.op_LessThanOrEqual
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_COMMIT_ID.LessThanOrEqual operator

Determine whether one commitid is before another commitid.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Windows8](./microsoft.isam.esent.interop.windows8-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Operator <= ( _
    lhs As JET_COMMIT_ID, _
    rhs As JET_COMMIT_ID _
) As Boolean
'Usage
Dim lhs As JET_COMMIT_ID
Dim rhs As JET_COMMIT_ID
Dim returnValue As Boolean

returnValue = (lhs <= rhs)
```

``` csharp
public static bool operator <=(
    JET_COMMIT_ID lhs,
    JET_COMMIT_ID rhs
)
```

#### Parameters

  - lhs  
    Type: [Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID](./jet-commit-id-class.md)  
    
    The first commitid to compare.

<!-- end list -->

  - rhs  
    Type: [Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID](./jet-commit-id-class.md)  
    
    The second commitid to compare.

#### Return value

Type: [System.Boolean](/dotnet/api/system.boolean)  
True if lhs comes before or equal to rhs.  

## See also

#### Reference

[JET_COMMIT_ID class](./jet-commit-id-class.md)

[JET_COMMIT_ID members](./jet-commit-id-members.md)

[Microsoft.Isam.Esent.Interop.Windows8 namespace](./microsoft.isam.esent.interop.windows8-namespace.md)
