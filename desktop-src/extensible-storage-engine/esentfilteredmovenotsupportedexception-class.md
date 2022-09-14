---
description: "Learn more about: EsentFilteredMoveNotSupportedException class"
title: EsentFilteredMoveNotSupportedException class
TOCTitle: EsentFilteredMoveNotSupportedException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentFilteredMoveNotSupportedException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentfilteredmovenotsupportedexception(v=EXCHG.10)
ms:contentKeyID: 55107268
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentFilteredMoveNotSupportedException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentFilteredMoveNotSupportedException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentFilteredMoveNotSupportedException class

Base class for JET_err.FilteredMoveNotSupported exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](./esentusageexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentFilteredMoveNotSupportedException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentFilteredMoveNotSupportedException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentFilteredMoveNotSupportedException
```

``` csharp
[SerializableAttribute]
public sealed class EsentFilteredMoveNotSupportedException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentFilteredMoveNotSupportedException members](./esentfilteredmovenotsupportedexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
