---
title: EsentLogTornWriteDuringHardRestoreException class
TOCTitle: EsentLogTornWriteDuringHardRestoreException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRestoreException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentlogtornwriteduringhardrestoreexception(v=EXCHG.10)
ms:contentKeyID: 55102166
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRestoreException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRestoreException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentLogTornWriteDuringHardRestoreException class

Base class for JET_err.LogTornWriteDuringHardRestore exceptions.

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentCorruptionException](dn274225\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRestoreException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentLogTornWriteDuringHardRestoreException _
    Inherits EsentCorruptionException
'Usage
Dim instance As EsentLogTornWriteDuringHardRestoreException
```

``` csharp
[SerializableAttribute]
public sealed class EsentLogTornWriteDuringHardRestoreException : EsentCorruptionException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentLogTornWriteDuringHardRestoreException members](dn334663\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

