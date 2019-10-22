---
title: IContentEquatable(T).ContentEquals method 
TOCTitle: 'ContentEquals method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.IContentEquatable`1.ContentEquals(`0)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Hh538970(v=EXCHG.10)
ms:contentKeyID: 39509953
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.IContentEquatable`1.ContentEquals
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.IContentEquatable`1.ContentEquals
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# IContentEquatable\<T\>.ContentEquals method

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Function ContentEquals ( _
    other As T _
) As Boolean
'Usage
Dim instance As IContentEquatable
Dim other As T
Dim returnValue As Boolean

returnValue = instance.ContentEquals(other)
```

``` csharp
bool ContentEquals(
    T other
)
```

#### Parameters

  - other  
    Type: [T](hh578046\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](https://docs.microsoft.com/dotnet/api/system.boolean?redirectedfrom=MSDN)  
True if the two instances are equal.  

## See also

#### Reference

[IContentEquatable\<T\> interface](hh578046\(v=exchg.10\).md)

[IContentEquatable\<T\> members](hh578119\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

