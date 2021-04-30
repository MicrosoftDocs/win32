---
description: "Learn more about: EsentSoftRecoveryOnBackupDatabaseException class"
title: EsentSoftRecoveryOnBackupDatabaseException class
TOCTitle: EsentSoftRecoveryOnBackupDatabaseException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentSoftRecoveryOnBackupDatabaseException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentsoftrecoveryonbackupdatabaseexception(v=EXCHG.10)
ms:contentKeyID: 55102863
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentSoftRecoveryOnBackupDatabaseException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentSoftRecoveryOnBackupDatabaseException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentSoftRecoveryOnBackupDatabaseException class

Base class for JET_err.SoftRecoveryOnBackupDatabase exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](./esentusageexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentSoftRecoveryOnBackupDatabaseException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentSoftRecoveryOnBackupDatabaseException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentSoftRecoveryOnBackupDatabaseException
```

``` csharp
[SerializableAttribute]
public sealed class EsentSoftRecoveryOnBackupDatabaseException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentSoftRecoveryOnBackupDatabaseException members](./esentsoftrecoveryonbackupdatabaseexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
