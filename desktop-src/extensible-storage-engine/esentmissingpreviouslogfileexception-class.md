---
description: "Learn more about: EsentMissingPreviousLogFileException class"
title: EsentMissingPreviousLogFileException class
TOCTitle: EsentMissingPreviousLogFileException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentMissingPreviousLogFileException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentmissingpreviouslogfileexception(v=EXCHG.10)
ms:contentKeyID: 55102244
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentMissingPreviousLogFileException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentMissingPreviousLogFileException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentMissingPreviousLogFileException class

Base class for JET_err.MissingPreviousLogFile exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentCorruptionException](./esentcorruptionexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentMissingPreviousLogFileException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentMissingPreviousLogFileException _
    Inherits EsentCorruptionException
'Usage
Dim instance As EsentMissingPreviousLogFileException
```

``` csharp
[SerializableAttribute]
public sealed class EsentMissingPreviousLogFileException : EsentCorruptionException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentMissingPreviousLogFileException members](./esentmissingpreviouslogfileexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
