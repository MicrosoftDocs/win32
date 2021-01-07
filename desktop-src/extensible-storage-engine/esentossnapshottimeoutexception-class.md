---
description: "Learn more about: EsentOSSnapshotTimeOutException class"
title: EsentOSSnapshotTimeOutException class
TOCTitle: EsentOSSnapshotTimeOutException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentOSSnapshotTimeOutException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentossnapshottimeoutexception(v=EXCHG.10)
ms:contentKeyID: 55102393
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentOSSnapshotTimeOutException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentOSSnapshotTimeOutException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentOSSnapshotTimeOutException class

Base class for JET_err.OSSnapshotTimeOut exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](./esentoperationexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentOSSnapshotTimeOutException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentOSSnapshotTimeOutException _
    Inherits EsentOperationException
'Usage
Dim instance As EsentOSSnapshotTimeOutException
```

``` csharp
[SerializableAttribute]
public sealed class EsentOSSnapshotTimeOutException : EsentOperationException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentOSSnapshotTimeOutException members](./esentossnapshottimeoutexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
