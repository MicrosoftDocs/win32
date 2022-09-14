---
description: "Learn more about: EsentAfterInitializationException class"
title: EsentAfterInitializationException class
TOCTitle: EsentAfterInitializationException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentAfterInitializationException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentafterinitializationexception(v=EXCHG.10)
ms:contentKeyID: 55101005
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentAfterInitializationException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentAfterInitializationException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentAfterInitializationException class

Base class for JET_err.AfterInitialization exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](./esentusageexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentAfterInitializationException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentAfterInitializationException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentAfterInitializationException
```

``` csharp
[SerializableAttribute]
public sealed class EsentAfterInitializationException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentAfterInitializationException members](./esentafterinitializationexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
