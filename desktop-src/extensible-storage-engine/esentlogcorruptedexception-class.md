---
title: EsentLogCorruptedException class
TOCTitle: EsentLogCorruptedException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentLogCorruptedException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentlogcorruptedexception(v=EXCHG.10)
ms:contentKeyID: 55107292
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentLogCorruptedException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentLogCorruptedException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentLogCorruptedException class

Base class for JET_err.LogCorrupted exceptions.

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentCorruptionException](dn274225\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentLogCorruptedException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentLogCorruptedException _
    Inherits EsentCorruptionException
'Usage
Dim instance As EsentLogCorruptedException
```

``` csharp
[SerializableAttribute]
public sealed class EsentLogCorruptedException : EsentCorruptionException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentLogCorruptedException members](dn334511\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

