---
description: "Learn more about: EsentCannotLogDuringRecoveryRedoException class"
title: EsentCannotLogDuringRecoveryRedoException class
TOCTitle: EsentCannotLogDuringRecoveryRedoException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentCannotLogDuringRecoveryRedoException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentcannotlogduringrecoveryredoexception(v=EXCHG.10)
ms:contentKeyID: 55101221
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentCannotLogDuringRecoveryRedoException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentCannotLogDuringRecoveryRedoException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentCannotLogDuringRecoveryRedoException class

Base class for JET_err.CannotLogDuringRecoveryRedo exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        Microsoft.Isam.Esent.Interop.EsentCannotLogDuringRecoveryRedoException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentCannotLogDuringRecoveryRedoException _
    Inherits EsentErrorException
'Usage
Dim instance As EsentCannotLogDuringRecoveryRedoException
```

``` csharp
[SerializableAttribute]
public sealed class EsentCannotLogDuringRecoveryRedoException : EsentErrorException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentCannotLogDuringRecoveryRedoException members](./esentcannotlogduringrecoveryredoexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
