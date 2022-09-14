---
description: "Learn more about: JET_RECSIZE.Subtraction operator"
title: JET_RECSIZE.Subtraction operator  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'Subtraction operator '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.op_Subtraction(Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE,Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.jet_recsize.op_subtraction(v=EXCHG.10)
ms:contentKeyID: 39516016
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.Subtraction
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.op_Subtraction
- Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE.Subtraction
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_RECSIZE.Subtraction operator

Calculate the difference in sizes between two JET_RECSIZE structures.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Operator - ( _
    left As JET_RECSIZE, _
    right As JET_RECSIZE _
) As JET_RECSIZE
'Usage
Dim left As JET_RECSIZE
Dim right As JET_RECSIZE
Dim returnValue As JET_RECSIZE

returnValue = (left - right)
```

``` csharp
public static JET_RECSIZE operator -(
    JET_RECSIZE left,
    JET_RECSIZE right
)
```

#### Parameters

  - left  
    Type: [Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE](./jet-recsize-structure2.md)  
    
    The first JET_RECSIZE.

<!-- end list -->

  - right  
    Type: [Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE](./jet-recsize-structure2.md)  
    
    The second JET_RECSIZE.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE](./jet-recsize-structure2.md)  
A JET_RECSIZE containing the difference in sizes between left and right.  

## See also

#### Reference

[JET_RECSIZE structure](./jet-recsize-structure2.md)

[JET_RECSIZE members](./jet-recsize-members.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
