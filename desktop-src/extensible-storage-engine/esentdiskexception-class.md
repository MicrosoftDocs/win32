---
description: "Learn more about: EsentDiskException class"
title: EsentDiskException class
TOCTitle: EsentDiskException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentDiskException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentdiskexception(v=EXCHG.10)
ms:contentKeyID: 55101517
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentDiskException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentDiskException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentDiskException class

Base class for Disk exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](./esentoperationexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentResourceException](./esentresourceexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentDiskException  
              [Microsoft.Isam.Esent.Interop.EsentDiskFullException](./esentdiskfullexception-class.md)  
              [Microsoft.Isam.Esent.Interop.EsentLogDiskFullException](./esentlogdiskfullexception-class.md)  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public MustInherit Class EsentDiskException _
    Inherits EsentResourceException
'Usage
Dim instance As EsentDiskException
```

``` csharp
[SerializableAttribute]
public abstract class EsentDiskException : EsentResourceException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentDiskException members](./esentdiskexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
