---
title: EsentResourceException constructor (SerializationInfo, StreamingContext) (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentResourceException constructor (SerializationInfo, StreamingContext)
ms:assetid: M:Microsoft.Isam.Esent.Interop.EsentResourceException.#ctor(System.Runtime.Serialization.SerializationInfo,System.Runtime.Serialization.StreamingContext)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentresourceexception.esentresourceexception(v=EXCHG.10)
ms:contentKeyID: 55102649
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.EsentResourceException..ctor
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentResourceException constructor (SerializationInfo, StreamingContext)

Initializes a new instance of the EsentResourceException class. This constructor is used to deserialize a serialized exception.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Protected Sub New ( _
    info As SerializationInfo, _
    context As StreamingContext _
)
'Usage
Dim info As SerializationInfo
Dim context As StreamingContext

Dim instance As New EsentResourceException(info, context)
```

``` csharp
protected EsentResourceException(
    SerializationInfo info,
    StreamingContext context
)
```

#### Parameters

  - info  
    Type: [System.Runtime.Serialization.SerializationInfo](http://msdn2.microsoft.com/en-us/library/a9b6042e)  
    
    The data needed to deserialize the object.

<!-- end list -->

  - context  
    Type: [System.Runtime.Serialization.StreamingContext](http://msdn2.microsoft.com/en-us/library/t16abws5)  
    
    The deserialization context.

## See also

#### Reference

[EsentResourceException class](dn350557\(v=exchg.10\).md)

[EsentResourceException members](dn350580\(v=exchg.10\).md)

[EsentResourceException overload](dn350556\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

