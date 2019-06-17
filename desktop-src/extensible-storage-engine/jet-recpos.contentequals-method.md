---
title: JET_RECPOS.ContentEquals method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'ContentEquals method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_RECPOS.ContentEquals(Microsoft.Isam.Esent.Interop.JET_RECPOS)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_recpos.contentequals(v=EXCHG.10)
ms:contentKeyID: 55103845
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_RECPOS.ContentEquals
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_RECPOS.ContentEquals
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_RECPOS.ContentEquals method

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function ContentEquals ( _
    other As JET_RECPOS _
) As Boolean
'Usage
Dim instance As JET_RECPOS
Dim other As JET_RECPOS
Dim returnValue As Boolean

returnValue = instance.ContentEquals(other)
```

``` csharp
public bool ContentEquals(
    JET_RECPOS other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET_RECPOS](dn335256\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](https://docs.microsoft.com/dotnet/api/system.boolean?redirectedfrom=MSDN)  
True if the two instances are equal.  

#### Implements

[IContentEquatable\<T\>.ContentEquals(T)](hh538970\(v=exchg.10\).md)  

## See also

#### Reference

[JET_RECPOS class](dn335256\(v=exchg.10\).md)

[JET_RECPOS members](dn335257\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

