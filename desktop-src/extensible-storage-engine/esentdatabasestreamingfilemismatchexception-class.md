---
description: "Learn more about: EsentDatabaseStreamingFileMismatchException class"
title: EsentDatabaseStreamingFileMismatchException class
TOCTitle: EsentDatabaseStreamingFileMismatchException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentDatabaseStreamingFileMismatchException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentdatabasestreamingfilemismatchexception(v=EXCHG.10)
ms:contentKeyID: 55101544
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentDatabaseStreamingFileMismatchException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentDatabaseStreamingFileMismatchException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentDatabaseStreamingFileMismatchException class

Base class for JET_err.DatabaseStreamingFileMismatch exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentObsoleteException](./esentobsoleteexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentDatabaseStreamingFileMismatchException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentDatabaseStreamingFileMismatchException _
    Inherits EsentObsoleteException
'Usage
Dim instance As EsentDatabaseStreamingFileMismatchException
```

``` csharp
[SerializableAttribute]
public sealed class EsentDatabaseStreamingFileMismatchException : EsentObsoleteException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentDatabaseStreamingFileMismatchException members](./esentdatabasestreamingfilemismatchexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
