---
description: "Learn more about: EsentInconsistentException constructor (SerializationInfo, StreamingContext)"
title: EsentInconsistentException constructor (SerializationInfo, StreamingContext)
TOCTitle: EsentInconsistentException constructor (SerializationInfo, StreamingContext)
ms:assetid: M:Microsoft.Isam.Esent.Interop.EsentInconsistentException.#ctor(System.Runtime.Serialization.SerializationInfo,System.Runtime.Serialization.StreamingContext)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentinconsistentexception.esentinconsistentexception(v=EXCHG.10)
ms:contentKeyID: 55101709
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.EsentInconsistentException..ctor
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentInconsistentException constructor (SerializationInfo, StreamingContext)

Initializes a new instance of the EsentInconsistentException class. This constructor is used to deserialize a serialized exception.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
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

Dim instance As New EsentInconsistentException(info, context)
```

``` csharp
protected EsentInconsistentException(
    SerializationInfo info,
    StreamingContext context
)
```

#### Parameters

  - info  
    Type: [System.Runtime.Serialization.SerializationInfo](/dotnet/api/system.runtime.serialization.serializationinfo)  
    
    The data needed to deserialize the object.

<!-- end list -->

  - context  
    Type: [System.Runtime.Serialization.StreamingContext](/dotnet/api/system.runtime.serialization.streamingcontext)  
    
    The deserialization context.

## See also

#### Reference

[EsentInconsistentException class](./esentinconsistentexception-class.md)

[EsentInconsistentException members](./esentinconsistentexception-members.md)

[EsentInconsistentException overload](./esentinconsistentexception-constructor.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
