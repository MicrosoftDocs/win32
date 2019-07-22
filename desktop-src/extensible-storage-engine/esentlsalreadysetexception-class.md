---
title: EsentLSAlreadySetException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentLSAlreadySetException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentLSAlreadySetException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentlsalreadysetexception(v=EXCHG.10)
ms:contentKeyID: 55102175
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentLSAlreadySetException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentLSAlreadySetException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentLSAlreadySetException class

Base class for JET_err.LSAlreadySet exceptions.

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](dn350849\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentLSAlreadySetException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentLSAlreadySetException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentLSAlreadySetException
```

``` csharp
[SerializableAttribute]
public sealed class EsentLSAlreadySetException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentLSAlreadySetException members](dn334669\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

