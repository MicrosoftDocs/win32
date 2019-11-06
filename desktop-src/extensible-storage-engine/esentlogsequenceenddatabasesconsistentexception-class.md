---
title: EsentLogSequenceEndDatabasesConsistentException class
TOCTitle: EsentLogSequenceEndDatabasesConsistentException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentLogSequenceEndDatabasesConsistentException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentlogsequenceenddatabasesconsistentexception(v=EXCHG.10)
ms:contentKeyID: 55102212
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentLogSequenceEndDatabasesConsistentException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentLogSequenceEndDatabasesConsistentException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentLogSequenceEndDatabasesConsistentException class

Base class for JET_err.LogSequenceEndDatabasesConsistent exceptions.

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentFragmentationException](dn350462\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentLogSequenceEndDatabasesConsistentException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentLogSequenceEndDatabasesConsistentException _
    Inherits EsentFragmentationException
'Usage
Dim instance As EsentLogSequenceEndDatabasesConsistentException
```

``` csharp
[SerializableAttribute]
public sealed class EsentLogSequenceEndDatabasesConsistentException : EsentFragmentationException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentLogSequenceEndDatabasesConsistentException members](dn334597\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

