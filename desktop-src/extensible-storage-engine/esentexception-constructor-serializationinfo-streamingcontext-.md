---
title: EsentException constructor (SerializationInfo, StreamingContext) (Microsoft.Isam.Esent)
TOCTitle: EsentException constructor (SerializationInfo, StreamingContext)
ms:assetid: M:Microsoft.Isam.Esent.EsentException.#ctor(System.Runtime.Serialization.SerializationInfo,System.Runtime.Serialization.StreamingContext)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.esentexception.esentexception(v=EXCHG.10)
ms:contentKeyID: 55100719
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.EsentException..ctor
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentException constructor (SerializationInfo, StreamingContext)

Initializes a new instance of the EsentException class. This constructor is used to deserialize a serialized exception.

**Namespace:**  [Microsoft.Isam.Esent](dn292085\(v=exchg.10\).md)  
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

Dim instance As New EsentException(info, context)
```

``` csharp
protected EsentException(
    SerializationInfo info,
    StreamingContext context
)
```

#### Parameters

  - info  
    Type: [System.Runtime.Serialization.SerializationInfo](https://docs.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo?redirectedfrom=MSDN)  
    
    The data needed to deserialize the object.

<!-- end list -->

  - context  
    Type: [System.Runtime.Serialization.StreamingContext](https://docs.microsoft.com/dotnet/api/system.runtime.serialization.streamingcontext?redirectedfrom=MSDN)  
    
    The deserialization context.

## See also

#### Reference

[EsentException class](dn292088\(v=exchg.10\).md)

[EsentException members](dn292086\(v=exchg.10\).md)

[EsentException overload](dn292116\(v=exchg.10\).md)

[Microsoft.Isam.Esent namespace](dn292085\(v=exchg.10\).md)

