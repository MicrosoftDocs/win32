---
description: "Learn more about: EsentDatabaseCorruptedNoRepairException class"
title: EsentDatabaseCorruptedNoRepairException class
TOCTitle: EsentDatabaseCorruptedNoRepairException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentDatabaseCorruptedNoRepairException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentdatabasecorruptednorepairexception(v=EXCHG.10)
ms:contentKeyID: 55101445
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentDatabaseCorruptedNoRepairException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentDatabaseCorruptedNoRepairException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentDatabaseCorruptedNoRepairException class

Base class for JET_err.DatabaseCorruptedNoRepair exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](./esentusageexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentDatabaseCorruptedNoRepairException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentDatabaseCorruptedNoRepairException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentDatabaseCorruptedNoRepairException
```

``` csharp
[SerializableAttribute]
public sealed class EsentDatabaseCorruptedNoRepairException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentDatabaseCorruptedNoRepairException members](./esentdatabasecorruptednorepairexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
