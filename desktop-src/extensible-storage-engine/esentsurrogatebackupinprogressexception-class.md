---
description: "Learn more about: EsentSurrogateBackupInProgressException class"
title: EsentSurrogateBackupInProgressException class
TOCTitle: EsentSurrogateBackupInProgressException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentSurrogateBackupInProgressException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentsurrogatebackupinprogressexception(v=EXCHG.10)
ms:contentKeyID: 55102946
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentSurrogateBackupInProgressException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentSurrogateBackupInProgressException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentSurrogateBackupInProgressException class

Base class for JET_err.SurrogateBackupInProgress exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentStateException](./esentstateexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentSurrogateBackupInProgressException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentSurrogateBackupInProgressException _
    Inherits EsentStateException
'Usage
Dim instance As EsentSurrogateBackupInProgressException
```

``` csharp
[SerializableAttribute]
public sealed class EsentSurrogateBackupInProgressException : EsentStateException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentSurrogateBackupInProgressException members](./esentsurrogatebackupinprogressexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
