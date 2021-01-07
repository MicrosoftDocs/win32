---
description: "Learn more about: EsentReadLostFlushVerifyFailureException class"
title: EsentReadLostFlushVerifyFailureException class
TOCTitle: EsentReadLostFlushVerifyFailureException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentReadLostFlushVerifyFailureException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentreadlostflushverifyfailureexception(v=EXCHG.10)
ms:contentKeyID: 55102493
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentReadLostFlushVerifyFailureException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentReadLostFlushVerifyFailureException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentReadLostFlushVerifyFailureException class

Base class for JET_err.ReadLostFlushVerifyFailure exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentCorruptionException](./esentcorruptionexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentReadLostFlushVerifyFailureException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentReadLostFlushVerifyFailureException _
    Inherits EsentCorruptionException
'Usage
Dim instance As EsentReadLostFlushVerifyFailureException
```

``` csharp
[SerializableAttribute]
public sealed class EsentReadLostFlushVerifyFailureException : EsentCorruptionException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentReadLostFlushVerifyFailureException members](./esentreadlostflushverifyfailureexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
