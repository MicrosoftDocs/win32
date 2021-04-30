---
description: "Learn more about: EsentOSSnapshotInvalidSnapIdException class"
title: EsentOSSnapshotInvalidSnapIdException class
TOCTitle: EsentOSSnapshotInvalidSnapIdException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentOSSnapshotInvalidSnapIdException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentossnapshotinvalidsnapidexception(v=EXCHG.10)
ms:contentKeyID: 55102431
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentOSSnapshotInvalidSnapIdException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentOSSnapshotInvalidSnapIdException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentOSSnapshotInvalidSnapIdException class

Base class for JET_err.OSSnapshotInvalidSnapId exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](./esentusageexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentOSSnapshotInvalidSnapIdException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentOSSnapshotInvalidSnapIdException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentOSSnapshotInvalidSnapIdException
```

``` csharp
[SerializableAttribute]
public sealed class EsentOSSnapshotInvalidSnapIdException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentOSSnapshotInvalidSnapIdException members](./esentossnapshotinvalidsnapidexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
