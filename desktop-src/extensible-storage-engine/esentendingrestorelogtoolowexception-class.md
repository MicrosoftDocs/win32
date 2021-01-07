---
description: "Learn more about: EsentEndingRestoreLogTooLowException class"
title: EsentEndingRestoreLogTooLowException class
TOCTitle: EsentEndingRestoreLogTooLowException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentEndingRestoreLogTooLowException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentendingrestorelogtoolowexception(v=EXCHG.10)
ms:contentKeyID: 55101575
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentEndingRestoreLogTooLowException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentEndingRestoreLogTooLowException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentEndingRestoreLogTooLowException class

Base class for JET_err.EndingRestoreLogTooLow exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentInconsistentException](./esentinconsistentexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentEndingRestoreLogTooLowException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentEndingRestoreLogTooLowException _
    Inherits EsentInconsistentException
'Usage
Dim instance As EsentEndingRestoreLogTooLowException
```

``` csharp
[SerializableAttribute]
public sealed class EsentEndingRestoreLogTooLowException : EsentInconsistentException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentEndingRestoreLogTooLowException members](./esentendingrestorelogtoolowexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
