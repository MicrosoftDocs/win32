---
description: "Learn more about: EsentOutOfFileHandlesException class"
title: EsentOutOfFileHandlesException class
TOCTitle: EsentOutOfFileHandlesException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentOutOfFileHandlesException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentoutoffilehandlesexception(v=EXCHG.10)
ms:contentKeyID: 55102419
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentOutOfFileHandlesException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentOutOfFileHandlesException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentOutOfFileHandlesException class

Base class for JET_err.OutOfFileHandles exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](./esentoperationexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentResourceException](./esentresourceexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMemoryException](./esentmemoryexception-class.md)  
              Microsoft.Isam.Esent.Interop.EsentOutOfFileHandlesException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentOutOfFileHandlesException _
    Inherits EsentMemoryException
'Usage
Dim instance As EsentOutOfFileHandlesException
```

``` csharp
[SerializableAttribute]
public sealed class EsentOutOfFileHandlesException : EsentMemoryException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentOutOfFileHandlesException members](./esentoutoffilehandlesexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
