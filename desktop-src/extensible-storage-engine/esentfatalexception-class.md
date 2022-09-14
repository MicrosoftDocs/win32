---
description: "Learn more about: EsentFatalException class"
title: EsentFatalException class
TOCTitle: EsentFatalException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentFatalException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentfatalexception(v=EXCHG.10)
ms:contentKeyID: 55101653
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentFatalException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentFatalException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentFatalException class

Base class for Fatal exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](./esentoperationexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentFatalException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public MustInherit Class EsentFatalException _
    Inherits EsentOperationException
'Usage
Dim instance As EsentFatalException
```

``` csharp
[SerializableAttribute]
public abstract class EsentFatalException : EsentOperationException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentFatalException members](./esentfatalexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)

## Derived types

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](./esentoperationexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentFatalException  
            [Microsoft.Isam.Esent.Interop.EsentInstanceUnavailableDueToFatalLogDiskFullException](./esentinstanceunavailableduetofatallogdiskfullexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInstanceUnavailableException](./esentinstanceunavailableexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogDisabledDueToRecoveryFailureException](./esentlogdisabledduetorecoveryfailureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRollbackErrorException](./esentrollbackerrorexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSectorSizeNotSupportedException](./esentsectorsizenotsupportedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentUnloadableOSFunctionalityException](./esentunloadableosfunctionalityexception-class.md)