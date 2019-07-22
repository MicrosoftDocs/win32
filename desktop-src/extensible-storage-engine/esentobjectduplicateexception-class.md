---
title: EsentObjectDuplicateException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentObjectDuplicateException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentObjectDuplicateException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentobjectduplicateexception(v=EXCHG.10)
ms:contentKeyID: 55102411
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentObjectDuplicateException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentObjectDuplicateException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentObjectDuplicateException class

Base class for JET_err.ObjectDuplicate exceptions.

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentObsoleteException](dn319668\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentObjectDuplicateException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentObjectDuplicateException _
    Inherits EsentObsoleteException
'Usage
Dim instance As EsentObjectDuplicateException
```

``` csharp
[SerializableAttribute]
public sealed class EsentObjectDuplicateException : EsentObsoleteException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentObjectDuplicateException members](dn319656\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

