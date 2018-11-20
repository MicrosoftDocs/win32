---
title: JET_COMMIT_ID.GreaterThan operator  (Microsoft.Isam.Esent.Interop.Windows8)
TOCTitle: 'GreaterThan operator '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.op_GreaterThan(Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID,Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.windows8.jet_commit_id.op_greaterthan(v=EXCHG.10)
ms:contentKeyID: 55104406
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.GreaterThan
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.GreaterThan
- Microsoft.Isam.Esent.Interop.Windows8.JET_COMMIT_ID.op_GreaterThan
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_COMMIT\_ID.GreaterThan operator

Determine whether one commitid is before another commitid.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Windows8](dn335439\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Operator > ( _
    lhs As JET_COMMIT_ID, _
    rhs As JET_COMMIT_ID _
) As Boolean
'Usage
Dim lhs As JET_COMMIT_ID
Dim rhs As JET_COMMIT_ID
Dim returnValue As Boolean

returnValue = (lhs > rhs)
```

``` csharp
public static bool operator >(
    JET_COMMIT_ID lhs,
    JET_COMMIT_ID rhs
)
```

#### Parameters

  - lhs  
    Type: [Microsoft.Isam.Esent.Interop.Windows8.JET\_COMMIT\_ID](dn335448\(v=exchg.10\).md)  
    
    The first commitid to compare.

<!-- end list -->

  - rhs  
    Type: [Microsoft.Isam.Esent.Interop.Windows8.JET\_COMMIT\_ID](dn335448\(v=exchg.10\).md)  
    
    The second commitid to compare.

#### Return value

Type: [System.Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)  
True if lhs comes after rhs.  

## See also

#### Reference

[JET\_COMMIT\_ID class](dn335448\(v=exchg.10\).md)

[JET\_COMMIT\_ID members](dn335451\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Windows8 namespace](dn335439\(v=exchg.10\).md)

