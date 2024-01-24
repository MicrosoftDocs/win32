---
description: "Learn more about: EsentStartingRestoreLogTooHighException class"
title: EsentStartingRestoreLogTooHighException class
TOCTitle: EsentStartingRestoreLogTooHighException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentStartingRestoreLogTooHighException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentstartingrestorelogtoohighexception(v=EXCHG.10)
ms:contentKeyID: 55102926
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentStartingRestoreLogTooHighException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentStartingRestoreLogTooHighException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentStartingRestoreLogTooHighException class

Base class for JET_err.StartingRestoreLogTooHigh exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentInconsistentException](./esentinconsistentexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentStartingRestoreLogTooHighException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentStartingRestoreLogTooHighException _
    Inherits EsentInconsistentException
'Usage
Dim instance As EsentStartingRestoreLogTooHighException
```

``` csharp
[SerializableAttribute]
public sealed class EsentStartingRestoreLogTooHighException : EsentInconsistentException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentStartingRestoreLogTooHighException members](./esentstartingrestorelogtoohighexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
