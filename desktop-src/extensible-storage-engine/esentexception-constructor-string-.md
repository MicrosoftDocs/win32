---
description: "Learn more about: EsentException constructor (String)"
title: EsentException constructor (String) (Microsoft.Isam.Esent)
TOCTitle: EsentException constructor (String)
ms:assetid: M:Microsoft.Isam.Esent.EsentException.#ctor(System.String)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.esentexception.esentexception(v=EXCHG.10)
ms:contentKeyID: 55100720
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

# EsentException constructor (String)

Initializes a new instance of the EsentException class with a specified error message.

**Namespace:**  [Microsoft.Isam.Esent](./microsoft.isam.esent-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Protected Sub New ( _
    message As String _
)
'Usage
Dim message As String

Dim instance As New EsentException(message)
```

``` csharp
protected EsentException(
    string message
)
```

#### Parameters

  - message  
    Type: [System.String](/dotnet/api/system.string)  
    
    The message that describes the error.

## See also

#### Reference

[EsentException class](./esentexception-class.md)

[EsentException members](./esentexception-members.md)

[EsentException overload](./esentexception-constructor.md)

[Microsoft.Isam.Esent namespace](./microsoft.isam.esent-namespace.md)
