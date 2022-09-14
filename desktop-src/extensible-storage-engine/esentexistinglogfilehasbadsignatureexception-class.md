---
description: "Learn more about: EsentExistingLogFileHasBadSignatureException class"
title: EsentExistingLogFileHasBadSignatureException class
TOCTitle: EsentExistingLogFileHasBadSignatureException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentExistingLogFileHasBadSignatureException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentexistinglogfilehasbadsignatureexception(v=EXCHG.10)
ms:contentKeyID: 55101651
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentExistingLogFileHasBadSignatureException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentExistingLogFileHasBadSignatureException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentExistingLogFileHasBadSignatureException class

Base class for JET_err.ExistingLogFileHasBadSignature exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentInconsistentException](./esentinconsistentexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentExistingLogFileHasBadSignatureException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentExistingLogFileHasBadSignatureException _
    Inherits EsentInconsistentException
'Usage
Dim instance As EsentExistingLogFileHasBadSignatureException
```

``` csharp
[SerializableAttribute]
public sealed class EsentExistingLogFileHasBadSignatureException : EsentInconsistentException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentExistingLogFileHasBadSignatureException members](./esentexistinglogfilehasbadsignatureexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
