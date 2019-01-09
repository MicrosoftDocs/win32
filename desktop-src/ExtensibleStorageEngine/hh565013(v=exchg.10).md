---
title: JET_LOGTIME.Equals method (JET_LOGTIME) (Microsoft.Isam.Esent.Interop)
TOCTitle: Equals method (JET_LOGTIME)
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_LOGTIME.Equals(Microsoft.Isam.Esent.Interop.JET_LOGTIME)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_logtime.equals(v=EXCHG.10)
ms:contentKeyID: 39512684
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.JET_LOGTIME.Equals
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_LOGTIME.Equals method (JET_LOGTIME)

Returns a value indicating whether this instance is equal to another instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function Equals ( _
    other As JET_LOGTIME _
) As Boolean
'Usage
Dim instance As JET_LOGTIME
Dim other As JET_LOGTIME
Dim returnValue As Boolean

returnValue = instance.Equals(other)
```

``` csharp
public bool Equals(
    JET_LOGTIME other
)
```

#### Parameters

  - other  
    Type: [Microsoft.Isam.Esent.Interop.JET_LOGTIME](hh557188\(v=exchg.10\).md)  
    
    An instance to compare with this instance.

#### Return value

Type: [System.Boolean](https://msdn.microsoft.com/en-us/library/a28wyd50)  
True if the two instances are equal.  

#### Implements

[IEquatable\<T\>.Equals(T)](https://msdn.microsoft.com/en-us/library/ms131190)  

## See also

#### Reference

[JET_LOGTIME structure](hh557188\(v=exchg.10\).md)

[JET_LOGTIME members](hh579151\(v=exchg.10\).md)

[Equals overload](hh566490\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

