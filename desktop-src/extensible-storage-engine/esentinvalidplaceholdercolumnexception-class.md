---
description: "Learn more about: EsentInvalidPlaceholderColumnException class"
title: EsentInvalidPlaceholderColumnException class
TOCTitle: EsentInvalidPlaceholderColumnException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentInvalidPlaceholderColumnException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentinvalidplaceholdercolumnexception(v=EXCHG.10)
ms:contentKeyID: 55102014
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentInvalidPlaceholderColumnException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentInvalidPlaceholderColumnException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentInvalidPlaceholderColumnException class

Base class for JET_err.InvalidPlaceholderColumn exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](./esentusageexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentInvalidPlaceholderColumnException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentInvalidPlaceholderColumnException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentInvalidPlaceholderColumnException
```

``` csharp
[SerializableAttribute]
public sealed class EsentInvalidPlaceholderColumnException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentInvalidPlaceholderColumnException members](./esentinvalidplaceholdercolumnexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
