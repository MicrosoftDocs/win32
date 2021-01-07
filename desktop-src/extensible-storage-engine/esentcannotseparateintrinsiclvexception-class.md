---
description: "Learn more about: EsentCannotSeparateIntrinsicLVException class"
title: EsentCannotSeparateIntrinsicLVException class
TOCTitle: EsentCannotSeparateIntrinsicLVException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentCannotSeparateIntrinsicLVException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentcannotseparateintrinsiclvexception(v=EXCHG.10)
ms:contentKeyID: 55101176
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentCannotSeparateIntrinsicLVException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentCannotSeparateIntrinsicLVException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentCannotSeparateIntrinsicLVException class

Base class for JET_err.CannotSeparateIntrinsicLV exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](./esentusageexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentCannotSeparateIntrinsicLVException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentCannotSeparateIntrinsicLVException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentCannotSeparateIntrinsicLVException
```

``` csharp
[SerializableAttribute]
public sealed class EsentCannotSeparateIntrinsicLVException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentCannotSeparateIntrinsicLVException members](./esentcannotseparateintrinsiclvexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
