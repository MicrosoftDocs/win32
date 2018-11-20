---
title: JET_HANDLE.Equality operator  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Equality operator '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_HANDLE.op_Equality(Microsoft.Isam.Esent.Interop.JET_HANDLE,Microsoft.Isam.Esent.Interop.JET_HANDLE)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_handle.op_equality(v=EXCHG.10)
ms:contentKeyID: 39512271
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_HANDLE.Equality
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_HANDLE.Equality
- Microsoft.Isam.Esent.Interop.JET_HANDLE.op_Equality
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_HANDLE.Equality operator

Determines whether two specified instances of JET\_HANDLE are equal.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Operator = ( _
    lhs As JET_HANDLE, _
    rhs As JET_HANDLE _
) As Boolean
'Usage
Dim lhs As JET_HANDLE
Dim rhs As JET_HANDLE
Dim returnValue As Boolean

returnValue = (lhs = rhs)
```

``` csharp
public static bool operator ==(
    JET_HANDLE lhs,
    JET_HANDLE rhs
)
```

#### Parameters

  - lhs  
    Type: [Microsoft.Isam.Esent.Interop.JET\_HANDLE](hh558081\(v=exchg.10\).md)  
    
    The first instance to compare.

<!-- end list -->

  - rhs  
    Type: [Microsoft.Isam.Esent.Interop.JET\_HANDLE](hh558081\(v=exchg.10\).md)  
    
    The second instance to compare.

#### Return value

Type: [System.Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)  
True if the two instances are equal.  

## See also

#### Reference

[JET\_HANDLE structure](hh558081\(v=exchg.10\).md)

[JET\_HANDLE members](hh557479\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

