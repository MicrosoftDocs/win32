---
description: "Learn more about: EsentLogTornWriteDuringHardRecoveryException class"
title: EsentLogTornWriteDuringHardRecoveryException class
TOCTitle: EsentLogTornWriteDuringHardRecoveryException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRecoveryException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentlogtornwriteduringhardrecoveryexception(v=EXCHG.10)
ms:contentKeyID: 55102218
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRecoveryException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRecoveryException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentLogTornWriteDuringHardRecoveryException class

Base class for JET_err.LogTornWriteDuringHardRecovery exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentCorruptionException](./esentcorruptionexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRecoveryException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentLogTornWriteDuringHardRecoveryException _
    Inherits EsentCorruptionException
'Usage
Dim instance As EsentLogTornWriteDuringHardRecoveryException
```

``` csharp
[SerializableAttribute]
public sealed class EsentLogTornWriteDuringHardRecoveryException : EsentCorruptionException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentLogTornWriteDuringHardRecoveryException members](./esentlogtornwriteduringhardrecoveryexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
