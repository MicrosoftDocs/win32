---
title: JET_INDEXID.Equals method (JET_INDEXID)
TOCTitle: Equals method (JET_INDEXID)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_INDEXID.Equals(Microsoft.Isam.Esent.Interop.JET_INDEXID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_indexid.equals(v=EXCHG.10)
ms:contentKeyID: 39515277
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXID.Equals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXID.Equals method (JET_INDEXID)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_INDEXID _
) As Boolean
'Usage
Dim instance As JET_INDEXID
Dim other As JET_INDEXID
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_INDEXID other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET_INDEXID](hh557060\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](https://docs.microsoft.com/dotnet/api/system.boolean?redirectedfrom=MSDN)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](https://docs.microsoft.com/dotnet/api/system.iequatable-1.equals?redirectedfrom=MSDN#System_IEquatable_1_Equals__0_)  

## See also

#### Reference

[JET_INDEXID structure](hh557060\(v=exchg.10\).md)

[JET_INDEXID members](hh565743\(v=exchg.10\).md)

[Equals overload](hh557490\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

