---
title: EsentLogSectorSizeMismatchException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentLogSectorSizeMismatchException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentLogSectorSizeMismatchException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentlogsectorsizemismatchexception(v=EXCHG.10)
ms:contentKeyID: 55102207
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentLogSectorSizeMismatchException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentLogSectorSizeMismatchException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentLogSectorSizeMismatchException class

Base class for JET\_err.LogSectorSizeMismatch exceptions.

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentFragmentationException](dn350462\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentLogSectorSizeMismatchException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentLogSectorSizeMismatchException _
    Inherits EsentFragmentationException
'Usage
Dim instance As EsentLogSectorSizeMismatchException
```

``` csharp
[SerializableAttribute]
public sealed class EsentLogSectorSizeMismatchException : EsentFragmentationException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentLogSectorSizeMismatchException members](dn334592\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

