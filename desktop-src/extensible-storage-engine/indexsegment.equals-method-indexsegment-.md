---
title: IndexSegment.Equals method (IndexSegment) (Microsoft.Isam.Esent.Interop)
TOCTitle: Equals method (IndexSegment)
ms:assetid: M:Microsoft.Isam.Esent.Interop.IndexSegment.Equals(Microsoft.Isam.Esent.Interop.IndexSegment)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.indexsegment.equals(v=EXCHG.10)
ms:contentKeyID: 55103276
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.IndexSegment.Equals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# IndexSegment.Equals method (IndexSegment)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As IndexSegment _
) As Boolean
'Usage
Dim instance As IndexSegment
Dim other As IndexSegment
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    IndexSegment other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.IndexSegment](dn350912\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](https://docs.microsoft.com/dotnet/api/system.boolean?redirectedfrom=MSDN)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](https://docs.microsoft.com/dotnet/api/system.iequatable-1.equals?redirectedfrom=MSDN#System_IEquatable_1_Equals__0_)  

## See also

#### Reference

[IndexSegment class](dn350912\(v=exchg.10\).md)

[IndexSegment members](dn350930\(v=exchg.10\).md)

[Equals overload](dn350933\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

