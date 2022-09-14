---
description: "Learn more about: EsentLogDisabledDueToRecoveryFailureException class"
title: EsentLogDisabledDueToRecoveryFailureException class
TOCTitle: EsentLogDisabledDueToRecoveryFailureException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentLogDisabledDueToRecoveryFailureException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentlogdisabledduetorecoveryfailureexception(v=EXCHG.10)
ms:contentKeyID: 55102151
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentLogDisabledDueToRecoveryFailureException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentLogDisabledDueToRecoveryFailureException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentLogDisabledDueToRecoveryFailureException class

Base class for JET_err.LogDisabledDueToRecoveryFailure exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](./esentoperationexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentFatalException](./esentfatalexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentLogDisabledDueToRecoveryFailureException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentLogDisabledDueToRecoveryFailureException _
    Inherits EsentFatalException
'Usage
Dim instance As EsentLogDisabledDueToRecoveryFailureException
```

``` csharp
[SerializableAttribute]
public sealed class EsentLogDisabledDueToRecoveryFailureException : EsentFatalException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentLogDisabledDueToRecoveryFailureException members](./esentlogdisabledduetorecoveryfailureexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
