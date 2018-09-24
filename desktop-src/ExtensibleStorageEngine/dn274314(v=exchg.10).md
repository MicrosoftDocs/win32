---
title: EsentErrorException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentErrorException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentErrorException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esenterrorexception(v=EXCHG.10)
ms:contentKeyID: 55101648
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentErrorException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentErrorException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentErrorException class

Base class for ESENT error exceptions.

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      Microsoft.Isam.Esent.Interop.EsentErrorException  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentCannotLogDuringRecoveryRedoException](dn274165\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](dn319727\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentPreviousVersionException](dn319852\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentVersionStoreEntryTooBigException](dn350862\(v=exchg.10\).md)  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public Class EsentErrorException _
    Inherits EsentException
'Usage
Dim instance As EsentErrorException
```

``` csharp
[SerializableAttribute]
public class EsentErrorException : EsentException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentErrorException members](dn274255\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

