---
title: Session Implicit conversion (Session to JET_SESID)
TOCTitle: Implicit conversion (Session to JET_SESID)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Session.op_Implicit(Microsoft.Isam.Esent.Interop.Session)~Microsoft.Isam.Esent.Interop.JET_SESID
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.session.op_implicit(v=EXCHG.10)
ms:contentKeyID: 55104121
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Session.Implicit
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Session.op_Implicit
- Microsoft.Isam.Esent.Interop.Session.Implicit
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Session Implicit conversion (Session to JET_SESID)

Implicit conversion operator from a Session to a JET_SESID. This allows a Session to be used with APIs which expect a JET_SESID.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Widening Operator CType ( _
    session As Session _
) As JET_SESID
'Usage
Dim input As Session
Dim output As JET_SESID

output = CType(input, JET_SESID)
```

``` csharp
public static implicit operator JET_SESID (
    Session session
)
```

#### Parameters

  - session  
    Type: [Microsoft.Isam.Esent.Interop.Session](dn351164\(v=exchg.10\).md)  
    
    The session to convert.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
The JET_SESID of the session.  

## See also

#### Reference

[Session class](dn351164\(v=exchg.10\).md)

[Session members](dn351125\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

