---
title: EsentMissingRestoreLogFilesException class
TOCTitle: EsentMissingRestoreLogFilesException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentMissingRestoreLogFilesException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentmissingrestorelogfilesexception(v=EXCHG.10)
ms:contentKeyID: 55102315
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentMissingRestoreLogFilesException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentMissingRestoreLogFilesException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentMissingRestoreLogFilesException class

Base class for JET_err.MissingRestoreLogFiles exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentInconsistentException](dn350488\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentMissingRestoreLogFilesException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentMissingRestoreLogFilesException _
    Inherits EsentInconsistentException
'Usage
Dim instance As EsentMissingRestoreLogFilesException
```

``` csharp
[SerializableAttribute]
public sealed class EsentMissingRestoreLogFilesException : EsentInconsistentException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentMissingRestoreLogFilesException members](dn334763\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)