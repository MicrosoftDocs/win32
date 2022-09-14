---
description: "Learn more about: JET_SETINFO.ContentEquals method"
title: JET_SETINFO.ContentEquals method 
TOCTitle: 'ContentEquals method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_SETINFO.ContentEquals(Microsoft.Isam.Esent.Interop.JET_SETINFO)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_setinfo.contentequals(v=EXCHG.10)
ms:contentKeyID: 55103913
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_SETINFO.ContentEquals
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_SETINFO.ContentEquals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_SETINFO.ContentEquals method

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function ContentEquals ( _
    other As JET_SETINFO _
) As Boolean
'Usage
Dim instance As JET_SETINFO
Dim other As JET_SETINFO
Dim returnValue As Boolean

returnValue = instance.ContentEquals(other)
```

``` csharp
public bool ContentEquals(
    JET_SETINFO other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET_SETINFO](./jet-setinfo-class.md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](/dotnet/api/system.boolean)  
True if the two instances are equal.  

#### Implements

[IContentEquatable\<T\>.ContentEquals(T)](./icontentequatable-t-.contentequals-method.md)  

## See also

#### Reference

[JET_SETINFO class](./jet-setinfo-class.md)

[JET_SETINFO members](./jet-setinfo-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
