---
title: JET_THREADSTATS.Addition operator  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'Addition operator '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.op_Addition(Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS,Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.vista.jet_threadstats.op_addition(v=EXCHG.10)
ms:contentKeyID: 39516195
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.Addition
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.Addition
- Microsoft.Isam.Esent.Interop.Vista.JET_THREADSTATS.op_Addition
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_THREADSTATS.Addition operator

Add the stats in two JET\_THREADSTATS structures.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](hh558039\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Operator + ( _
    t1 As JET_THREADSTATS, _
    t2 As JET_THREADSTATS _
) As JET_THREADSTATS
'Usage
Dim t1 As JET_THREADSTATS
Dim t2 As JET_THREADSTATS
Dim returnValue As JET_THREADSTATS

returnValue = (t1 + t2)
```

``` csharp
public static JET_THREADSTATS operator +(
    JET_THREADSTATS t1,
    JET_THREADSTATS t2
)
```

#### Parameters

  - t1  
    Type: [Microsoft.Isam.Esent.Interop.Vista.JET\_THREADSTATS](hh578565\(v=exchg.10\).md)  
    
    The first JET\_THREADSTATS.

<!-- end list -->

  - t2  
    Type: [Microsoft.Isam.Esent.Interop.Vista.JET\_THREADSTATS](hh578565\(v=exchg.10\).md)  
    
    The second JET\_THREADSTATS.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.Vista.JET\_THREADSTATS](hh578565\(v=exchg.10\).md)  
A JET\_THREADSTATS containing the result of adding the stats in t1 and t2.  

## See also

#### Reference

[JET\_THREADSTATS structure](hh578565\(v=exchg.10\).md)

[JET\_THREADSTATS members](hh579250\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Vista namespace](hh558039\(v=exchg.10\).md)

