---
title: EsentObsoleteException constructor (SerializationInfo, StreamingContext)
TOCTitle: EsentObsoleteException constructor (SerializationInfo, StreamingContext)
ms:assetid: M:Microsoft.Isam.Esent.Interop.EsentObsoleteException.#ctor(System.Runtime.Serialization.SerializationInfo,System.Runtime.Serialization.StreamingContext)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentobsoleteexception.esentobsoleteexception(v=EXCHG.10)
ms:contentKeyID: 55102167
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.EsentObsoleteException..ctor
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentObsoleteException constructor (SerializationInfo, StreamingContext)

Initializes a new instance of the EsentObsoleteException class. This constructor is used to deserialize a serialized exception.

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

Dim instance As New EsentObsoleteException(info, context)
```

``` csharp
protected EsentObsoleteException(
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

[EsentObsoleteException class](dn319668\(v=exchg.10\).md)

[EsentObsoleteException members](dn319669\(v=exchg.10\).md)

[EsentObsoleteException overload](dn319672\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

