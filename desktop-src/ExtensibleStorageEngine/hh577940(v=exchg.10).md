---
title: JET_DBID.Inequality operator  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Inequality operator '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_DBID.op_Inequality(Microsoft.Isam.Esent.Interop.JET_DBID,Microsoft.Isam.Esent.Interop.JET_DBID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_dbid.op_inequality(v=EXCHG.10)
ms:contentKeyID: 39511214
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBID.Inequality
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBID.op_Inequality
- Microsoft.Isam.Esent.Interop.JET_DBID.Inequality
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBID.Inequality operator

Determines whether two specified instances of JET_DBID are not equal.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Operator <> ( _
    lhs As JET_DBID, _
    rhs As JET_DBID _
) As Boolean
'Usage
Dim lhs As JET_DBID
Dim rhs As JET_DBID
Dim returnValue As Boolean

returnValue = (lhs <> rhs)
```

``` csharp
public static bool operator !=(
    JET_DBID lhs,
    JET_DBID rhs
)
```

#### Parameters

  - lhs  
    Type: [Microsoft.Isam.Esent.Interop.JET_DBID](hh596176\(v=exchg.10\).md)  
    
    The first instance to compare.

<!-- end list -->

  - rhs  
    Type: [Microsoft.Isam.Esent.Interop.JET_DBID](hh596176\(v=exchg.10\).md)  
    
    The second instance to compare.

#### Return value

Type: [System.Boolean](https://msdn.microsoft.com/en-us/library/a28wyd50)  
True if the two instances are not equal.  

## See also

#### Reference

[JET_DBID structure](hh596176\(v=exchg.10\).md)

[JET_DBID members](hh566162\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

