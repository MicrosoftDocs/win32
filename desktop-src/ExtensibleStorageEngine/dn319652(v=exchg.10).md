---
title: EsentMultiValuedDuplicateException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentMultiValuedDuplicateException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentMultiValuedDuplicateException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentmultivaluedduplicateexception(v=EXCHG.10)
ms:contentKeyID: 55102340
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentMultiValuedDuplicateException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentMultiValuedDuplicateException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentMultiValuedDuplicateException class

Base class for JET\_err.MultiValuedDuplicate exceptions.

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentStateException](dn334920\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentMultiValuedDuplicateException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentMultiValuedDuplicateException _
    Inherits EsentStateException
'Usage
Dim instance As EsentMultiValuedDuplicateException
```

``` csharp
[SerializableAttribute]
public sealed class EsentMultiValuedDuplicateException : EsentStateException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentMultiValuedDuplicateException members](dn334704\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

