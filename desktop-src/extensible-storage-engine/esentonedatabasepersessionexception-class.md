---
title: EsentOneDatabasePerSessionException class
TOCTitle: EsentOneDatabasePerSessionException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentOneDatabasePerSessionException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentonedatabasepersessionexception(v=EXCHG.10)
ms:contentKeyID: 55102432
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentOneDatabasePerSessionException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentOneDatabasePerSessionException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentOneDatabasePerSessionException class

Base class for JET_err.OneDatabasePerSession exceptions.

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](dn350849\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentOneDatabasePerSessionException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentOneDatabasePerSessionException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentOneDatabasePerSessionException
```

``` csharp
[SerializableAttribute]
public sealed class EsentOneDatabasePerSessionException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentOneDatabasePerSessionException members](dn319679\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

