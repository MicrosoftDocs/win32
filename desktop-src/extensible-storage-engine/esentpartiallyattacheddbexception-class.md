---
description: "Learn more about: EsentPartiallyAttachedDBException class"
title: EsentPartiallyAttachedDBException class
TOCTitle: EsentPartiallyAttachedDBException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentPartiallyAttachedDBException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentpartiallyattacheddbexception(v=EXCHG.10)
ms:contentKeyID: 55107313
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentPartiallyAttachedDBException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentPartiallyAttachedDBException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentPartiallyAttachedDBException class

Base class for JET_err.PartiallyAttachedDB exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](./esentusageexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentPartiallyAttachedDBException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentPartiallyAttachedDBException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentPartiallyAttachedDBException
```

``` csharp
[SerializableAttribute]
public sealed class EsentPartiallyAttachedDBException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentPartiallyAttachedDBException members](./esentpartiallyattacheddbexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
