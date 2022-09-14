---
description: "Learn more about: EsentRedoAbruptEndedException class"
title: EsentRedoAbruptEndedException class
TOCTitle: EsentRedoAbruptEndedException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentRedoAbruptEndedException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentredoabruptendedexception(v=EXCHG.10)
ms:contentKeyID: 55102536
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentRedoAbruptEndedException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentRedoAbruptEndedException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentRedoAbruptEndedException class

Base class for JET_err.RedoAbruptEnded exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentCorruptionException](./esentcorruptionexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentRedoAbruptEndedException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentRedoAbruptEndedException _
    Inherits EsentCorruptionException
'Usage
Dim instance As EsentRedoAbruptEndedException
```

``` csharp
[SerializableAttribute]
public sealed class EsentRedoAbruptEndedException : EsentCorruptionException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentRedoAbruptEndedException members](./esentredoabruptendedexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
