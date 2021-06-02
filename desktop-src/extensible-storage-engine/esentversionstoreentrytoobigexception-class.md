---
description: "Learn more about: EsentVersionStoreEntryTooBigException class"
title: EsentVersionStoreEntryTooBigException class
TOCTitle: EsentVersionStoreEntryTooBigException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentVersionStoreEntryTooBigException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentversionstoreentrytoobigexception(v=EXCHG.10)
ms:contentKeyID: 55103188
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentVersionStoreEntryTooBigException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentVersionStoreEntryTooBigException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentVersionStoreEntryTooBigException class

Base class for JET_err.VersionStoreEntryTooBig exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        Microsoft.Isam.Esent.Interop.EsentVersionStoreEntryTooBigException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentVersionStoreEntryTooBigException _
    Inherits EsentErrorException
'Usage
Dim instance As EsentVersionStoreEntryTooBigException
```

``` csharp
[SerializableAttribute]
public sealed class EsentVersionStoreEntryTooBigException : EsentErrorException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentVersionStoreEntryTooBigException members](./esentversionstoreentrytoobigexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
