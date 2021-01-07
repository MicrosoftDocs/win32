---
description: "Learn more about: EsentContainerNotEmptyException class"
title: EsentContainerNotEmptyException class
TOCTitle: EsentContainerNotEmptyException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentContainerNotEmptyException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentcontainernotemptyexception(v=EXCHG.10)
ms:contentKeyID: 55101375
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentContainerNotEmptyException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentContainerNotEmptyException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentContainerNotEmptyException class

Base class for JET_err.ContainerNotEmpty exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentObsoleteException](./esentobsoleteexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentContainerNotEmptyException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentContainerNotEmptyException _
    Inherits EsentObsoleteException
'Usage
Dim instance As EsentContainerNotEmptyException
```

``` csharp
[SerializableAttribute]
public sealed class EsentContainerNotEmptyException : EsentObsoleteException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentContainerNotEmptyException members](./esentcontainernotemptyexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
